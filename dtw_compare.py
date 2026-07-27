import sys
from analyze_pitch import extract_pitch_and_intensity, clean_pitch, get_semitone_range
from compare_tones import normalize_pitch_to_chao_scale
from reference_tones import TONE_CONTOURS, generate_reference_contour
from dtw import align

FLAT_THRESHOLD_SEMITONES = 2.0
MAGNITUDE_PENALTY = 50

def compare_against_all_tones(filename):
    times, frequencies, intensities = extract_pitch_and_intensity(filename)
    clean_times, clean_frequencies = clean_pitch(times, frequencies, intensities)
    semitone_range = get_semitone_range(clean_frequencies)
    normalized_pitch = normalize_pitch_to_chao_scale(clean_frequencies)

    for tone_number in TONE_CONTOURS:
        reference_times, reference_values = generate_reference_contour(TONE_CONTOURS[tone_number], 100)
        path, total_cost = align(normalized_pitch, reference_values)
        if tone_number != 1 and semitone_range < FLAT_THRESHOLD_SEMITONES:
            total_cost = total_cost + MAGNITUDE_PENALTY
        print("tone", tone_number, "- total cost:", round(total_cost, 2))

if __name__ == "__main__":
    filename = sys.argv[1]
    compare_against_all_tones(filename)