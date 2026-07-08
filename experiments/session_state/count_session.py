import streamlit as st

st.title("🧪 Session State Experiment")

# Create the counter only once
if "count" not in st.session_state:
    st.session_state.count = 0

st.write(f"Current Count: {st.session_state.count}")

# Increase button
if st.button("Increase"):
    st.session_state.count += 1
    st.rerun()

# Reset button
if st.button("Reset"):
    st.session_state.count = 0
    st.rerun()