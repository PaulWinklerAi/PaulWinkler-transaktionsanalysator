Detta projekt är en transaktionsanalysator, kan även användas som en reseplanerare om olika valutor är inblandade i din resa. Programmet är byggt med Python och syftet med programmet är att analysera olika utgifter som har olika valutor och ge användaren en översikt av utgifterna samt omvandla dessa till Svenska kronor. Programmet analyserar utgifterna från en CSV-fil. För att underlätta för användaren har programmet ett GUI byggt med Tkinter.

För att starta applikationen:
1. Installera nödvändiga beroenden: pip install -r requirements.txt  (Alla beroenden finns listade i requirements.txt)
2. Dokumentera dina utgifter i CSV-filen: Detta genom "Belopp,Valutakoden,Kategori" Exempel: "400,CAD,Transport"
3. Starta applikationen: Genom "Run" knappen i GUI filen eller genom "python gui.py" i terminalen.

Kursmoment och dokumentation:

API-Integrationer: Jag har valt att använda API-integrationer för att hämta aktuella valutakurser från ExchangeRate-API. Detta ger projektet dynamisk och aktuell data, vilket gör analysen mer relevant.

Avancerad datahantering: Med hjälp av biblioteket Pandas kan jag läsa in, manipulera och analysera stora mängder transaktionsdata effektivt. Detta gör applikationen kapabel att hantera komplexa datamängder.

Filhantering: Projektet inkluderar filhantering genom att läsa och uppdatera CSV-filer.

Motivering:
Jag valde dessa moment för att skapa ett praktiskt verktyg som inte bara analyserar data, utan också visar aktuella valutakonverteringar. Genom att använda API-integrationer lärde jag mig hämta och hantera extern data, vilket är en ovärdelig färdighet i dagen programmeringsvärld. Datahanteringen med Pandas gav mig en insikt i att arbeta med större datamängder, filtrera och analysera dem på ett strukturerad sätt. Filhanteringen säkerställde att jag förstår hur man läser och sparar data effektivt, vilket ofta behövs i verkliga projekt.
