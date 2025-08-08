from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# load the .env file variables
load_dotenv()


def db_connect():
    import os
    engine = create_engine(os.getenv('DATABASE_URL'))
    engine.connect()
    return engine


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_scatter_heatmaps(dataframe, target_variable):
    numeric_variables = dataframe.select_dtypes(include=['float64', 'int64']).columns
    num_cols = 2
    num_rows = len(numeric_variables) - 1
    fig, axis = plt.subplots(num_rows, num_cols, figsize=(13, 5 * num_rows))
    for i, x_variable in enumerate(numeric_variables):
        # Evitar plotear la variable target
        if x_variable == target_variable:
            continue
        # Gráfico de dispersión
        sns.regplot(ax=axis[i, 0], data=dataframe, x=x_variable, y=target_variable)
        axis[i, 0].set_title(f'Regplot: {x_variable} vs {target_variable}')
        # Mapa de calor
        sns.heatmap(dataframe[[x_variable, target_variable]].corr(), annot=True, fmt=".2f", ax=axis[i, 1])
        axis[i, 1].set_title(f'Heatmap: {x_variable} vs {target_variable}')
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Ajustar la posición del título
    plt.show()    
