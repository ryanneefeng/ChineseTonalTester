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

- [ ] Record audio from my microphone
- [ ] Plot my pitch over time
- [ ] Recognize basic Mandarin tones
- [ ] Compare my pitch to the expected tone
- [ ] Give simple feedback
- [ ] Eventually support full sentences

## Why I'm making this

Mostly because I think it'd be useful for me.

I've also never built anything involving audio processing before, so this seems like a fun excuse to learn about things like pitch detection, speech analysis, and signal processing.

I'm intentionally trying to understand every part of the project instead of just pasting together code that works. If I add a library or write a function, I want to know *why* it's there.

If other people find it useful someday, that's awesome too.
