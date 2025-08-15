from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd 
vectorizer = TfidfVectorizer()
df = pd.read_csv("emails.csv")

X = vectorizer.fit_transform(df["clean_email"])
# print(df.columns)
print(X)