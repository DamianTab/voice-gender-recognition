from voice_recognition import VoiceRecognitionAlgorithm
from voice_recognition_HPS import main

from os import listdir
from os.path import isfile, join

def run():
    path = "train"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    files.sort()

    for name in files:
        print("\n" + name)

        # Recognition Algorithm
        # algorithm = VoiceRecognitionAlgorithm()
        # gender = algorithm.run(path + "/" + name)

        # Harmonic Product Spectrum Algorithm
        gender = main(path + "/" + name)
        print(gender)


if __name__ == '__main__':
    run()
