import pandas as pd
import altair as alt
# URL til dokumentet i CSV form
sheet_id = "2PACX-1vTNyfIONjiVcGnDofx3LgIKRavBYYbtmXJ8CClTfYwBOvMCki5FBQoehhWaKiVrQr_e2hJhDtEyMRna"
csv_url = f"https://docs.google.com/spreadsheets/d/e/2PACX-1vTNyfIONjiVcGnDofx3LgIKRavBYYbtmXJ8CClTfYwBOvMCki5FBQoehhWaKiVrQr_e2hJhDtEyMRna/pub?output=csv"

# Får dokumentete in till pandas addon
df = pd.read_csv(csv_url)



# Siden dokumentete som ble referert til har dessimaler i seg måtte jeg bytte det til . slik at python klarer å forstå 
df ['2015'] = df ['2015'].str.replace(',', '.')
df ['2016'] = df ['2016'].str.replace(',', '.')
df ['2017'] = df ['2017'].str.replace(',', '.')
df ['2018'] = df ['2018'].str.replace(',', '.')
df ['2019'] = df ['2019'].str.replace(',', '.')
df ['2020'] = df ['2020'].str.replace(',', '.')
df ['2021'] = df ['2021'].str.replace(',', '.')
df ['2022'] = df ['2022'].str.replace(',', '.')
df ['2023'] = df ['2023'].str.replace(',', '.')
# Siden alle kolonnene under er tall måtte jeg gjøre dem til numeric
df['2015'] = pd.to_numeric(df['2015'], errors = 'coerce')
df['2016'] = pd.to_numeric(df['2016'], errors = 'coerce')
df['2017'] = pd.to_numeric(df['2017'], errors = 'coerce')
df['2018'] = pd.to_numeric(df['2018'], errors = 'coerce')
df['2019'] = pd.to_numeric(df['2019'], errors = 'coerce')
df['2020'] = pd.to_numeric(df['2020'], errors = 'coerce')
df['2021'] = pd.to_numeric(df['2021'], errors = 'coerce')
df['2022'] = pd.to_numeric(df['2022'], errors = 'coerce')
df['2023'] = pd.to_numeric(df['2023'], errors = 'coerce')

# Tar komunne kolonnen og finner gjennomsnitt mellom 2015-2023
df_avg = df.groupby('Komunne')['2015'].mean().reset_index()

# Finner komunnenen med høyest gjennomsnitts barn i 1 og 2 års alderen
min_avg = df_avg['2015'].min()
# Finner ut hvilken kommune som har lavest antall barn i 1 og 2 års alderen i barnehagen 
highest_kommune = df_avg[df_avg['2015'] == min_avg]
# Fremviser en svar linje
print(f"Kommunene med høyest gjennomsnits antall barn i barnehagen mellom i 2 års alderen:\n{highest_kommune}")