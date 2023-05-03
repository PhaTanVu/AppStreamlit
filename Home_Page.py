import streamlit as st
import base64

st.set_page_config(
    page_title="Phan Tấn Vũ",
    page_icon="👋",
    
)
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
background-image: url("https://anhdepfree.com/wp-content/uploads/2022/05/anh-nen-gaming-4k_959021.jpg");
background-size: 200%;
background-position: 30% 45%;
background-repeat: no-repeat;
background-attachment: local;
color:black;
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
<style>
    h2, h4, h1 {{
        color:  brown;}}
    p {{ color: white

    }}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True
)



st.write("# Chào mừng bạn đến với website của Phan Tấn Vũ 👋")

st.sidebar.success("Bạn có thể chọn một trong các dự án của tôi ở trên.")

st.markdown(
    
    
    """
    ***Xin chào!Cảm ơn bạn đã ghé thăm website của tôi.***
    ***Ở đây là những dự án tôi học được từ môn học Học Máy và Thị Giác Máy của Thầy Trần Tiến Đức.***
    ***Website này được tạo ra để nhằm mục đích báo cáo project cuối kì cho 2 môn học trên và chỉ dùng để phục vụ mục đích học tập.***
    ***👈 Bạn có thể tham khảo những dự án mà tôi học được ở bên phải.***
    #### Thông tin của tôi:
    - ****Họ và tên : Phan Tấn Vũ.****
    - ****Mã số sinh viên : 20146463.****
    - ****Trường đại học : Đại học Sư phạm Kỹ thuật TP. Hồ Chí Minh.****

    #### Liên hệ với tôi:
    - ****Gifhub:**** https://github.com/PhaTanVu
    - ****Facebook:**** https://www.facebook.com/profile.php?id=100038164449673&mibextid=LQQJ4d
    - ****Mail:**** bevu19042002@gmail.com
    - ****Phone:**** 0353723536
    #### Thông tin giảng viên hướng dẫn:
    - ****Thầy: Trần Tiến Đức.****
    - ****Mail:**** ductt@hcmute.edu.vn
    - ****Phone:**** 0919622862
    - ****Gifhub:**** https://github.com/TranTienDuc
"""
)
