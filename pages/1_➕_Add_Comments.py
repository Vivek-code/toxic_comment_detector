# pages/1_➕_Add_Comments.py

import streamlit as st
from database import add_comment, init_db

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Add Comments",
    page_icon="➕"
)

st.title("➕ Add Comments to the Database")
st.markdown("""
Use this page to add new comments to the moderation queue. You can add multiple comments at once by placing each one on a new line.
""")

# --- INITIALIZE DATABASE ---
# This ensures the tables are created when the app starts.
init_db()

# --- INPUT FORM ---
with st.form("add_comments_form", clear_on_submit=True):
    # Use a text area for multi-line input
    comments_input = st.text_area(
        "Enter comments (one per line):",
        height=200,
        placeholder="This is a great stream!\nWow, that's just stupid.\nCan you do that again?"
    )
    
    # Form submission button
    submitted = st.form_submit_button("Add to Queue")

    if submitted and comments_input:
        # Split the input text into a list of individual comments
        comments_list = comments_input.strip().split('\n')
        
        # Counter for added comments
        added_count = 0
        
        # Loop through each line and add it as a comment
        for comment in comments_list:
            if comment.strip(): # Ensure the line is not empty
                add_comment(comment.strip())
                added_count += 1
        
        if added_count > 0:
            st.success(f"Successfully added {added_count} comment(s) to the moderation queue!")
    elif submitted:
        st.warning("Please enter at least one comment.")