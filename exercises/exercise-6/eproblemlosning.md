# Problemlösning och algoritmer

## Nyckelkoncept:

### 📋 **Problemlösningsprocessen (Polya's 4 steg)**
1. **Förstå problemet** - Formulera om, identifiera vad som är känt/okänt
2. **Ta fram en plan** - Testa lösningar, jämför med liknande problem, dela upp i mindre delar
3. **Genomför planen** - Implementera lösningen
4. **Utvärdera lösningen** - Kontrollera korrekthet och lär av processen

### 💻 **Algoritmer**
- **Definition**: Ordnad uppsättning otvetydiga, körbara steg som definierar en terminerande process
- **Verktyg för att beskriva algoritmer**:
  - **Flödesschema** - Visuell representation av programmets flöde
  - **Pseudokod** - Kod ämnad för människor, inte datorer

### 🏗️ **Programmeringsmodeller**

**Top-down**: 
- Börja med helheten, dela upp i mindre delproblem
- Specificera funktioner innan implementation
- Ger bra separation of concerns

**Bottom-up**: 
- Börja med enskilda funktioner, bygg uppåt
- Testa varje del med enhetstester
- Mer praktiskt testbar från början

**Hybrid**: Kombinerar båda - vanligast i verkligheten

### ⚡ **Algoritmkomplexitet**
- **Mål**: Minimera kostsamma operationer
- **Exempel** (lapptäcke n×n):
  - Algoritm 1: O(n²) sömmar
  - Algoritm 2: O(n²/2) sömmar  
  - Algoritm 3: O(n) sömmar - "blivit av med kvadraten"
- **Viktigt**: Effektiv algoritm > optimerad kod av ineffektiv algoritm

---

**🔑 Huvudpoäng**: Tänk först, koda sen. Planering med pseudokod/flödesschema sparar tid jämfört med att skriva och kasta bort felaktig kod.