import streamlit as st
from PIL import Image

# Configuring the page
st.set_page_config(page_title="My Portfolio", page_icon=":briefcase:", layout="wide")

# Adding custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;
    }
    .main {
        background: linear-gradient(135deg, #1e1e1e, #2d2d2d);
        padding: 20px;
        border-radius: 10px;
        color: #d4d4d4;
    }
    .stButton button {
        background-color: #61dafb;
        color: white;
        border-radius: 5px;
    }
    .stButton button:hover {
        background-color: #4caf50;
        color: white;
    }
    .stTextInput input {
        border-radius: 5px;
        background-color: #3c3c3c;
        color: white;
    }
    .header-title {
        color: #61dafb;
        font-size: 2.5em;
    }
    .project-title {
        color: #61dafb;
        font-size: 1.5em;
    }
    .card {
        background-color: #2d2d2d;
        border-radius: 10px;
        margin: 10px;
        transition: all 0.3s ease;
        box-shadow: 0 8px 8px rgba(0, 0, 0, 0.1);
        color: #d4d4d4;
        text-align: center;
        text-decoration: none;
        height: 600px; /* Adjusted height for better display of images */
    }
    .card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    .card a {
        text-decoration: none;
        color: #61dafb;
        display: block;
        height: 100%;
    }
    .navbar {
        background-color: #252526;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        margin-top: 0;
    }
    .navbar a {
        color: #61dafb;
        margin: 0 15px;
        text-decoration: none;
        font-size: 1.2em;
    }
    .navbar a:hover {
        color: #4caf50;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar content
st.sidebar.title("Welcome to My Portfolio")
st.sidebar.write("Hi! I'm Lomesh Soni, a Software Engineer.")
st.sidebar.write("Here you can find information about my projects, skills, and ways to contact me.")
st.sidebar.image("lomesh.jpg", caption="Your Image Here", use_column_width=True)

# Navigation bar
st.markdown("""
    <div class="navbar">
        <a href="https://github.com/Lomesh2000" target="_blank">GitHub</a>
        <a href="https://www.linkedin.com/in/lomesh-soni" target="_blank">LinkedIn</a>
        <a href="mailto:lomeshsoniwork@gmail.com" target="_blank">Email</a>
    </div>
    """, unsafe_allow_html=True)

# Home page content
st.markdown('<div class="main">', unsafe_allow_html=True)

# Projects section
st.markdown('<div class="header-title">My Projects</div>', unsafe_allow_html=True)
st.write("Here are some of the projects I've worked on:")

# Create a two-column layout for projects
col1, col2 = st.columns(2)

github_links = ['https://github.com/Lomesh2000/Algorithmic-Trading-using-LSTM',
                'https://github.com/Lomesh2000/movies-recommender',
                'https://github.com/Lomesh2000/driver-drowsiness-detection']

project_title = ['Algorithm Trading using LSTM', 'Movies Recommender System', 
                 'Project 3: Driver Drowsiness Detection']

# Path to your images
image_paths = ['path/to/your/image1.png', 'path/to/your/image2.png', 'path/to/your/image3.png']

# Function to resize images
def resize_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    return img

# Display projects
with col1:
    for i in range(0, len(github_links), 2):
        st.markdown(f"""
        <a href="{github_links[i]}" class="card">
            <h3>{project_title[i]}</h3>
            <p>Description of {project_title[i]}.</p>
        </a>
        """, unsafe_allow_html=True)
        st.image(resize_image(f'images/{str(i+1)}.png', 400, 300), caption=f"Project {i+1} Image", use_column_width=True)

with col2:
    for i in range(1, len(github_links), 2):
        st.markdown(f"""
        <a href="{github_links[i]}" class="card">
            <h3>{project_title[i]}</h3>
            <p>Description of {project_title[i]}.</p>
        </a>
        """, unsafe_allow_html=True)
        st.image(resize_image(f'images/{str(i+1)}.png', 400, 300), caption=f"Project {i+1} Image", use_column_width=True)

# Contact section
st.markdown('<div class="header-title">Contact Me</div>', unsafe_allow_html=True)
st.write("Feel free to reach out to me through the following channels:")
st.markdown("""
- [Email](mailto:lomeshsoniwork@gmail.com)
- [GitHub](https://github.com/Lomesh2000)
- [LinkedIn](https://www.linkedin.com/in/lomesh-soni)
""")

# Adding a contact form
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit_button = st.form_submit_button(label="Send")

if submit_button:
    st.success(f"Thank you {name}! Your message has been received.")