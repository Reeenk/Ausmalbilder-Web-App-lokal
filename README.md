# 🖍️ Ausmalbilder-Web-App für Home Assistant

Eine lokale Web-App für Home Assistant, mit der Kinder Ausmalbilder übersichtlich ansehen, auswählen und direkt ausdrucken können. Neue Bilder werden über ein Python-Skript erfasst und die Bildübersicht kann automatisch aktualisiert werden.

## ✨ Funktionen

- 🖼️ Ausmalbilder aus eigenen Ordnern anzeigen
- 📂 Eigene Kategorien und Unterordner verwenden
- 🔄 Neue, geänderte und gelöschte Bilder automatisch erfassen
- 🖨️ Bilder direkt über den Browser ausdrucken
- 🏠 Lokal im Heimnetzwerk nutzbar
- 👨‍👩‍👧‍👧 Ideal für PC, Tablet und Kinder

## 📁 1. Ordnerstruktur

Lege die Dateien im Home-Assistant-Konfigurationsverzeichnis unter `/config/www/malbilder/` ab.

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

- `index.html` – Oberfläche der Web-App
- `scan.py` – durchsucht die Bildordner und erstellt bzw. aktualisiert die Bildübersicht
- `manifest.json` – enthält die erfassten Bildinformationen
- `bilder/` – enthält die Ausmalbilder im JPG- oder PNG-Format

## ⚙️ 2. Home Assistant konfigurieren

### Shell Command

Füge folgenden Eintrag in die `configuration.yaml` ein:

```yaml
shell_command:
  scan_malbilder: "python3 /config/www/malbilder/scan.py"
```

### Automatische Aktualisierung

Die Automation reagiert auf `folder_watcher`-Ereignisse. Werden Bilder im überwachten Ordner erstellt, geändert oder gelöscht, wartet sie zwei Sekunden und startet anschließend das Scan-Skript.

Damit das funktioniert, müssen folgende Voraussetzungen erfüllt sein:

- Der Folder Watcher überwacht `/config/www/malbilder/bilder/`.
- Die Ereignisse enthalten den Dateipfad und den Ereignistyp `created`, `modified` oder `deleted`.
- Die Automation ist eingerichtet.
- Der Helfer `input_boolean.neue_bilder` existiert.

### Lokaler Zugriff

Öffne die App im Browser über:

```text
http://HOME-ASSISTANT-IP:8123/local/malbilder/index.html
```

Ersetze `HOME-ASSISTANT-IP` durch die lokale IP-Adresse deines Home-Assistant-Systems.

**Hinweis:** Nach Änderungen an der `configuration.yaml` muss Home Assistant gegebenenfalls neu gestartet werden. Die automatische Aktualisierung setzt einen korrekt eingerichteten Folder Watcher voraus.



<img width="1800" height="821" alt="Web App" src="https://github.com/user-attachments/assets/fcead338-5a8a-49bf-8300-43b1825fa579" />

<img width="1893" height="854" alt="image" src="https://github.com/user-attachments/assets/270f7da1-bf43-4371-addd-30cfdbbdd0bd" />

<img width="846" height="528" alt="image" src="https://github.com/user-attachments/assets/880bb6ad-bdfc-45c3-9264-282704e4a71d" />



