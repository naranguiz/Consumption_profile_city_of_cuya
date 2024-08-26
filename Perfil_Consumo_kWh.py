import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# Step 1: Load the CSV file
file_path =  'C:\\Users\\naran\\OneDrive\\Escritorio\\Perfil_Consumo_Cuya-20240826T011724Z-001\\Perfil_Consumo_Cuya\\Cuya_consumo_cge.csv'
data = pd.read_csv(file_path, sep=';', header=0, dayfirst=True)

# Convert the "Fecha/Hora" column to date and time format
data['Fecha/Hora'] = pd.to_datetime(data['Fecha/Hora'], format="%d-%m-%Y %H:%M", dayfirst=True)

# Clean and convert the "Potencia_kW" column
data["Potencia_kW"] = data["Econsumida"].str.replace(',', '.').astype(float)

# Step 3: Group by hour and calculate the average
consumption_profile = data.groupby(data["Fecha/Hora"].dt.hour)["Potencia_kW"].mean()

# Step 4: Plot the consumption profile
plt.figure(figsize=(10, 6))
plt.plot(consumption_profile.index, consumption_profile.values, marker='o', label='Consumo promedio por hora')
plt.title('Perfil de consumo por hora en Agosto - Año 2023 - Localidad de Cuya (Arica)')
plt.xlabel('Hora del día')
plt.ylabel('Potencia (kW)')
plt.grid(True)

# Set x-axis ticks to cover all 24 hours
plt.xticks(range(24))

# Set y-axis ticks based on the actual data
plt.yticks(range(int(min(consumption_profile)), int(max(consumption_profile))+1))

# Highlight mean power
mean_power = consumption_profile.mean()
plt.axhline(y=mean_power, color='r', linestyle='--', label=f'Potencia Media: {mean_power:.2f} kW')

# Highlight peak power
peak_hour = consumption_profile.idxmax()
peak_power = consumption_profile.max()
plt.scatter(peak_hour, peak_power, color='g', marker='*', s=100, zorder=5, label=f'Pico de Potencia: {peak_power:.2f} kW')

plt.legend()
plt.show()

