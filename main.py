from record import record_until_enter, save_audio
from pinyin_parser import parse_pinyin_phrase
from feedback import give_feedback

SAMPLE_RATE = 16000

def practice_phrase(phrase):
    syllables = parse_pinyin_phrase(phrase)
    for syllable, tone_number in syllables:
        if tone_number == 5:
            print("")
            print("'" + syllable + "' doesn't have a tone mark, so I can't tell which tone to check it against.")
            print("Make sure every syllable has one of the four tone marks (like ni, hao, wo become nǐ, hǎo, wǒ) before trying again.")
            return []
    results = []
    for index in range(len(syllables)):
        syllable, tone_number = syllables[index]
        print("")
        print("Say:", syllable)
        recording = record_until_enter(SAMPLE_RATE)
        filename = str(index) + "_" + syllable + ".wav"
        save_audio(recording, SAMPLE_RATE, filename)
        score, message = give_feedback(filename, tone_number)
        print(round(score), "% -", message)
        results.append((syllable, tone_number, score, message))
    return results

def print_summary(results):
    print("")
    print("=== Summary ===")
    total_score = 0
    for syllable, tone_number, score, message in results:
        print(syllable, "(tone", str(tone_number) + "):", round(score), "% -", message)
        total_score = total_score + score
    average_score = total_score / len(results)
    print("")
    print("Average score:", round(average_score), "%")

def main():
    phrase = input("Type the pinyin phrase you want to practice: ")
    results = practice_phrase(phrase)
    if results:
        print_summary(results)

if __name__ == "__main__":
    main()