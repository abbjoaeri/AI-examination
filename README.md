# AI-examination
En github med tillhörande filer och instruktioner samt analys av AI examinationen, i mitt fall en redditbot som analyserar bilder och försöker hitta fotbollar. Fortsätt läsa för att få veta mer. @footballrecognizer på reddit!

![Exempel kommentar](https://github.com/abbjoaeri/AI-examination/blob/master/images/redditbot3.PNG)

### Hur körs scriptet?
För att köra scriptet så ska först och främst mappen 'Reddit-bot-kod' öppnas i din kodläsare. Ladda sedan ned de bibliotek som står importerade högst upp i koden 'evaluate.py' med hjälpa av pip. Se även till att du har python 3.7 nedladdat på datorn. Sedan ska filen 'evaluate.py' köras som en vanlig python fil. När scriptet sedan körs kan vad som sker följas i terminalen och så småningom kan man eventuellt se en bild som innehåller en fotboll och vart någonstans den befinner sig i bilden. I mappen vid namn "mapp" finns den bild som just nu analyseras, oavsett om den innehåller en fotboll eller inte.

När scriptet körs så börjar programmet att kolla vilken eller vilka subreddits som valts. I mitt fall har jag valt subredditen "soccerbanners", mest på grund av att jag ville ha en subreddit relaterad till fotboll som till största delen består av bilder. När sedan en subreddit har valts så börjar scriptet att hämta den första posten från subredditen. Det första som då sker är att scriptet kollar om "jpg" finns i posten. Finns det ingen "jpg" så finns det ingen bild i posten och då avslutas denna post här och en ny post väljs ut ur samma subreddit. Om det finns "jpg", alltså bokstäverna och filformatet "jpg" i posten, så innebär det att det finns en bild i posten och processen går vidare. Då laddas denna bild ned till datorn och sparas i mappen 'mapp', som förövrigt finns med hör i githuben. I samma veva så omvandlas bilden till 'jpeg'-format för att bildigenkänningsalgoritmerna ska kunna tillämpas. Där efter börjar analysen på bilden för att försöka finna en fotboll i den. En ganska stor del av koden innehåller denna del av processen. 

När en bild sedan har analyserats färdigt så finns två olika saker som kan ske. Antingen så anser programmet att det inte finns en fotboll i bilden som anlyseras, och går isåfall bara vidare till nästa bild. Det andra alternativet är att programmet tycker att det finns en fotboll i bilden. Isåfall kommer boten att kommentera det inlägg som bilden på fotbollen finns i på reddit, kommentaren kommer säga att det finns en boll samt sannolikheten för att bollen finna. I mitt fall har jag suttit en gräns på minst 70% för att en kommentar ska skrivas. Efter att en kommentar har skrivits så har jag suttit en time.sleep()-funktion som varar i 10 minuter. Detta för att kringgå spamskyddet som finns på reddit. När sedan dessa 10 minuter passerat så raderas den gamla bilden från datorn processen börjar om med en ny post i samma subreddit. 

Om du som läser detta är intresserad av att testa och se vilka bilder som boten har kommenterat på reddit så är det bara att använda botens inloggningsuppgifter för att logga in. Dessa finns här: username='footballrecognizer', password='qwerty12345'. Om du även vill testa köra scriptet så är det bara att ladda ner det härifrån githuben. Det finns några saker att tänka på. Bland annat så styr variabeln 'subreddit' vilken subreddit som bilderna ska hämtas från. Det är en fördel att på detta ställe välja en subreddit som är fotbollsrelaterad, men om du vill så kan du testa 'all'. Då kommer boten däremot att få leta länge innan den finner en fotboll. 

### Viktiga filer
##### Reddit-bot-kod / dataSetFotbollar
Innehåller de bilder som använts för att träna upp algoritmen som används för att finna fotbollar i bilderna som analyseras. Bilderna finns i både XML- och JPEG- format. 
##### Reddit-bot-kod / detected
Denna mapp innehåller den bild som granskas och sedan visar sig innehålla en fotboll. När sedan väntetiden är slut efter att en kommentar har publicerats och en ny bild funnits med en fotboll så försvinner den gamla bilden och ersätts av den nya. 
##### Reddit-bot-kod / evaluate
Denna fil är som tidigare nämnt den fil som ska köras när man vill köra hela scriptet. Den innehåller både delarna där bilden hämtas från reddit, där den granskas av algoritmen och där en eventuell kommentar publiceras. 
##### Reddit-bot-kod / model.h5 & AI-Reddit-bot-kod / model2.tflite
Detta är de algoritmer som har tränats för att granska bilderna. Just att den ena heter 2 är ingen skillnad, det är samma runda de har tränats. Den enda skillnaden är att de är två olika filformat på de två filerna. 
##### Övriga filer
Desutom följer en hel del andra filer med för dig som vill kolla in dessa och hur de använts i träningen av AI-modellen (model.h5 & model2.tflite). Denna guide har använts för att träna modellen, delar av denna kod och vissa filer finns alltså med här i githuben där de eventuellt kan ha redigerats något: https://colab.research.google.com/drive/1nziez-jthZ4YuOl1GERwCygI0ozkDJsh.

### Exempel på hur det kan se ut
Här nedan ett exempel på hur det kan se ut när botten kommenterar att det finns en fotboll i bilden och dessutom med vilken sannolikhet.

![Här är ett exempel på hur det kan se ut när botten kommenterar att det finns en fotboll i bilden och dessutom med vilken sannolikhet.](https://github.com/abbjoaeri/AI-examination/blob/master/images/redditbot1.PNG)

Samtidigt får användaren detta meddelande i sin terminal: 

![terminal](https://github.com/abbjoaeri/AI-examination/blob/master/images/redditbot4.PNG)


### Problem och annat jag stött på
Det mest tidskrävande i projektet, även om det kanske inte var ett problem i mitt fall var att skapa ett datset att använda till träningen av AI-modellen. Den delen gick ut på att ladda ned hundratals bilder från google och i samband med det på varje enstaka bild markera ut vart någonstans själva fotbollen befann sig. Otroligt tidskrävande men värt att göra för att nå ett så bra resultat som möjligt. 

Ett annat problem, som egentligen inte var ett problem var att jag letade efter ett sätt att nå inlägget där bilden fanns när jag hade bilden. Efter en stunds felsökning testade jag med lite olika bibliotek men till slut kom jag på att jag har en variabel för inlägget innan det att jag kollar om inlägget har en bild i sig. Då kunde jag använda den istället. 

Något som var väldigt tidskrävande var att omvandla koden så att den kunde köras i Visiual studio code och så att den var kompatibel med den bild som hämtas från reddit. Det var det som tog den huvudsakliga tiden under projektets gång och mycket felsökning krävdes för att åstadkomma det resultat som finns idag. 

### Vad kan utvecklas på projektet?
Det som först och främst kan och bör utvecklas är datasetet som använts vid träningen av AI-modellen som används för att känna igen fotbollar. I nuläget innehåller datasetet några hundra bilder på fotbollar som främst befinner sig ensamma i fotot på en allt som oftast vit bakgrund. Det skapar problem när modellen ska tillämpas på verklighetsförankrade situationer. I detta fall är det sällan någon som lägger ut en bild på reddit på enbart en fotboll. Det gör det i vissa fall svårt för boten att hitta en fotboll. Det första jag ska göra när jag kommer tillbaks till skolan är att försöka lösa detta problem. Google Chrome har förändrat sina verktyg för programmerare så därför kan inte den guide som användes vid skapandet av datasetet användas idag. Men om ytterliggare några hundra bilder föreställande fotbollar i exempelvis en match läggs till i datasetet så kommer detta problem vara löst och boten kommer då att fungera optimalt. Jag ber om ursäkt för detta problem men direkt när vi är tillbaka i skolan ska jag försöka få hjälp med detta för jag har försökt och försökt men inte fått ordning på det hemifrån. Ha gärna överseende med detta!

På längre sikt skulle boten kunna utvecklas till att exempelvis följa en hel match och hela tiden markera ut bollen på skärmen. Detta skulle sedan till exempelvis kunna användas för att räkna ut statistik som exempelvis bollinnehav och vart på planen respektive lag har bollen. En liknande teknik finns faktiskt redan idag, denna kallas veo: https://www.veo.co/. Kolla gärna in länken. Detta företag tillverkar kameror som filmar matcherna automatiskt utan att någon styr kameran, alltså följer kameran bollen av sig själv. Min förening äger en sådan och för bara några veckor sedan filmades min match med en sån kamera. Ett potentiellt drömjobb att arbeta där då mitt huvudintresse skulle kunna kombineras med kunskaperna från detta projekt.  

### Frågor?
Har du några frågor eller har någon feedback? Hör gärna av dig via teams eller mail (joakim.eriksson@abbindustrigymnasium.se) isåfall!

