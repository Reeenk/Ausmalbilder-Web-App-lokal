# 🖍️ Ausmalbilder-Web-App für Home Assistant

Eine einfache, lokale Web-App für Home Assistant, mit der Kinder Ausmalbilder ansehen, auswählen und direkt ausdrucken können.

Die Bilder werden auf dem eigenen Home-Assistant-System gespeichert. Neue, geänderte oder gelöschte Bilder können automatisch erkannt werden.

## ✨ Funktionen

- 🖼️ Ausmalbilder im Browser anzeigen
- 📂 Bilder nach Ordnern und Kategorien sortieren
- 🔄 Bildübersicht automatisch aktualisieren
- 🖨️ Ausmalbilder direkt ausdrucken
- 🏠 Zugriff im eigenen Heimnetzwerk
- 💻 Nutzung auf PC, Tablet und Smartphone

## 📁 1. Ordnerstruktur

Die Dateien werden im Home-Assistant-Konfigurationsverzeichnis unter `/config/www/malbilder/` abgelegt.

```text
/config/www/malbilder/
├── index.html
├── scan.py
├── manifest.json
└── bilder/
    ├── Tiere/
    ├── Fahrzeuge/
    └── Weihnachten/
```

**Dateien und Ordner:**

- `index.html` – Oberfläche der Web-App
- `scan.py` – durchsucht die Bildordner und aktualisiert die Bildübersicht
- `manifest.json` – enthält die erfassten Bildinformationen
- `bilder/` – enthält die Ausmalbilder im JPG- oder PNG-Format

Die Unterordner können nach eigenen Themen benannt werden.

## ⚙️ 2. Home Assistant konfigurieren

### Shell Command

Füge folgenden Eintrag in die `configuration.yaml` ein:

```yaml
shell_command:
  scan_malbilder: "python3 /config/www/malbilder/scan.py"
```

Der Befehl startet das Scan-Skript und aktualisiert die Bildübersicht.

### Automatische Aktualisierung

Die Home-Assistant-Automation reagiert auf Dateiänderungen im Ordner `bilder/`.

Bei neu erstellten, geänderten oder gelöschten Dateien wartet sie zwei Sekunden und startet anschließend das Scan-Skript.

Voraussetzungen:

- Der Folder Watcher überwacht `/config/www/malbilder/bilder/`.
- Die Ereignisse enthalten den Dateipfad und den Ereignistyp.
- Die Automation ist eingerichtet.
- Der Helfer `input_boolean.neue_bilder` ist vorhanden.

### Lokaler Zugriff

Öffne die Web-App im Browser:

```text
http://HOME-ASSISTANT-IP:8123/local/malbilder/index.html
```

Ersetze `HOME-ASSISTANT-IP` durch die lokale IP-Adresse deines Home-Assistant-Systems.

## 🔄 Neue Ausmalbilder hinzufügen

1. Kopiere neue JPG- oder PNG-Dateien in den passenden Unterordner.
2. Warte auf die automatische Aktualisierung durch Home Assistant.
3. Öffne oder aktualisiere die Web-App im Browser.

Falls die automatische Aktualisierung nicht eingerichtet ist, kann das Scan-Skript manuell ausgeführt werden.

## 🔒 Datenschutz

Die Web-App ist für den lokalen Betrieb im Heimnetzwerk vorgesehen. Die Bilder werden auf dem eigenen Home-Assistant-System gespeichert.

## 🛠️ Voraussetzungen

- Home Assistant
- Zugriff auf das Konfigurationsverzeichnis
- Python 3 für das Scan-Skript
- Webbrowser auf PC, Tablet oder Smartphone




<img width="1800" height="821" alt="Web App" src="https://github.com/user-attachments/assets/fcead338-5a8a-49bf-8300-43b1825fa579" />

<img width="1893" height="854" alt="image" src="https://github.com/user-attachments/assets/270f7da1-bf43-4371-addd-30cfdbbdd0bd" />

<img width="846" height="528" alt="image" src="https://github.com/user-attachments/assets/880bb6ad-bdfc-45c3-9264-282704e4a71d" />



