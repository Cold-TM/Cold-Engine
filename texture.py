import pygame as pg
import moderngl as mgl

class Texture:
	def __init__(self, ctx):
		self.ctx = ctx
		self.textures = {}
		self.textures[0] = self.get_texture(path='C:/Users/Admin/Desktop/Cold 2 Global/textures/img2.png')
		self.textures[1] = self.get_texture(path='C:/Users/Admin/Desktop/Cold 2 Global/textures/img.png')
		self.textures['Spec'] = self.get_texture(path='C:/Users/Admin/Desktop/Cold 2 Global/objects/Spec/Textures/Character/Camo/HeadGear_Base_color.png')
		self.textures['Spec2'] = self.get_texture(path='C:/Users/Admin/Desktop/Cold 2 Global/objects/Spec/Textures/Character/Camo/Body_Base_color.png')

	def get_texture(self, path):
		texture = pg.image.load(path).convert()
		texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
		texture = self.ctx.texture(size=texture.get_size(), components=3,
									data=pg.image.tostring(texture, 'RGB'))
		texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
		texture.build_mipmaps()
		texture.anisotropy = 32.0
		return texture

	def destroy(self):
		[tex.release() for tex in self.textures.values()]