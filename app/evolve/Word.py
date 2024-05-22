import re


class Validator:
    def __init__(self, word: str, ipa: str, declension: int) -> None:
        self.word = word
        self.ipa = ipa
        self.declension = declension

    def validate(self) -> None:
        self.is_declension_valid()
        self.is_word_valid()
        self.is_ipa_valid()

    def is_declension_valid(self) -> None:
        if self.declension not in {1, 2, 3, 4, 5}:
            raise ValueError("Declension must be one of the following values: 1, 2, 3, 4, 5")

    def is_word_valid(self) -> None:
        if not self.word:
            raise ValueError("Word cannot be empty")

    def is_ipa_valid(self) -> None:
        if not self.ipa:
            raise ValueError("IPA cannot be empty")
        self.has_stress_marking()
        self.has_syllable_separation()

    def has_stress_marking(self) -> None:
        primary_stress = 'ˈ'
        secondary_stress = 'ˌ'
        if primary_stress not in self.ipa and secondary_stress not in self.ipa and "'" not in self.ipa:
            raise ValueError("IPA must contain a stress mark to indicate the stressed syllable")

    def has_syllable_separation(self) -> None:
        # Check if the IPA contains stress mark or syllable separator
        primary_stress = 'ˈ'
        secondary_stress = 'ˌ'
        syllable_separator = '.'
        if primary_stress not in self.ipa and secondary_stress not in self.ipa and syllable_separator not in self.ipa:
            raise ValueError("IPA must contain a syllable separator to indicate syllable boundaries")


class Word:
    def __init__(self, word: str, ipa: str, declension: int) -> None:
        """
        Constructor for the Word class
        :param word: The word as a string
        :param ipa: The International Phonetic Alphabet (IPA) representation of the word
        :param declension: The declension of the word, must be one of [1, 2, 3, 4, 5]
        """
        self.word: str = word
        self.ipa: str = ipa.replace('/', '')
        self.declension: int = declension

        validator = Validator(word, ipa, declension)
        validator.validate()
        print(self.ipa)
