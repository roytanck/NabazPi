import unicornhat as unicorn
import time
import math
import colorsys
import random

class Nabazpileds:

	height = 0;
	width = 0;

	def __init__(self):
		unicorn.set_layout(unicorn.HAT)
		unicorn.rotation(90)
		unicorn.brightness(1)
		self.width,self.height=unicorn.get_shape()
		# print('inited')

	def startup(self):
		for y in range(self.height):
			for x in range(self.width):
				unicorn.set_pixel(x,(self.height-1)-y,0,255,0)
				unicorn.show()
				time.sleep(0.05)
		time.sleep(0.5)
		unicorn.off();

	def glow(self):
		unicorn.off()
		steps = 100
		for i in range(0, steps):
			brightness = int( round( math.sin( (i/steps) * math.pi ) * 255 ) )
			# print(brightness)
			for y in range(self.height):
				for x in range(self.width):
					unicorn.set_pixel(x,y,brightness,0,brightness)
			unicorn.show();
			time.sleep(0.01)
		unicorn.off()

	# don't hassle the hoff!
	def kitt(self):
		steps = 64
		for i in range(0,steps):
			unicorn.clear();
			mod = i%13
			if( mod < 6 ):
				x = mod
			else:
				x = 6 - (mod-6)
			for y in range(3,6):
				unicorn.set_pixel(x,y,255,0,0)
				unicorn.set_pixel(x+1,y,255,0,0)
			unicorn.show()
			time.sleep(0.1)
		unicorn.off()

	def cross(self):
		unicorn.off()
		for i in range(0,8):
			unicorn.set_pixel(i,i,255,0,0);
			unicorn.set_pixel(i,7-i,255,0,0);
		unicorn.show()
		time.sleep(1)
		unicorn.off()


	def wave(self):
		# print('wave')
		steps = 200
		for i in range(steps):
			for y in range(self.height):
				for x in range(self.width):
					dist = math.sqrt( math.pow( math.fabs(x-3.5), 2 ) + math.pow( math.fabs(y-3.5),2 ) )
					b = round( 128 + math.sin( (dist-i/20) ) * 127 )
					unicorn.set_pixel( x, y, round(b/3), round(b/2), b )
			unicorn.show()
			time.sleep(0.01)
		unicorn.off()

	def colorcycle(self):
		steps = 360
		for i in range(0,steps):
			# col = colorsys.hsv_to_rgb( i, 1, 1 )
			# brightness = math.sin( (i/steps) * math.pi )
			# print(brightness)
			col = self.hsv2rgb( (i+240)%360, 1, 1 )
			for x in range(0,self.width):
				for y in range(0,self.height):
					unicorn.set_pixel( x, y, col[0], col[1], col[2] )
			unicorn.show()
			time.sleep(0.01)
		unicorn.off()

	def rainbow(self):
		steps = 200
		for s in range(steps):
			for i in range(8):
				col = self.hsv2rgb( (i*45+s*5)%360, 1, 1 )
				self.drawRect( 0, i, 8, 1, col[0], col[1], col[2] )
			unicorn.show()
			time.sleep(0.02)
		unicorn.off()

	def disco(self):
		steps = 25
		for i in range( steps ):
			for x in range(4):
				for y in range(4):
					col = self.hsv2rgb( random.randint( 0, 359 ), 1, random.uniform( 0.5, 1 ) )
					for i in range(2):
						for j in range(2):
							unicorn.set_pixel( x*2 + i, y*2 + j, col[0], col[1], col[2] );
			unicorn.show()
			time.sleep(0.2)
		unicorn.off()

	def police(self):
		for i in range(3):
			for j in range(8):
				self.drawRect( 0, 0, 8, 8, 80, 100, 255 )
				time.sleep(0.05)
				unicorn.clear()
				unicorn.show()
				time.sleep(0.05)
			time.sleep(0.25)
		unicorn.off()

	def traffic(self):
		unicorn.clear()
		self.drawRect( 3, 0, 2, 2, 255, 0, 0 )
		unicorn.show()
		time.sleep(1)
		unicorn.clear()
		self.drawRect( 3, 3, 2, 2, 255, 185, 0 )
		unicorn.show()
		time.sleep(1)
		unicorn.clear()
		self.drawRect( 3, 6, 2, 2, 0, 255, 0)
		unicorn.show()
		time.sleep(1)
		unicorn.off()

	def drawRect(self, sx, sy, w, h, r, g, b ):
		for x in range( sx, sx+w ):
			for y in range( sy, sy+h ):
				unicorn.set_pixel( x, y, r, g, b )
		unicorn.show();

	def hsv2rgb( self, h, s, v ):
		col = colorsys.hsv_to_rgb( h/360.0, s, v )
		return ( round( col[0] * 255 ), round( col[1] * 255 ), round( col[2] * 255 ) )
