import unicornhat as unicorn
import time
import math
from random import randint

class Nabazpileds:

	height = 0;
	width = 0;

	def __init__(self):
		unicorn.set_layout(unicorn.HAT)
		unicorn.rotation(90)
		unicorn.brightness(0.5)
		self.width,self.height=unicorn.get_shape()
		print('inited')

	def turnon(self):
		print('turnon')
		for y in range(self.height):
			for x in range(self.width):
				unicorn.set_pixel(x,y,255,0,255)
				unicorn.show()
				time.sleep(0.05)

		time.sleep(1)
		unicorn.off();

	def glow(self):
		unicorn.off()
		steps = 100
		for i in range(0, steps):
			brightness = int( round( math.sin( (i/steps) * math.pi ) * 255 ) )
			# print(brightness)
			for y in range(self.height):
				for x in range(self.width):
					unicorn.set_pixel(x,y,0,brightness,0)
			unicorn.show();
			time.sleep(0.01)
		# print('ja')
		unicorn.off()

	def kitt(self):
		unicorn.off()
		steps = 100
		for i in range(0, steps):
			unicorn.clear()
			progress = 3.5 + ( math.cos( (i/steps) * 2 * math.pi * 2 ) * 3 )

			for x in range( math.floor(progress)-1, math.ceil(progress)+1 ):
				if x >= 0 and x < 9:
					b = round( ( 2 - math.fabs( progress - x ) ) * 127 )
					for y in range(self.height):
						unicorn.set_pixel(x,y,b,0,0)

			unicorn.show()
			time.sleep(0.02)

		unicorn.off()

	def cross(self):
		print('cross')
		unicorn.off()
		for i in range(0,8):
			unicorn.set_pixel(i,i,255,0,0);
			unicorn.set_pixel(i+1,i,255,0,0);
			unicorn.set_pixel(i-1,i,255,0,0);
			unicorn.set_pixel(i,7-i,255,0,0);
			unicorn.set_pixel(i,6-i,255,0,0);
			unicorn.set_pixel(i,8-i,255,0,0);
		unicorn.show()
		time.sleep(1)
		unicorn.off()

	def wave(self):
		print('wave')
		steps = 200
		for i in range(steps):
			for y in range(self.height):
				for x in range(self.width):
					dist = math.sqrt( math.pow( math.fabs(x-3.5), 2 ) + math.pow( math.fabs(y-3.5),2 ) )
					b = round( 128 + math.sin( (dist-i/20) ) * 127 )
					unicorn.set_pixel(x,y,0,b,round(b/2))
			unicorn.show()
			time.sleep(0.01)
		unicorn.off()
