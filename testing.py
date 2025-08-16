from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Load your dataset
df = pd.read_csv("emails.csv")

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["clean_email"])
y = df["labelling"]

# Train model
model = LogisticRegression()
model.fit(X, y)

print("Model trained ✅")

# --- Now test a real email directly ---
new_email = ["""From: noreply@linkedin.com  
Subject: You appeared in 5 searches this week  

Hi Arslan,  
Congratulations! Your profile appeared in **5 searches** this week.  
Check who’s viewing your profile and grow your network.  

👉 View analytics on LinkedIn


"""]

# Clean + vectorize same way
new_email_vec = vectorizer.transform(new_email)

# Predict
prediction = model.predict(new_email_vec)
print("Prediction:", "Spam" if prediction[0] == 1 else "Ham")
