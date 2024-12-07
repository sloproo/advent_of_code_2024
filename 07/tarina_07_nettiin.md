# Riippusillan korjaus

Tämän päivän tarina ja tehtävä olivat hauskoja. Palattiin vuoden 2022 tarinaan, hajonneeseen riippusiltaan ja matemaattisesti hämmästyttävän taitaviin elefantteihin.

Datana oli joukko numerorivejä, joista eka oli vastaus johon pyritään ja loput numeroita, joita laskemalla siihen pitäisi päästä. Ekassa osiossa on käytössä yhteen- ja kertolaskut, ja jos laskettavilla numeroilla ja jollain laskutoimitusten yhdistelmällä pääsee vastaukseen ni hyvä. Ratkesi aika nätisti.

Tokassa tehtävässä ei annettukaan lisäoperaattoreiksi vähennystä ja jakamista vaan yhdistäminen ||, jolla siis vaikka 44 || 123 = 44123. Tämän toteutus oli helppo, mutta kun mahdollisia laskutoimitusten yhdistelmiä olikin nyt kolmella operaattorilla ei 2^n vaan 3^n, niin vastausta joutui odottamaan. Pikku karsintaoptimointi siitä, että koska ynnäämällä, kertomalla ja yhdistämällä kaikilla numerot vain kasvavat, laskutoimitusten yhdistelmän käsittelyn voi keskeyttää siinä vaiheessa, jos ollaan jo menty yli vastauksesta.

Koodi ruksutti tuolla siistimisellä minuutissa ja homma paketissa ✌
