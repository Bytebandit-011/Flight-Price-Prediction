# %% [markdown]
# # Import necessary libraries

# %%
import numpy as np

import pandas as pd

import sklearn
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import learning_curve

from feature_engine.datetime import DatetimeFeatures

# from xgboost import XGBRegressor

import joblib

import matplotlib.pyplot as plt

# %%
pd.set_option("display.max_columns", None)

# %%
sklearn.set_config(transform_output="default")

# %% [markdown]
# # Split the Dataset

# %%
train_df = pd.read_csv("data/train1.csv")
test_df = pd.read_csv("data/test1.csv")
val_df = pd.read_csv("data/val.csv")

# %%
def split_dataset(data):
	X = data.drop(columns="price")
	y = data.price.copy()
	return (X, y)

# %%
X_train, y_train = split_dataset(train_df)
print(X_train.info(), y_train.info())
X_train

# %%
X_val , y_val = split_dataset(val_df)
print(X_val.info(), y_val.info())

# %%
X_test , y_test = split_dataset(test_df)
print(X_test.info(), y_test.info())

# %%
dt_cols = ["date_of_journey", "dep_time", "arrival_time"]

num_cols = ["duration", "total_stops"]

cat_cols = ["airline","source","additional_info","destination"]

# %%
num_transformer =  Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler" , StandardScaler())
])

date_transformer = Pipeline(steps=[
    ("impuuter", SimpleImputer(strategy="most_frequent")),
    ("scaler", StandardScaler())
])

cat_transformer = Pipeline(steps = [
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("extractor", DatetimeFeatures(features_to_extract=["month", "week", "day_of_week", "day_of_month"], format="mixed")),
    ("scaler", StandardScaler())
])

time_transformer = Pipeline(steps = [
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("extractor", DatetimeFeatures(features_to_extract=["hour","minute"],format="mixed")),
    ("scaler", StandardScaler())

])



# %%
preprocessor = ColumnTransformer(transformers=[
	("num", num_transformer, num_cols),
	("cat", cat_transformer, cat_cols),
	("doj", date_transformer, ["date_of_journey"]),
	("time", time_transformer, ["dep_time", "arrival_time"])
])

# %%
preprocessor.fit_transform(X_train)


