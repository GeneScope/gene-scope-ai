import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('../../data/sample_genetic_data.csv')

# Feature Engineering
data['risk_factor'] = data['gene_expression'] * data['age'] * 0.01

# Preprocessing
X = data[['gene_expression', 'age', 'risk_factor']]
y = data['health_status'].apply(lambda x: 1 if x == 'Unhealthy' else 0)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Visualization
feature_importance = model.feature_importances_
plt.barh(X.columns, feature_importance)
plt.title('Feature Importances in Disease Risk Prediction')
plt.show()