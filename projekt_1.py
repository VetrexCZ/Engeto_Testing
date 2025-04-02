"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Daniel Skřivánek
email: ddaniel.skrivanek@seznam.cz
discord: vetrex89cz #3080
"""

from task_template import TEXTS

# Seznam registrovaných uživatelů

registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}


# Funkce pro ověření přihlašovacích údajů

def prihlaseni():
    uzivatelske_jmeno = input("username: ")
    heslo = input("password: ")

    if uzivatelske_jmeno in registrovani_uzivatele and \
            registrovani_uzivatele[uzivatelske_jmeno] == heslo:
        print("-" * 40)
        print(f"Welcome to the app, {uzivatelske_jmeno}")
        return True
    else:
        print("Unregistered user, terminating the program..")
        return False


# Funkce pro analýzu textu "list comprehension"

def analyza_textu(text):
    words = text.split()
    word_lengths = [len(word.strip(".,")) for word in words]

    titlecase_words = [word for word in words if word.istitle()]
    uppercase_words = [word for word in words if word.isupper()]
    lowercase_words = [word for word in words if word.islower()]

    numeric_strings = [word for word in words if word.isdigit()]
    numeric_sum = sum(int(word) for word in numeric_strings)

    word_length_occurrences = {
        length: word_lengths.count(length) for length in set(word_lengths)
    }

    print(f"There are {len(words)} words in the selected text.")
    print(f"There are {len(titlecase_words)} titlecase words.")
    print(f"There are {len(uppercase_words)} uppercase words.")
    print(f"There are {len(lowercase_words)} lowercase words.")
    print(f"There are {len(numeric_strings)} numeric words.")
    print(f"The sum of all the numbers {numeric_sum}")

    print("-" * 40)
    print("LEN | OCCURENCES | NR.")
    print("-" * 40)
    for length, occurrences in sorted(word_length_occurrences.items()):
        print(f"{length:2d} | {'*' * occurrences} {occurrences}")


# Hlavní funkce programu
def hlavni():
    if prihlaseni():
        print("We have 3 texts to be analyzed.")
        print("-" * 40)
        try:
            vyber = int(input("Enter a number btw. 1 and 3 to select: "))
            print("-" * 40)
            if 1 <= vyber <= 3:
                analyza_textu(TEXTS[vyber - 1])
            else:
                print("Invalid selection, terminating the program..")
        except ValueError:
            print("Invalid input, terminating the program..")


if __name__ == "__main__":
    hlavni()
