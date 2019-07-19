from PIL import Image
import math as m


LIMITS = {'x_min': 2167, 'x_max': 2318, 'y_min': 4861-3485, 'y_max': 4861-3389}
BLUR = 1
CENTER_X = 2275
CENTER_Y = 4861-3432
FACTOR = 0.001874609

def read_image(file_name):
	image = Image.open(file_name)
	return image

class File:
    pixels = None
    counter = None
    pixels_array = None

    def __init__(self, filename):
        self.filename = filename
        self.pixels = []
        self.counter = 0
        self.pixels_array = []

    def add(self, pixel, row):
        self.pixels.append(f'{self.counter}    {repr(pixel)}')
        self.pixels_array.append(pixel)
        self.counter += 1

    def save(self):
        file_end=open(self.filename, 'w')
        for i, pixel in enumerate(self.pixels_array):
            file_end.write(f'{i} {repr(pixel)}')
        file_end.close()

class Pixel:
    def __init__(self, picture, column, row, file):
        self.x = column
        self.y = row
        self.value = picture[column, row][0] * FACTOR
        self.file = file

    def __repr__(self):
        return f"{2902-self.x}    {4861-self.y}    {self.value} \n"

    def write_me_to_file(self, row):
        self.file.add(self, row)

class Rotator:
    def __init__(self, pixels):
        self.pixels = pixels

    def rotate(self, angle):
        for pixel in self.pixels:
            new_x = pixel.x*m.cos(angle) - pixel.y*m.sin(angle)
            new_y = pixel.x*m.sin(angle) + pixel.y*m.cos(angle)
            pixel.x = new_x
            pixel.y = new_y

class Picture:
    def __init__(self, image, file):
        self.width = image.size[0]
        self.height = image.size[1]
        self.picture = image.load()
        self.file = file

    def create_array(self):
        for row in range(LIMITS['y_min'], LIMITS['y_max'], BLUR):
            for column in range(LIMITS['x_min'], LIMITS['x_max'], BLUR):
                pixel = Pixel(self.picture, column, row, self.file)
                pixel.write_me_to_file(row)

    def get_pixels(self):
        return [pixel for row in self.pixels for pixel in row]

def main():
    file_name = 'serpens_bw2.jpeg'
    file_end_name = 'serpens_dust.txt'

    output = File(file_end_name)
    image = read_image(file_name)
    picture = Picture(image, output)
    picture.create_array()

    rotator = Rotator(output.pixels_array)
    rotator.rotate(angle=m.radians(-30))
    output.save()
    
if __name__ == '__main__':
	main()
