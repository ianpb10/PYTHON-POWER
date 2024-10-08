import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(2)

pyautogui.click(x=768, y=443)
pyautogui.write('ssilvaian2004@gmail.com')
pyautogui.press('tab')
pyautogui.write('password123')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(2)

table = pandas.read_csv("produtos.csv")

for x in table.index:
    cod = str(table.loc[x, 'codigo'])
    brand = str(table.loc[x, 'marca'])
    _type = str(table.loc[x, 'tipo'])
    category = str(table.loc[x, 'categoria'])
    price = str(table.loc[x, 'preco_unitario'])
    cost = str(table.loc[x, 'custo'])
    obs = str(table.loc[x, 'obs'])

    pyautogui.click(x=896, y=306)
    pyautogui.write(cod)
    pyautogui.press('tab')
    pyautogui.write(brand)
    pyautogui.press('tab')
    pyautogui.write(_type)
    pyautogui.press('tab')
    pyautogui.write(category)
    pyautogui.press('tab')
    pyautogui.write(price)
    pyautogui.press('tab')
    pyautogui.write(cost)
    pyautogui.press('tab')
    pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)


