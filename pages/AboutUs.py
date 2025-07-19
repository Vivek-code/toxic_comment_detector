# Welcome.py

import streamlit as st
import base64

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Welcome - Toxic Comment Detector",
    page_icon="👋",
    layout="wide"
)

# # --- BACKGROUND IMAGE ---
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     .stApp {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)

# # Make sure the path is correct
# set_png_as_page_bg('assets/background.jpg')


# --- PAGE CONTENT ---
st.title("👋 Welcome to the Live Stream Chat Moderator")
st.markdown("""
This project is a real-time moderation assistant designed to automatically detect and filter toxic comments from live stream chats. 
It uses a sophisticated machine learning model to classify comments into categories like toxic, obscene, threat, and insult, helping to create a safer and more positive environment for streamers and viewers.
""")
st.divider()

# --- HOW TO USE ---
st.header("📖 How to Use the Application")
st.markdown("""
Navigating and using this tool is simple. Just follow these three steps:

**1. ➕ Add Comments**
   - Navigate to the **'Add Comments'** page from the sidebar.
   - Add new comments to the moderation queue, with each new comment on a new line.

**2. 🛡️ Moderate Comments**
   - Go to the **'Moderator Dashboard'** page.
   - Here you can analyze comments from the queue one by one or start the auto-analysis feature to process them in real-time.

**3. 📊 View Analytics**
   - Visit the **'Overall Analytics'** page to see a high-level view of all analyzed comments.
   - Explore interactive charts showing toxicity rates, trends over time, and more.
""")
st.divider()

# --- CONTACT US ---
st.header("📞 Contact Us")
st.markdown("Feel free to reach out with any questions or feedback!")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **Emails:**
    - hfskksjfjsjfhk@gmail.com
    - djhsaadaksdbahs@gmail.com
    """)
    st.markdown("""
    **Phone:**
    - +91 98981 65456
    - 033 4565 8489
    """)
with col2:
    st.markdown("""
    **GitHub Repository:**
    - [Vivek-code/toxic-comment-detector](https://github.com/Vivek-code)
    """)
st.success("Thank you for checking out the project!")