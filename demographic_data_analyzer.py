import pandas as pd

def demographic_data_analyzer():
    # Load the dataset
    df = pd.read_csv('adult.data.csv', header=None, names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education-num', 
        'marital-status', 'occupation', 'relationship', 'race', 'sex', 
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'])

    # How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    percentage_advanced_education_rich = (df[advanced_education]['salary'] == '>50K').mean() * 100

    # What percentage of people without advanced education make more than 50K?
    non_advanced_education = ~advanced_education
    percentage_non_advanced_education_rich = (df[non_advanced_education]['salary'] == '>50K').mean() * 100

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_hours = (min_hours_workers['salary'] == '>50K').mean() * 100

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    highest_earning_country = country_salary['>50K'].idxmax()
    highest_earning_country_percentage = country_salary['>50K'].max() * 100

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Return all the results
    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'percentage_advanced_education_rich': round(percentage_advanced_education_rich, 1),
        'percentage_non_advanced_education_rich': round(percentage_non_advanced_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage_min_hours': round(rich_percentage_min_hours, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation,
    }
