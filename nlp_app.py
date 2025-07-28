# Streamlit Libraries
import streamlit as st
# NLP Libraries
import nltk
# I got an error message asking to include nltk.download('wordnet')
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob
import re

def analyze(text):
    text = clean(text)
    blob = TextBlob(text)
    result = blob.sentiment.polarity

    if result > 0:
        custom_emoji = ':blush:'
        st.success(f'Happy {custom_emoji} : {text}')
    elif result < 0:
        custom_emoji = ':disappointed:'
        st.warning(f'Sad {custom_emoji} : {text}')
    else:
        custom_emoji = ':confused:'
        st.info(f'Confused {custom_emoji} : {text}')
    
    st.success(f"Polarity Score is: {result}")


def clean(text):
    # Keeping only text and digits
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    # Removes possessives
    text = re.sub(r"\'s", " ", text)
    # Removing links
    text = re.sub(r"http\S+", " link ", text)
    # Removes numbers
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
    # Split
    text = text.split()
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
    text = " ".join(lemmatized_words)
    return text


st.title("Sentiment Analyzer")
st.subheader("Enter some text below to analyze.")

input = st.text_area("Your text:", height=150)

if st.button("Analyze"):
    if input.strip() == "":
        st.warning("Can't analyze nothing! Please enter some text")
    else:
        st.write("Analyzing Sentiment...")
        analyze(input)
