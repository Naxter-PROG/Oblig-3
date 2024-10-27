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


# Be brukeren om å skrive inn en kommune
kommune_input = input("Skriv inn navnet på kommunen: ").strip()

# Filtrer data for den valgte kommunen
df_kommune = df[df['Komunne'] == kommune_input]


# Sjekk om kommunen finnes i datasettet
if not df_kommune.empty:
    print("Test 3 bestått: Kommunen finnes i datasettet.")


# Sjekk om kommunen finnes i datasettet
if not df_kommune.empty:
    # Konverter data til lang format for Altair-visualisering
    df_long = df_kommune.melt(id_vars=['Komunne'], 
                              value_vars=[str(year) for year in range(2015, 2024)], 
                              var_name='År', 
                              value_name='Prosent')

    # Lag diagrammet med Altair
    chart = alt.Chart(df_long).mark_line(point=True).encode(
        x=alt.X('År:O', title='År'),
        y=alt.Y('Prosent:Q', title='Prosentandel barn i barnehagen'),
        tooltip=['År', 'Prosent']
    ).properties(
        title=f"Prosent barn i ett- og to-årsalderen i barnehagen i {kommune_input} (2015-2023)",
        width=600,
        height=400
    )

    # Lagre grafen som HTML-fil
    chart.save('kommune_barn_diagram.html')

    # Gi beskjed til brukeren om at grafen er lagret
    print(f"Diagrammet er lagret som 'kommune_barn_diagram.html'")
else:
    print(f"Kommune '{kommune_input}' ble ikke funnet i datasettet.")
