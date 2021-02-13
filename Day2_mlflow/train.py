import argparse
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, log_loss
import lightgbm as lgb
import matplotlib as mpl

import optuna
import mlflow
import mlflow.lightgbm

mpl.use("Agg")

# def mlflow_callback(study, trial):
#     loss = trial.value if trial.value is not None else float("nan")
#     with mlflow.start_run(run_name=study.study_name):
#         mlflow.log_params(trial.params)
#         mlflow.log_metrics({"log_loss": loss})

def objective(trial):
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    train_set = lgb.Dataset(X_train, label=y_train)
    test_set = lgb.Dataset(X_test, label=y_test)

    param = dict(objective="multiclass", metric="multi_logloss", num_class=3,
                 lambda_l1=trial.suggest_loguniform("lambda_l1", 1e-8, 10.0),
                 lambda_l2=trial.suggest_loguniform("lambda_l2", 1e-8, 10.0),
                 num_leaves=trial.suggest_int("num_leaves", 2, 256),
                 feature_fraction=trial.suggest_uniform("feature_fraction", 0.4, 1.0),
                 bagging_fraction=trial.suggest_uniform("bagging_fraction", 0.4, 1.0),
                 bagging_freq=trial.suggest_int("bagging_freq", 1, 7),
                 min_child_samples=trial.suggest_int("min_child_samples", 5, 100), seed=42)

    gbm = lgb.train(param, train_set, valid_sets=test_set)
    y_proba = gbm.predict(X_test)
    y_pred = np.argmax(y_proba, axis=1)
    # accuracy = accuracy_score(y_test, y_pred)
    loss = log_loss(y_test, y_proba)

    return loss


def main():
    # enable auto logging
    print("#"*20)
    mlflow.lightgbm.autolog()



    study = optuna.create_study(direction='minimize')
    study.optimize(objective, n_trials=100)#, callbacks=[mlflow_callback])


    print("Number of finished trials: {}".format(len(study.trials)))

    print("Best trial:")
    trial = study.best_trial

    print("  Value: {}".format(trial.value))

    print("  Params: ")
    for key, value in trial.params.items():
        print("    {}: {}".format(key, value))


if __name__ == "__main__":
    main()



