import re 
import pandas as pd 
# lets make a method 
def clean(text):
    text = re.sub(r"From:.*\n", "", text)
    text = re.sub(r"Subject:.*\n","",text)
    text = re.sub(r"[^a-z\s]", "", text.lower())
    return text

df = pd.read_csv("emails.csv")
df['clean_email'] = df['email'].apply(clean)
# df.to_csv("emails.csv" , index=False)
print(df.head())

