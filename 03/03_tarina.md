# Kätketyt kertolaskut

Tänään ollaan sit pulkkavuokraamossa, josta sieltäkään ei löydy historioitsijatonttua. Mutta rikkinäinen tietokone löytyy, ja se antaa merkkisekasotkua jossa on seassa mul(123,456) -muotoisia kertolaskuja. Tehtävänä oli ekassa vaiheessa vaan etsiä kaikki tuollaiset, kertoa lukuparin numerot keskenään ja vastaus oli kaikkien tulojen summa.

Tässä käytetään sellaista välinettä haussa kuin regexp eli regular expressions eli säännölliset lausekkeet. Se on ihan hieno systeemi sille, miten voi hakea täsmälleen halutunlaisia merkkijonoja, mutta en osaa sen syntaksia kovin hyvin. Ykkösosa oli onneksi simppeli, halutut kohdat löytyvät hakulausekkeella "mul\(\d{1,3}\,\d{1,3}\)"

Tuossa kauttaviivalla väistetään sulut ja pilkut jotka olisivat muuten regexpin syntaksia, \d{1,3} tarkoittaa 1-3 mittaista numeromerkkien sarjaa.

Kakkososassa piti huomioida, että siellä tekstin seassa on myös do() ja don't() -rimpsuja. don't() tarkoittaa sitä, että sen jälkeen tulevia kertolaskuja ei huomioida ennen kuin vastaan tulee taas do(). Regexpillä haetaan lauseketta "(?s)don't\(\).*?do\(\)" ja korvataan se tyhjällä, jolloin kaikki don't():it, sitä seuraavat merkit ja niitä seuraava do() poistuvat. Koska en ole koskaan opetellut tätä kunnolla, oli ensinnäkin hankaluuksia sen suhteen, että don't():in ja do():n välissä oleva . * (piste = jokerimerkki, * se että niitä voi olla peräkkäin kuinka monta vaan) vaatii vielä peräänsä kysymysmerkin, jolloin se on "ei-ahne" "ahneen" sijaan ja lopettaa ensimmäiseen, ei viimeiseen löytämäänsä do():hon. Lisäksi ihan alussa pitää olla (?s), jotta sen haun jokerimerkki menee läpi myös rivinvaihdosta eikä pysähdy siihen.

Jos kuulostaa tekniseltä ja sellaiselta, että se vaan pitää tietää eikä sitä voi intuitiolla päätellä, niin oma kokemukseni oli samanlainen. Viime vuoden kalenteri hyytyi regexp-tehtävään, toivottavasti nämä ovat tämän vuoden osalta tässä.
