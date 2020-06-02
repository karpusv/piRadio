#!/usr/bin/python3

from subprocess import run


def play_wav(filename, freq="100.0", sample_rate="22050", stereo=True):
    if(stereo):
        run(["./pifm", filename, freq, sample_rate, "stereo"],capture_output=True)
    else:
        run(["./pifm", filename, freq, sample_rate], capture_output=True)
    return