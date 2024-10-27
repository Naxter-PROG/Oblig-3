# Importerer google_sheets tabellen til python vedbruk av pandas
import pandas as pd
sheet_id = "2PACX-1vQmBYjQs2MQBNbpYSDjkmVEwwIhBNHydafXjv-_s2pwE0mp-O48Dj7f4mpQrSrGoIIJA7Do8vKUGvFe"

csv_url =f"https://docs.google.com/spreadsheets/d/e/2PACX-1vQmBYjQs2MQBNbpYSDjkmVEwwIhBNHydafXjv-_s2pwE0mp-O48Dj7f4mpQrSrGoIIJA7Do8vKUGvFe/pub?output=csv"

df = pd.read_csv(csv_url)

import pandas as pd



# Siden dokumentet innheold , når det var desimaler måtte jeg gjørde det om til .
df['Prosent'] = df['Prosent'].str.replace(',', '.')

# Setter prosent kolonnen til nomeric og gjør sånn at "," blir "NaN"
df['Prosent'] = pd.to_numeric(df['Prosent'], errors='coerce')

# Sorterer Prosent kolonnen til å vise høyeste tall
df_sorted = df.sort_values(by='Prosent', ascending= False)

# Fremviser kommunene med høyest andel barn 1-2 år i barnehager i en topp 5 liste
print(df_sorted.head(1))

