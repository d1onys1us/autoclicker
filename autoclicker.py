from pynput.mouse import Button, Controller
import time, random

mouse = Controller()
rng = random.SystemRandom()

# Autoclicker
def auto_click():
    num_clicks = 0
    while (True):
        random_hold, random_between = rng.uniform(0, 0.2), rng.random()

        mouse.press(Button.left)   # left click press
        print("Time holding: " + str(random_hold))
        time.sleep(random_hold)    # sleep
        mouse.release(Button.left) # left click release
        print("Time between: " + str(random_between))
        time.sleep(random_between) # sleep

        num_clicks += 1
        print("Clicks: " + str(num_clicks))

# Execution
auto_click()