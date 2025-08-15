import pandas as pd
#
# spam_df = pd.read_csv("spam_emails.csv")
# ham_df = pd.read_csv("ham_emails.csv")

# df = pd.concat([spam_df, ham_df], ignore_index=True)

# # Save the merged file
# df.to_csv("emails.csv", index=False)

# print("Merged into emails.csv successfully.")
# #

# lets make data cleaning 
df = pd.read_csv("emails.csv")
# print(df.head())
# print(df.isnull().sum())
# print(df["label"].dtype)
# print(df["id"].dtype)
# print(df["email"].dtype)

df["labelling"] = df["label"].map({"ham" : 0 , "spam" : 1})
print(df.head())
print(df.tail())
df.to_csv("emails.csv" , index=False)

