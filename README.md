# ⚡ Widerstand Parallel Rechner

> Findet automatisch zwei E12-Widerstände, die parallel geschaltet einem Zielwiderstand am nächsten kommen – inklusive Abweichungsanzeige in Ohm und Prozent.

Ein Python-Programm zur automatischen Suche optimaler Widerstandskombinationen aus der **E12-Reihe** für eine gewünschte Parallelschaltung.

---

## 📋 Projektbeschreibung

Gegeben einen Zielwiderstand (in Ohm) findet das Programm automatisch zwei Widerstände aus der E12-Normreihe, die parallel geschaltet dem Zielwert am nächsten kommen. Zusätzlich wird die Abweichung in Ohm und Prozent angezeigt.

Entwickelt im Rahmen eines Schulprojekts an der **Technischen Fachschule Bern**.

---

## ✨ Features

- 🔍 **Automatische Suche** des optimalen Widerstandspaars aus der E12-Reihe
- 📐 **E12-Werte** über mindestens 6 Dekaden (10 Ω bis 10 MΩ)
- 📊 **Abweichungsanzeige** in Ohm und Prozent
- ⚡ **Schnelle Berechnung** durch systematisches Durchsuchen aller Kombinationen

---

## 🚀 Verwendung

### Voraussetzungen

- Python 3.x
- Spyder IDE (empfohlen) oder beliebige Python-Umgebung

### Programm starten

```bash
python parallel_rechner.py
```

### Eingabe

Das Programm fragt nach dem gewünschten Zielwiderstand in Ohm:

```
Zielwiderstand eingeben (Ohm): 1500
```

### Beispielausgabe

```
Ziel: 1500 Ω
Beste Kombination:
  R1 = 3300 Ω
  R2 = 2700 Ω
  R_parallel = 1485.0 Ω
  Abweichung = -15.0 Ω (-1.0 %)
```

---

## 🔢 Technischer Hintergrund

### E12-Reihe

Die E12-Reihe enthält 12 normierte Widerstandswerte pro Dekade:

`10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82`

Diese Werte werden über mehrere Dekaden (×1, ×10, ×100, ...) skaliert.

### Parallelschaltung

Der Gesamtwiderstand zweier parallel geschalteter Widerstände berechnet sich nach:

$$R_{parallel} = \frac{R_1 \cdot R_2}{R_1 + R_2}$$

---

## 📁 Projektstruktur

```
parallel-rechner/
│
├── parallel_rechner.py   # Hauptprogramm
└── README.md             # Diese Datei
```

---

## 👥 Autoren

Gruppenprojekt – Technische Fachschule Bern

---

## 📄 Lizenz

Dieses Projekt steht unter der **GNU General Public License v2.0 (GPL v2)**.  
Siehe [LICENSE](LICENSE) für Details oder besuche [gnu.org/licenses/gpl-2.0](https://www.gnu.org/licenses/gpl-2.0.html).
