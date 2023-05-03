import streamlit as st
import math

import base64
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("image.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://isinhvien.com/wp-content/uploads/t-leech-pro/2022/06/22/isinhvien-311-p5-1024x576.jpg");
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

def gptb2(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                ket_qua = 'PTB1 có vô số nghiệm'
            else:
                ket_qua = 'PTB1 vô nghiệm'
        else:
            X = -c/b
            ket_qua = 'PTB1 có nghiệm %.2f' % X
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            ket_qua = 'PTB2 vô nghiệm'
        else:
            X1 = (-b + math.sqrt(delta))/(2*a)
            X2 = (-b - math.sqrt(delta))/(2*a)
            ket_qua = 'PTB2 có nghiệm X1 = %.2f và X2 = %.2f' % (X1, X2)
    return ket_qua

def clear_input():
    st.session_state["nhap_a"] = 0.0
    st.session_state["nhap_b"] = 0.0
    st.session_state["nhap_c"] = 0.0

st.subheader('Giải phương trình bậc 2')
with st.form(key='columns_in_form', clear_on_submit = False):
    a = st.number_input('Nhập a', key = 'nhap_a')
    b = st.number_input('Nhập b', key = 'nhap_b')
    c = st.number_input('Nhập c', key = 'nhap_c')
    c1, c2 = st.columns(2)
    with c1:
        btn_giai = st.form_submit_button('Giải')
    with c2:
        btn_xoa = st.form_submit_button('Xóa', on_click=clear_input)
    if btn_giai:
        s = gptb2(a, b, c)
        st.markdown('<span style="color:black;font-size:18px">Kết quả: ' + s + '</span>', unsafe_allow_html=True)
    else:
       st.markdown('<span style="font-size:18px">Kết quả:</span>', unsafe_allow_html=True)