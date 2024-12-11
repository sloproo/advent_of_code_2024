# Kivijono

Nyt näissä tehtävissä saa jo vähän miettiäkin, ja se on ihanaa! Tämän päivän tehtävässä ollaan Plutossa ja katsellaan kivijonoa. Jokaisessa kivessä on numero ja aina kun räpäyttää silmiä, kivet muuttuvat seuraavien sääntöjen mukaan:
- Jos kivessä on numero 0, se muuttuu 1:ksi.
- Jos kiven numerossa on parillinen määrä numeroita, se jakautuu kahdeksi, esim 123789 -> 123 ja 789
- Jos kumpikaan aiemmista säännöistä ei päde, niin kiven numero kasvaa 2024-kertaiseksi, esim 7 -> 14168

Tehtävän ekassa osassa piti selvittää, paljonko kiviä on kun silmiä on räpäytetty 25 kertaa. Tämä oli vielä ihan helppoa, käy joka kiven läpi, tekee uuden jonon ja käy sen taas läpi. Alun viidestä kivestä ehti siinä tulla 199946 kiveä. 

Tokassa osassa piti selvittää paljonko kiviä on 75 silmänräpäyksen jälkeen ja sen tiesi, että ekan osan koodi ei enää riitä: Kivien lukumäärä kasvaa kai jotakuinkin eksponentiaalisesti ja sitten kun aletaan käydä miljardeja ja biljoonia ym. kohtia käyviä listoja läpi, ni touhu on aika hidasta.

Eka ajatus oli, että koska jotain luuppaavuutta tuossa kuitenkin tapahtuu (jokaisesta nollasta tulee ykkönen, siitä 2024, siitä 20 ja 24, niistä 2, 0, 2 ja 4 jne.), niin voisi vaan laskea jotenkin kai Droste-efektiä soveltaen niin, että jokaisesta nollasta muodostuu oma "taskunsa" ja sen sisällä sitten kasvu on aina ennakoitavaa. En päässyt toteutamaan sitä kuitenkaan loppuun asti, koska jo testaillessa huomasi, että sekin alkaa hidastua liian aikaisin. Siinä missä eka alkoi pykiä jossain 30 kierroksen kohdalla, toka jaksoi ripeästi jonnekin vähän 40:n päälle.

Mut jotenkin mielessä kummitteli vuoden 2021 tehtävä, jossa syvänmerenkalat syntyivät, kypsyivät ja alkoivat lisääntyä. Siinäkään ei kone kestänyt, jos joka kalaa olisi laskenut erikseen, mutta pitämällä kirjaa siitä, kuinka paljon minkäkinikäisiä kaloja oli, numerot pysyivät kontrollissa. Sama tässäkin: Unohtaa kivien järjestyksen ja päivittää aina silmänräpäysten välillä vain sen, että kuinka monta kappaletta minkäkinnumeroista kiveä jonossa on ja kuinka monta minkäkinnumeroista kiveä siitä tulee seuraavaksi. Jonon järjestyksestä ei ole siinä enää mitään tietoa, mutta ei ole väliäkään.

Ratkaisukoodi oli nopea ja meni läpi ygösellä. Höllii!

