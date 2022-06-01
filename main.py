import os.path
import sys

from PIL import Image

N1, N2, N, input_file, output_file = sys.argv[1:]
if not (N.isdigit() and 0 <= int(N) <= 255):
    print("Введите корректное значение N")
elif not (N1.isdigit() and N2.isdigit() and int(N1) < int(N2)):
    print("Введите корректные границы промежутка")
elif not os.path.exists(input_file):
    print("Исходный файл не существует")
else:
    img = Image.open(input_file)
    pixels = img.load()
    N1 = int(N1)
    N2 = int(N2)
    N = int(N)
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            if N1 <= r + g + b <= N2:
                pixels[x, y] = N, N, N
    img.save(output_file)
