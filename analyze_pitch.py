import sys
import math
import parselmouth
import matplotlib.pyplot as plt

INTENSITY_MARGIN_DB = 20

def extract_pitch_and_intensity(filename):
    sound = parselmouth.Sound(filename)
    pitch = sound.to_pitch(pitch_ceiling=200)
    intensity = sound.to_intensity()
    pitch_frequencies = pitch.selected_array['frequency']
    pitch_times = pitch.xs()
    intensity_values = []
    for t in pitch_times:
        intensity_values.append(intensity.get_value(time=t))
    return pitch_times, pitch_frequencies, intensity_values

def clean_pitch(times, frequencies, intensities):
    real_intensities = []
    for value in intensities:
        if not math.isnan(value):
            real_intensities.append(value)
    max_intensity = max(real_intensities)
    threshold = max_intensity - INTENSITY_MARGIN_DB
    print("total frames:", len(frequencies))
    voiced_count = 0
    for f in frequencies:
        if f != 0:
            voiced_count += 1
    print("frames with nonzero frequency:", voiced_count)
    print("max intensity:", max_intensity)
    print("threshold:", threshold)
    clean_times = []
    clean_frequencies = []
    for i in range(len(frequencies)):
        if frequencies[i] != 0 and not math.isnan(intensities[i]) and intensities[i] >= threshold:
            clean_times.append(times[i])
            clean_frequencies.append(frequencies[i])
    print("frames passing both filters:", len(clean_frequencies))
    return clean_times, clean_frequencies

def get_semitone_range(frequencies):
    min_freq = min(frequencies)
    max_freq = max(frequencies)
    semitone_range = 12 * math.log2(max_freq / min_freq)
    print("min frequency:", min_freq)
    print("max frequency:", max_freq)
    print("semitone range:", semitone_range)
    return semitone_range

def plot_pitch(times, frequencies, title):
    plt.figure()
    plt.plot(times, frequencies, marker="o")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.title(title)
    plt.show()

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "ma1.wav"
    times, frequencies, intensities = extract_pitch_and_intensity(filename)
    clean_times, clean_frequencies = clean_pitch(times, frequencies, intensities)
    get_semitone_range(clean_frequencies)
    plot_pitch(clean_times, clean_frequencies, "Pitch contour")

if __name__ == "__main__":
    main()