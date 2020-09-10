import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
#from thinkdsp import read_wave
#from thinkdsp import play_wave
#import matplotlib.pyplot as plt

frecuencia697 = SinSignal(freq=697, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)
frecuencia852 = SinSignal(freq=852, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)

#frecuencia440 = SinSignal(freq=440, amp=1, offset=0)
#frecuencia622 = SinSignal(freq=622, amp=1, offset=0)

wave_697 = frecuencia697.make_wave(duration=0.5, start=0, framerate=44100)
wave_1209 = frecuencia1209.make_wave(duration=0.5, start=0, framerate=44100)
wave_770 = frecuencia770.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_1336 = frecuencia1336.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_852 = frecuencia852.make_wave(duration=0.5, start=1, framerate=44100)
wave_1477 = frecuencia1477.make_wave(duration=0.5, start=1, framerate=44100)
wave_697_2 = frecuencia697.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_1209_2 = frecuencia1209.make_wave(duration=0.5, start=1.5, framerate=44100)

#wave_440 = frecuencia440.make_wave(duration=0.5, start=0, framerate=44100)
#wave_622 = frecuencia622.make_wave(duration=0.5, start=0.5, framerate=44100)

wave_1 = wave_697 + wave_1209
wave_5 = wave_770 + wave_1336
wave_9 = wave_852 + wave_1477
wave_1_2 = wave_697_2 + wave_1209_2

#decorate(xlabel="Tiempo (s)")
#decorate(ylabel="Amplitud")

#wave_1.plot()

#wave_1.write("output1.wav")
#wave_5.write("output5.wav")
#wave_9.write("output9.wav")
#wave_1_2.write("output11.wav")

wave_sonido = wave_1 + wave_5 + wave_9 + wave_1_2

#wave_sonido = wave_440 + wave_622

wave_sonido.write("output.wav")

#plt.show()