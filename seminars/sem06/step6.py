"""
TDDE23 Seminarium 6 - En sak i taget
Undantag och Testning
"""

# =============================================================================
# DISKUSSION: VAD ÄR "FEL"?
# =============================================================================

print("=" * 70)
print("DISKUSSION: VAD ÄR 'FEL'?")
print("=" * 70)

discussion_1 = """
1. Vad är ett fel i ett program?
   ─────────────────────────────────────────────────────────────────
   Ett fel (bug) är när programmet:
   
   • SYNTAXFEL: Bryter mot språkets regler
     Exempel: saknad parentes, felstavat nyckelord
     
   • KÖRNINGSFEL (Runtime errors): Kraschar under exekvering
     Exempel: division med noll, indexering utanför lista
     
   • LOGISKA FEL: Ger fel resultat men kraschar inte
     Exempel: fel formel, felaktig algoritm, off-by-one errors
     
   • SEMANTISKA FEL: Kod som fungerar men gör något annat än avsett
     Exempel: räknar min istället för max
   
   
2. När och hur upptäcks fel?
   ─────────────────────────────────────────────────────────────────
   • KOMPILERINGSTID (Python: vid parsing):
     - Syntaxfel upptäcks direkt när Python läser koden
     - Exempel: SyntaxError, IndentationError
   
   • KÖRTID (Runtime):
     - Fel som uppstår när programmet körs
     - Exempel: ZeroDivisionError, IndexError, KeyError
     - Upptäcks när den felaktiga koden exekveras
   
   • UNDER TESTNING:
     - Logiska fel som ger fel resultat
     - Upptäcks genom manuell testning eller automatiska tester
     - Exempel: funktionen returnerar 5 istället för 4
   
   • EFTER RELEASE (av användare):
     - Edge cases som inte testats
     - Fel som bara uppstår i produktionsmiljö
     - Exempel: problem med specifik användardata


3. Vad kan orsaka fel?
   ─────────────────────────────────────────────────────────────────
   • MISSFÖRSTÅND AV PROBLEMET:
     - Felaktig tolkning av krav/specifikation
     - Kommunikationsproblem
   
   • PROGRAMMERINGSFEL:
     - Stavfel, slarvfel, tankefel
     - Felaktig logik eller algoritm
     - Off-by-one errors (räknefel med index)
   
   • BRIST PÅ KUNSKAPER:
     - Missförstånd av språkets funktioner
     - Felaktig användning av bibliotek/API:er
   
   • OVÄNTAD INPUT:
     - Användare matar in ogiltig data
     - External system ger oväntat format
   
   • RESURSPROBLEM:
     - Slut på minne
     - Fil finns inte
     - Nätverksfel


4. Hur kan man lokalisera och åtgärda fel?
   ─────────────────────────────────────────────────────────────────
   LOKALISERINGSSTRATEGIER:
   
   • LÄSA FELMEDDELANDEN:
     - Traceback visar var felet uppstod
     - Feltyp ger hints om vad som är fel
   
   • PRINT-DEBUGGING:
     - Lägg in print() för att se variabelvärden
     - Följ programmets flöde
   
   • ANVÄND DEBUGGER:
     - Sätt breakpoints
     - Stega igenom kod rad för rad
     - Inspektera variabler
   
   • GUMMIANKA-METODEN (Rubber Duck Debugging):
     - Förklara koden högt (för en anka/kollega)
     - Ofta hittar man felet när man förklarar
   
   • BINÄR SÖKNING:
     - Kommentera bort halva koden
     - Identifiera vilken del som innehåller felet
     - Upprepa tills felet hittas
   
   • TESTA MED ENKLARE INPUT:
     - Använd minimal testdata
     - Gör problemet mindre och enklare
   
   ÅTGÄRDSSTRATEGIER:
   
   • FIXA ROTEN TILL PROBLEMET:
     - Inte bara symptomen
     - Förstå varför felet uppstod
   
   • SKRIV TEST:
     - Skapa test som visar felet
     - Säkerställ att fix faktiskt löser problemet
   
   • REFAKTORERA:
     - Skriv om förvirrande kod
     - Gör koden mer läsbar och underhållbar
   
   • DOKUMENTERA:
     - Kommentera varför en fix gjordes
     - Hjälper framtida underhåll
"""

