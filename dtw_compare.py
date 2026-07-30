import sys
from analyze_pitch import extract_pitch_and_intensity, clean_pitch, get_semitone_range
from compare_tones import normalize_pitch_to_chao_scale, normalize_time
from reference_tones import TONE_CONTOURS, generate_reference_contour
from dtw import align

FLAT_THRESHOLD_SEMITONES = 2.0
MAGNITUDE_PENALTY = 50
EARLY_MIN_THRESHOLD = 0.25
LATE_MIN_THRESHOLD = 0.75
SHAPE_PENALTY = 50

def find_min_time_fraction(normalized_times, frequencies):
    min_index = 0
    for i in range(len(frequencies)):
        if frequencies[i] < frequencies[min_index]:
            min_index = i
    return normalized_times[min_index]

def compare_against_all_tones(filename):
    times, frequencies, intensities = extract_pitch_and_intensity(filename)
    clean_times, clean_frequencies = clean_pitch(times, frequencies, intensities)
    semitone_range = get_semitone_range(clean_frequencies)
    normalized_times = normalize_time(clean_times)
    min_time_fraction = find_min_time_fraction(normalized_times, clean_frequencies)
    print("minimum pitch occurs at normalized time:", round(min_time_fraction, 3))
    normalized_pitch = normalize_pitch_to_chao_scale(clean_frequencies)

    for tone_number in TONE_CONTOURS:
        reference_times, reference_values = generate_reference_contour(TONE_CONTOURS[tone_number], 100)
        path, total_cost = align(normalized_pitch, reference_values)
        if tone_number != 1 and semitone_range < FLAT_THRESHOLD_SEMITONES:
            total_cost = total_cost + MAGNITUDE_PENALTY
        if tone_number == 3 and min_time_fraction < EARLY_MIN_THRESHOLD:
            total_cost = total_cost + SHAPE_PENALTY
        if tone_number == 2 and EARLY_MIN_THRESHOLD <= min_time_fraction <= LATE_MIN_THRESHOLD:
            total_cost = total_cost + SHAPE_PENALTY
        print("tone", tone_number, "- total cost:", round(total_cost, 2))

if __name__ == "__main__":
    filename = sys.argv[1]
    compare_against_all_tones(filename)