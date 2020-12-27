import cv2
import numpy as np

'''
	# GREEN HSV VALUES (10:45, 40:255, 10:255), (65:255, 255, 255)
	# RED HSV VALUES (0, 30:255, 0:230), (0:45, 255, 255)
'''

YELLOW = (0,255,255)

def main(image_path):

	while True:

		frame = cv2.imread(image_path)
		frame = cv2.resize(frame, (300, 300))

		hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		lower_red = np.array([0, 100, 100],  dtype=np.uint8)
		upper_red = np.array([10, 255, 255], dtype=np.uint8)

		mask_red = cv2.inRange(hsv_frame, lower_red, upper_red)

		res_red = cv2.bitwise_and(frame, frame, mask=mask_red)

		circles = cv2.HoughCircles(cv2.cvtColor(res_red, cv2.COLOR_BGR2GRAY),
							cv2.HOUGH_GRADIENT, 8.5,70,minRadius=0,maxRadius=70)
		circles = np.round(circles[0, :]).astype("int")
		circles_len = len(circles)
		circles = np.sum(np.sort(circles, axis=0)[-circles_len//2:], axis=0)


		x, y, r = circles
		cv2.circle(frame, (x, y), r, YELLOW, 3)
		cv2.circle(frame, (x, y), r+90, YELLOW, 3)

		cv2.imshow('frame', frame)
		cv2.imshow('res_red', res_red)

		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

if __name__ == '__main__':
	main('land.jpg')
