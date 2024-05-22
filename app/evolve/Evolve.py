import re
from app.evolve.Word import Word
from app.logger.Logger import Logger


class Evolve:
    def __init__(self, word: Word) -> None:
        self.word = word

    def evolve(self) -> Word:
        Logger.info("OK!")
        Logger.info("Initiating stress shift...")
        self.stress_shift()
        Logger.info("Initiating vowel length reduction...")
        self.vowel_length_reduction()
        Logger.info("Initiating vowel raising...")
        self.vowel_raising()
        Logger.info("Initiating vowel lowering...")
        self.vowel_lowering()
        Logger.info("Initiating monophthongization...")
        self.monophthongization()
        Logger.info("Initiating lenition...")
        self.lenition()
        Logger.info("Initiating palatalisation...")
        self.palatalisation()
        Logger.info("Initiating fricativisation...")
        self.fricativisation()
        Logger.info("Initiating nasal assimilation...")
        self.nasal_assimilation()
        return self.word

    def stress_shift(self) -> Word:
        Logger.info("OK!")
        ipa = self.word.ipa
        syllables = re.split(r'[ˈˌ\'.]', ipa)
        syllables = [s for s in syllables if s]  # Remove empty strings

        if len(syllables) == 3:
            # Add primary stress to the initial syllable
            new_ipa = f'ˈ{syllables[0]}.{syllables[1]}.{syllables[2]}'
            self.word.ipa = new_ipa
            Logger.info("Stress shift complete.")
            Logger.changes_made(f"Before: {ipa} → {new_ipa}")
        else:
            Logger.warning("Stress shift not applicable as the word does not have 3 syllables.")
            Logger.warning("Skipping stress shift...")
        return self.word

    def vowel_length_reduction(self) -> Word:
        Logger.info("OK!")
        ipa = self.word.ipa

        # Function to check if a vowel is stressed
        def is_stressed(s):
            return 'ˈ' in s or 'ˌ' in s or "'" in s

        # Function to reduce vowel length
        def reduce_vowel_length(s):
            return s.replace(':', '').replace('ː', '')

        syllables = ipa.split('.')

        # Process each syllable
        new_syllables = []
        for syllable in syllables:
            if not is_stressed(syllable):
                syllable = reduce_vowel_length(syllable)
            new_syllables.append(syllable)

        # Join the syllables back together
        new_ipa = '.'.join(new_syllables)

        # Compare if they are any differences
        if new_ipa != ipa:
            Logger.info("Vowel length reduction complete.")
            Logger.changes_made(f"Before: {ipa} → {new_ipa}")
        else:
            Logger.warning("Vowel length reduction not applicable as there are no unstressed vowels "
                           "or there are no long vowels to reduce.")
            Logger.warning("Skipping vowel length reduction...")
        self.word.ipa = new_ipa
        return self.word

    def vowel_raising(self) -> Word:
        ipa = self.word.ipa

        # Replace /a/ followed by a nasal consonant
        ipa = re.sub(r'a([mn])', r'ε\1', ipa)
        ipa = re.sub(r'a\.([mn])', r'ε.\1', ipa)

        if ipa != self.word.ipa:
            Logger.info("Vowel raising complete.")
            Logger.changes_made(f"Before: {self.word.ipa} → {ipa}")
        else:
            Logger.warning("Vowel raising not applicable as there are no /a/ followed by a nasal consonant.")
            Logger.warning("Skipping vowel raising...")

        self.word.ipa = ipa
        return self.word

    def vowel_lowering(self) -> Word:
        Logger.info("OK!")
        ipa = self.word.ipa

        # Replace /e/ followed by /r/
        ipa = re.sub(r'e(r)', r'a\1', ipa)
        ipa = re.sub(r'e\.r', r'a.r', ipa)

        if ipa != self.word.ipa:
            Logger.info("Vowel lowering complete.")
            Logger.changes_made(f"/{self.word.ipa}/ → /{ipa}/")
        else:
            Logger.warning("Vowel lowering not applicable as there are no /e/ followed by /r/.")
            Logger.warning("Skipping vowel lowering...")

        self.word.ipa = ipa
        return self.word

    def monophthongization(self) -> Word:
        Logger.info("OK!")
        ipa = self.word.ipa

        # Ensure syllable separation
        syllables = ipa.split('.')

        # Process each syllable for monophthongization
        new_syllables = []
        for syllable in syllables:
            syllable = syllable.replace('ae', 'ε:')
            syllable = syllable.replace('oe', 'e:')
            new_syllables.append(syllable)

        # Join the syllables back together
        new_ipa = '.'.join(new_syllables)

        if new_ipa != ipa:
            Logger.info("Monophthongization complete.")
            Logger.changes_made(f"Before: {ipa} → {new_ipa}")
        else:
            Logger.warning("Monophthongization not applicable as there are no diphthongs to monophthongize.")
            Logger.warning("Skipping monophthongization...")

        self.word.ipa = new_ipa
        return self.word

    def lenition(self) -> Word:
        ipa = self.word.ipa

        # Replace /p/ with /b/ if between vowels: /p/ -> /b/ if /VpV/ -> /VbV/
        ipa = re.sub(r'([aeεiou])p([aeεiou])', r'\1b\2', ipa)

        # Replace /t/ with /d/ if between vowels: /t/ -> /d/ if /VtV/ -> /VdV/
        ipa = re.sub(r'([aeεiou])t([aeεiou])', r'\1d\2', ipa)
        ipa = re.sub(r'([aeεiou])\.t([aeεiou])', r'\1.d\2', ipa)

        # Replace /k/ with /g/ if between vowels: /k/ -> /g/ if /VkV/ -> /VgV/
        ipa = re.sub(r'([aeεiou])k([aeεiou])', r'\1g\2', ipa)
        ipa = re.sub(r'([aeεiou])\.k([aeεiou])', r'\1.g\2', ipa)

        if ipa != self.word.ipa:
            Logger.info("Lenition complete.")
            Logger.changes_made(f"Before: {self.word.ipa} → {ipa}")
        else:
            Logger.warning("Lenition not applicable as there are no /p/, /t/ or /k/ between vowels.")
            Logger.warning(
                "Please note that lenition is not applicable to /p/ if the following vowel is not in the same syllable.")
            Logger.warning("Skipping lenition...")

        self.word.ipa = ipa

        return self.word

    def palatalisation(self) -> Word:
        ipa = self.word.ipa

        # Split the IPA string into syllables
        syllables = ipa.split('.')

        # Process each syllable for palatalisation
        new_syllables = []
        for syllable in syllables:
            syllable = re.sub(r'k([ieε])', r'tʃ\1', syllable)
            syllable = re.sub(r'g([ieε])', r'dʒ\1', syllable)
            new_syllables.append(syllable)

        # Join the syllables back together
        new_ipa = '.'.join(new_syllables)

        if new_ipa != ipa:
            Logger.info("Palatalisation complete.")
            Logger.changes_made(f"Before: {ipa} → {new_ipa}")
        else:
            Logger.warning("Palatalisation not applicable as there are no /k/ or /g/ followed by /i/, /e/, or /ε/.")
            Logger.warning("Skipping palatalisation...")

        self.word.ipa = new_ipa
        return self.word

    def fricativisation(self) -> Word:
        ipa = self.word.ipa

        # Replace /b/ with /β/ between vowels: /b/ -> /β/ if /VbV/ -> /VβV/
        ipa = re.sub(r'([aeεiou])b([aeεiou])', r'\1β\2', ipa)
        ipa = re.sub(r'([aeεiou])\.b([aeεiou])', r'\1.β\2', ipa)

        # Replace /d/ with /ð/ between vowels: /d/ -> /ð/ if /VdV/ -> /VðV/
        ipa = re.sub(r'([aeεiou])d([aeεiou])', r'\1ð\2', ipa)
        ipa = re.sub(r'([aeεiou])\.d([aeεiou])', r'\1.ð\2', ipa)

        # Replace /g/ with /ɣ/ between vowels: /g/ -> /ɣ/ if /VgV/ -> /VɣV/
        ipa = re.sub(r'([aeεiou])g([aeεiou])', r'\1ɣ\2', ipa)
        ipa = re.sub(r'([aeεiou])\.g([aeεiou])', r'\1.ɣ\2', ipa)

        if ipa != self.word.ipa:
            Logger.info("Fricativisation complete.")
            Logger.changes_made(f"Before: {self.word.ipa} → {ipa}")
        else:
            Logger.warning("Fricativisation not applicable as there are no /b/, /d/ or /g/ between vowels.")
            Logger.warning("Skipping fricativisation...")

        self.word.ipa = ipa

        return self.word

    def nasal_assimilation(self) -> Word:
        ipa = self.word.ipa

        # Replace /n/ with /ŋ/ before /k/ or /g/
        ipa = re.sub(r'n([kg])', r'ŋ\1', ipa)
        ipa = re.sub(r'n\.([kg])', r'ŋ.\1', ipa)

        # Replace /n/ with /m/ before /p/ or /b/
        ipa = re.sub(r'n([pb])', r'm\1', ipa)

        if ipa != self.word.ipa:
            Logger.info("Nasal assimilation complete.")
            Logger.changes_made(f"Before: {self.word.ipa} → {ipa}")
        else:
            Logger.warning("Nasal assimilation not applicable as there are no /n/ followed by /k/, /g/, /p/, or /b/.")
            Logger.warning("Skipping nasal assimilation...")
        self.word.ipa = ipa

        return self.word
