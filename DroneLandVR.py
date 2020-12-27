from ursina import *

window.borderless = False

camera.orthographic = True
#camera.position = Vec3(10, 0, 10)

app = Ursina()

ent = Entity(model='drone', color=color.black66,
			scale=(.5,.5,.5), position=Vec3(0,2.7, 10))

ground_out = Entity(model='circle', color=color.green,
			position=Vec3(0,-3.5, 10), rotation_x=90, scale=(15,15,15))

ground_in = Entity(model='circle', color=color.red,
			position=Vec3(0,-3.4, 10), rotation_x=90, scale=(7,7,7))


def update():

	ent.rotation_y += .5

	move_drone()
	move_cam()

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
