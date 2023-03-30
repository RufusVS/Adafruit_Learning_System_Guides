# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
CircuitPython PWM Audio Out tone example
Plays a tone for one second on, one
second off, in a loop.

Remove this line and all of the following docstring content before submitting to the Learn repo.

Update the audio out pin to match the wiring chosen for the microcontroller. 
Update the following pin name to a viable pin:
* AUDIO_OUTPUT_PIN
"""
import time
import array
import math
import board
from audiocore import RawSample

try:
    from audioio import AudioOut
    print("Using AudioOut")
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
        print("Using PWMAudioOut")
    except ImportError:
        pass

audio = AudioOut(board.AUDIO_OUTPUT_PIN)

tone_volume = 0.1  # Increase this to increase the volume of the tone.
frequency = 440  # Set this to the Hz of the tone you want to generate.
length = 8000 // frequency
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int((1 + math.sin(math.pi * 2 * i / length)) * tone_volume * (2 ** 15 - 1))

sine_wave_sample = RawSample(sine_wave)

while True:
    audio.play(sine_wave_sample, loop=True)
    time.sleep(1)
    audio.stop()
    time.sleep(1)
