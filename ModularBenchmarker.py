#!usr/bin/env python3

"""
Code written by Mattias Kockum
On 05/07/2022
The aim of this program is to create a modular benchmarking tool
"""


import numpy as np
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt

class BenchMarker(object):
    """
    A modular benchmarking tool
    functions for each model have to be coded outside of the class
    """
    def __init__(self, models, args, df_path):
        """
        models = list of models objects
        args = list of args to be inputed into models eval function
        """
        self.models = models
        self.args = args
        self.df_path = df_path
        # storing lens
        self.len_models = len(models)
        self.len_args = len(args)
        # storing name lists
        self.models_name_list = [m.name for m in models]
        self.args_name_list = [f"{a}" for a in args]
        # value table
        self.df = pd.DataFrame(
            columns = self.args_name_list,
            index = self.models_name_list
        )

    def add_model(self, model):
        """
        adds a model to the table
        updates every attribute
        """
        self.models.append(model)
        self.models_name_list.append(model.name)
        self.len_models += 1
        self.df.loc[model.name] = [np.NaN for i in self.args]

    def add_arg(self, arg):
        """
        adds a model to the table
        updates every attribute
        """
        self.args.append(arg)
        self.args_name_list.append(f"{arg}")
        self.len_args += 1
        self.df[f"{arg}"] = [np.NaN for i in self.models]

    def sort_values(self):
        """
        sort the dataframe by the values
        """
        self.df = self.df.sort_values(self.df.index[0], axis=1)
        self.args = list(self.df.columns)
        self.args_name_list = [f"{a}" for a in self.args]

    def sort_models(self):
        """
        sorts models in dataframe by their value for first argument
        choosing first argument is debatable,
        could be mean score, median score, best score, worst score etc
        This configuration tells 'First argument is the most important'
        """
        self.df = self.df.sort_values(by=self.args_name_list[0])
        new_models = []
        for target_model_name in self.df.index:
            for model in self.models:
                if model.name == target_model_name:
                    new_models.append(model)
        self.models = new_models
        self.models_name_list = [m.name for m in self.models]

    def sort_args(self):
        """
        sorts columns in dataframe by their argument
        """
        self.args = sorted(self.args)
        self.df = self.df[[f"{a}" for a in self.args]]
        self.args_name_list = [f"{a}" for a in self.args]

    def sort(self):
        """
        does both sortings
        """
        self.sort_models()
        self.sort_args()

    def populate(self):
        """
        populates the table with the benchmarking values
        """
        if os.path.exists(self.df_path):
            print("dataframe file found : loading")
            self.load_df()
        else:
            print("dataframe file not found : creating")
            self.compute_df()
            # saving dataframe
            self.save_df()

    def load_df(self):
        """
        loads df from self.df_path with csv format
        """
        self.df = pd.read_csv(self.df_path, index_col=0)

    def save_df(self):
        """
        saves df to csv format at self.path
        """
        self.df.to_csv(self.df_path)

    def compute_df(self):
        """
        computes df from models' eval function
        """
        for m in self.models:
            for arg in self.args:
                if pd.isna(self.df.loc[m.name][f"{arg}"]):
                    #print(f"{m} ({type(m)}) : {arg} ({type(arg)})")
                    self.df.loc[m.name][f"{arg}"] = m.eval(arg)


    def plot_df(self, name):
        """
        outputs a pretty table
        """
        sns.heatmap(
            np.array(self.df, dtype=float),
            xticklabels=self.args_name_list,
            yticklabels=self.models_name_list,
            annot=True
        )
        plt.savefig(name, bbox_inches="tight")
        print(f"saved {name}")
