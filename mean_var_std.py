import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convertir la lista en una matriz 3x3
    matrix = np.array(numbers).reshape(3, 3)
    
    # Crear el diccionario con los cálculos
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),   # Media por columnas
            matrix.mean(axis=1).tolist(),   # Media por filas
            matrix.mean().item()            # Media total
        ],
        'variance': [
            matrix.var(axis=0).tolist(),    # Varianza por columnas
            matrix.var(axis=1).tolist(),    # Varianza por filas
            matrix.var().item()             # Varianza total
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),    # Desviación estándar por columnas
            matrix.std(axis=1).tolist(),    # Desviación estándar por filas
            matrix.std().item()             # Desviación estándar total
        ],
        'max': [
            matrix.max(axis=0).tolist(),    # Máximo por columnas
            matrix.max(axis=1).tolist(),    # Máximo por filas
            matrix.max().item()             # Máximo total
        ],
        'min': [
            matrix.min(axis=0).tolist(),    # Mínimo por columnas
            matrix.min(axis=1).tolist(),    # Mínimo por filas
            matrix.min().item()             # Mínimo total
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),    # Suma por columnas
            matrix.sum(axis=1).tolist(),    # Suma por filas
            matrix.sum().item()             # Suma total
        ]
    }
    
    return calculations