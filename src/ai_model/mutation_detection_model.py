import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('../../data/sample_genetic_data.csv')

# Preprocessing
le = LabelEncoder()
data['mutation_type'] = le.fit_transform(data['mutation_type'])

X = data[['gene_expression', 'age']]
y = data['mutation_type']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Decision Tree Classifier
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Visualization
feature_importance = model.feature_importances_
plt.barh(X.columns, feature_importance)
plt.title('Feature Importances in Mutation Detection')
plt.show()
