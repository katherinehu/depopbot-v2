import pyautogui, time
import findPrice

recentItem = (100,600)
buyNow = (361, 792)
address = (140,590)

order = [{'address': 'blahblah',
          'city':'Mason',
          'zip':'45040',
          'phone':'5133834483'}]
time.sleep(3)
pyautogui.click(recentItem[0],recentItem[1])
time.sleep(1)
pyautogui.scroll(-150)

# @clairehucodes: get url using urllib.request
findPrice("https://www.depop.com/products/kaylakosuga-everything-posted-is-new-or-41/")

# @clairehucodes: if price more than...
pyautogui.click(buyNow[0],buyNow[1])
pyautogui.click(address[0],address[1])




'''
pyautogui.typewrite(order['address'] + '\t')
pyautogui.typewrite(order['city'] + '\t')
#states
pyautogui.typewrite(order['zip'] + '\t'+ '\t'+'\t')
pyautogui.typewrite(order['phone'] + '\t')
'''

