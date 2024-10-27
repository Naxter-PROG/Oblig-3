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



# Be brukeren om å skrive inn et årstall
year_input = input("Skriv inn et år (mellom 2015 og 2023): ").strip()

if year_input in df.columns:
    print(f"Test 3 bestått: {year_input} er et gyldig årstall.")

# Sjekk om input er et gyldig årstall i datasettet
if year_input in df.columns:
    # Beregn gjennomsnittlig prosentandel for det valgte året
    avg_prosent = df[year_input].mean(skipna=True)
    
    # Vis gjennomsnittet
    print(f"Gjennomsnittlig prosentandel for alle kommuner i {year_input} er {avg_prosent:.2f}%")
else:
    print(f"År '{year_input}' er ikke gyldig. Vennligst skriv inn et år mellom 2015 og 2023.")


 # Lager en diagram av prosentandelen for hver kommune
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Komunne:N', title='Kommune'),
        y=alt.Y(f'{year_input}:Q', title='Prosentandel barn mellom 1 til 2 års alderen i barnehagen'),
        tooltip=['Komunne', year_input]
    ).properties(
        title=f"Prosent barn i barnehagen i ulike kommuner i {year_input}",
        width=800,
        height=400
    )

    # Lagre grafen som HTML-fil
    chart.save(f'barnehage_prosent_{year_input}.html')

    # Gi beskjed til brukeren om at grafen er lagret
    print(f"Diagrammet for {year_input} er lagret som 'barnehage_prosent_{year_input}.html'")

