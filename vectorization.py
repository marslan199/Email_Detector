from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd 
from sklearn.model_selection import train_test_split
vectorizer = TfidfVectorizer()
df = pd.read_csv("emails.csv")

X = vectorizer.fit_transform(df["clean_email"])
# print(df.columns)
# print(X)

# lets start trainig
y = df["labelling"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


