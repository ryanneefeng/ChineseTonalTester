import matplotlib.pyplot as plt

TONE_CONTOURS = {
    1: [(0.0, 5), (1.0, 5)],
    2: [(0.0, 3), (1.0, 5)],
    3: [(0.0, 2), (0.5, 1), (1.0, 4)],
    4: [(0.0, 5), (1.0, 1)],
}

def interpolate(control_points, t):
    for i in range(len(control_points) - 1):
        t0, v0 = control_points[i]
        t1, v1 = control_points[i + 1]
        if t0 <= t <= t1:
            fraction = (t - t0) / (t1 - t0)
            return v0 + fraction * (v1 - v0)
    return control_points[-1][1]

def generate_reference_contour(control_points, num_points):
    times = []
    values = []
    for i in range(num_points):
        t = i / (num_points - 1)
        times.append(t)
        values.append(interpolate(control_points, t))
    return times, values

def plot_all_tones():
    plt.figure()
    for tone_number in TONE_CONTOURS:
        times, values = generate_reference_contour(TONE_CONTOURS[tone_number], 100)
        plt.plot(times, values, label="Tone " + str(tone_number))
    plt.xlabel("Normalized time")
    plt.ylabel("Relative pitch (Chao scale)")
    plt.title("Idealized tone contours")
    plt.ylim(0, 6)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_all_tones()