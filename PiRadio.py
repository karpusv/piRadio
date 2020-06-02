#!/usr/bin/python3

from subprocess import run, Popen, PIPE


def play_wav(filename, freq="100.0", sample_rate="22050", stereo=True):
    if(stereo):
        run(["./pifm", filename, freq, sample_rate, "stereo"], capture_output=True)
    else:
        run(["./pifm", filename, freq, sample_rate], capture_output=True)
    return


def play_mp3(filename, freq="100.0", sample_rate="22050", stereo=False):
    if(stereo):
        ps = Popen(("ffmpeg", "-hide_banner", "-loglevel", "warning", "-i", filename, "-f",
                    "s16le", "-ar", sample_rate, "-ac", "2", "-af", "arealtime", "-"), stdout=PIPE)
        run(["./pifm", "-", "91.1", sample_rate, "stereo"],
            stdin=ps.stdout, capture_output=True)

    else:
        ps = Popen(("ffmpeg", "-hide_banner", "-loglevel", "warning", "-i", filename, "-f",
                    "s16le", "-ar", sample_rate, "-ac", "1", "-af", "arealtime", "-"), stdout=PIPE)
        run(["./pifm", "-", "91.1", sample_rate],
            stdin=ps.stdout, capture_output=True)
    return
