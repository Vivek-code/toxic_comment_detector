# Moderator_Dashboard.py

import streamlit as st
from transformers import pipeline
import pandas as pd
import time
from database import init_db, get_pending_comment, add_analysis_result

st.set_page_config(page_title="Moderator Dashboard", page_icon="🛡️", layout="wide")

@st.cache_resource
def load_model():
    return pipeline(task="text-classification", model="unitary/toxic-bert", tokenizer="bert-base-uncased")

classifier = load_model()

if 'latest_comment_info' not in st.session_state:
    st.session_state.latest_comment_info = None
if 'auto_run' not in st.session_state:
    st.session_state.auto_run = False

def analyze_and_store_comment():
    """Fetches, analyzes, and stores a comment using the NEW database logic."""
    comment_data = get_pending_comment()
    if comment_data:
        comment_id, comment_text = comment_data
        
        analysis_raw = classifier(comment_text, top_k=None)
        
        is_toxic = any(item['label'] != 'toxic' and item['score'] > 0.5 for item in analysis_raw) or \
                   any(item['label'] == 'toxic' and item['score'] > 0.8 for item in analysis_raw)

        # Convert the list of dicts from the model into a single dict of scores
        scores = {item['label']: item['score'] for item in analysis_raw}

        # Save the processed scores to the database
        add_analysis_result(comment_id, is_toxic, scores)
        
        st.session_state.latest_comment_info = {
            "comment": comment_text,
            "analysis": analysis_raw,
            "is_toxic": is_toxic
        }
    else:
        st.session_state.latest_comment_info = None
        st.session_state.auto_run = False
        st.info("The moderation queue is empty.")

st.title("🛡️ Live Moderator Dashboard")
st.markdown("Analyze comments from the queue either manually or automatically.")
init_db()

st.subheader("Moderation Controls")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Analyze Next Comment", use_container_width=True):
        st.session_state.auto_run = False
        analyze_and_store_comment()
with col2:
    if st.button("▶️ Start Auto-Analysis", type="primary", use_container_width=True):
        st.session_state.auto_run = True
with col3:
    if st.button("⏹️ Stop Auto-Analysis", use_container_width=True):
        st.session_state.auto_run = False

st.header("Latest Analysis")
if st.session_state.latest_comment_info:
    info = st.session_state.latest_comment_info
    if info['is_toxic']:
        st.error(f"🚨 FLAGGED: \"{info['comment']}\"", icon="🚨")
    else:
        st.success(f"✅ OK: \"{info['comment']}\"", icon="✅")
    
    st.write("**Toxicity Breakdown:**")
    analysis_df = pd.DataFrame(info['analysis'])
    analysis_df = analysis_df.rename(columns={'label': 'Category', 'score': 'Confidence Score'})
    st.bar_chart(analysis_df.set_index('Category'))
else:
    st.info("No comment analyzed yet.")

if st.session_state.auto_run:
    analyze_and_store_comment()
    if st.session_state.latest_comment_info:
        time.sleep(3)
        st.rerun()