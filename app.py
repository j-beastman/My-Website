import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import json


st.set_page_config(page_title="John Eastman", page_icon="🦦")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottiefile(path):
    with open(path, "r") as f:
        return json.load(f)


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_github = load_lottiefile("images/animation_ll78d7sr.json")
# img_contact_form = Image.open("images/yt_contact_form.png")
# img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        # st.image("images/IMG_3964.JPG")
        st.title("Hi, I'm John :wave:")
        st.subheader("Thank you for checking out my page!")
    with right_column:
        image = 'images/github.png'
        st.markdown(f"<a href='https://github.com/j-beastman' target='_blank'><img src={image} width='100'></a>", unsafe_allow_html=True)
        
# ---- Skills ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Skills")
        st.write(
            """
            Languages: Python, C++, C,  \n
            SDKs: Streamlit, Langchain, Deeplake, DataRobot, pandas, scikit-learn
            Development Tools: git, TDD, DDD, Excel, Adobe Illustrator & Photoshop
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=100, key="coding")

# ---- Experiences ----
with st.container():
    st.write("---")
    
    st.header("Experiences")
    st.write("#####") # Inserts a space
    st.write(
        """
        **MAKE MORE PURPOSE ORIENTED, why did I do x, what did it solve?
        - TA at Tufts University (Fall 2023):
            - TA for CS40, "Machine Structure and Assembly Language Programming"
            - Teach low-level programming practices (in C)
        - Intern Engineer at DataRobot (Summer 2023):
            - Placed 2nd in company-wide hackathon with "RFP Monster"
            - Performed pre/post sales work with the Data Science team
            - Helped develop the datarobotx python sdk package 
            - Created 'accelerator' notebooks for the DataRobot community
            - Developed forecasts for Warner Brothers' "Barbie"
        - Boathouse Custodian @ Bacow Sailing Pavilion (2022-2023):
            - Head of maintenance and repair for Tufts' fleet of 27 sailboats and two motorboats
            - Perform professional-grade fiberglass repairs
        - Head Sailing Instructor @ American Yacht Club:
            - Led a team of a dozen instructors to teach ~100 young sailors
            - Organized home events for the junior program
            - Personalized schedules & routines for competitive sailors in the program
        """
    )

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        print("Y")
    with text_column:
        st.subheader("RFP Monster")
        st.write(
            """
            The RFP Monster has a unique workflow. 
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        print("X")
    with text_column:
        st.subheader("TABot")
        st.write(
            """
            """
        )

# ---- Skills ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Education & Coursework")
        st.subheader("Candidate for Bachelor of Science in Computer Science")
        st.write("Current GPA: 3.78/4.0 \n"
                 "Expected Graduation: Fall 2024")
        st.write("##")
        st.write(
            """
            - Computer Science:
                - Artificial Intelligence
                - Intro to ML
                - Data Structures
                - Machine Structure & Assembly Language
                - Algorithms
            - Mathematics:
                - Probability
                - Linear Algebra
                - Discrete Mathematics
            - Economics & Finance:
                - Intro to Finance
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/john@bee-haven.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
