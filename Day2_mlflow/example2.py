import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, log_loss
from sklearn.linear_model import LogisticRegression
import mlflow
import sys


def main():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    C = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5

    mlflow.set_experiment('Logistic')
    mlflow.sklearn.autolog()
    lr = LogisticRegression(C=C)
    lr.fit(X_train, y_train)
    y_proba = lr.predict_proba(X_test)
    loss = log_loss(y_test, y_proba)


if __name__ == "__main__":
    main()
