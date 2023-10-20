# Erstelle eine Liste aller möglichen Puzzleteile
moegliche_puzzleteile = []
seiten = ['K', 'H']

for seite1 in seiten:
    for seite2 in seiten:
        for seite3 in seiten:
            for seite4 in seiten:
                puzzleteil = f'{seite1},{seite2},{seite3},{seite4}'
                moegliche_puzzleteile.append(puzzleteil)

# Filtere Puzzleteile, bei denen das erste Element nach vorne verschoben gleich bleibt
ergebnis = [puzzleteil for puzzleteil in moegliche_puzzleteile if puzzleteil == puzzleteil[1:] + puzzleteil[0]]

# Gib die gefilterte Liste aus
for puzzleteil in ergebnis:
    print(f'"{puzzleteil}"')
