import sys
import matplotlib.pyplot as plt
from analyze_pitch import extract_pitch_and_intensity, clean_pitch
from reference_tones import TONE_CONTOURS, generate_reference_contour

def normalize_time(times):
    start = times[0]
    end = times[-1]
    normalized = []
    for t in times:
        normalized.append((t - start) / (end - start))
    return normalized

def normalize_pitch_to_chao_scale(frequencies):
    low = min(frequencies)
    high = max(frequencies)
    normalized = []
    for f in frequencies:
        scaled = 1 + (f - low) / (high - low) * 4
        normalized.append(scaled)
    return normalized

def interpolate_series(times, values, query_time):
    if query_time <= times[0]:
        return values[0]
    if query_time >= times[-1]:
        return values[-1]
    for i in range(len(times) - 1):
        if times[i] <= query_time <= times[i + 1]:
            fraction = (query_time - times[i]) / (times[i + 1] - times[i])
            return values[i] + fraction * (values[i + 1] - values[i])
    return values[-1]

def resample_contour(times, values, num_points):
    resampled_values = []
    for i in range(num_points):
        query_time = i / (num_points - 1)
        resampled_values.append(interpolate_series(times, values, query_time))
    return resampled_values

def plot_comparison(filename, tone_number):
    times, frequencies, intensities = extract_pitch_and_intensity(filename)
    clean_times, clean_frequencies = clean_pitch(times, frequencies, intensities)
    normalized_times = normalize_time(clean_times)
    normalized_pitch = normalize_pitch_to_chao_scale(clean_frequencies)
    resampled_pitch = resample_contour(normalized_times, normalized_pitch, 100)
    reference_times, reference_values = generate_reference_contour(TONE_CONTOURS[tone_number], 100)

    plt.figure()
    plt.plot(reference_times, reference_values, label="Reference tone " + str(tone_number), linestyle="--")
    plt.plot(reference_times, resampled_pitch, label="Your recording")
    plt.xlabel("Normalized time")
    plt.ylabel("Relative pitch (Chao scale)")
    plt.title("Comparison against tone " + str(tone_number))
    plt.ylim(0, 6)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    filename = sys.argv[1]
    tone_number = int(sys.argv[2])
    plot_comparison(filename, tone_number)