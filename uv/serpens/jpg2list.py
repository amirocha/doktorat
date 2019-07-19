from PIL import Image
import math as m


LIMITS = {'x_min': 2167, 'x_max': 2318, 'y_min': 4861-3485, 'y_max': 4861-3389}
BLUR = 1

def read_image(file_name):
	image = Image.open(file_name)
	return image

class File:
    pixels = None
    counter = None

    def __init__(self, filename):
        self.filename = filename
        self.pixels = []
        self.counter = 0

    def add(self, pixel, row):
        self.pixels.append(f'{self.counter}    {repr(pixel)}')
        self.counter += 1

    def save(self):
        file_end=open(self.filename, 'w')
        for pixel in self.pixels:
            file_end.write(pixel)
        file_end.close()

class Pixel:
    def __init__(self, picture, column, row, file):
        self.x = column
        self.y = row
        self.value = picture[column, row][0]
        self.file = file

    def __repr__(self):
        return f"{2902-self.x}    {4861-self.y}    {self.value} \n"

    def write_me_to_file(self, row):
        self.file.add(self, row)

class Rotator:
    def __init__(self, pixels):
        self.pixels = pixels

    def rotate(angle):
        pass
	

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

    rotator = Rotator(output.pixels)
    #rotator.rotate(angle=(m.pi/2))
    output.save()
    
if __name__ == '__main__':
	main()
