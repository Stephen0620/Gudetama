import subprocess
from datetime import datetime
import time


if __name__ == '__main__':
    WAIT_TIME = 10
    while True:
        current_secs = datetime.now().second
        if (current_secs + 2) % 60 == 0:
            print('Waiting')
            time.sleep(WAIT_TIME)
        subprocess.run(['adb', 'shell', 'input', 'touchscreen', 'tap', '223', '638'])