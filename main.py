import pyautogui, time

position =pyautogui.position()
pesan = "Suruh Pulang Sal Korek Belom Mandi"
for a in range(50):
    pyautogui.click(position.x,position.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    time.sleep(0.5)
    pyautogui.typewrite(["enter"])