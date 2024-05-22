import colorama

from app.evolve.Word import Word
from app.evolve.Evolve import Evolve
from app.logger.Logger import Logger


def main():
    word = input("Enter a Latin word to evolve: ")
    ipa = input("Enter the International Phonetic Alphabet (IPA) representation of the word: ")
    declension = int(input("Enter the declension of the word (1, 2, 3, 4, or 5): "))
    word = Word(word, ipa, declension)
    evolve = Evolve(word)
    Logger.info("Initiating the evolution...")
    word = evolve.evolve()
    print(f"Evolved word: {word.ipa}")


if __name__ == '__main__':
    colorama.init()
    # Name, version and author
    print("App: conlang-evolver-python")
    print("Version: 0.1")
    print("Author: hikarukbit")
    print("")
    main()
