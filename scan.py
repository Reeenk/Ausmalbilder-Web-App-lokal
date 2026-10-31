#!/usr/bin/env python3
"""
Malbilder: erzeugt manifest.json aus dem Ordner "bilder/".

Liegt neben index.html. Jeder Unterordner von bilder/ wird eine Gruppe,
jede Bilddatei darin ein Bild. Namen werden aus den Datei-/Ordnernamen gemacht:

    bilder/tiere/hund_mit_ball.png        ->  Gruppe "Tiere",  Bild "Hund Mit Ball"
    bilder/tiere/3.png                    ->  Bild "Bild 3"
    bilder/02-14_valentinstag/herz.png    ->  Termin-Gruppe "Valentinstag" (jedes Jahr am 14.2.)

Ordner/Dateien, die mit "." oder "_" beginnen, werden ignoriert.
Nur Standardbibliothek, laeuft mit jedem Python 3.
"""
import datetime
import json
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
BILDER = os.path.join(HIER, "bilder")
AUSGABE = os.path.join(HIER, "manifest.json")
ENDUNGEN = (".png", ".jpg", ".jpeg", ".webp", ".gif")


def natuerlich(text):
    """1, 2, 10 statt 1, 10, 2"""
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", text)]


def woerter(text):
    text = re.sub(r"[_\-]+", " ", text).strip()
    text = re.sub(r"\s+", " ", text)
    return " ".join(w[:1].upper() + w[1:] for w in text.split(" ")) or text


EMOJI_PATTERN = re.compile(
    r"[\U0001F300-\U0001FAFF]|[\U00002600-\U000027BF]|[\U0001F1E6-\U0001F1FF]"
)


def ohne_datumspraefix(teil):
    """Entfernt ein optionales Terminpräfix wie 10-31_ oder 10-31 ."""
    return re.sub(r"^\d{2}-\d{2}[_ ]", "", teil)


def emoji_am_anfang(teil):
    """Liefert ein am Anfang stehendes Emoji, wenn der Ordner so benannt ist."""
    teil = ohne_datumspraefix(teil).lstrip()
    match = EMOJI_PATTERN.match(teil)
    if not match:
        return ""
    emoji = match.group(0)
    # Häufige Bestandteile eines Emoji-Zeichens (z.B. Variation Selector / Hautton).
    ende = match.end()
    while ende < len(teil) and teil[ende] in ("\ufe0f", "\ufe0e"):
        ende += 1
    if ende < len(teil) and "\U0001f3fb" <= teil[ende] <= "\U0001f3ff":
        ende += 1
    emoji = teil[:ende]
    # Flaggen bestehen meist aus zwei Regional-Indikator-Zeichen.
    if "\U0001f1e6" <= emoji <= "\U0001f1ff" and ende < len(teil) and "\U0001f1e6" <= teil[ende] <= "\U0001f1ff":
        emoji += teil[ende]
        ende += 1
    return emoji


def ordner_name(teil):
    """Macht aus '🎃 Halloween' den Anzeigenamen 'Halloween'."""
    teil = ohne_datumspraefix(teil)
    emoji = emoji_am_anfang(teil)
    if emoji:
        teil = teil[len(emoji):].lstrip()
        teil = re.sub(r"^[\ufe0e\ufe0f]+", "", teil).lstrip()
    return woerter(teil) or teil or woerter(ohne_datumspraefix(teil))


def passendes_icon(ordner_id, ordner_name_str):
    """Nutzt ein führendes Ordner-Emoji; sonst erfolgt die Erkennung per Schlüsselwort."""
    # Bei verschachtelten Ordnern gilt das Icon des untersten Ordners.
    letzter_ordner = ordner_id.split("/")[-1] if ordner_id else ""
    explizites_icon = emoji_am_anfang(letzter_ordner)
    if explizites_icon:
        return explizites_icon

    # Rückwärtskompatibel: erkennt ein Emoji auch an anderer Stelle im Namen.
    match = EMOJI_PATTERN.search(ordner_name_str)
    if match:
        return match.group(0)

    # 2. Automatische Erkennung anhand von Schlüsselwörtern
    text = (ordner_id + " " + ordner_name_str).lower()
    
    if "ostern" in text:
        return "🐰"
    elif "weihnachten" in text or "winter" in text:
        return "🎄"
    elif "valentinstag" in text:
        return "💖"
    elif "sankt martin" in text or "martin" in text:
        return "🏮"
    elif "geburtstag" in text or "party" in text:
        return "🎂"
    elif "tiere" in text or "bauernhof" in text or "dschungel" in text:
        return "🐾"
    elif "fahrzeug" in text or "auto" in text or "traktor" in text:
        return "🚗"
    elif "fantasie" in text or "prinzessin" in text or "einhorn" in text:
        return "✨"
    elif "grusel" in text or "halloween" in text:
        return "🎃"
    else:
        return "📁"  # Standard-Ordner-Icon


def datei_name(datei):
    basis = os.path.splitext(datei)[0]
    if basis.isdigit():
        return "Bild " + str(int(basis))
    return woerter(basis) or basis


def main():
    ordner = []
    if os.path.isdir(BILDER):
        for root, dirs, files in os.walk(BILDER):
            dirs[:] = sorted((d for d in dirs if not d.startswith((".", "_"))), key=natuerlich)
            rel = os.path.relpath(root, BILDER).replace(os.sep, "/")
            rel = "" if rel == "." else rel
            
            bilder = [
                {"datei": f, "name": datei_name(f)}
                for f in sorted(files, key=natuerlich)
                if f.lower().endswith(ENDUNGEN) and not f.startswith((".", "_"))
            ]
            if not bilder:
                continue
                
            name = " / ".join(ordner_name(t) for t in rel.split("/")) if rel else "Bilderbibliothek"
            icon = passendes_icon(rel, name)
            
            ordner.append({
                "id": rel, 
                "name": name, 
                "icon": icon,
                "bilder": bilder
            })
    else:
        print("Hinweis: Ordner nicht gefunden:", BILDER, file=sys.stderr)

    daten = {"erstellt": datetime.datetime.now().isoformat(timespec="seconds"), "ordner": ordner}
    tmp = AUSGABE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(daten, f, ensure_ascii=False, indent=1)
    os.replace(tmp, AUSGABE)
    try:
        os.chmod(AUSGABE, 0o644)
    except OSError:
        pass

    summe = sum(len(o["bilder"]) for o in ordner)
    print("manifest.json geschrieben: %d Ordner, %d Bilder" % (len(ordner), summe))
    for o in ordner:
        print("  %-30s %3d Bilder    (%s)" % (o["id"] or "(lose Bilder)", len(o["bilder"]), o["name"]))


if __name__ == "__main__":
    main()
