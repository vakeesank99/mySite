from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir /"styles"/ "main.css"
resume_file = current_dir / "assets" / "vakeesan_resume1.pdf"
profile_pic = current_dir / "assets" / "profile.png"

#emoji link https://emojidb.org/arrow-emojis?user_typed_query=1&utm_source=user_search

PAGE_TITLE = "Vakeesan Karunanithy"
PAGE_ICON = ":memo:"
NAME="Vakeesan Karunanithy"
DESCRIPTION = '''
Final year student of Electronic & Telecommunication Engineering at University of Moratuwa

'''
EMAIL = "vakeesank99@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn🔗": "https://linkedin.com/in/vakeesan-karunanithy-70a394207",
    "Github🔗": "https://github.com/vakeesank99"
}
PROJECTS= {
    "Image processing on ZYNQ SoC" : "https://github.com/vakeesank99/Image_processing_on_ZYNQ",
    "Matrix multiplication IP" : "https://github.com/vakeesank99/Matrix_multiplication_ip",
    "Flowers image classification using CNN" : "https://github.com/vakeesank99/flower102classifier",
    "Lead-acid battery charger" :"https://github.com/vakeesank99/Lead-acid-battery-charger",
    "PIR sensor module using analog components" : "https://github.com/vakeesank99/PIR_sensor_module_using_basic_components",
    "RGB colour sensor using analog components" : "https://github.com/Dinuka-1999/RGB_Sensor_project_group_26"

}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")
# st.title("Hello there!")

with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    resume_bytes = pdf_file.read()
profile_pic = Image.open(profile_pic)



col1,col2 = st.columns(2,gap = "small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button("Download Resume",
                        resume_bytes, 
                        file_name= resume_file.name,
                        mime="application/oclet-stream")
    st.write("📧", EMAIL)
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform, ink) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({ink})")
    # with cols[index]:
    #     st.markdown(f"[{platform}]({ink})")
st.write("#")
st.subheader("Education")
st.write(
    '''
        - B.Sc. Engineering Hons. in Electronic and Telecommunication Engineering at University of Moratuwa
        - G.C.E. Advanced Level in physical science stream 
        '''
)

st.write("#")
st.subheader("Hard skills")
st.write(
    '''
    - 👨🏻‍💻 Programming: Python, C , C++
    - 📊 Frameworks: Pytorch, Tensorflow
    -  🖥️  HDL: Verilog, SystemVerilog


'''
)

#work experience
st.write("#")
st.subheader("Work History")
st.write("---")

#job1
st.write("**🚧 Electronic Engineering Intern | ExcelTech OU**")
st.write("01/2023 - 06/2023")
st.write(
    '''
    - ▶ ️ Worked in PCB hardware debugging and firmware development.
    - ▶ ️ Found a method in hand soldering to deliver the samples on time.
    - ▶ ️ PCB antenna impedance matching using MATLAB

'''
)

#job2
st.write("#")
st.write("**🚧 Visiting Instructor(Full-time) | University of Moratuwa**")
st.write("08/2023 - 12/2023")
st.write(
    '''
    - ▶ ️ Guided first year students to understand the basic of analog and digital electronics
    - ▶ ️ Taught fundamentals of development boards such as Intel's Altera FPGAs and STM32 
    - ▶ ️ Given an analog project inorder to apply analog electronics knowledge 

'''
)

#job3
st.write("#")
st.write("**🚧 Visiting Instructor(Part-time) | University of Moratuwa**")
st.write("10/2022 - 02/2023")
st.write(
    '''
    - ▶ ️ Taught second year students the introduction to robotics.
    - ▶ ️ Introduced wide variety of topics and tools such as PID controlling, Interrupt and polling, Servo motor controlling.  
    - ▶ ️ Basic movement of robots were taught from fundamental knowledge about encoders and their usage 

'''
)


#projects
st.write("#")
st.subheader("Projects")
st.write("---")

for project, link in PROJECTS.items():
    st.write(f"- 🏆[{project}]({link})")