from PIL import Image


LIMITS = {'x_max': 2902-2076, 'x_min': 2902-2757, 'y_min': 3320, 'y_max': 3511} #reverse x axis


def read_image(file_name):
	image = Image.open(file_name)
	return image

class Pixel:
	def __init__(self, picture, column, row, file_name):
		self.x = column
		self.y = row
		self.value = picture[column, row][0]
		self.filename = file_name

	def __str__(self):
		return f"{self.x}    {self.y}    {self.value}"

	def __repr__(self):
		return f"{self.x}    {self.y}    {self.value} \n"

	def write_me_to_file(self, row):
		file_end=open(self.filename,'a')
		file_end.write(str(row)+'    ')
		file_end.write(repr(self))
		file_end.close()


class Picture:
	def __init__(self, image, file_end_name):
		self.width = image.size[0]
		self.height = image.size[1]
		self.picture = image.load()
		self.file_end_name = file_end_name
		self.pixels = self.create_array()
		

	def create_array(self):
		pixels = []
		for row in range(LIMITS['y_min'], LIMITS['y_max']):
			row_pixels = []
			for column in range(LIMITS['x_min'], LIMITS['x_max']):
				pixel = Pixel(self.picture, column, row, self.file_end_name)
				row_pixels.append(pixel)
				pixel.write_me_to_file(row)
			pixels.append(row_pixels)
		return pixels

	def get_pixels(self):
		return [pixel for row in self.pixels for pixel in row]
		
def clear_file(filename):
	trash = open(filename, 'w')
	trash.close()

def main():
	file_name = 'serpens_bw2.jpeg'
	file_end_name = 'serpens_dust.txt'

	image = read_image(file_name)
	clear_file(file_end_name)
	picture = Picture(image, file_end_name)
	pixels = picture.pixels
	
	
	#print(picture.width, picture.height, pixels[0])

if __name__ == '__main__':
	main()
