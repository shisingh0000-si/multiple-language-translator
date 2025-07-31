import streamlit as st
from multi_language_translator import translate_text

st.set_page_config(page_title="AI Language Translator", layout="centered")

st.title("🌍 AI Powered Multiple Language Translator")

text_input = st.text_area("Enter Text to Translate", height=150)
target_lang = st.selectbox("Choose Language to Translate To", ['en', 'hi', 'fr', 'es', 'de', 'zh-cn'])

if st.button("Translate"):
    if text_input.strip():
        translated_text = translate_text(text_input, target_lang)
        st.success(f"✅ Translated Text:\n\n{translated_text}")
    else:
        st.warning("⚠️ Please enter some text to translate.")