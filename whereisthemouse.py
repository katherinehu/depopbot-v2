import pyautogui, time


print ("press Ctrl-C to quit")

while True:
    x, y = pyautogui.position()
    posStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
    print(posStr, end='')
    print('\b' * len(posStr), end='', flush=True)