print(discussion_1)


# =============================================================================
# DISKUSSION: UNDANTAG (EXCEPTIONS)
# =============================================================================

print("\n" + "=" * 70)
print("DISKUSSION: UNDANTAG I PYTHON")
print("=" * 70)

print("\nVanliga undantag och deras orsaker:")
print("-" * 70)

# Demonstrera vanliga undantag med exempel
exceptions_demo = [
    {
        "name": "SyntaxError",
        "cause": "Felaktig syntax, bryter mot Pythons grammatik",
        "example": "if x == 5  # Saknar kolon",
        "code": None  # Kan inte köra kod med syntaxfel
    },
    {
        "name": "IndentationError",
        "cause": "Fel indentering (indrag)",
        "example": "def func():\nprint('hej')  # Fel indrag",
        "code": None
    },
    {
        "name": "NameError",
        "cause": "Variabel eller funktion som inte existerar",
        "example": "print(x)  # x är inte definierad",
        "code": lambda: print(x)
    },
    {
        "name": "TypeError",
        "cause": "Operation på fel datatyp",
        "example": "'hello' + 5  # Kan inte addera sträng och int",
        "code": lambda: "hello" + 5
    },
    {
        "name": "ValueError",
        "cause": "Rätt typ men ogiltigt värde",
        "example": "int('abc')  # 'abc' kan inte konverteras till int",
        "code": lambda: int('abc')
    },
    {
        "name": "IndexError",
        "cause": "Index utanför listans gränser",
        "example": "[1, 2, 3][5]  # Index 5 finns inte",
        "code": lambda: [1, 2, 3][5]
    },
    {
        "name": "KeyError",
        "cause": "Nyckel finns inte i dictionary",
        "example": "{'a': 1}['b']  # Nyckel 'b' finns inte",
        "code": lambda: {'a': 1}['b']
    },
    {
        "name": "AttributeError",
        "cause": "Objekt har inte det attributet/metoden",
        "example": "'hello'.append('!')  # Strängar har ingen append",
        "code": lambda: "hello".append('!')
    },
    {
        "name": "ZeroDivisionError",
        "cause": "Division eller modulo med noll",
        "example": "10 / 0",
        "code": lambda: 10 / 0
    },
    {
        "name": "FileNotFoundError",
        "cause": "Filen som ska öppnas finns inte",
        "example": "open('finns_inte.txt')",
        "code": lambda: open('finns_inte.txt')
    },
    {
        "name": "ImportError / ModuleNotFoundError",
        "cause": "Kan inte importera modul",
        "example": "import icke_existerande_modul",
        "code": None
    },
]

for exc in exceptions_demo:
    print(f"\n{exc['name']}:")
    print(f"  Orsak: {exc['cause']}")
    print(f"  Exempel: {exc['example']}")
    
    if exc['code']:
        print(f"  Demonstration:")
        try:
            exc['code']()
        except Exception as e:
            print(f"    → {type(e).__name__}: {e}")


# Visa hur man hanterar undantag
print("\n" + "-" * 70)
print("Hantera undantag med try-except:")
print("-" * 70)

print("\nEXEMPEL 1: Grundläggande try-except")
print("─" * 40)
try:
    result = 10 / 0
    print(f"Resultat: {result}")
except ZeroDivisionError:
    print("Fel: Kan inte dela med noll!")
    result = None

print("\nEXEMPEL 2: Hantera flera undantagstyper")
print("─" * 40)
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Fel: Division med noll")
        return None
    except TypeError:
        print("Fel: Kan bara dela tal")
        return None

print(f"safe_divide(10, 2) = {safe_divide(10, 2)}")
print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")
print(f"safe_divide(10, 'x') = {safe_divide(10, 'x')}")

print("\nEXEMPEL 3: try-except-else-finally")
print("─" * 40)
def read_file_safe(filename):
    try:
        # Försök öppna filen
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        # Körs om filen inte finns
        print(f"Filen '{filename}' hittades inte")
        content = None
    else:
        # Körs om inget undantag kastades
        print(f"Filen lästes framgångsrikt")
    finally:
        # Körs alltid, oavsett vad som hände
        print("Fil-operation avslutad")
    
    return content

