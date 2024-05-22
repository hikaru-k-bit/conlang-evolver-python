from app.evolve.Word import Word, Evolve


def main():
    word = input("Enter a Latin word to evolve: ")
    ipa = input("Enter the International Phonetic Alphabet (IPA) representation of the word: ")
    declension = int(input("Enter the declension of the word (1, 2, 3, 4, or 5): "))
    word = Word(word, ipa, declension)
    evolve = Evolve(word)
    word = evolve.stress_shift()
    print(f"Evolved word: {word.ipa}")
    word = evolve.vowel_length_reduction()
    print(f"Evolved word: {word.ipa}")
    word = evolve.vowel_raising()
    print(f"Evolved word: {word.ipa}")
    word = evolve.vowel_lowering()
    print(f"Evolved word: {word.ipa}")


if __name__ == '__main__':
    # Name, version and author
    print("App: conlang-evolver-python")
    print("Version: 0.1")
    print("Author: hikarukbit")
    print("")
    main()
