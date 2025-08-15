# ui.py
import streamlit as st
from agent import ManagerAgent

def run_streamlit_app():
    st.title("Hierarchical Reasoning Agent")
    
    # Using a form to group the input and submit button
    with st.form("query_form"):
        user_query = st.text_input("Enter your problem statement:")
        submitted = st.form_submit_button("Submit")
        spinner = st.spinner("Processing...")
    
    if submitted and user_query:
        st.markdown("### Agent Response:")
        placeholder = st.empty()
        manager = ManagerAgent()
        
        # Callback function to update the placeholder with the current streamed answer.
        def update_callback(text):
            placeholder.markdown(f"\n{text}")
        
        # Execute the agent's reasoning with streaming updates.
        with spinner:
            manager.execute_streamlit(user_query, update_callback)

if __name__ == '__main__':
    run_streamlit_app()
