# Engeto: Textový analyzátor

>Program, který se prokousává libovolně dlouhým textem a zjišťuje o něm různé informace.

>Úvod začína popis hlavičkou, kde je název kurzu, email absolventa atd.

>Program začne tím, že si od uživatele vyžádá `input` přihrašovacích údaju.

>Přihlašovací údaje jsou napsané ve slovníku `(dictionary)`.

>Pokud uživatel zadá jméno nebo heslo které není ve slovníku uživatele upozorní a program skončí.

>Poté program uživatele vyzve aby zadal čislo 1 až 3 což představuje výběr části textu z proměnné `TEXTS` z externího Python modulu

>Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a opět skončí,
pokud zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.

>Následně program vytvoří histogram kde spočítá délku slov(bez teček a čárek), spočítá slova začínající velkýmI a malými písmeneny, hledá čiselné hodnoty a sečte dohromady.