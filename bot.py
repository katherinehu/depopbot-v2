import pyautogui, time

recentItem = (100,600)
buyNow = (361, 792)
address = (140,590)

order = [{'address': '6423 Tall Timbers Ct.', 'city':'Mason', 'zip':'45040'}]
time.sleep(3)
pyautogui.click(recentItem[0],recentItem[1])
time.sleep(3)
pyautogui.scroll(-150)
pyautogui.click(buyNow[0],buyNow[1])
pyautogui.click(address[0],address[1])

pyautogui.typewrite()
