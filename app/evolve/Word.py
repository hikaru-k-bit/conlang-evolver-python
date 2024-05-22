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
        if '.' not in self.ipa:
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


class Evolve:
    def __init__(self, word: Word) -> None:
        self.word = word

    def stress_shift(self) -> Word:
        ipa = self.word.ipa
        syllables = re.split(r'[ˈˌ\'.]', ipa)
        syllables = [s for s in syllables if s]  # Remove empty strings

        if len(syllables) == 3:
            # Add primary stress to the initial syllable
            new_ipa = f'ˈ{syllables[0]}.{syllables[1]}.{syllables[2]}'
            self.word.ipa = new_ipa
        return self.word

    def vowel_length_reduction(self) -> Word:
        ipa = self.word.ipa

        # Function to check if a vowel is stressed
        def is_stressed(s):
            return 'ˈ' in s or 'ˌ' in s or "'" in s

        # Function to reduce vowel length
        def reduce_vowel_length(s):
            return s.replace(':', '').replace('ː', '')

        syllables = ipa.split('.')
        print(syllables)

        # Process each syllable
        new_syllables = []
        for syllable in syllables:
            if not is_stressed(syllable):
                syllable = reduce_vowel_length(syllable)
            new_syllables.append(syllable)

        # Join the syllables back together
        new_ipa = '.'.join(new_syllables)
        self.word.ipa = new_ipa
        return self.word

    def vowel_raising(self) -> Word:
        ipa = self.word.ipa

        # Replace /a/ followed by a nasal consonant
        ipa = re.sub(r'a([mn])', r'ε\1', ipa)
        ipa = re.sub(r'a\.([mn])', r'ε.\1', ipa)

        self.word.ipa = ipa
        return self.word

    def vowel_lowering(self) -> Word:
        ipa = self.word.ipa

        # Replace /e/ followed by /r/
        ipa = re.sub(r'e(r)', r'a\1', ipa)
        ipa = re.sub(r'e\.r', r'a.r', ipa)

        self.word.ipa = ipa
        return self.word
