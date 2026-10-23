
import unittest
import numpy as np


def count_repetitions(signal, threshold=55, min_gap=20):
    peaks = []

    for i in range(1, len(signal) - 1):
        is_peak = (
            signal[i] > signal[i - 1]
            and signal[i] >= signal[i + 1]
            and signal[i] > threshold
        )

        if is_peak and (not peaks or i - peaks[-1] >= min_gap):
            peaks.append(i)

    return len(peaks)


class TestKinetiCare(unittest.TestCase):

    def test_normal_movement(self):
        time = np.arange(0, 30, 0.1)
        signal = 45 + 25 * np.sin(2 * np.pi * time / 3)
        self.assertGreater(count_repetitions(signal), 0)

    def test_noisy_movement(self):
        np.random.seed(42)
        time = np.arange(0, 30, 0.1)
        signal = (
            45 + 25 * np.sin(2 * np.pi * time / 3)
            + np.random.normal(0, 4, len(time))
        )
        result = count_repetitions(signal)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 20)

    def test_paused_flat_signal(self):
        signal = np.full(100, 45.0)
        self.assertEqual(count_repetitions(signal), 0)

    def test_incomplete_signal(self):
        signal = np.array([40, 50, 60, 55, 45])
        self.assertEqual(count_repetitions(signal), 1)

    def test_low_range_movement(self):
        time = np.arange(0, 30, 0.1)
        signal = 45 + 8 * np.sin(2 * np.pi * time / 3)
        self.assertEqual(count_repetitions(signal), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
