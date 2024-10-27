import pandas as pd
import altair as alt

# URL til dokumentet i CSV form
sheet_id = "2PACX-1vTNyfIONjiVcGnDofx3LgIKRavBYYbtmXJ8CClTfYwBOvMCki5FBQoehhWaKiVrQr_e2hJhDtEyMRna"
csv_url = f"https://docs.google.com/spreadsheets/d/e/2PACX-1vTNyfIONjiVcGnDofx3LgIKRavBYYbtmXJ8CClTfYwBOvMCki5FBQoehhWaKiVrQr_e2hJhDtEyMRna/pub?output=csv"

# Les inn dataene til pandas
df = pd.read_csv(csv_url)

# Tar en titt på at CSV-filen ble riktig lastet inn (bør ikke være tom)
assert not df.empty, "Feil: CSV-filen ble ikke riktig lastet inn."

# Rens data - konverterer komma til punktum og deretter til numerisk verdi
for year in range(2015, 2024):
    df[str(year)] = df[str(year)].str.replace(',', '.')
    df[str(year)] = pd.to_numeric(df[str(year)], errors='coerce')

# Sjekker at konvorteringen fungerer ved å bekrefte at ingen verdier inneholder kommaer
assert df['2015'].dtype == 'float64', "Feil: Dataene for 2015 er ikke konvertert til numerisk format."
# Du kan legge til samme test for andre år hvis nødvendig

# Fjern rader som har noen manglende verdier for årene 2015-2023
df_clean = df.dropna(subset=[str(year) for year in range(2015, 2024)])

# Beregn gjennomsnittlig prosentandel for årene 2015-2023 for hver kommune
df_clean['AvgProsent'] = df_clean[[str(year) for year in range(2015, 2024)]].mean(axis=1)

# Kontroller at kolonnen 'AvgProsent' har blitt riktig lagt til
assert 'AvgProsent' in df_clean.columns, "Feil: Gjennomsnittskolonnen ble ikke generert riktig."

# Sorter kommuner etter gjennomsnittlig prosentandel og velg de 10 med høyest verdi
df_top10 = df_clean.nlargest(10, 'AvgProsent')

# Konverter data til lang format for Altair-visualisering
df_long = df_top10.melt(id_vars=['Komunne'], 
                        value_vars=[str(year) for year in range(2015, 2024)], 
                        var_name='År', 
                        value_name='Prosent')

# Lag diagrammet med Altair
chart = alt.Chart(df_long).mark_line(point=True).encode(
    x=alt.X('År:O', title='År'),
    y=alt.Y('Prosent:Q', title='Prosentandel barn i barnehagen'),
    color='Komunne:N',
    tooltip=['Komunne', 'År', 'Prosent']
).properties(
    title='Gjennomsnittlig prosent barn i barnehagen for topp 10 kommuner (2015-2023)',
    width=700,
    height=500
)

# Lagre grafen som HTML-fil
chart.save('topp10_kommuner_gjennomsnitt_diagram.html')

# Gi beskjed til brukeren om at grafen er lagret
print("Diagrammet er lagret som 'topp10_kommuner_gjennomsnitt_diagram.html'")
