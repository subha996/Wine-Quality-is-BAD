# read the parameter
# process it
# reyturn the dataframe.
import os
import yaml
import pandas as pd
import argparse

# creating read param.yaml file 
def read_params(config_path): 
    """This functon will read the yaml file and 
        will return a dictionary."""
    with open(config_path, 'r') as ymlfile:
        config = yaml.safe_load(ymlfile) # reading the yaml file as dictionary
    return config


# creating function to get the data
def get_data(config_path):
    # reading the data
    config = read_params(config_path)
    # print(config)
    data_path = config["data_source"]["s3_source"] # geeting data path from config file
    # print(data_path)
    df = pd.read_csv(data_path, sep=",", encoding="utf-8")
    # print(df.head())
    return df
 
# extra comment to make a example changes

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)

