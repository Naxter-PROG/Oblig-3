# Funksjon eller kontrakt for å fremvise Gruppe 2B eller personer som er over alderen av 30
def Eldre_garde(table):
    
    filtered_table = [row for row in table[1:] if row[1] > 30]
    
    
    print("{:<15} {:<15} {:<20}".format(*table[0]))  
    for row in filtered_table:
        print("{:<15} {:<15} {:<20}".format(*row))
        
#Funksjon eller kontrakt for å fremvise Gruppe 2A eller personer under alderen av 30
def Yngre_garde(table):
    filtered_table =[row for row in table[1:] if row[1] < 30]
    print("{:<15} {:<15} {:<20}".format(*table[0]))  
    for row in filtered_table:
        print("{:<15} {:<15} {:<20}".format(*row))            

# Tabell med data som Navn, alder og gruppe
table = [
    ["Navn", "Alder", "Gruppe"],
    ["Jon", 25, "2A"],
    ["Eva", 31, "2B"],
    ["Ali", 22, "2A"],
    ["Joy", 21, "2A"],
    ["Elise", 32, "2B"],
    ["Tor-Egil", 44, "2B"]
]

# Funksjoner for å fremvise de forskjellige personenes "Navn, Alder og gruppe"
Eldre_garde(table)
Yngre_garde(table)