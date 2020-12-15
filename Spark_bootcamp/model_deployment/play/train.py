import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

# read dataset
df = pd.read_csv("https://raw.githubusercontent.com/erkansirin78/datasets/master/iris.csv")

# split data vertically ax feature matrix and target
X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

print(X.shape)
print(y.shape)

# target is categorical, needs to be mapped integers
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Save the label_encoder model (yes, it is a quite model :) ) in order to use deployment (for reverse transformation)
joblib.dump(label_encoder, "saved_models/01.knn_with_iris_label_encoder.pkl")

# split data horizontally as train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=142)

# Create and classification object
estimator = KNeighborsClassifier(n_neighbors=6, metric='minkowski', p=2)

# Train the model
estimator.fit(X_train, y_train)

# Make predictions with test set
y_pred = estimator.predict(X_test)

# Calculate the performance (accuracy) metric
acc = accuracy_score(y_true=y_test, y_pred=y_pred)
print("Accuracy = " + str(acc))

# Train the model with whole data
estimator_final = KNeighborsClassifier(n_neighbors=6, metric='minkowski', p=2)
estimator_final = estimator.fit(X, y)

# Save the model in order to use deployment
joblib.dump(estimator_final, "saved_models/01.knn_with_iris_dataset.pkl")