def all_z_words(wordlist: list) -> list:
    """Produce list of words from the input that contain 'z'."""
    zlist = []  
    for wd in wordlist:
        if "z" in wd:
            zlist = [wd] + zlist 
    return zlist

# Test the function 
def test_all_z_words():
    # Test for å sjekke om alle ord med z ble med i svaret.
    words = ["zebra", "pizza", "buzz", "fizz", "apple", "aligator", "giraffe"]
    result = all_z_words(words)
    print("Test case 1 result:", result)  # Forventer: ['buzz', 'pizza', 'zebra', 'fizz']
    
    
  
  
test_all_z_words()
  #"Kontrakt for å deffinere alle i listen"
new_z_words = ["zuduko", "zalza", "zalazar", "mayones", "oksekamp" ]

#Filter funksjon for å filtrere ord med z ved bruk av funksjonen "Filter"
ny_z_wrd_filter = list(filter(lambda wd: "z" in wd, new_z_words))

#Test for å sjekke om filteret "ny_z_wrd_filter" funker
print ("Test case 2 result.") 
print (ny_z_wrd_filter) #Forventet svar er zuduko, zalza og zalazar

