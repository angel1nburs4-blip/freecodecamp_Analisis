import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Importar datos
csv_path = os.path.join(os.path.dirname(__file__), 'medical_examination.csv')
df = pd.read_csv(csv_path)

# 1. Agregar columna 'overweight'
# IMC = peso / altura^2 (altura en metros)
df['overweight'] = ((df['weight'] / ((df['height']/100)**2)) > 25).astype(int)

# 2. Normalizar datos de 'cholesterol' y 'gluc' (0 = bueno, 1 = malo)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 3. Función para dibujar gráfico categórico
def draw_cat_plot():
    # Crear DataFrame para el catplot
    df_cat = pd.melt(df, 
                     id_vars=['cardio'], 
                     value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    
    # Crear gráfico con seaborn
    fig = sns.catplot(
        data=df_cat,
        kind='count',
        x='variable',
        hue='value',
        col='cardio'
    )
    
    fig.set_axis_labels("variable", "total")
    
    # Guardar figura
    fig.savefig('catplot.png')
    return fig.fig  # retornar la figura para pruebas

# 4. Función para dibujar mapa de calor
def draw_heat_map():
    # Limpiar datos
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # Calcular matriz de correlación
    corr = df_heat.corr()
    
    # Generar máscara para triángulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Configurar figura
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Dibujar heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", square=True, cbar_kws={'shrink':0.5})
    
    # Guardar figura
    fig.savefig('heatmap.png')
    return fig