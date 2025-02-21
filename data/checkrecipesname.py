import json
from collections import Counter

# โหลดข้อมูลจากไฟล์ JSON
with open("ChatBot/data/recipes.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# ดึงชื่อเมนูทั้งหมด
names = [recipe["name"] for recipe in data]

# นับจำนวนชื่อที่ซ้ำกัน
duplicates = {name: count for name, count in Counter(names).items() if count > 1}

# แสดงผล
if duplicates:
    print("พบชื่อเมนูซ้ำกัน:")
    for name, count in duplicates.items():
        print(f"- {name}: {count} ครั้ง")
else:
    print("ไม่พบชื่อเมนูซ้ำกัน")