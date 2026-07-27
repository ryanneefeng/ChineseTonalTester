TONE_MARKS = {
    "ā": 1, "ē": 1, "ī": 1, "ō": 1, "ū": 1, "ǖ": 1,
    "á": 2, "é": 2, "í": 2, "ó": 2, "ú": 2, "ǘ": 2,
    "ǎ": 3, "ě": 3, "ǐ": 3, "ǒ": 3, "ǔ": 3, "ǚ": 3,
    "à": 4, "è": 4, "ì": 4, "ò": 4, "ù": 4, "ǜ": 4,
}

def get_tone_number(syllable):
    for character in syllable:
        if character in TONE_MARKS:
            return TONE_MARKS[character]
    return 5

def parse_pinyin_phrase(phrase):
    cleaned = phrase.replace(",", "").replace(".", "")
    raw_syllables = cleaned.split()
    parsed = []
    for syllable in raw_syllables:
        tone_number = get_tone_number(syllable)
        parsed.append((syllable, tone_number))
    return parsed