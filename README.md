# AI-examination
En github med tillhörande filer och instruktioner samt analys av AI examinationen, i mitt fall en redditbot som analyserar bilder och försöker hitta fotbollar.

### Hur körs scriptet?
För att köra scriptet så ska filen evaluate.py öppnas och köras som en vanlig python fil. När scriptet sedan körs kan vad som sker följas i terminalen och sedan kan man se bilden som eventuellt innehåller en fotboll i mappen detected. I mappen vid namn "mapp" finns den bild som just nu analyseras. 

### Viktiga filer
##### Reddit-bot-kod / dataSetFootball
Innehåller de bilder som använts för att träna upp algoritmen som används för att finna fotbollar i bilderna som analyseras. Bilderna finns i både XML- och JPEG- format. 
##### AI-Reddit-bot-kod / detected
Denna mapp innehåller den bild som granskas och sedan visar sig innehålla en fotboll. När sedan väntetiden är slut efter att en kommentar har publicerats och en ny bild funnits med en fotboll så försvinner den gamla bilden och ersätts av den nya. 
##### AI-Reddit-bot-kod / evaluate
Denna fil är som tidigare nämnt den fil som ska köras när man vill köra hela scriptet. Den innehåller både delarna där bilden hämtas från reddit, där den granskas av algoritmen och där en eventuell kommentar publiceras. 
##### AI-Reddit-bot-kod / model.h5 & ##### AI-Reddit-bot-kod / model2.tflite
Detta är de algoritmer som har tränats för att granska bilderna. Just att den ena heter 2 är ingen skillnad, det är samma runda de har tränats. Den enda skillnaden är att de är två olika filformat på de två filerna. 
