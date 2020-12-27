import cv2
import numpy as np

'''
	# GREEN HSV VALUES (10:45, 40:255, 10:255), (65:255, 255, 255)
	# RED HSV VALUES (0, 30:235, 0:230), (0:45, 255, 255)
'''

YELLOW = (0,255,255)
TERQUIZE = (255,255,0)

def main(cam=0):

	cap = cv2.VideoCapture(cam)

	while cap.isOpened():

		_, frame = cap.read()
		WIDTH, HEIGHT, _ = frame.shape
		frame = cv2.resize(frame, (HEIGHT//2, WIDTH//2))

		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


		lower_red = np.array([0, 200, 200],  dtype=np.uint8)
		upper_red = np.array([20, 255, 255], dtype=np.uint8)

		lower_green = np.array([15, 120, 120],  dtype=np.uint8)
		upper_green = np.array([80, 255, 255], dtype=np.uint8)

		mask_red = cv2.inRange(hsv_frame, lower_red, upper_red)
		mask_green = cv2.inRange(hsv_frame, lower_green, upper_green)

		res_red = cv2.bitwise_and(frame, frame, mask=mask_red)

		circles = cv2.HoughCircles(cv2.cvtColor(res_red, cv2.COLOR_BGR2GRAY), cv2.HOUGH_GRADIENT, .8, 50, param1=20, param2=20) # .7, 100, 50, 50
		if circles is not None:

			circles = circles[0, :]
			circles_len = circles.shape[0]
			# print(circles.shape)
			circles = np.sort(circles, axis=0)
			print(circles)
			if circles_len > 25:
				circles = circles[(circles_len//2)-5:(circles_len//2)+5]
				circles = np.sum(circles, axis=0) / circles_len
			else:
				circles = np.sum(circles, axis=0) / circles_len
			# circles = circles[0]
			x, y, r = map(int, circles)
			cv2.circle(frame, (x, y), r, YELLOW, 3)
			cv2.circle(frame, (x, y), r+60, TERQUIZE, 3)


		cv2.imshow('res_red', res_red)
		cv2.imshow('frame', frame)

		if cv2.waitKey(25) & 0xFF == ord('q'):
			cap.release()
			cv2.destroyAllWindows()
			break

if __name__ == '__main__':
	main('land.mp4')
