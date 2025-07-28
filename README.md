# Sentiment Analyzer Streamlit App

A simple web app built with Streamlit to analyze the sentiment of text.

## How to Run

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the app:**
    ```bash
    streamlit run nlp_app.py
    ```

## How It Works

This application takes text input, cleans it by removing special characters and links, and then uses the `TextBlob` library to calculate a sentiment polarity score. The result is classified as positive, negative, or neutral.
