
# for traning and evaluating the model
# save the metrics and params

import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from get_data import read_params
import argparse
import joblib
import json


def eval_metrics(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return rmse, mae, r2


def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]

    alpha = config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]

    target = [config["base"]["target_col"]]


    train = pd.read_csv(train_data_path, sep=",") # traning data
    test = pd.read_csv(test_data_path, sep=",") # test data 

    X_train = train.drop(target, axis=1)
    X_test = test.drop(target, axis=1)
    y_train = train[target]
    y_test = test[target]

    # create ElasticNet model
    lr = ElasticNet(alpha=alpha, 
                    l1_ratio=l1_ratio,
                     random_state=random_state)

    # fitting the data
    lr.fit(X_train, y_train)

    # prediction
    pred = lr.predict(X_test)
    (rmse, mae, r2) = eval_metrics(y_test, pred)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    
