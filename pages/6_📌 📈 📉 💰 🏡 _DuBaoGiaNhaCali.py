import joblib
import streamlit as st
import pandas as pd
import numpy as np

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

def my_format(x):
    s = "{:,.0f}".format(x)
    L = len(s)
    if L < 14:
        s = '&nbsp'*(14-L) + s
    return s


forest_reg = joblib.load("forest_reg_model.pkl")

column_names=['longitude','latitude','housing_median_age','total_rooms',
              'total_bedrooms','population','households','median_income',
              'rooms_per_household','population_per_household',
              'bedrooms_per_room','ocean_proximity_1', 
              'ocean_proximity_2', 'ocean_proximity_3', 
              'ocean_proximity_4', 'ocean_proximity_5']
st.subheader('Dự báo giá nhà California')
x_test = pd.read_csv('x_test.csv', header = None, names=column_names)
y_test = pd.read_csv('y_test.csv', header = None)
y_test = y_test.to_numpy()
N = len(x_test)
st.dataframe(x_test)
get_5_rows = st.button('Lấy 5 hàng ngẫu nhiên và dự báo')
if get_5_rows:
    index = np.random.randint(0,N-1,5)
    some_data = x_test.iloc[index]
    st.dataframe(some_data)
    result = 'y_test:' + '&nbsp&nbsp&nbsp&nbsp' 
    for i in index:
        s = my_format(y_test[i,0])
        result = result + s
    result = '<p style="font-family:Consolas; color:Blue; font-size: 15px;">' + result + '</p>'
    st.markdown(result, unsafe_allow_html=True)

    some_data = some_data.to_numpy()
    y_pred = forest_reg.predict(some_data)
    result = 'y_predict:' + '&nbsp'
    for i in range(0, 5):
        s = my_format(y_pred[i])
        result = result + s
    result = '<p style="font-family:Consolas; color:Blue; font-size: 15px;">' + result + '</p>'
    st.markdown(result, unsafe_allow_html=True)

