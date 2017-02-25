import wave
import random
import struct
import datetime

###CREDIT TO https://github.com/sole/snippets/blob/master/audio/generate_noise_test_python/script.py
#SOLEDAD PENADÉS for starter code for writing audio file

SAMPLE_LEN = 44100 * 30 # 30 seconds of noise, .5 minutes
noise_output = wave.open('noise2.wav', 'w')
noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

d1 = datetime.datetime.now()
values = []

values = [ _ in range(0, SAMPLE_LEN)]
for i in range(0, SAMPLE_LEN):
    #Range of single sample in 16bits
    value = random.randint(-32767, 32767)
    #Convert to hex
    packed_value = struct.pack('h', value)
    values.append(packed_value)
    values.append(packed_value)

value_str = b''.join(values)
noise_output.writeframes(value_str)

d2 = datetime.datetime.now()
print (d2 - d1), "(time for writing frames)"

noise_output.close()

d3 = datetime.datetime.now()
print (d3 - d2), "(time for closing the file)"