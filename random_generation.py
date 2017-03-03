import numpy
import png
import requests
import time
import re
import struct
import wave
import random


def main():
    random_rgb_bitmap(128,128, 'random128.png')
    random_noise(44100*3, 'random3sec.wav')

url_prefix = 'https://www.random.org/'


def random_rgb_bitmap(height, width, filepath):
    """
    Create a random bitmap using Random.org API. Max width of 3333 pixels (due to Random API caps)
    May take long time depending on the size of the image
    :param width: Width of bitmap
    :param height: Height of bitmap
    :param filepath: Filepath for where to save image
    :return: None
    """
    if width > 3333:
        raise Exception("Bitmap requested too large")
    pixels = []
    for i in range(height):
        row = get_true_random_integers(width*3, 0, 255, width*3, 10)[0]
        pixels.append(row)
        time.sleep(0.05) #Limit API requests

    png_writer = png.Writer(width=width, height=height)
    png_writer.write(open(filepath, 'wb'), pixels)


def random_noise(sample_len=44100 * 30, filepath='random30sec.wav'):
    """
    Generates a file of white/random noise.
    :param sample_len:
    :param filepath:
    :return:
    """
    if sample_len > 44100 * 120:
        raise Exception("Sound file requested too long")

    total_requested = 0
    vals = []
    noise_output = wave.open(filepath, 'w')
    noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))
    while total_requested < sample_len:
        if sample_len - total_requested < 10000:
            total_requested = sample_len
            vals += get_true_random_integers(sample_len, -32767, 32767, sample_len, 10)[0]
            #vals += [random.randint(-32767, 32767) for _ in range(sample_len)]
        else:
            total_requested += 10000
            vals += get_true_random_integers(10000, -32767, 32767, sample_len, 10)[0]
            #vals += [random.randint(-32767, 32767) for _ in range(10000)]

    packed_vals = ([struct.pack('h', sample) for sample in vals])
    joined_vals = b''.join(packed_vals)
    noise_output.writeframes(joined_vals)
    noise_output.close()


def get_true_random_integers(n, min, max, cols, base):
    """
    Queries Random.org for truly random integers
    :param n:
    :param min:
    :param max:
    :param cols:
    :param base:
    :return:
    """
    params = {'num': n,
              'min': min,
              'max': max,
              'col': cols,
              'base': base,
              'format': 'plain',
              'rnd': 'new'}
    url = url_prefix + 'integers/'
    j = requests.get(url, params=params)
    #j = gen_test_input(min, max, n)
    #return random_org_to_list(j)
    #j = gen_test_input(min, max,n)
    return random_org_to_list(j.text)

def random_org_to_list(text):
    """
    Converts random org response text into a list of lists of integers.
    :param text:
    :return:
    """
    lines = text.splitlines()
    clean =  [re.split(r'\t+', x) for x in lines]
    num_list = [[int(val.strip()) for val in x] for x in clean]
    return num_list

def gen_test_input(low, high, size):
    """
    Generates a single row of inputs simulating random.org data.
    :param low:
    :param high:
    :param size:
    :return:
    """
    nums = numpy.random.randint(low, high, size)
    strings = [str(n) for n in nums]
    my_str = '\t'.join(strings)
    return my_str

if __name__ == '__main__':
    main()

