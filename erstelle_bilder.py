# Damit kann man sich die ersten Bilder erstellen lassen#


import os

pdf_dir = "/config/www/malbilder/pdfs"
img_dir = "/config/www/malbilder/vorschauen"
os.makedirs(pdf_dir, exist_ok=True)
os.makedirs(img_dir, exist_ok=True)

collections = {
    "tiere": [("Katze", "🐱"), ("Hund", "🐶"), ("Hase", "🐰"), ("Pferd", "🐴"), ("Löwe", "🦁"), ("Elefant", "🐘"), ("Giraffe", "🦒"), ("Schmetterling", "🦋"), ("Delfin", "🐬"), ("Eule", "🦉"), ("Fuchs", "🦊"), ("Igel", "🦔"), ("Bär", "🐻"), ("Frosch", "🐸"), ("Pinguin", "🐧"), ("Schildkröte", "🐢"), ("Bauernhoftiere", "🐮"), ("Vögel", "🐦"), ("Tierbabys", "🐾"), ("Waldtiere", "🌳")],
    "pferde": [("Einhorn", "🦄"), ("Pony", "🐴"), ("Pferd auf der Wiese", "🐎"), ("Einhorn mit Sternen", "✨"), ("Fohlen", "🐴"), ("Pferdekopf", "🐴"), ("Pferd mit Blumen", "🌼"), ("Pegasus", "🪽"), ("Einhorn-Regenbogen", "🌈"), ("Pferd im Stall", "🏡"), ("Pony mit Schleife", "🎀"), ("Einhorn-Schloss", "🏰"), ("Pferd beim Springen", "🐎"), ("Einhorn mit Herz", "💗"), ("Pferdefamilie", "🐴"), ("Pony auf der Koppel", "🌱"), ("Einhorn-Mandala", "🌸"), ("Pferd mit Fohlen", "🐎"), ("Einhorn-Kuchen", "🧁"), ("Magisches Einhorn", "⭐")],
    "dinos": [("T-Rex", "🦖"), ("Triceratops", "🦕"), ("Langhals-Dino", "🦕"), ("Dino-Ei", "🥚"), ("Dino im Dschungel", "🌴"), ("Dino-Familie", "🦖"), ("Fliegender Dino", "🪽"), ("Baby-Dino", "🦕"), ("Dino mit Vulkan", "🌋"), ("Dino-Fußspuren", "👣"), ("Dino beim Fressen", "🌿"), ("Dino-Freunde", "🦖"), ("Dino im Ei", "🥚"), ("Dino-Mandala", "⭕"), ("Dino mit Partyhut", "🎉"), ("Dino am See", "💧"), ("Dino im Wald", "🌲"), ("Dino mit Blumen", "🌼"), ("Dino auf Abenteuer", "🗺️"), ("Dino-Ausgrabung", "⛏️")],
    "fahrzeuge": [("Bagger", "🚜"), ("Traktor", "🚜"), ("Feuerwehrauto", "🚒"), ("Polizeiauto", "🚓"), ("Krankenwagen", "🚑"), ("Rennwagen", "🏎️"), ("Motorrad", "🏍️"), ("Fahrrad", "🚲"), ("Zug", "🚂"), ("Flugzeug", "✈️"), ("Hubschrauber", "🚁"), ("Schiff", "🚢"), ("Müllauto", "🚛"), ("Betonmischer", "🚚"), ("Kran", "🏗️"), ("Bus", "🚌"), ("Rakete", "🚀"), ("Traktor auf dem Feld", "🌾"), ("Baustelle", "🏗️"), ("Monstertruck", "🚙")],
    "fantasie": [("Prinzessin", "👑"), ("Drache", "🐉"), ("Fee", "🧚"), ("Meerjungfrau", "🧜‍♀️"), ("Schloss", "🏰"), ("Zauberer", "🪄"), ("Pegasus", "🪽"), ("Regenbogen", "🌈"), ("Sternenwelt", "⭐"), ("Kobold", "🍄"), ("Prinz und Prinzessin", "👑"), ("Zauberwald", "🌳"), ("Einhorn im Wald", "🦄"), ("Drachenbaby", "🐉"), ("Feenhaus", "🍄"), ("Magischer Schlüssel", "🗝️"), ("Wolken-Schloss", "☁️"), ("Fliegender Teppich", "🪄"), ("Meerjungfrau mit Fisch", "🐠"), ("Märchenbuch", "📖")],
    "ostern": [("Osterhase", "🐰"), ("Ostereier", "🥚"), ("Küken", "🐣"), ("Osternest", "🧺"), ("Hase mit Karotte", "🥕"), ("Osterkorb", "🧺"), ("Lämmchen", "🐑"), ("Hase auf der Wiese", "🌷"), ("Eier suchen", "🔎"), ("Küken im Ei", "🐣"), ("Hase mit Schleife", "🎀"), ("Blumen und Eier", "🌷"), ("Osterhase im Garten", "🌱"), ("Osterküken", "🐥"), ("Hasenfamilie", "🐇"), ("Ei mit Mustern", "🥚"), ("Hase im Korb", "🧺"), ("Frühlingsblumen", "🌼"), ("Osterkarte", "💌"), ("Oster-Mandala", "🌸")],
    "halloween": [("Kürbis", "🎃"), ("Freundlicher Geist", "👻"), ("Hexe", "🧙‍♀️"), ("Fledermaus", "🦇"), ("Schwarze Katze", "🐈‍⬛"), ("Spinnennetz", "🕸️"), ("Gespensterhaus", "🏚️"), ("Hexenhut", "🎩"), ("Monster", "👾"), ("Eule im Mondlicht", "🦉"), ("Kürbis mit Gesicht", "🎃"), ("Süßes oder Saures", "🍬"), ("Zaubertrank", "🧪"), ("Vampir", "🧛"), ("Skelett", "💀"), ("Geist mit Kürbis", "👻"), ("Spinne", "🕷️"), ("Fledermäuse am Mond", "🌙"), ("Halloween-Katze", "🐈‍⬛"), ("Gruselschloss", "🏰")],
    "weihnachten": [("Weihnachtsbaum", "🎄"), ("Weihnachtsmann", "🎅"), ("Rentier", "🦌"), ("Schneemann", "⛄"), ("Geschenke", "🎁"), ("Lebkuchenmann", "🍪"), ("Engel", "👼"), ("Weihnachtssocke", "🧦"), ("Schlitten", "🛷"), ("Stern", "⭐"), ("Weihnachtskugel", "🔴"), ("Wichtel", "🧝"), ("Lebkuchenhaus", "🏠"), ("Glocken", "🔔"), ("Kerzen", "🕯️"), ("Schneeflocken", "❄️"), ("Weihnachtskatze", "🐱"), ("Rentier mit Schal", "🦌"), ("Adventskranz", "🕯️"), ("Weihnachtskarte", "💌")],
    "geburtstag": [("Geburtstagstorte", "🎂"), ("Luftballons", "🎈"), ("Geschenke", "🎁"), ("Girlande", "🎊"), ("Partyhüte", "🥳"), ("Cupcakes", "🧁"), ("Konfetti", "🎉"), ("Geburtstagskrone", "👑"), ("Teddybär mit Geschenk", "🧸"), ("Einhorn-Party", "🦄"), ("Dino-Party", "🦖"), ("Zahl 1", "1️⃣"), ("Zahl 2", "2️⃣"), ("Zahl 3", "3️⃣"), ("Kerzen auspusten", "🕯️"), ("Geburtstagskarte", "💌"), ("Partytiere", "🐶"), ("Pinata", "🎊"), ("Muffins", "🧁"), ("Feier mit Freunden", "🎉")]
}

