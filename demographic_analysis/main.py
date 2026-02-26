from demographic_data_analyzer import calculate_demographics

# Cambia el nombre del CSV si es necesario
results = calculate_demographics(r'C:\Users\angel\Documents\freecodecamp_Analisis\demographic_analysis\demographic_data.csv')

# Mostrar resultados
for key, value in results.items():
    print(f"{key}:")
    print(value)
    print()