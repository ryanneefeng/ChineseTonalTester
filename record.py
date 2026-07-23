import sys
import numpy as np
import sounddevice as sd
import soundfile as sf

SAMPLE_RATE = 16000

def record_until_enter(sample_rate):
    print("Press Enter to start recording")
    input()
    print("Recording... press Enter to stop")
    recorded_chunks = []

    def callback(indata, frames, time, status):
        recorded_chunks.append(indata.copy())

    stream = sd.InputStream(samplerate=sample_rate, channels=1, callback=callback)
    stream.start()
    input()
    stream.stop()
    stream.close()

    recording = np.concatenate(recorded_chunks, axis=0)
    print("Recording finished")
    return recording

def save_audio(recording, sample_rate, filename):
    sf.write(filename, recording, sample_rate)
    print("Saved to " + filename)

def play_audio(filename):
    data, sample_rate = sf.read(filename)
    print("Playing back...")
    sd.play(data, sample_rate)
    sd.wait()

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "test_recording.wav"
    recording = record_until_enter(SAMPLE_RATE)
    save_audio(recording, SAMPLE_RATE, filename)
    play_audio(filename)

if __name__ == "__main__":
    main()