def make_pdf(filepath, title):
    stream_content = f"BT /F1 24 Tf 100 750 Td (Ausmalbild: {title}) ET 3 w 50 50 495 650 Cl S 2 w 297 375 150 0 360 arc S 297 375 100 0 360 arc S 297 375 50 0 360 arc S"
    stream_len = len(stream_content)
    pdf_text = f"""%PDF-1.4
1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj
2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj
3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >> endobj
4 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >> endobj
5 0 obj << /Length {stream_len} >> stream
{stream_content}
endstream endobj
xref
0 6
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000223 00000 n 
0000000292 00000 n 
trailer << /Size 6 /Root 1 0 R >>
startxref
{360 + stream_len}
%%EOF"""
    with open(filepath, "wb") as f:
        f.write(pdf_text.encode('latin1', errors='ignore'))

# Simples 1x1 Pixel Bild als reiner Bytes-Code (ohne ungültige Zeichen)
tiny_jpg = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00`\x00`\x00\x00\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c \$.\"\x11\x01\xff\xc0\x00\x0b\x08\x00\x01\x00\x01\x01\x01\x11\x00\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\xfa\xff\xda\x00\x08\x01\x01\x00\x00?\x00\x7f\xff\xd9'

count = 0
for cat_id, items in collections.items():
    for idx, (name, emoji) in enumerate(items):
        make_pdf(os.path.join(pdf_dir, f"{cat_id}-{idx}.pdf"), name)
        with open(os.path.join(img_dir, f"{cat_id}-{idx}.jpg"), "wb") as f:
            f.write(tiny_jpg)
        count += 1

print(f"Erfolgreich {count} PDFs und Vorschaubilder erstellt!")
