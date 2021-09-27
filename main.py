player0_char = 'X'  # Pelaajan 0 merkki
player1_char = 'O'  # Pelaajan 1 merkki
gameRunning = True
#available_inputs = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'C0', 'C1', 'C2']
player = 0


def printGameboard():
    print(gameboard['A'])
    print(gameboard['B'])
    print(gameboard['C'])


def setUserPointTo(alpha, number, player):
    if player:
        player_char = player0_char
    else:
        player_char = player1_char
    gameboard[alpha][number] = player_char

def check_valid_point(row, col):
    if row in gameboard and 0 <= col <= 2:
        if gameboard[row][col] == " ":
            return True
        else:
            print("* Virhe: ruutu on varattu")
            return False
    else:
        print("* Virhe: virheellinen syöte")
        return False

def check_win():
    if player == 0:
        mark = 'X'
    else:
        mark = 'O'

    # Vaaka
    for row in gameboard:
        if gameboard[row][0] == mark and gameboard[row][1] == mark and gameboard[row][2] == mark:
            print("* Vaaka")
            return True

    # Pysty
    for i in range(0,2):
        if gameboard['A'][i] == mark and gameboard['B'][i] == mark and gameboard['C'][i] == mark:
            print("* Pysty")
            return True

    # Risti
    if gameboard['A'][0] == mark and gameboard['B'][1] == mark and gameboard['C'][2] == mark:
        print("* Vino 1")
        return True
    if gameboard['C'][0] == mark and gameboard['B'][1] == mark and gameboard['A'][2] == mark:
        print("* Vino 2")
        return True

    return False


"""	
 Kuvitteellinen pelilauta
 Ajatellaan että koordinaatit ovat ensimmäisellä rivillä     A0, A1 ja A2
					toisella rivillä     B0, B1 ja B2
					kolmannella rivillä  C0, C1 ja C2
"""
gameboard = {'A': [" ", " ", " "],
             'B': [" ", " ", " "],
             'C': [" ", " ", " "]}

print("* Huomio: anna syöte muodossa esim. A0, C2, B1")

while gameRunning:
    # Kirjoita koodisi tänne

    #	setUserPointTo('A', 0, 0)	# Aseta koordinaattiin A0 pelaajan 0 merkki
    #	setUserPointTo('C', 2, 1)	# Aseta koordinaattiin C2 pelaajan 1 merkki

    action = input(f"Pelaaja {player}: ")
    if check_valid_point(action[0], int(action[1])):
        #setUserPointTo(XXXX,YYYYY,ZZZZ)

        printGameboard()

        if check_win():
            input(f"Pelaaja {player} voitti! Paina mitä tahansa näppäintä sulkeaksesi pelin.")
            break

        if not ' ' in gameboard['A'] and not ' ' in gameboard['B'] and not ' ' in gameboard['C']:
            print("jotain")

        player = 1 - player

























#print("Peli päättyi. Kaikki koordinaatit käytetty.")
            #break