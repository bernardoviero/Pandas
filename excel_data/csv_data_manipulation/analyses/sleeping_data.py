import pandas as pd
import matplotlib.pyplot as plt

file_path = "/home/bernardo/git/pandas/PandasPythonLearning/excel_data/glicose_data.xlsx"
data = pd.read_excel(file_path)

#map the result values to numeric values
result_mapping = {"Abaixo": 1, "Normal": 2, "Acima": 3}
data['Resultado'] = data['Resultado'].map(result_mapping)

average_sleep_low_glucose = data[data['Resultado'] == 1]['sono'].mean()
average_glucose_high_sleep = data[data['sono'] >= 4]['Resultado'].mean()

#plot the graph to show the relationship between the days when glucose is low and sleep is high
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['sono'], marker='o', markersize=8, color='blue', label='Sleep')
plt.plot(data.index, data['Resultado'], marker='o', markersize=8, color='red', label='Glucose Level')
for i, txt in enumerate(data['Resultado']):
    plt.annotate(txt, (data.index[i], data['Resultado'][i]), textcoords="offset points", xytext=(0, 10), ha='center')
plt.text(0.5, average_sleep_low_glucose, f"Average Sleep ({average_sleep_low_glucose:.2f})", fontsize=12, ha='center', color='green')
plt.text(0.5, average_glucose_high_sleep, f"Average Glucose ({average_glucose_high_sleep:.2f})", fontsize=12, ha='center', color='orange')
plt.title('Relationship between Days with Low Glucose and High Sleep', fontsize=16)
plt.xlabel('Days', fontsize=14)
plt.ylabel('Sleep Level / Glucose Level', fontsize=14)
plt.legend()
plt.show()

if average_sleep_low_glucose > average_glucose_high_sleep:
    print("Based on the analysis, sleep is more directly related to the glucose level.")
elif average_glucose_high_sleep > average_sleep_low_glucose:
    print("Based on the analysis, the glucose level is more directly related to sleep.")
else:
    print("There is no clear relationship between sleep and the glucose level based on the analyzed data.")