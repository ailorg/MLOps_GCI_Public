#!/bin/sh

export AIRFLOW_HOME=~/airflow

AIRFLOW_VERSION=2.0.1
PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
airflow db init

expect -c "
    set timeout 10
    spawn airflow users create \
          --username admin \
          --firstname Gci \
          --lastname Student \
          --role Admin \
          --email example@example.com
    expect \"Password:\"
    send -- \"airflow\n\"
    expect \"Repeat for confirmation:\"
    send -- \"airflow\n\"
interact
"
exit
