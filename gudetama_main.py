import subprocess
from datetime import datetime

if __name__ == '__main__':
    while True:
        current_secs = datetime.now().second
        if current_secs % 60 == 0:
            print('drag and drop')
            # 680 ~ 805
            for height in range(670, 810, 30):
                subprocess.run(['adb', 'shell', 'input', 'touchscreen', 'draganddrop',
                                '478', str(height),
                                '0', str(height)])