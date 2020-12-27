from ursina import *
import socket
from threading import Thread


window.borderless = False
window.size = 853, 480

camera.orthographic = True

ADDRESS = ('127.0.0.1', 55555)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(ADDRESS)

app = Ursina()

ent = Entity(model='drone', color=color.rgb(6, 23, 2),
			scale=(.5,.5,.5), position=Vec3(0, -3.2, 10))

ground_out = Entity(model='circle', color=color.green,
			position=Vec3(0,-3.5, 10), rotation_x=90, scale=(10,10,10))

ground_in = Entity(model='circle', color=color.red,
			position=Vec3(0,-3.4, 10), rotation_x=90, scale=(3,3,3))

x, z = 0, 0

def recv_data():
	global x
	global z

	try:
		while True:
			data, addr = s.recvfrom(1024)
			if data.decode('utf-8') == 'quit':
				break
			x, z = map(float, data.decode('utf-8').split(','))

			print(x, z)

	except ValueError as e:
		print(str(e))

recv_thread = Thread(target=recv_data)
recv_thread.start()

def update():

	ent.rotation_y += .5

	move_drone()
	move_cam()

	ent.x = x*1.5
	ent.z = z*1.5


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
