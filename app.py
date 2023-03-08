import streamlit as st
from time import sleep
import easyocr
import pandas as pd
import re
import psycopg2

image_file=''
global con

def DisplayInfo():
    with placeholder.container():
        reader = easyocr.Reader(['en'])
        img=image_file.read()
        result = reader.readtext(img,paragraph="False",detail=0)
        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", ' '.join(result))
        phonenos = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]',' '.join(result))
        st.write(result)

def ConnectToDatabase():
    con = psycopg2.connect(
        database="likitha",
        user="postgres",
        password="PASSWORD",
        host="localhost",
        port= '5432'
        )

def DisplayRecordsFromDatabase():
    cursor_obj = con.cursor()
    cursor_obj.execute("SELECT * FROM BusinessCards")
    print(cursor_obj.fetchall())

placeholder = st.empty()
with placeholder.container():
    image_file = st.file_uploader("Upload business card",type=['png','jpg','jpeg'],help='Please upload files in format png,jpg,jpeg')
if image_file is not None:
    placeholder.empty()
    sleep(0.01)
    DisplayInfo()
    print("Image Uploaded successfully")
else:
    print("Image not uploaded")
