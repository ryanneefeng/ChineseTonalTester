# Chinese Tonal Tester

A small project I'm building to help myself and perhaps others(?) practice their Mandarin tones.
I'm a heritage Chinese speaker, meaning I grew up around the language but never really became fluent. I'm starting Chinese classes at Cornell soon, and I've always struggled with tonal pronunciation, so I'm creating something to aid in my studies, hopefully.
Apps like Duolingo will usually tell you if your pronunciation is right or wrong, but they don't really show *why*. I thought it'd be cool to make something that lets me actually **see** my pitch while I'm speaking and compare it to what the tone is supposed to look like.

The idea I am thinking of will work similarly to this:

```
English:
Hello, my name is Ryan.

↓

Mandarin:
你好，我叫瑞安
nǐ hǎo, wǒ jiào ruì ān

↓

Speak into your microphone...

↓

Your pitch graph 📈
Expected tone graph 📉

nǐ ✅
hǎo ✅
wǒ ✅
jiào ❌ (too flat)
ruì ❌ (too flat)
ān ✅
```
## Goals

Right now the plan is to be able to:

- [x] Record audio from my microphone
- [x] Plot my pitch over time
- [x] Recognize basic Mandarin tones (DTW alignment against each of the 4 reference tones, plus a magnitude check for near-flat recordings and a timing check for tone 2/3 confusion — 4/4 on my own test recordings)
- [x] Compare my pitch to the expected tone
- [x] Give simple feedback (score % + short message, reusing the same signals from tone detection)
- [ ] Eventually support full sentences (pinyin parsing works standalone, not wired into a real multi-syllable loop yet)

## Known issues

- Only tested on a handful of recordings per tone, one speaker. Real robustness is unproven.
- The four reference shapes are idealized curves from the Chao tone-number system (55/35/214/51), not drawn from real speech.
- No main.py yet so each script below is run individually.

## Example usage

There's no single entry point yet — `main.py` is still the last unchecked item above. Until then, each script runs on its own.

**The core loop — record, then get feedback:**

    python record.py ma3.wav

Press Enter to start, say the syllable, press Enter to stop. Saves and plays it back.

    python feedback.py ma3.wav 3

Second argument is the tone you *meant* to say (1-4). Prints a score and a short message, e.g. `85 % - Good dip and rise.`

**Everything else is a diagnostic tool** — useful for understanding *why* a score came out how it did, not something you need every rep:

    python analyze_pitch.py ma3.wav

Raw pitch-over-time chart, plus the semitone range (how much your pitch actually moved).

    python compare_tones.py ma3.wav 3

Plots your recording against one specific reference tone shape, overlaid.

    python dtw_compare.py ma3.wav

Compares against all four reference tones at once and prints a cost for each — doesn't need you to say which tone you meant, useful for checking if a recording is genuinely ambiguous between two tones.

## Project structure

Run directly: `record.py`, `analyze_pitch.py`, `compare_tones.py`, `dtw_compare.py`, `feedback.py`
Imported only, not run on their own: `reference_tones.py`, `dtw.py`, `pinyin_parser.py`

## Why I'm making this

Mostly because I think it'd be useful for me.
I've also never built anything involving audio processing before, so this seems like a fun excuse to learn about things like pitch detection, speech analysis, and signal processing.
I'm intentionally trying to understand every part of the project instead of just pasting together code that works. If I add a library or write a function, I want to know *why* it's there.

If other people find it useful someday, that's awesome too 👍
