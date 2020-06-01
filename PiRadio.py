#!/usr/bin/python3

from subprocess import run


def play_sound(filename, freq="100.0", sample_rate="22050"):
    run(["./pifm", filename, freq, sample_rate])
    return