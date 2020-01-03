from scipy.io import wavfile
from scipy.signal import decimate

import sys
import numpy as np
import matplotlib.pyplot as plt


class VoiceRecognitionAlgorithm:
    def run(self, filename, should_show_plot=False):
        try:
            rate_per_second, data = wavfile.read(filename)
        except:
            return "Failed to read file"

        # If Data is in 2D Array we should take only 1 dimension (in our example the first one)
        if len(data.shape) > 1:
            signal = [x[0] for x in data]
        else:
            signal = data
        length = len(signal)

        # Plot of readed data
        if should_show_plot:
            plt.plot(signal)
            plt.show()

        # Compute the one-dimensional discrete Fourier Transform
        fftsignal = np.fft.fft(signal)
        fftsignal = abs(fftsignal) * 2 / length

        # Compute all frequencies range
        frequencies = [i * rate_per_second / length for i in range(length)]

        fragment = int((1000 / rate_per_second) * length)
        fftfragment = fftsignal[:fragment]
        frequencyfragment = frequencies[:fragment]

        # Plot amplitude against frequency
        if should_show_plot:
            plt.ylabel('Amplitude')
            plt.xlabel('Frequency [Hz]')
            plt.stem(frequencyfragment, fftfragment, use_line_collection=True)
            plt.show()

        final_fft = fftfragment
        for x in range(2, 5):
            # Downsample the signal after applying an anti-aliasing filter.
            fft = decimate(fftfragment, x)
            # Refill rest of new_fft values with 0
            new_fft = list(fft) + [0 for i in range(fragment - len(fft))]

            # Plot step by step changes - amplitude against frequency
            if should_show_plot:
                plt.xlabel(x)
                plt.stem(frequencyfragment, new_fft, use_line_collection=True)
                plt.show()

            final_fft = final_fft * np.array(new_fft)

        # Plot final result of fft
        if should_show_plot:
            plt.xlabel("final")
            plt.stem(frequencyfragment, final_fft, use_line_collection=True)
            plt.show()

        # Rescale and get the most significant value
        final_fft = final_fft[int((70 / 1000) * len(frequencyfragment)):]
        frequencyfragment = frequencyfragment[int((70 / 1000) * len(frequencyfragment)):]
        result = frequencyfragment[np.argmax(final_fft)]

        return "M" if abs(132.5 - result) < abs(210 - result) else "K";


if __name__ == '__main__':
    print(sys.argv[1])
    gender = VoiceRecognitionAlgorithm().run(sys.argv[1])
    print(gender)
