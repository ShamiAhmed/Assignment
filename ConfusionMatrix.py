# Creating a Confusion Matrix in Python with sklearn 
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Create a Model
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
   data.data, data.target, test_size=0.2)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Create a Confusion Matrix
print(confusion_matrix(y_test, y_pred))



# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)

# Calculate the precision
precision = precision_score(y_test, y_pred)

# Calculate the recall
recall = recall_score(y_test, y_pred)

# Calculate the f1 score
f1 = f1_score(y_test, y_pred)

# Print the results
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# Returns:
# Accuracy: 0.956140350877193
# Precision: 0.9459459459459459
# Recall: 0.9859154929577465
# F1 Score: 0.9655172413793103