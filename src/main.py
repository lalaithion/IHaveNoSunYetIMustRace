import time

import pyautogui
import numpy as np

import screen


def main():
    time.sleep(2)

    monitor = {"top": 250, "left": 830, "width": 500, "height": 130}

    total_frames = 0
    average_fps = 0
    last_time = time.time()

    current_key = "left"

    for array in screen.capture_processed(monitor):
        pyautogui.keyUp(current_key)

        lsum = np.mean(array[:, :8, :])
        rsum = np.mean(array[:, -8:, :])
        msum = np.mean(array[:, 6:-6, :])

        open = min(lsum, rsum, msum)

        if open == rsum:
            current_key = "right"
        elif open == lsum:
            current_key = "left"

        print(current_key)

        pyautogui.keyDown(current_key)
        # do stuff here


main()
