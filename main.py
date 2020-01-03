from voice_recognition import VoiceRecognitionAlgorithm

from os import listdir
from os.path import isfile, join

def run():
    path = "train"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for name in files:
        print("\n" + name)
        algorithm = VoiceRecognitionAlgorithm()
        gender = algorithm.run(path + "/" + name)
        print(gender)


if __name__ == '__main__':
    run()
