import cv2
import numpy as np


def main():
	img = cv2.imread('land.jpg')
	while True:
		cv2.imshow('frame', img)

		if cv2.waitKey(25) & 0xFF == ord('q'):
			break

if __name__ == '__main__':
	main()
