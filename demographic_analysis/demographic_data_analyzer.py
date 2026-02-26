import pandas as pd

def calculate_demographics(file_path=r'C:\Users\angel\Documents\freecodecamp_Analisis\demographic_analysis\demographic_data.csv'):
    column_names = [
        "age", "workclass", "fnlwgt", "education", "education-num", 
        "marital-status", "occupation", "relationship", "race", "sex", 
        "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"
    ]
    # Cargar CSV
    df = pd.read_csv(file_path, names=column_names, skipinitialspace=True)

    print(df.head())

    # Número de personas por raza
    race_count = df['race'].value_counts()

    # Edad promedio de hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Porcentaje de personas con licenciatura
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Porcentaje de personas con educación avanzada (>50K)
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # Mínimo número de horas trabajadas por semana
    min_work_hours = df['hours-per-week'].min()

    # Porcentaje de personas que trabajan mínimo y ganan >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # País con mayor porcentaje de personas que ganan >50K
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country = (country_rich_counts / country_counts).idxmax()
    highest_earning_country_percentage = round((country_rich_counts / country_counts).max() * 100, 1)

    # Ocupación más popular en India entre quienes ganan >50K
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }