from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import json

# โหลดโมเดลและ Tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# โหลดข้อมูลสูตรอาหารจากไฟล์ JSON
with open('data/recipes.json', 'r', encoding='utf-8') as f:
    recipes = json.load(f)

app = Flask(__name__)

# จัดการประวัติการสนทนา
chat_history_ids = None

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]  # รับข้อความจากฟอร์ม
    response = get_Chat_response(msg)  # ส่งข้อความไปยังฟังก์ชันตอบกลับ
    return jsonify({"response": response})

def get_Chat_response(text):
    global chat_history_ids

    # ค้นหาชื่อสูตรอาหารจากคำถาม
    response = search_recipe(text)

    if response:
        return response
    else:
        # ถ้าหากไม่พบสูตรอาหาร ให้ใช้โมเดลตอบกลับ
        return chat_with_model(text)

def search_recipe(query):
    query = query.lower()  # แปลงคำถามเป็นตัวพิมพ์เล็กเพื่อการค้นหาที่สะดวก

    # ค้นหาชื่อสูตรอาหารจากคำถาม
    for recipe in recipes:
        if recipe['name'].lower() in query:  # ค้นหาชื่ออาหารใน query
            ingredients = ", ".join(recipe['ingredients'])
            return f"สูตรอาหาร: {recipe['name']}\nส่วนผสม: {ingredients}\nวิธีทำ: {recipe['instructions']}"

    # ถ้าหากไม่พบชื่อสูตรอาหารให้ส่งข้อความว่าไม่พบข้อมูล
    return None

def chat_with_model(text):
    global chat_history_ids

    # การสร้างการสนทนาใหม่
    new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')

    # ถ้ามีประวัติการสนทนาแล้ว ก็เชื่อมประวัติการสนทนากับข้อความใหม่
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if chat_history_ids is not None else new_user_input_ids

    # สร้างคำตอบจากโมเดล
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # แปลงคำตอบจากโมเดลกลับเป็นข้อความ
    return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

if __name__ == '__main__':
    app.run(debug=True)
