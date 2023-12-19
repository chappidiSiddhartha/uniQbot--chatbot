import streamlit as st

st.set_page_config(page_title="🤖 UniQbot App 💬")
st.title('🤖 UniQbot App 💬')
# Custom CSS for styling
custom_css = """
body {
    background-image: url('iStock-872962368-chat-bots-883x1000.jpg'); 
    background-size: cover;
    background-position: center;
}
"""

# Apply the custom CSS
st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)
