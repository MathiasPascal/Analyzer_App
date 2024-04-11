# perfume_detector.py
import pandas as pd

# Load the CSV data
data = pd.read_csv('new_final.csv')

def check_asthma_trigger(name):
    perfume = data[data['Name'] == name]
    if perfume.empty:
        return 'Perfume not found'
    elif perfume['Asthma_Trigger'].values[0] == 1:
        return 'This perfume triggers asthma'
    else:
        return 'This perfume does not trigger asthma'

def get_perfume_names():
    return data['Name'].tolist()