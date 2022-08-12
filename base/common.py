import os
import time


def save_screenshot(app, file_name):
    filename = "outputs/test_" + file_name + ".png"
    output_path = os.path.join(os.path.dirname(__file__), filename)
    if not os.path.isdir(os.path.dirname(output_path)):
        os.mkdir(os.path.dirname(output_path))
    if os.path.isfile(output_path):
        os.remove(output_path)
    time.sleep(2)
    ret = app.screen_shot(output_path)

def delay(sec):
    time.sleep(sec)