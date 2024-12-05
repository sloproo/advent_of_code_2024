# Sivut sotkussa

Tämän päivän tehtävä oli kiva, niin kuin ekan osan tehtävänannosta aamulla saattoi päätellä. Nyt ollaan vuoden 17 talon (?) kellarissa ja etsijätontut taas etsivät ja paikalla ollut tonttu kertoo, että kelkan laukaisun turvallisuusohjeista on tullut uusi painos mutta printteri temppuilee ja asia olisi tärkeä saada reeraan. Vaikea edes selittää mikä järki tehtävässä on tarinan kannalta, enkä aio yrittää, mutta tehtävä:

Datassa oli kaksi osaa: Ensimmäisessä oli joukko numeropareja, joissa kerrotaan missä järjestyksessä sen (sivu)numeroiden täytyy olla tulostetuissa ohjeissa. Tämä on vähän pulman ratkaisijan sekoittamista, koska järjestys ei noudata numeroiden perus järjestystä ja esim 22 | 15 tarkoittaa, että oikein printatussa manuaalissa sivun 22 täytyy olla ennen sivua 15.

Tokassa osassa on sitten printattuja manuaaleja. Joissain sivujen järjestys on sellainen, että se noudattaa annettuja sääntöjä, toisissa ei.

Sääntöjä oli 1176, manuaaleja 175.

Ekassa osassa tehtävänä oli vain tsekata, minkä manuaalien sivut ovat jo valmiiksi oikeassa järjestyksessä (ja vastaukseksi laskea virheettömien manuaalien keskimmäisten sivujen numerot yhteen). 

Tämä oli helppoa: Ottaa vaan säännöt omaksi listakseen ja manuaalit toiseksi listakseen. Sitten käy manuaaleja läpi yksi kerrallaan ja joka manuaalista käy säännöt läpi yksi kerrallaan. Kerrankin jos narahtaa ni pieleen meni, ja jos kaikki säännöt menevät läpi ni sitten manuaali kirjataan kelvolliseksi.

Toisen osan tehtävän arvasi jo ennalta, mutta ei haittaa. Siinä piti siis korjata virheelliset manuaalit kelvollisiksi. En ole varmaan koskaan tehnytkään järjestämisalgoritmia ja tyylejä siihen on varmasti monia, mutta toteutin sen ekalla tavalla joka mieleen tuli: Otetaan aiempaan tapaan listat manuaaleista ja säännöistä, käydään läpi kelvolliset ja otetaan talteen virheelliset. Sit jokaisesta virheellisestä käydään läpi joka sääntö: Jos säännön molemmat sivunumerot ovat manuaalissa ja jos ne eivät ole keskenään oikeassa järjestyksessä, niin vaihdetaan niiden paikkoja keskenään. Kun kaikki säännöt on käyty läpi, katsotaan kelpaako ja jos ei niin tehdään sama uudestaan ja ennen pitkää kelpaa.

Aivan varmasti elegantimpia tapoja toteuttaa tuo olisi ollut, mutta sou not. Tällaiset perusjutut menevät tässä kohtaa jo vanhalla rutiinilla, ihan pikkuisen piti ajatella ja molemmat ratkesivat ongelmitta 🙂
