import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load and train (simple version — you could pickle and load instead for speed)
df = pd.read_csv("emails.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["clean_email"])
y = df["labelling"]

model = LogisticRegression()
model.fit(X, y)

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Fake Email Detector", page_icon="📧", layout="centered")

st.title("📧 Fake Email Detector")
st.write("Paste any email text below and find out if it's **spam or safe**.")

email_input = st.text_area("Email content:", height=200, placeholder="Paste your email here...")

if st.button("Check Email"):
    if email_input.strip():
        email_vec = vectorizer.transform([email_input])
        prediction = model.predict(email_vec)[0]
        
        if prediction == 1:
            st.error("🚨 Spam / Fake Email Detected!")
        else:
            st.success("✅ This email looks safe (but be cautious).")
    else:
        st.warning("Please paste some email text before checking.")
