from ursina import *

window.borderless = False
window.size = 640, 360

camera.orthographic = True

app = Ursina()

ent = Entity(model='drone', color=color.rgb(6, 23, 2),
			scale=(.5,.5,.5), position=Vec3(0,2.7, 10))

ground_out = Entity(model='circle', color=color.green,
			position=Vec3(0,-3.5, 10), rotation_x=90, scale=(15,15,15))

ground_in = Entity(model='circle', color=color.red,
			position=Vec3(0,-3.4, 10), rotation_x=90, scale=(5,5,5))


def update():

	ent.rotation_y += .5

	move_drone()
	move_cam()
	read_data('data.txt')

def read_data(file):
	with open(file) as f:
		data = f.read().strip().split(',')
		try:
			x, z = map(float, data)
			ent.x = x
			ent.z = z

			# print(x, z)
		except ValueError as e:
			print(str(e))

def move_cam():
	if held_keys['c']:
		camera.position += (.1, 0, 0)
	if held_keys['v']:
		camera.position -= (.1, 0, 0)
	if held_keys['b']:
		camera.position += (0, .1, 0)
	if held_keys['n']:
		camera.position -= (0, .1, 0)
	if held_keys['m']:
		camera.position += (0, 0, .1)
	if held_keys['x']:
		camera.position -= (0, 0, .1)



def move_drone():
	ent.x += held_keys['d'] * .1
	ent.x -= held_keys['a'] * .1

	ent.y += held_keys['w'] * .1
	ent.y -= held_keys['s'] * .1

	ent.z += held_keys['q'] * .1
	ent.z -= held_keys['e'] * .1


if __name__ == '__main__':
	app.run()
