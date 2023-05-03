import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json 
from tensorflow.keras.optimizers import SGD 
import cv2
import numpy as np
import base64

st.set_page_config(page_title="Chào Mừng Bạn Đến Với Website Nhận Dạng Chữ Số Viết Tay Của Phan Tấn Vũ", page_icon=":pencil2:")
st.title("Nhận dạng chữ số viết tay")
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("image.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size: 200%;
background-position: 30% 45%;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: 50% 45%;
background-size: 400%;
}}
[data-testid="stSidebarNav"] span {{
color:white;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True
)

model_architecture = "digit_config.json"
model_weights = "digit_weight.h5"
model = model_from_json(open(model_architecture).read())
model.load_weights(model_weights) 

optim = SGD()
model.compile(loss="categorical_crossentropy", optimizer=optim, metrics=["accuracy"]) 

mnist = keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
X_test_image = X_test

RESHAPED = 784

X_test = X_test.reshape(10000, RESHAPED)
X_test = X_test.astype('float32')

#normalize in [0,1]
X_test /= 255

def create_digit_random_image():
    index = np.random.randint(0, 9999, 150)
    digit_random = np.zeros((10*28, 15*28), dtype = np.uint8)
    for i in range(0, 150):
        m = i // 15
        n = i % 15
        digit_random[m*28:(m+1)*28, n*28:(n+1)*28] = X_test_image[index[i]] 
    cv2.imwrite('digit_random.jpg', digit_random)

    image = Image.open('digit_random.jpg')
    return image


def draw_digit_prediction(image, prediction, color):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 24)
    width, height = image.size
    cell_width = width // 15
    cell_height = height // 10
    
    # Chuyển kết quả nhận dạng từ 1 chiều sang ma trận 10x15
    pred_matrix = np.argmax(prediction, axis=1).reshape(10, 15)
    
    # Duyệt qua từng phần tử của ma trận kết quả và in lên ảnh
    for row in range(pred_matrix.shape[0]):
        for col in range(pred_matrix.shape[1]):
            digit = pred_matrix[row][col]
            x = col * cell_width + 5
            y = row * cell_height + 5
            draw.text((x, y), str(digit), font=font, fill=color)

    return image


def predict_digits(image):
    X_test_sample = np.zeros((150,784), dtype = np.float32)
    for i in range(0, 150):
        row = i // 15
        col = i % 15
        x = col * 28
        y = row * 28
        digit = image.crop((x, y, x+28, y+28))
        X_test_sample[i] = np.asarray(digit).reshape(1, -1)
    
    prediction = model.predict(X_test_sample)
    return prediction


def main():
    

    col1, col2 = st.columns([1, 1])
    with col1:
        st.write('## Tạo ảnh chữ số')
        btn_tao_anh = st.button('Tạo ảnh')
        if btn_tao_anh:
            image = create_digit_random_image()
            st.image(image, width=350, caption='Ảnh chữ số viết tay')
            st.write('**Hướng dẫn**: Nhấn "Nhấn nhận dạng" để hiển thị kết quả')
            st.session_state['image'] = image

    with col2:
        st.write('## Kết quả nhận dạng')
        btn_nhan_dang = st.button('Nhận dạng')
        if btn_nhan_dang:
            image = Image.open('digit_random.jpg')
            prediction = predict_digits(image)
            image_with_prediction = draw_digit_prediction(image, prediction, color='red')
            st.image(image_with_prediction, width=350, caption='Kết quả nhận dạng chữ số')
            
            st.write('**Kết quả**: ')
            results = np.argmax(prediction, axis=1)
            columns = st.columns(15)
            for i in range(len(results)):
                with columns[i%15]:
                    st.write(results[i], font_size=50, bg_color='red', text_color='black', style='text-align: center')

if __name__ == '__main__':
    main()
