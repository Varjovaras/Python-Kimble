KIMBLE PELI
Kristjan Rajaniemi

Pelaaja liikkuu ympäri pelipöytää, nimellä table
Jokaisen listan alku tablessa on yhden pelaajan alkupiste

Tehdessä siirron move() funktio tarkistaa tarviiko pyörittää noppaa uudelleen

move() tarkistaa funktiolla checkLegalMoves() funktiolla mitä tehdään seuraavaksi

checkLegalMoves() kutsuu newPiece(), jos pyörität 6

Jos pöydällä on jo nappula, suorittaa funktiona skIfYouWantNewPiece()

countMove() suorittaa kaiken laskemisen mistä mennään mihin

countMove() tarkistaa meneekö maaliin ja jatketaanko ilman maaliinmenoa vuoroa
checkFinish() funktion avulla

Ohjelma arpoo kuka aloittaa pelin firstPlayer() funktiolla

Ohjelma looppaa kaiken printBoard() funktion kautta

- ###TODO###

Pelaajien vaihtaminen numeroista kirjaimiin B Y G R
Ohjelman logiikka ei muutu tästä. Tehdessä helpompi määritellä pelaajille vain numerot.

Ohjelman hajottaminen muutamaan tiedostoon, esim. yksi tiedosto hoitaa pelaajan liikkumisen
Yleinen siistiminen
XW
