from sklearn.naive_bayes import MultinomialNB
from vectorization import X_test , y_test ,X_train , y_train

model = MultinomialNB()
model.fit(X_train , y_train)

print("Model trained success fully")