print("\nFörsök läsa en fil som inte finns:")
read_file_safe("finns_inte.txt")

print("\nEXEMPEL 4: Kasta egna undantag med raise")
print("─" * 40)
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Ålder måste vara ett heltal")
    if age < 0:
        raise ValueError("Ålder kan inte vara negativ")
    if age > 150:
        raise ValueError("Ålder verkar osannolik")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Valideringsfel: {e}")


# =============================================================================
# DISKUSSION: TESTNING
# =============================================================================

print("\n" + "=" * 70)
print("DISKUSSION: TESTNING")
print("=" * 70)

testing_discussion = """
TESTNIVÅER:
───────────────────────────────────────────────────────────────────

1. ENHETSTESTNING (Unit Testing):
   • Testar enskilda funktioner/metoder isolerat
   • Minsta testbara enhet
   • Snabba, många tester
   • Exempel: Testa att add(2, 3) returnerar 5
   
2. INTEGRATIONSTESTNING (Integration Testing):
   • Testar hur komponenter fungerar tillsammans
   • Fokus på gränssnitten mellan moduler
   • Testar dataflöde mellan komponenter
   • Exempel: Testa att databasen och affärslogik fungerar tillsammans
   
3. SYSTEMTEST (System Testing):
   • Testar hela systemet som helhet
   • End-to-end testning
   • Testar fullständiga användningsscenarier
   • Exempel: Testa hela flödet från inloggning till utloggning
   
4. ACCEPTANSTEST (Acceptance Testing):
   • Testar om systemet uppfyller kundens krav
   • Ofta utfört av kund/användare
   • Validerar affärsnytta
   • Exempel: Kunden testar att systemet löser deras problem


TESTSTRATEGIER:
───────────────────────────────────────────────────────────────────

1. WHITE-BOX TESTNING (Glasbox):
   • Testaren känner till intern struktur/kod
   • Testar baserat på kodtäckning
   • Fokus på logiska vägar genom koden
   • Mål: Hög kodtäckning (code coverage)
   
   Fördelar:
   • Kan hitta dolda fel
   • Kan testa specifika kodvägar
   • Bra för komplex logik
   
   Nackdelar:
   • Kräver kunskap om implementation
   • Kan missa användarperspektiv
   • Tidskrävande

2. BLACK-BOX TESTNING (Svartlåda):
   • Testaren känner INTE till intern struktur
   • Testar baserat på specifikation/krav
   • Fokus på input och förväntad output
   • Användarperspektiv
   
   Fördelar:
   • Oberoende av implementation
   • Fokuserar på användarbehov
   • Enklare att komma igång
   
   Nackdelar:
   • Kan missa edge cases i koden
   • Svårt att få full kodtäckning
   • Kan missa intern logikfel


PLANERA OCH GENOMFÖRA TESTNING:
───────────────────────────────────────────────────────────────────

1. PLANERING:
   • Identifiera vad som ska testas
   • Definiera testfall (test cases)
   • Bestäm framgångskriterier
   • Prioritera viktiga funktioner
   
2. SKRIVA TESTER:
   • Börja med enkla, grundläggande fall
   • Lägg till edge cases (gränsfall)
   • Testa felhantering
   • Testa med ogiltig input
   
3. ORGANISERA TESTER:
   • Gruppera relaterade tester
   • Använd beskrivande namn
   • En assert per test (helst)
   • Tester ska vara oberoende av varandra
   
4. AUTOMATISERA:
   • Använd testramverk (unittest, pytest)
   • Kör tester ofta
   • Integrera i build-process (CI/CD)
   
5. UNDERHÅLL:
   • Uppdatera tester när kod ändras
   • Ta bort föråldrade tester
   • Refaktorera tester som blir komplexa


BRA TESTPRAXIS:
───────────────────────────────────────────────────────────────────

• AAA-PATTERN (Arrange-Act-Assert):
  1. Arrange: Sätt upp testdata
  2. Act: Utför åtgärden som testas
  3. Assert: Verifiera resultatet

• TESTA GRÄNSFALL:
  - Tomma listor/strängar
  - Noll och negativa värden
  - Mycket stora värden
  - null/None-värden

• TESTA FELFALL:
  - Ogiltig input
  - Undantag kastas korrekt
  - Felmeddelanden är tydliga

• F.I.R.S.T PRINCIPER:
  - Fast: Snabba tester
  - Independent: Oberoende av varandra
  - Repeatable: Samma resultat varje gång
  - Self-validating: Tydlig pass/fail
  - Timely: Skriv tester tidigt (helst först - TDD)
"""

