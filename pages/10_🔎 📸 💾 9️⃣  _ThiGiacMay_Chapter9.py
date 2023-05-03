import cv2
import numpy as np
import streamlit as st
import Chapter09 as c9

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

    st.sidebar.title("Chapter9")

    sub_menu = ["Erosion", "Dilation", "OpeningClosing", "Boundary", "HoleFilling", "Mouse", "HoleFillingMouse", "ConnectedComponent", "CountRice"]
    sub_choice = st.sidebar.selectbox("Select a chapter9 function", sub_menu)

    if sub_choice == "Erosion":
        if "image" in locals():
            imgout = c9.Erosion(image)
            st.image(imgout, use_column_width=True)
        else:
            st.warning("Please open an image first.")

    elif sub_choice == "Dilation":
        if "image" in locals():
            imgout = c9.Dilation(image)
            st.image(imgout, use_column_width=True)
        else:
            st.warning("Please open an image first.")

    elif sub_choice == "OpeningClosing":
        if "image" in locals():
            imgout = c9.OpeningClosing(image)
            st.image(imgout, use_column_width=True)
        else:
            st.warning("Please open an image first.")
    elif sub_choice == "Boundary":
        if "image" in locals():
            imgout = c9.Boundary(image)
            st.image(imgout, use_column_width=True)
        else:
            st.warning("Please open an image first.")

    elif sub_choice == "HoleFilling":
        if "image" in locals():
            imgin = c9.HoleFilling(image)
            st.image(imgin, use_column_width=True)
        else:
            st.warning("Please open an image first.")
    elif sub_choice == "Mouse":
        if "image" in locals():
            imgout = c9.Mouse(image)
            mask = np.zeros((image.shape[0] + 2, image.shape[1] + 2), np.uint8)
            st.write("Click and drag to fill areas with white")
            st_canvas = st.get_canvas(0, height=image.shape[0])
            st_canvas.set_on_mouse_down_handler(lambda x, y: cv2.floodFill(image, mask, (x, y), (255,255,255)) or st_canvas.image(image))
            st_canvas.image(image)
            st.image(imgout, use_column_width=True)
        else:
            st.warning("Please open an image first.")
    elif sub_choice == "HoleFillingMouse":
        if "image" in locals():
           M, N, _ = image.shape
           mask = np.zeros((M+2, N+2), np.uint8)
           st.write("Click and drag to fill areas with white")
           st_canvas = st.image(image, use_column_width=True, caption="ImageIn")
           st_canvas = st_canvas._get_streamlit_component()
           st_canvas.set_on_canvas_clicked(lambda x, y: cv2.floodFill(image, mask, (y, x), (255, 255, 255)) or st_canvas.image(image))
           st_canvas.image(image)
           st.image(imgout, use_column_width=True)
        else:
            st.warning("Please open an image first.")

    elif sub_choice == "ConnectedComponent":
        if "image" in locals():
            imgin = c9.ConnectedComponent(image)
            st.image(imgin, use_column_width=True)
        else:
            st.warning("Please open an image first.")
    
    elif sub_choice == "CountRice":
        if "image" in locals():
            imgin = c9.CountRice(image)
            st.image(imgin, use_column_width=True)
        else:
            st.warning("Please open an image first.")

    

if __name__ == '__main__':
    main()