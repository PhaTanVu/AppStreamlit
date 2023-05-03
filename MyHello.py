import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Chào mừng bạn đến với website của Phan Tấn Vũ 👋")

st.sidebar.success("Bạn có thể chọn một trong các dự án của tôi ở trên.")

st.markdown(
    """
    Xin chào!Cảm ơn bạn đã ghé thăm website của tôi. 
    Ở đây là những dự án tôi học được từ môn học ** Học Máy** và ** Thị Giác Máy** của Thầy ** Trần Tiến Đức **.
    Website này được tạo ra để nhằm mục đích báo cáo project cuối kì cho 2 môn học trên và chỉ dùng để phục vụ mục đích học tập.
    **👈 Bạn có thể tham khảo những dự án mà tôi học được ở bên phải.**
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
