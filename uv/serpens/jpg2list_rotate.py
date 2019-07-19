from PIL import Image
import math as m


# LIMITS = {'x_min': 1667, 'x_max': 2518, 'y_min': 4861-3485, 'y_max': 4861-3389}
LIMITS = {'x_min': 1467, 'x_max': 2718, 'y_min': 4861-3785, 'y_max': 4861-3089}
BLUR = 1
CENTER_X = 2260
CENTER_Y = 4861-3434

WIDTH = 54
# WIDTH = 850
# HEIGHT = 90
HEIGHT = 68

FACTOR = 0.001874609


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
        self.pixels.append(pixel)
        self.counter += 1

    def sort_and_round_pixels(self):
        for pixel in self.pixels:
            pixel.x = round(pixel.x)
            pixel.y = round(pixel.y)
        self.pixels = sorted(self.pixels, key=lambda pixel: pixel.x)
        self.pixels = sorted(self.pixels, key=lambda pixel: -pixel.y)

    def save(self):
        file_end=open(self.filename, 'w')

        previous_x = self.pixels[0].x - 1
        previous_y = self.pixels[0].y
        previous_value = self.pixels[0].value
        counter = 0

        for i in range(len(self.pixels)):
            if (
                self.pixels[i].x == previous_x + 1 and
                self.pixels[i].y == previous_y
            ) or (
                self.pixels[i].y != previous_y
            ):
                file_end.write(f'{counter:<7}{repr(self.pixels[i])}')
                previous_x = self.pixels[i].x
                previous_y = self.pixels[i].y
                previous_value = self.pixels[i].value
            else:
                previous_x += 1
                file_end.write(f'{counter:<7}{(2902-previous_x):<7}{(4861-previous_y):<7}'
                               f'{(previous_value):<5.5}\n')
                counter += 1
                file_end.write(f'{counter:<7}{repr(self.pixels[i])}')
                previous_x = self.pixels[i].x
                previous_y = self.pixels[i].y
                previous_value = self.pixels[i].value
            counter += 1

        file_end.close()


class Pixel:
    def __init__(self, picture, column, row, file):
        self.x = column
        self.y = row
        self.value = picture[column, row][0] * FACTOR
        self.file = file

    def __repr__(self):
        return f"{(2902-self.x):<7}{(4861-self.y):<7}{(self.value):<5.5}\n"

    def write_me_to_file(self, row):
        self.file.add(self, row)

    def within_boundaries(self):
        left_boundary = CENTER_X - WIDTH / 2
        right_boundary = CENTER_X + WIDTH / 2
        upper_boundary = CENTER_Y + HEIGHT / 2
        lower_boundary = CENTER_Y - HEIGHT / 2

        return (
            left_boundary < self.x < right_boundary and
            lower_boundary < self.y < upper_boundary
        )


class Rotator:
    def __init__(self, pixels):
        self.pixels = pixels

    def rotate(self, angle):
        for pixel in self.pixels:
            shift_x = pixel.x - CENTER_X
            shift_y = pixel.y - CENTER_Y

            new_x = shift_x*m.cos(angle) - shift_y*m.sin(angle)
            pixel.x = new_x + CENTER_X

            new_y = shift_x*m.sin(angle) + shift_y*m.cos(angle)
            pixel.y = new_y + CENTER_Y


class Cutter:
    def __init__(self, pixels):
        self.pixels = pixels

    def crop(self):
        cropped_image = [pixel for pixel in self.pixels if pixel.within_boundaries()]
        self.pixels = cropped_image


class Solver:
    def __init__(self, pixels):
        self.pixels = pixels

    def make_unique(self):
        unique = []
        coords = []
        for pixel in self.pixels:
            if (pixel.x, pixel.y) not in coords:
                unique.append(pixel)
                coords.append((pixel.x, pixel.y))

        self.pixels = unique


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
    image = read_image('serpens_bw2.jpeg')
    output = File('serpens_dust.txt')

    picture = Picture(image, output)
    picture.create_array()

    rotator = Rotator(output.pixels)
    rotator.rotate(angle=m.radians(-30))
    output.sort_and_round_pixels()

    cutter = Cutter(output.pixels)
    cutter.crop()

    solver = Solver(cutter.pixels)
    solver.make_unique()

    output.pixels = solver.pixels
    output.save()



if __name__ == '__main__':
	main()
