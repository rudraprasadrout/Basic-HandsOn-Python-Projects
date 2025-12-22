# Drink water remender app using python

import time
from plyer import notification

while True:
    print("Please drink some water!")
    notification.notify(title = "Please drink some Water",message = "You need to drink some water!",)
    time.sleep(60*60)