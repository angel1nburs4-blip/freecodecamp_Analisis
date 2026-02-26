import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
import os

# Importar datos
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'epa-sea-level.csv'))

def draw_plot():
    # Crear figura
    fig, ax = plt.subplots(figsize=(12, 6))

    # Diagrama de dispersión
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

    # Línea de mejor ajuste con todos los datos
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(df['Year'].min(), 2051)
    ax.plot(years_all, intercept + slope*years_all, 'r', label='Fit all data')

    # Línea de mejor ajuste desde 2000
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    ax.plot(years_recent, intercept2 + slope2*years_recent, 'green', label='Fit from 2000')

    # Etiquetas y título
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Guardar figura
    fig.savefig('sea_level_plot.png')
    return fig