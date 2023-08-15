import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import json


st.set_page_config(page_title="John Eastman", page_icon="🦦", layout="centered")


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
# lottie_github = load_lottiefile("images/animation_ll78d7sr.json")

# ---- Links ----
with st.container():
    resume, github, linkedin, photography = st.columns(4)
    with resume:
        st.markdown("[![resume](./app/static/resume.png)](http://google.com.au/)")
    with github:
        st.markdown("[![github](./app/static/github.png)](https://github.com/j-beastman)")
    with linkedin:
        st.markdown("[![linkedin](./app/static/linkedin.png)](https://www.linkedin.com/in/john-eastman-614174144/)")
    with photography:
        st.markdown("[![photography](./app/static/photography.png)](https://www.eecs.tufts.edu/~jeastm01/photo.html)")


# ---- BIO SECTION ----
with st.container():
    st.write("---")
    picture,left_column = st.columns([1, 2], gap="small")
    with picture:
        st.markdown("[![me](./app/static/john.png)](https://www.eecs.tufts.edu/~jeastm01/photo.html)")
    with left_column:
        st.subheader("Hi, I'm John :wave:")
        st.write("I'm happy you're here! Please explore my projects below; they are my pride and joy. "
                 "Above you'll find the images link to my resume, Github, LinkedIn, and my photography website. "
                 "If you want to copy this template and make your own resume website, find the project on my Github!")
   
# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((2, 3))
    with image_column:
        st.markdown("[![rfp_monster](./app/static/rfp_monster.gif)](https://www.eecs.tufts.edu/~jeastm01/photo.html)")
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
            TABot follows the same workflow as the RFP monster. It's really just a knowledge base
            for a computer science course's cirriculum. Why is it special?
            - Piazza API (link)
            - Chatting, working with different langchain features.
            - Took everything I learned from RFP Monster and improved on it.
            - Scheduled updates the RFP monster.
            """
        )

# ---- Skills ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns([2,1])
    with left_column:
        st.subheader("Skills")
        st.write(
            """
            Languages: Python, C++, C  \n
            SDKs: Streamlit, Langchain, Deeplake, DataRobot, pandas, scikit-learn \n
            Development Tools: git, TDD, DDD, Excel, Adobe Illustrator & Photoshop
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=150, key="coding")

# ---- Experiences ----
with st.container():
    st.write("---")
    st.header("Experiences")
    option = st.radio(
                'Select to see more information',
                    ('Teaching Assistant in CS', 
                    'Intern Engineer at DataRobot', 
                    'Boathouse Custodian @ Bacow Sailing Pavilion',
                    'Head Sailing Instructor @ American Yacht Club'))
    if option == 'Teaching Assistant in CS':
        st.markdown("![tufts](./app/static/Tufts_blue.png)")
        st.write("""- TA for CS40, "Machine Structure and Assembly Language Programming"
            - Teach low-level programming practices (in C)
                 """)
    elif option == 'Intern Engineer at DataRobot':
        st.markdown("![datarobot](./app/static/datarobot.png)")
        st.write("""
            - Placed 2nd in company-wide hackathon with "RFP Monster"
            - Performed pre/post sales work with the Data Science team
            - Helped develop the datarobotx python sdk package 
            - Created 'accelerator' notebooks for the DataRobot community
            - Developed forecasts for Warner Brothers' "Barbie"
            - Called 'Eastman the Beastman' by the CCO
                 """)
    elif option == 'Boathouse Custodian @ Bacow Sailing Pavilion':
        st.markdown("![tufts_sailing](./app/static/tuftssailing.png)")
        st.write("""
            - Head of maintenance and repair for Tufts' fleet of 27 sailboats and two motorboats
            - Perform professional-grade fiberglass repairs
                    """)
    elif option == 'Head Sailing Instructor @ American Yacht Club':
        st.markdown("![ayc](./app/static/ayc.png)")
        st.write("""
            - Led a team of a dozen instructors to teach ~100 young sailors
            - Organized home events for the junior program
            - Personalized schedules & routines for competitive sailors in the program
        """)

# ---- Education & Coursework ----
with st.container():
    st.write("---")
    
    st.header("Education & Coursework")
    st.subheader("Candidate for Bachelor of Science in Computer Science")
    st.write("Current GPA: 3.78/4.0 --- Expected Graduation: Fall 2024")
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
    
    st.markdown(contact_form, unsafe_allow_html=True)
    
