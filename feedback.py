import sys
from analyze_pitch import extract_pitch_and_intensity, clean_pitch, get_semitone_range
from compare_tones import normalize_pitch_to_chao_scale, normalize_time
from reference_tones import TONE_CONTOURS, generate_reference_contour
from dtw import align
from dtw_compare import find_min_time_fraction, FLAT_THRESHOLD_SEMITONES, EARLY_MIN_THRESHOLD

COST_CEILING = 150

def calculate_score(cost):
    score = 100 * (1 - cost / COST_CEILING)
    if score < 0:
        score = 0
    if score > 100:
        score = 100
    return score

def generate_message(intended_tone, semitone_range, min_time_fraction):
    if intended_tone == 1:
        if semitone_range > FLAT_THRESHOLD_SEMITONES:
            return "Try to keep your pitch flatter throughout."
        return "Good, nice and flat."
    if intended_tone == 2:
        if semitone_range < FLAT_THRESHOLD_SEMITONES:
            return "Not enough rise. Push your pitch up higher by the end."
        if min_time_fraction >= EARLY_MIN_THRESHOLD:
            return "Your low point should be right at the start, then rise steadily."
        return "Good, clear rise."
    if intended_tone == 3:
        if semitone_range < FLAT_THRESHOLD_SEMITONES:
            return "Not enough dip. Let your pitch drop lower before rising back up."
        if min_time_fraction < EARLY_MIN_THRESHOLD:
            return "Your dip came too early. Start a bit higher before dipping."
        return "Good dip and rise."
    if intended_tone == 4:
        if semitone_range < FLAT_THRESHOLD_SEMITONES:
            return "Not enough fall. Commit harder to dropping your pitch."
        return "Good, strong fall."
    return ""

def give_feedback(filename, intended_tone):
    times, frequencies, intensities = extract_pitch_and_intensity(filename)
    clean_times, clean_frequencies = clean_pitch(times, frequencies, intensities)
    semitone_range = get_semitone_range(clean_frequencies)
    normalized_times = normalize_time(clean_times)
    min_time_fraction = find_min_time_fraction(normalized_times, clean_frequencies)
    normalized_pitch = normalize_pitch_to_chao_scale(clean_frequencies)

    reference_times, reference_values = generate_reference_contour(TONE_CONTOURS[intended_tone], 100)
    path, cost = align(normalized_pitch, reference_values)

    score = calculate_score(cost)
    message = generate_message(intended_tone, semitone_range, min_time_fraction)
    return score, message

if __name__ == "__main__":
    filename = sys.argv[1]
    intended_tone = int(sys.argv[2])
    score, message = give_feedback(filename, intended_tone)
    print(round(score), "% -", message)