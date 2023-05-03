import streamlit as st
import cv2
import numpy as np
import Chapter05 as c5
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

def main():
    st.title("Machine Vision")

    menu = ["Open", "OpenColor", "Save", "Exit"]
    choice = st.sidebar.selectbox("Select an action", menu)

    if choice == "Open":
        st.set_option('deprecation.showfileUploaderEncoding', False)
        file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "bmp", "tif"])
        if file:
            image = cv2.imdecode(np.fromstring(file.read(), np.uint8), 0)
            st.image(image, use_column_width=True)

    elif choice == "OpenColor":
        st.set_option('deprecation.showfileUploaderEncoding', False)
        file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "bmp", "tif"])
        if file:
            image = cv2.imdecode(np.fromstring(file.read(), np.uint8), 1)
            st.image(image, channels="BGR", use_column_width=True)

    elif choice == "Save":
        st.warning("This feature is not available in Streamlit.")

    elif choice == "Exit":
        st.stop()

    st.sidebar.title("Chapter5")

    sub_menu = ["CreateMotionNoise", "DenoiseMotion", "DenoisestMotion"]
    sub_choice = st.sidebar.selectbox("Select a chapter5 function", sub_menu)

    if sub_choice == "CreateMotionNoise":
        if "image" in locals():
            imgout = c5.CreateMotionNoise(image)
            st.image(imgout, use_column_width=True)
        else:
            st.warning("Please open an image first.")

    elif sub_choice == "DenoiseMotion":
        if "image" in locals():
            imgout = c5.DenoiseMotion(image)
            st.image(imgout, use_column_width=True)
        else:
            st.warning("Please open an image first.")

    elif sub_choice == "DenoisestMotion":
        if "image" in locals():
            temp = cv2.medianBlur(image, 7)
            imgout = c5.DenoiseMotion(temp)
            st.image(imgout, use_column_width=True)
        else:
            st.warning("Please open an image first.")


if __name__ == "__main__":
    main()
