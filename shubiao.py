import pyautogui
count = int(input ("请输入:"))
currentMouseX, currentMouseY = pyautogui.position() # 鼠标当前位置
print(currentMouseX, currentMouseY)
while (count >= 0):
# 控制鼠标移动,duration为持续时间
 for i in range(2):
   pyautogui.moveTo(100, 100, duration=0.25) # 移动到 (100,100)
   pyautogui.moveTo(200, 100, duration=0.25)
   pyautogui.moveTo(200, 200, duration=0.25)
   pyautogui.moveTo(100, 200, duration=0.25)
 
 for i in range(2):
   pyautogui.moveRel(50, 0, duration=0.25) # 从当前位置右移100像素
   pyautogui.moveRel(0, 50, duration=0.25) # 向下
   pyautogui.moveRel(-50, 0, duration=0.25) # 向左
   pyautogui.moveRel(0, -50, duration=0.25) # 向上
   count = count - 1

print ('Good bye!')
 
