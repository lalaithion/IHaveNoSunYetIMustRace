import time
import datetime

import mss
import numpy as np
from PIL import Image
from PIL import ImageEnhance


def capture(info):
    with mss.mss() as sct:
        while True:
            array = np.array(sct.grab(info))
            yield array


def capture_processed(info, width=25, saturate=True, contrast=True, sharpen=True):
    height = int(width * info["height"] / info["width"])

    with mss.mss() as sct:
        while True:

            sct_img = sct.grab(info)

            # create image out of numpy array
            img = Image.new("RGB", sct_img.size)
            pixels = zip(sct_img.raw[2::4], sct_img.raw[1::4], sct_img.raw[0::4])
            img.putdata(list(pixels))

            # sharpen
            if sharpen:
                control = ImageEnhance.Sharpness(img)
                img = control.enhance(2.0)

            # downres
            img = img.resize((width, height))

            # increase saturation
            if saturate:
                control = ImageEnhance.Color(img)
                img = control.enhance(2.0)

            # increase contrast
            if contrast:
                control = ImageEnhance.Contrast(img)
                img = control.enhance(2.0)

            img.save("tmp/image_{}.png".format(datetime.datetime.now()))

            yield np.asarray(img, dtype=np.uint8)
