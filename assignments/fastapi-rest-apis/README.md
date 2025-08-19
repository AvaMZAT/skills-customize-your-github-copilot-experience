# 📘 Assignment: FastAPI – Building REST APIs

## 🎯 Objective

Erstelle eine kleine REST-API mit FastAPI, um CRUD-Operationen für eine einfache Ressource (z. B. Tasks, Books oder Students) umzusetzen. Du lernst Routen, Request/Response-Modelle und Validierung kennen.

## 📝 Tasks

### 🛠️ Aufgabe 1: Projektgerüst & Hello World

#### Beschreibung
-Richte ein FastAPI-Projekt ein und implementiere eine einfache Root-Route `GET /` mit einer JSON-Antwort.

#### Anforderungen
Das fertige Programm soll:

- Eine lauffähige FastAPI-App bereitstellen
- Eine Route `GET /` mit `{ "message": "Hello FastAPI" }` zurückgeben
- Startanleitung im README enthalten

### 🛠️ Aufgabe 2: CRUD für Ressource

#### Beschreibung
-Implementiere CRUD-Endpunkte für eine Ressource deiner Wahl (z. B. `items`). Nutze Pydantic-Modelle für Eingabe/Antwort.

#### Anforderungen
Das fertige Programm soll:

- Datenmodell(e) mit Pydantic definieren (z. B. ItemCreate, ItemUpdate, Item)
- Endpunkte: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, `DELETE /items/{id}`
- In-Memory-Speicher (Liste/Dikt) verwenden
- Sinnvolle Statuscodes zurückgeben (201, 404, 204, ...)

### 🛠️ Aufgabe 3 (Bonus): Validierung & Filter

#### Beschreibung
-Erweitere die API um Validierungen (z. B. Länge, Wertebereiche) und optionale Filter-/Suchparameter.

#### Anforderungen
Mögliche Erweiterungen:

- Query-Parameter für Suche/Filter (z. B. `?q=` oder `?min_price=`)
- Fehlerbehandlung mit HTTPException (404, 422)
- Paginierung (limit/offset)

---

## ▶️ Starten

1. Abhängigkeiten installieren
2. Server starten
3. Swagger-UI öffnen

```
# Install
pip3 install fastapi uvicorn[pstandard] pydantic

# Run
uvicorn app:app --reload

# Open Docs
# http://127.0.0.1:8000/docs
```

## ✅ Abgabehinweise

- API läuft lokal, README enthält klare Startanleitung
- Alle geforderten Endpunkte vorhanden, Antworten getestet
- Bonus: Mindestens eine Erweiterung umgesetzt
