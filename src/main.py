import time

import screen

monitor = {"top": 172, "left": 822, "width": 505, "height": 280}


total_frames = 0
average_fps = 0
last_time = time.time()

for array in screen.capture_processed(monitor):

    print(array.shape)

    current_fps = 1 / (time.time() - last_time)
    average_fps = (average_fps * total_frames + current_fps) / (total_frames + 1)
    total_frames += 1
    print("fps: {0} {1}".format(average_fps, current_fps))
    last_time = time.time()
