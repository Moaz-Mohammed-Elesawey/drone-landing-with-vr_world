from threading import Thread
import os


def run_script(world):
    if world == 'vr':
        os.system('python DroneLandVR.py')
    elif world == 'real':
        os.system('python DroneLandReal.py')

if __name__ == '__main__':
    vr_thread = Thread(target=run_script, args=['vr'])
    real_thread = Thread(target=run_script, args=['real'])

    vr_thread.start()
    real_thread.start()
