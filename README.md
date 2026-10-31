# 🖍️ Ausmalbilder-Web-App für Home Assistant

Eine einfache, lokale Web-App für Home Assistant, mit der Kinder Ausmalbilder ansehen, auswählen und direkt ausdrucken können.

Die App läuft im eigenen Heimnetzwerk. Die Bilder werden lokal auf dem Home-Assistant-System gespeichert.

## ✨ Funktionen

- 🖼️ Ausmalbilder übersichtlich anzeigen
- 📂 Eigene Kategorien und Unterordner verwenden
- 🔄 Neue, geänderte und gelöschte Bilder automatisch erkennen
- 🖨️ Ausmalbilder direkt über den Browser ausdrucken
- 🏠 Lokaler Zugriff über Home Assistant
- 💻 Nutzung auf PC, Tablet und Smartphone
- 👨‍👩‍👧‍👧 Ideal für Kinder und den Familienalltag

---

## 📁 1. Ordnerstruktur

Lege die Dateien im Home-Assistant-Konfigurationsverzeichnis unter `/config/www/malbilder/` ab.

    /config/www/malbilder/
    ├── index.html
    ├── scan.py
    ├── manifest.json
    ├── erstelle_bilder.py
    └── bilder/
        ├── Tiere/
        ├── Fahrzeuge/
        └── Weihnachten/

**Dateien und Ordner:**

- `index.html` – Oberfläche der Web-App
- `scan.py` – durchsucht die Bildordner und aktualisiert die Bildübersicht
- `manifest.json` – enthält die erfassten Bildinformationen
- `erstelle_bilder.py` – Skript zur Erstellung von Bildern
- `bilder/` – enthält die Ausmalbilder im JPG- oder PNG-Format

Die Unterordner können nach eigenen Themen benannt werden.

---

## ⚙️ 2. Home Assistant konfigurieren

### Shell Command

Füge folgenden Eintrag in die `configuration.yaml` ein:

    shell_command:
      scan_malbilder: "python3 /config/www/malbilder/scan.py"

Der Befehl startet das Python-Skript und aktualisiert die Bildübersicht.

### Automatische Aktualisierung

Die Home-Assistant-Automation reagiert auf Dateiänderungen im Ordner `bilder/`.

Bei neu erstellten, geänderten oder gelöschten Dateien wartet sie zwei Sekunden und startet anschließend das Scan-Skript.

Voraussetzungen:

- Der Folder Watcher überwacht `/config/www/malbilder/bilder/`.
- Die Ereignisse enthalten den Dateipfad und den Ereignistyp.
- Die Automation ist eingerichtet.
- Der Helfer `input_boolean.neue_bilder` ist vorhanden.

### Automation

Die folgende Automation kann unter Home Assistant im YAML-Modus eingefügt werden:

    alias: 'Malbilder: Automatisch scannen bei neuen Dateien'
    description: Aktualisiert die manifest.json bei Änderungen im Malbilder-Ordner.
    triggers:
      - trigger: event
        event_type: folder_watcher
    conditions:
      - condition: template
        value_template: >
          {% set p = trigger.event.data.path | default('') %}
          {% set t = trigger.event.data.event_type | default('') %}
          {{
            p.startswith('/config/www/malbilder/bilder/')
            and t in ['created', 'modified', 'deleted']
          }}
    actions:
      - delay:
          seconds: 2
      - action: shell_command.scan_malbilder
      - action: input_boolean.turn_off
        target:
          entity_id: input_boolean.neue_bilder
    mode: restart

**Wichtig:** Der Folder Watcher muss separat eingerichtet sein und die entsprechenden Ereignisse liefern.

---

## 🌐 3. Lokaler Zugriff

Öffne die Web-App im Browser:

    http://HOME-ASSISTANT-IP:8123/local/malbilder/index.html

Ersetze `HOME-ASSISTANT-IP` durch die lokale IP-Adresse deines Home-Assistant-Systems.

Beispiel:

    http://192.168.178.10:8123/local/malbilder/index.html

---

## 🔄 4. Neue Ausmalbilder hinzufügen

1. Kopiere neue JPG- oder PNG-Dateien in den passenden Unterordner.
2. Der Folder Watcher erkennt die Änderung.
3. Home Assistant startet automatisch das Scan-Skript.
4. Die `manifest.json` wird aktualisiert.
5. Die Web-App kann mit der aktualisierten Bildübersicht geladen werden.

Falls die automatische Aktualisierung nicht eingerichtet ist, kann das Scan-Skript manuell ausgeführt werden.

---

## 🔒 5. Datenschutz

Die Web-App ist für den lokalen Betrieb im eigenen Heimnetzwerk vorgesehen.

- Die Bilder werden lokal gespeichert.
- Es ist kein externer Webdienst erforderlich.
- Die Nutzung erfolgt über Home Assistant.

---

## 🛠️ 6. Voraussetzungen

- Home Assistant
- Zugriff auf das Konfigurationsverzeichnis
- Python 3 für das Scan-Skript
- Home Assistant Folder Watcher
- Webbrowser auf PC, Tablet oder Smartphone

---

Viel Spaß beim Ausmalen! 🖍️






<img width="1800" height="821" alt="Web App" src="https://github.com/user-attachments/assets/fcead338-5a8a-49bf-8300-43b1825fa579" />

<img width="1893" height="854" alt="image" src="https://github.com/user-attachments/assets/270f7da1-bf43-4371-addd-30cfdbbdd0bd" />

<img width="846" height="528" alt="image" src="https://github.com/user-attachments/assets/880bb6ad-bdfc-45c3-9264-282704e4a71d" />



