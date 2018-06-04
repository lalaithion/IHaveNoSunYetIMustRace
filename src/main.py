import time

import screen

monitor = {"top": 51, "left": 758, "width": 640, "height": 480}


total_frames = 0
average_fps = 0
last_time = time.time()

for array in screen.capture_processed(
    monitor, saturate=False, contrast=False, sharpen=False
):

    print(array.shape)

    current_fps = 1 / (time.time() - last_time)
    average_fps = (average_fps * total_frames + current_fps) / (total_frames + 1)
    total_frames += 1
    print("fps: {0} {1}".format(average_fps, current_fps))
    last_time = time.time()
