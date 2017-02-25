import numpy  # Using numpy is much faster
import png
import requests


def main():
    rows = [[255 for element in range(4) for number_of_pixles in range(256)] for number_of_rows in range(256)]
    rows = numpy.zeros((256, 256 * 4), dtype='int')
    rows[:] = 255
    png_writer = png.Writer(width=256, height=256, alpha='RGBA')
    png_writer.write(open('white_panel.png', 'wb'), rows)


url_prefix = 'https://www.random.org/'


def get_true_random_integers(n, min, max, cols, base):
    params = {'num': n,
              'min': min,
              'max': max,
              'col': cols,
              'base': base,
              'format': 'plain',
              'rnd': 'new'}
    url = url_prefix + 'integers/'
    j = requests.get(url, params=params)
    print(j)


if __name__ == '__main__':
    main()
