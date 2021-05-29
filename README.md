# MLOps_tutorial
このリポジトリは、機械学習の初心者を対象に、どのように機械学習をプロダクト化するかを簡単に体験してもらうためのものです。

Day1では、機械学習コードをノートブック形式から.py形式に書き直す一例を紹介しています。

Day2では、機械学習プロダクト開発における実験管理とワークフロー管理の一例について紹介しています。ここでは実験管理には`MLflow`をワークフロー管理には`Airflow`を使用しています。

## How to use
```
docker build -t mlops_env .
docker run -it -v <path/to/dir>/MLOps_tutorial:/home --rm --name mlops -p 8080:8080 -p 5000:5000 mlops_env /bin/bash
```
## Day1
MLOps_tutorial/Day1では機械学習プロダクトの以下の流れを再現しています。

1. sample.dbからデータを取得し、前処理をする：preprocessing.py
2. 前処理済みデータを使って学習する：train.py
3. 学習済みモデルを使ってSQLで取得したテストデータに対する予測をする：inference.py
```
├── LR_model.pkl
├── README.md
├── sample.db
├── test.csv
├── train.csv
├── inference.py
├── preprocessing.py
└── train.py
```

## Day2_mlflow
- Irisデータセットを使って、LogisticRegressionをmlflowで記録・管理する:example.py
- Irisデータセットを使って、LogisticRegressionをmlflow.sklearn.autologで記録・管理する:example2.py
- Irisデータセットを使って、Lightgbmをoptunaでハイパラ最適化をmlflow.lightgbm.autologで記録・管理する:train.py

```
├── MLproject
├── README.md
├── conda.yaml
├── example.py
├── example2.py
└── train.py
```

## Day2_airflow
- Airflowを使ってDay1で行った一連の機械学習の流れを管理する:workflow.py

```
├── LR_model.pkl
├── README.md
├── dags
│   ├── inference
│   │   └── inference.py
│   ├── preprocess
│   │   └── preprocessing.py
│   ├── train
│   │   └── train.py
│   ├── workflow.py
│   └── workflow2.py
├── sample.db
├── test.csv
└── train.csv
```
