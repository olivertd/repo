# PROGRAM FELHANTERING SDPÅRVAGN FELHANTERING 3
# KOKCHun

# Välkommnar användaren till programmet
print("Hej Kokchun, Detta program är för dig som är en ovan och klumpig datoranvändare.\nVi ska ta reda på om det är värt för dig att köpa månadskort eller inte, Du kommer behöva svara på några frågor.")

# Skapar en fin while sats som frågar användaren om antalet gånger hen ska åka spårvagn, den breakar endast om användaren skriver heltal och skriver annars ut ett felmeddelande och frågar användaren igen.
while True:
    try:
        antlggrvgn = int(input("Hur många gånger vill du åka spårvagn? "))
        break
    except ValueError:
        print("Du måste skriva in hela tal kokchun!")

# Skapar en fin while sats som frågar användaren om engångspriset för spårvagn, den breakar endast om användaren skriver heltal och skriver annars ut ett felmeddelande och frågar användaren igen.
while True:
    try:
        enggskstnd = int(
            input("Hur mycket kostar det att åka spårvagn EN enstaka gång för dig? "))
        break
    except ValueError:
        print("Du måste skriva in hela tal kokchun!")

# Skapar en fin while sats som frågar användaren om månadskortspriset, den breakar endast om användaren skriver heltal och skriver annars ut ett felmeddelande och frågar användaren igen.
while True:
    try:
        mndskstn = int(input("Vad kostar ett månadskort för dig? "))
        break
    except ValueError:
        print("Du måste skriva in hela tal kokchun!, vänligen svara på frågan igen")

# HÄR kollar jag vad det kommer kosta att åka spårvagn ifall man kör på engångspriserna gånger antalet gånger man ska åka
engangsbljtmndskstnad = enggskstnd * antlggrvgn

if engangsbljtmndskstnad > mndskstn:
    print("Månadskort kostar", mndskstn, "kr och om du endast köper engangsbiljetter kommer det istället att kosta dig", engangsbljtmndskstnad,"kr.\nDetta innebär att du kommer att spara pengar genom att köpa månadskortet.")
else:
    print("Månadskort kostar", mndskstn, "kr och om du endast köper engangsbiljetter kommer det istället att kosta dig", engangsbljtmndskstnad,"kr.\nDetta innebär att du kommer att spara pengar genom att skippa månadskortet och istället köpa biljetter.")
