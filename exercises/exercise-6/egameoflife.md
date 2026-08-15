# Game of Life


## 🎮 **Grundläggande koncept**

**Game of Life** är en cellulär automat skapad av matematikern John Conway 1970.
- "Spel för 0 spelare" - inget mänskligt ingripande efter start
- Spelas på ett oändligt rutat papper
- Varje cell kan vara **död (vit)** eller **levande (svart)**
- Används för att studera kaotiska system eller bara för nöjes skull

## 📜 **De fyra reglerna**

1. **Ensamhet**: Levande cell med 0-1 levande grannar → dör
2. **Trängsel**: Levande cell med 4-8 levande grannar → dör  
3. **Återfödelse**: Död cell med exakt 3 levande grannar → återföds
4. **Oförändrad**: Alla övriga celler förblir som de är

## 🔄 **Återkommande mönster**

### **Stabila mönster** (förändras aldrig)
- **Block**: 2×2 kvadrat av levande celler
- **Bikupa**: Hexagon-liknande form

### **Oscillerande mönster** (repeterar i cykler)
- **Blinker**: Växlar mellan horisontell/vertikal linje (2 steg)
- **Pulsar**: Komplext mönster (3 steg)

### **Rymdskepp** (flyttar sig)
- **Seglare (Glider)**: Rör sig diagonalt
- **Lätt rymdskepp**: Rör sig rakt

## 🔬 **Fördjupning: 1-dimensionella automater**

- En rad celler istället för 2D-rutnät
- Varje cell uppdateras baserat på sig själv + 2 grannar
- 8 möjliga input-kombinationer → 2⁸ = **256 möjliga regler**
- **Regel 30**: Skapar kaotiska mönster
- Vissa regler skapar fraktaler (t.ex. Sierpinski-trianglar)
- Mönster har hittats i naturen (snäckskal!)

---

**🔑 Huvudpoäng**: Enkla regler kan skapa komplexa, oförutsägbara och vackra mönster - ett exempel på emergent komplexitet från simpla grundregler.