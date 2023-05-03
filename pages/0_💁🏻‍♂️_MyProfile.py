import streamlit as st
import base64
from pydub import AudioSegment
from pydub.playback import play
# Set page config
st.set_page_config(
    page_title="Personal Information",
    page_icon=":guardsman:",
    layout="wide"
)
st.markdown(
    "<h1 style='text-align: center'>👱🏻‍♂️ MY PROFILE </h1>",
    unsafe_allow_html=True,
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
    h1 {{
        color:  brown;}}
    p, h4 {{ color: Black;}}
    h2 {{ color : white;


    }}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True
)

# Define function to read image file as base64 string
@st.cache_data
def get_image_download_link(image_path):
    with open(image_path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:file/jpg;base64,{b64}" download="{image_path}">Download image</a>'
    return href

# Define function to play audio
def play_music(file):
    audio = AudioSegment.from_file(file, format="mp3")
    play(audio)

# Define page layout
col1, col2 = st.columns((2,3))

# Add image to column 1
with col1:
    st.title("📸👱🏻‍♂️👇🏻")
    st.image("avatar.jpg", use_column_width=True)
    #st.markdown(get_image_download_link("avatar.jpg"), unsafe_allow_html=True)

# Add text to column 2
with col2:
    st.header("👤Thông tin cá nhân")
    st.markdown(
        """
        - #### **👱🏻‍♂️Họ và tên:  Phan Tấn Vũ.**
        - #### **🪪MSSV:  20146463.**
        - #### **🏢Trường ĐH:  Đại học Sư phạm Kỹ thuật TP. Hồ Chí Minh.**
        - #### **🏠Quê quán:  Quảng Ngãi.**
        - #### **📞Phone:  0353723536.**
        - #### **📩Mail:  Bevu19042002@gmail.com.**
        

        """
    )

# Add music player
st.write("🎶 **Play My Music**")

# Define function to read audio file as base64 string
@st.cache_data
def get_audio_download_link(audio_path):
    with open(audio_path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:audio/mp3;base64,{b64}" download="{audio_path}">Download audio</a>'
    return href

# Define audio file path
audio_file = open('Arena of Valor Soundtrack AOV.mp3', 'rb')
audio_bytes = audio_file.read()

# Define state to store music player status
play_music = st.checkbox('Play music')

# Add music player using audio tag
if play_music:
    st.audio(audio_bytes, format='audio/mp3', start_time=0)
else:
    st.write('Music is paused')

# Add button to download music file
st.markdown(get_audio_download_link("Arena of Valor Soundtrack AOV.mp3"), unsafe_allow_html=True)


def main():
    pass

if __name__ == '__main__':
    main()
