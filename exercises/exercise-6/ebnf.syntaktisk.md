# EBNF

**EBNF** är ett sätt att beskriva **grammatikregler** för programmeringsspråk. Det är som en "ritning" som visar vilka kombinationer av ord och symboler som är tillåtna.

## **Analogi: Recept**

Tänk på EBNF som ett recept som säger vilka ingredienser du kan använda och i vilken ordning.

---

## **Grundläggande symboler:**

| Symbol | Betydelse | Exempel |
|--------|-----------|---------|
| `=` | "definieras som" | `greeting = "hello"` |
| `,` | "följt av" | `a, b` (först a, sen b) |
| `\|` | "eller" | `a \| b` (antingen a eller b) |
| `[ ]` | "valfritt" | `[a]` (a kan finnas eller inte) |
| `{ }` | "upprepa 0+ gånger" | `{a}` (ingen a, en a, eller många a) |
| `( )` | "gruppera" | `(a \| b)` |
| `" "` | "exakt text" | `"hello"` |
| `;` | "slut på regel" | Avslutar definitionen |

---

## **Enkelt exempel: Hälsningar**

```ebnf
greeting = "hello" | "hej" | "hi" ;
```

**Betyder:** En hälsning kan vara "hello" ELLER "hej" ELLER "hi"

**Giltiga exempel:**
- `hello` ✓
- `hej` ✓
- `hi` ✓
- `goodbye` ✗ (inte i regeln)

---

## **Exempel med följd:**

```ebnf
sentence = greeting, name ;
greeting = "hello" | "hi" ;
name = "Anna" | "Erik" ;
```

**Betyder:** En mening är en hälsning FÖLJT AV ett namn

**Giltiga exempel:**
- `hello Anna` ✓
- `hi Erik` ✓
- `hello` ✗ (namn saknas)

---

## **Exempel med upprepning:**

```ebnf
program = { statement } ;
statement = "hello" | "goodbye" ;
```

**Betyder:** Ett program är 0 eller fler statements

**Giltiga exempel:**
- `` (tomt program) ✓
- `hello` ✓
- `hello goodbye hello` ✓

---

## **Exempel med valfritt:**

```ebnf
greeting = "hello", [ name ] ;
name = "Anna" | "Erik" ;
```

**Betyder:** En hälsning är "hello" och KANSKE ett namn

**Giltiga exempel:**
- `hello` ✓
- `hello Anna` ✓

---

## **Verkligt exempel: Enkelt matematiskt uttryck**

```ebnf
expression = number, operator, number ;
number = "0" | "1" | "2" | "3" | "4" | "5" ;
operator = "+" | "-" | "*" ;
```

**Giltiga exempel:**
- `2 + 3` ✓
- `5 * 1` ✓
- `2 + + 3` ✗ (två operatorer)

---

## **Varför använda EBNF?**

1. **Dokumentation** - Visa exakt vad som är giltig syntax
2. **Bygga parser** - Datorn kan läsa EBNF och förstå språket
3. **Kommunikation** - Utvecklare förstår språkets regler

**Kort sagt:** EBNF är en manual som säger "så här får man skriva kod i detta språk"! 📖
