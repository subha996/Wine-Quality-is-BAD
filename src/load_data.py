
# raed the data from data source and save it  in the data\raw for further processing
import os
from get_data import get_data, read_params
import argparse

def load_and_save(config_path):
    config = read_params(config_path) # read the config file
    df = get_data(config_path) # get the data
    new_cols = [col.replace(" ", "_") for col in df.columns] # list of columns names
    # print(new_cols)
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    # df.columns = new_cols # rename the columns with underscores
    df.to_csv(raw_data_path, sep=",", index=False, header=new_cols) # save the data # header will replace new col names
    


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)