print(testing_discussion)


# =============================================================================
# EXEMPEL: PRAKTISK TESTNING MED unittest
# =============================================================================

print("\n" + "=" * 70)
print("PRAKTISKT EXEMPEL: Testning med unittest")
print("=" * 70)

import unittest

# Funktion att testa
def calculate_average(numbers):
    """Beräknar medelvärdet av en lista med tal"""
    if not numbers:
        raise ValueError("Listan kan inte vara tom")
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("Alla element måste vara tal")
    return sum(numbers) / len(numbers)


# Testklasser
class TestCalculateAverage(unittest.TestCase):
    """Enhetstester för calculate_average"""
    
    def test_basic_average(self):
        """Testa grundläggande medelvärdeskalkulation"""
        result = calculate_average([1, 2, 3, 4, 5])
        self.assertEqual(result, 3.0)
    
    def test_negative_numbers(self):
        """Testa med negativa tal"""
        result = calculate_average([-5, -10, -15])
        self.assertEqual(result, -10.0)
    
    def test_floats(self):
        """Testa med decimaltal"""
        result = calculate_average([1.5, 2.5, 3.5])
        self.assertAlmostEqual(result, 2.5)
    
    def test_single_number(self):
        """Testa med ett enda tal"""
        result = calculate_average([42])
        self.assertEqual(result, 42.0)
    
    def test_empty_list_raises_error(self):
        """Testa att tom lista kastar ValueError"""
        with self.assertRaises(ValueError):
            calculate_average([])
    
    def test_non_numeric_raises_error(self):
        """Testa att icke-numeriska värden kastar TypeError"""
        with self.assertRaises(TypeError):
            calculate_average([1, 2, "three"])


# Kör tester
print("\nKör enhetstester:")
print("-" * 70)

# Skapa en test suite
suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculateAverage)
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

print(f"\nTestresultat:")
print(f"  Körda tester: {result.testsRun}")
print(f"  Lyckade: {result.testsRun - len(result.failures) - len(result.errors)}")
print(f"  Misslyckade: {len(result.failures)}")
print(f"  Fel: {len(result.errors)}")


# =============================================================================
# SAMMANFATTNING
# =============================================================================

print("\n" + "=" * 70)
print("SAMMANFATTNING")
print("=" * 70)

summary = """
FEL OCH FELHANTERING:
• Syntaxfel upptäcks vid parsing
• Körningsfel upptäcks under exekvering
• Logiska fel upptäcks genom testning
• Använd try-except för att hantera förväntade fel
• Använd raise för att kasta egna undantag

UNDANTAG:
• Undantag = Pythons sätt att signalera fel
• Hantera med try-except-else-finally
• Olika undantagstyper för olika fel
• Kasta egna undantag med raise

TESTNING:
• Olika nivåer: Enhets-, Integrations-, System-, Acceptanstest
• Strategier: White-box (glasbox) vs Black-box (svartlåda)
• Skriv tester tidigt och kör ofta
• Testa både lyckade fall och felfall
• Automatisera med testramverk (unittest, pytest)

TIPS FÖR FELSÖKNING:
1. Läs felmeddelanden noggrant
2. Använd print-debugging eller debugger
3. Testa med enklare input
4. Förklara koden högt (gummianka)
5. Ta pauser och kom tillbaka med friska ögon
"""

print(summary)

print("\n" + "=" * 70)
print("SEMINARIUM 6 SLUTFÖRT!")
print("=" * 70)