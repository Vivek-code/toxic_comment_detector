# pages/2_📊_Overall_Analytics.py

import streamlit as st
import pandas as pd
import plotly.express as px

from database import get_all_analytics, init_db

st.set_page_config(page_title="Overall Analytics", page_icon="📊", layout="wide")
st.title("📊 Overall Analytics Dashboard")
st.markdown("A high-level overview of all comments analyzed by the moderation system.")

init_db()
columns, all_data = get_all_analytics()

if not all_data:
    st.warning("No data to display. Please analyze some comments on the '🛡️ Moderator Dashboard' page first.")
else:
    # --- DATA PROCESSING IS NOW SUPER SIMPLE ---
    df = pd.DataFrame(all_data, columns=columns)
    df['is_toxic'] = df['is_toxic'].astype(bool) # Ensure boolean type
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # --- TOP-LEVEL METRICS ---
    st.header("Key Performance Indicators (KPIs)")
    total_comments = len(df)
    total_toxic = df['is_toxic'].sum()
    toxicity_rate = (total_toxic / total_comments) * 100 if total_comments > 0 else 0

    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Total Comments Analyzed", total_comments)
    kpi2.metric("Total Toxic Comments Flagged", int(total_toxic))
    kpi3.metric("Overall Toxicity Rate", f"{toxicity_rate:.2f}%")

    st.divider()

    # --- VISUALIZATIONS ---
    viz1, viz2 = st.columns(2)

    with viz1:
        st.subheader("Toxic vs. Non-Toxic Distribution")
        pie_data = df['is_toxic'].value_counts()
        pie_data.index = pie_data.index.map({True: 'Toxic', False: 'Non-Toxic'})
        st.plotly_chart(px.pie(pie_data, values=pie_data.values, names=pie_data.index, title='Overall Comment Distribution'), use_container_width=True)

    with viz2:
        st.subheader("Breakdown of Toxicity Types")
        toxic_df = df[df['is_toxic'] == True]
        if not toxic_df.empty:
            categories = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
            category_sums = toxic_df[categories].sum().sort_values(ascending=False)
            st.bar_chart(category_sums)
        else:
            st.info("No toxic comments have been recorded to break down.")

    # (Existing code from the previous step)
    st.subheader("Toxicity Trend Over Time")

    # --- NEW: Add a dropdown to select the time scale ---
    time_agg = st.selectbox(
        "Select Time Scale:",
        options=['Hourly', 'Daily'],
        index=0  # Default to 'Hourly'
    )

    # Map the user-friendly option to a pandas resampling code
    resample_code = 'H' if time_agg == 'Hourly' else 'D'

    # Resample the data based on the selected time scale
    toxic_over_time = df.set_index('timestamp').resample(resample_code)['is_toxic'].sum()
    
    st.line_chart(toxic_over_time, use_container_width=True)
    # (Rest of the code)

    st.divider()
    st.header("Log of All Flagged Comments")
    
    # --- THIS IS THE CORRECTED LINE ---
    # We select 'comment_text' which is the actual column name from the database.
    st.dataframe(df[df['is_toxic'] == True][['comment_text']], use_container_width=True)