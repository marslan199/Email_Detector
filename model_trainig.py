from sklearn.naive_bayes import MultinomialNB
from vectorization import X_test , y_test ,X_train , y_train

model = MultinomialNB()
model.fit(X_train , y_train)

print("Model trained success fully")

y_pred = model.predict(X_test)
# print(y_pred)
# print(y_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
