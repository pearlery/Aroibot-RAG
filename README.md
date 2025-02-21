# Project
## AroiBot ChatBot

# About
Chatbot for answering questions about matters Thai food recipe menu: You can ask AroiBot about the food menu you want to make. What raw materials are required and what are the steps for making it?


# Installation & Setup

[Install Python] https://www.python.org/downloads/

### [Install pip]

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py


``` 
python3 get-pip.py 
```


Ensure pip is installed by running the following command

``` 
pip --version 
```
``` 
Python.org 
```
``` 
Download Python 
```
The official home of the Python Programming Language

If you have Python & pip installed then check their version in the terminal or command line tools

``` 
python3 --version 
```


``` 
pip --version 
```

## Libraries required.
* flask
* transformers
* torch

Installing Libraries required
In your terminal run the requirements.txt file using this pip

``` 
pip install -r requirements.txt 
```



## Running ChatBot Application in Terminal
cd into your directory

``` 
python app.py 
```


What you will create
In this tutorial, I will guide you through the process of building a chatbot that can carry out conversations with users using natural language processing.

To start, we will be using Microsoft DialoGPT, a pre-trained language model that can generate human-like responses to given prompts. We will be integrating DialoGPT with Flask, a popular Python web framework, to create a web application that can communicate with users via a chat interface.

For the frontend of our application, we will be using HTML, CSS, and JavaScript to create a visually appealing and interactive chat interface.

ChatBot Link
The Chatbot is constructed using the Microsoft/DialoGPT-medium model.

curl https://huggingface.co/microsoft/DialoGPT-medium


Recipe Datasets our collected information from many sources. 
We've cleaned up the data and converted it into a single, easy-to-use format in the recipes.json file.
You can find the original datasets in the data folder.
Examples of primary data sources

curl https://huggingface.co/datasets/pythainlp/thai_food_v1.0/blob/main/data/train-00000-of-00001-e8b362f32bb3715c.parquet



Sample menu 50 from 194

1. ต้มยำกุ้ง
2. ผัดไท
3. ข้าวผัด
4. แกงเขียวหวานไก่
5. ข้าวมันไก่
6. แกงจืดเต้าหู้หมูสับ
7. หมูทอดกระเทียม
8. ส้มตำ
9. ขนมจีนน้ำยา
10. ยำวุ้นเส้น
11. ข้าวต้ม
12. แกงมัสมั่น
13. ข้าวคลุกกะปิ
14. แกงป่า
15. ปลาทอดน้ำปลา
16. ยำปลาดุกฟู
17. หมูปิ้ง
18. ผัดกระเพรา
19. ขนมถ้วย
20. ขนมเบื้อง
21. ข้าวผัดกุ้ง
22. หมูทอดพริกเกลือ
23. แกงส้ม
24. ข้าวต้มมัด
25. ขนมชั้น
26. ขนมกรอบ
27. ผัดพริกไทยดำ
28. สตูว์เนื้อ
29. ข้าวเหนียวสังขยา
30. น้ำพริกอ่อง
31. ข้าวหมกไก่
32. ต้มแซ่บหมู
33. แกงเลียง
34. ผัดขี้เมา
35. ข้าวราดกระเพรา
36. ไข่เจียว
37. น้ำพริกปลาทู
38. หมูย่าง
39. ต้มยำปลาหมึก
40. ผัดผักบุ้งไฟแดง
41. ข้าวหน้าเป็ด
42. แกงจืดหมูสับ
43. ขนมปังปิ้งสังขยา
44. ข้าวต้มปลากะพง
45. สุกี้น้ำ
46. หมูสเต๊ะ
47. ข้าวเหนียวมะม่วง
48. ขนมครก
49. แกงเผ็ดเนื้อ
50. ผัดผักรวมมิตร
