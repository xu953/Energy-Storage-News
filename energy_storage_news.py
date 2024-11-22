import streamlit as st
from datetime import date
from markdown import markdown
import get_news

st.title(":mailbox: Energy Storage & EV News")
st.markdown(markdown(), unsafe_allow_html=True)

default_date = date.today()
selected_date = st.date_input(
    "Which date you are interested?",
    default_date
)

if st.button("Start", type="primary"):
    with st.spinner(f"Fetching news at {selected_date}"):
        news_bi = get_news.from_batteryindustry(selected_date)
        news_es = get_news.from_energystorage(selected_date)
        news_ek = get_news.from_electrek(selected_date)
