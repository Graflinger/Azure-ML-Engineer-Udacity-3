from sklearn.model_selection import train_test_split
from azureml.core import Run
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import argparse
import os
import joblib
import numpy as np


# Get the experiment run context
run = Run.get_context()

# Get arguments
parser = argparse.ArgumentParser()
parser.add_argument('--in_n_estimator', type=int, default=8)
parser.add_argument('--in_criterion', type=str, default="gini")
parser.add_argument('--in_max_depth', type=int, default=2)

args = parser.parse_args()
in_n_estimators = args.in_n_estimator
in_criterion = args.in_criterion
in_max_depth = args.in_max_depth


# read prepared data
df = pd.read_csv("prepared_data.csv")
columns = df.iloc[1:2, :-1].columns
x = df[columns]
y = df.iloc[:, -1:]

# split data into train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=2)

# “gini”, “entropy”
model = RandomForestClassifier(n_estimators=in_n_estimators, criterion=in_criterion, max_depth=in_max_depth)

model.fit(x_train, y_train)

accuracy = model.score(x_test, y_test)
run.log("Accuracy", float(accuracy))

os.makedirs('outputs', exist_ok=True)
joblib.dump(model, 'outputs/model_forest.joblib')
