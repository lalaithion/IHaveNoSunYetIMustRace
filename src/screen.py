import time
import datetime

import mss
import numpy as np


def capture(info):
    with mss.mss() as sct:
        while True:
            array = np.array(sct.grab(info))
            yield array
