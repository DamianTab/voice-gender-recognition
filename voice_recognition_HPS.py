import numpy as np
import numpy.fft as fft
import sys
import librosa


def divide(signal, chunk_length, overlap_length):
    d = chunk_length - overlap_length
    chunks = []
    for i in range(0, len(signal) - chunk_length + 1, d):
        chunks.append(signal[i:i + chunk_length])
    return chunks


def window(chunks):
    windowed_chunks = []
    for ch in chunks:
        windowed_chunks.append(ch * np.hamming(len(ch)))
    return windowed_chunks


def hps(signal, steps, fft_length):
    f_signal = fft.fft(signal, fft_length)
    f_signal = f_signal[:len(f_signal) // 2]
    f_signal = np.abs(f_signal)

    result_length = len(f_signal) // steps
    result = f_signal[:result_length].copy()

    for i in range(2, steps + 1):
        result *= f_signal[::i][:result_length]

    return result


def find_fundamental_frequency(hps_result, sample_rate, signal_length):
    min_f = 50
    start_i = int((min_f / sample_rate) * signal_length)

    mx_i = start_i
    for i in range(start_i + 1, len(hps_result)):
        if hps_result[i] > hps_result[mx_i]:
            mx_i = i

    return (mx_i / signal_length) * sample_rate


def main(file):
    signal, w = librosa.load(file)

    signal = signal.astype(float) / 2 ** 16
    w = float(w)

    if len(signal.shape) > 1:
        signal = [s[0] for s in signal]

    chunk_length = 16 * 1024
    overlap_length = chunk_length // 2
    hps_steps = 4
    fft_length = 4 * chunk_length

    chunks = divide(signal, chunk_length, overlap_length)
    chunks = window(chunks)

    frequencies = []
    for ch in chunks:
        hps_result = hps(ch, hps_steps, fft_length)
        frequencies.append(find_fundamental_frequency(hps_result, w, fft_length))

    fr = np.median(frequencies)
    if fr < 170:
        return 'M'
    else:
        return 'K'


if __name__ == '__main__':
    print(sys.argv[1])
    print(main(sys.argv[1]))
