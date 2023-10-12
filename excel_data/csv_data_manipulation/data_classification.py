import pandas as pd

data = pd.read_excel('excel_data/glicose_data.xlsx')

filtered_data = data[data['Resultado'] == 'Normal']

# 1. determine which day of the week blood glucose appears most frequently as normal
day_counts = filtered_data['Dia Semana'].value_counts()
print(day_counts)

perfect_day = day_counts.idxmax()

print(
    f"The most perfect day based on the 'Result = Normal' criterion is {perfect_day}.")

relevant_columns = ["Dose Insulina", "carb", "kcal", "padel", "musculacao R", "musculacao H",
                    "pilates", "tenis", "sauna", "bike", "caminhada", "corrida", "natacao", "eliptico", "volei de areia"]

filtered_data_temp = filtered_data[relevant_columns]

criteria_counts = {}
for column in relevant_columns:
    criteria_counts[column] = filtered_data_temp[column].value_counts()

for column, counts in criteria_counts.items():
    print(f"Counts for {column}:\n{counts}\n")


# 2. check which exercise is most frequently practiced when blood glucose is normal
exercise_columns = ["padel", "musculacao R", "musculacao H", "pilates", "tenis",
                    "sauna", "bike", "caminhada", "corrida", "natacao", "eliptico", "volei de areia"]

exercise_counts = {}

for column in exercise_columns:
    exercise_counts[column] = filtered_data[column].sum()

most_practiced_exercise = max(exercise_counts, key=exercise_counts.get)

print(
    f"The most practiced exercise based on the 'Result = Normal' criterion is {most_practiced_exercise}.")
