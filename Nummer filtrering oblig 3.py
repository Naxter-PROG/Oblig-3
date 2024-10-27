numb = [3, -1, 0, 8, -5, 22, -44, 0, 5, 5, 10, 12, 14, 16, 18, 20]

# Konverterer listen til enten pos, neg eller zero basert på verdien av nummeret
signs = ["pos" if x > 0 else "neg" if x < 0 else "zero" for x in numb]

print(signs)

# Variabler i listen som har verdien av 5 
five_numb = list(filter(lambda wd: int(wd) == 5, numb))
print (five_numb)

#Varaibler i listen som er partall mellom 10 og 20
even_numb = list(filter(lambda x: 10 <= x <= 20 and x % 2 == 0, numb))

print(even_numb)
