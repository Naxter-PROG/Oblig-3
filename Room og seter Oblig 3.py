from dataclasses import dataclass

@dataclass
class Classroom:
    code: str
    seats: int

# Liste over klasserom og antall seter
schedule = [
    Classroom('B0018', 50),
    Classroom('A1189', 50),
    Classroom('B0027', 120),
    Classroom('C9928', 175 + 10),
    Classroom('D3338', 0)
]


def capacity1(for_code: str, classrooms: list):
    '''Får sete kapsiset i kalsserom med koden under'''
    for fl in classrooms:
        if fl.code == for_code:
            #Funksjon for å gi ut svaret med antal seter + 10 av de orginale setene om du vill ha for ett spesefikt rom skriver du + 10 etter kapasitet nummeret i schedule.
            return fl.seats
    return None  # Svarer med none hvis ikke klasserommet er funnet i listen

# Test der jeg skriver inn rom koden og får svar på antal seter som er ledige
room_code = ('C9928')  
capacity = capacity1(room_code, schedule )



def list_rooms_with_50_seats(classrooms: list):
    '''Viser alle rom med 50 seter med koden under'''
    rooms_with_50 = []  # Initialize an empty list to hold matching rooms
    for room in classrooms:
        if room.seats == 50:
            rooms_with_50.append(room.code)  # Add the code of the room with 50 seats
    return rooms_with_50

# Test for å sjekke hvilket klassrom som har 50 seter
rooms_with_50 = list_rooms_with_50_seats(schedule)
print("Classrooms with 50 seats:", rooms_with_50)
# Test for å finne ut kapasiteten i ett definert klassrom
print (capacity)