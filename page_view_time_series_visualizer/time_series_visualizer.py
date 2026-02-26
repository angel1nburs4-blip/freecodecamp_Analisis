import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importar datos (ruta relativa)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Limpiar datos: filtrar top 2.5% y bottom 2.5%
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]

# Función para dibujar gráfico de líneas
def draw_line_plot():
    # Copiar dataframe
    data = df.copy()
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(data.index, data['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Guardar figura
    fig.savefig('line_plot.png')
    return fig

# Función para dibujar gráfico de barras
def draw_bar_plot():
    # Copiar dataframe y agregar columnas de año y mes
    data = df.copy()
    data['year'] = data.index.year
    data['month'] = data.index.month
    
    # Agrupar por año y mes
    df_bar = data.groupby(['year','month'])['value'].mean().unstack()
    
    # Crear figura
    fig = df_bar.plot(kind='bar', figsize=(12,6)).get_figure()
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    
    # Guardar figura
    fig.savefig('bar_plot.png')
    return fig

# Función para dibujar gráficos de caja
def draw_box_plot():
    # Copiar dataframe y preparar columnas
    data = df.copy()
    data.reset_index(inplace=True)
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.strftime('%b')
    data['month_num'] = data['date'].dt.month
    
    # Ordenar por número de mes para que enero sea primero
    data = data.sort_values('month_num')
    
    # Crear figura con dos subplots
    fig, axes = plt.subplots(1, 2, figsize=(15,6))
    
    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=data, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise box plot
    sns.boxplot(x='month', y='value', data=data, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    # Guardar figura
    fig.savefig('box_plot.png')
    return fig