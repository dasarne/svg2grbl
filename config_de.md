# Konfiguration (config.py)

Die Datei `config.py` ermöglicht die Anpassung wichtiger Parameter für den CNC-Betrieb:

### Wichtige Parameter

```python
SAFE_HEIGHT = 5.0   # Sicherheitsabstand in mm (Z-Position beim Verfahren zwischen Pfaden)
CUT_DEPTH = -1.0    # Gravurtiefe in mm (Z-Position während der Bearbeitung)
FEED_RATE = 300     # Vorschubgeschwindigkeit in mm/min
```

- **SAFE\_HEIGHT**: Die Höhe, auf die sich die Spindel zwischen den Gravurpfaden bewegt.
- **CUT\_DEPTH**: Die Tiefe, in die während der Gravur geschnitten wird.
- **FEED\_RATE**: Die Geschwindigkeit, mit der das Werkzeug während der Gravur bewegt wird.

### Bewegungssteuerung

```python
def pen_up():
    yield f'G0 Z{SAFE_HEIGHT}'  # Hebt die Spindel auf die Sicherheitsposition

def pen_down():
    yield f'G1 Z{CUT_DEPTH} F{FEED_RATE}'  # Senkt die Spindel auf Gravurtiefe
```

Diese Funktionen steuern die Bewegung der Spindel:

- **`pen_up()`** hebt das Werkzeug vor schnellen Bewegungen an.
- **`pen_down()`** senkt das Werkzeug vor der Gravur ab und wendet die festgelegte Vorschubgeschwindigkeit an.

### Automatische Skalierung und Rotation (Optional)

```python
AUTO_SCALING = False  # Auf True setzen, um SVG auf den CNC-Arbeitsbereich zu skalieren
AUTO_ROTATE = False   # Auf True setzen, um eine automatische Rotation zu ermöglichen
```

- **AUTO\_SCALING**: Wenn aktiviert, wird das SVG auf den verfügbaren Arbeitsbereich skaliert.
- **AUTO\_ROTATE**: Wenn aktiviert, dreht das Programm das Design automatisch, um es optimal auf den CNC-Arbeitsbereich anzupassen.

### Anpassung des SVG-Ursprungs

```python
SVG_ORIGIN_BOTTOM_LEFT = True  # Konvertiert den SVG-Oben-Links-Ursprung in Unten-Links für CNC
```

- **SVG\_ORIGIN\_BOTTOM\_LEFT**: Wenn aktiviert, werden die SVG-Koordinaten so verschoben, dass die CNC (0,0) als die untere linke Ecke interpretiert.

## Nutzung

1. Erstelle eine **SVG-Datei** mit den gewünschten Gravurpfaden.
2. Konvertiere sie mit `svg2gcode.py` in G-Code.
3. Lade den G-Code in deine CNC-Maschine.
4. Starte die Gravur.

## Lizenz & Mitwirkung

Dieser Fork ist eine Weiterentwicklung des ursprünglichen Projekts. Pull Requests und Verbesserungen sind jederzeit willkommen!

Das Ziel ist, **die Nutzung für CNC-Maschinen zu optimieren, während die Softwaremodifikationen an der SVG-Datei minimal bleiben und maximale Kontrolle über das Gravurergebnis gewährleistet wird**.

