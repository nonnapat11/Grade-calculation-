from function import score
import os
import time

try:
    time.sleep(0.3)
    accumulated = float(input('ใส่คะแนนเก็บ: '))
    time.sleep(0.3)
    mid_score = float(input('ใส่คะแนนกลางภาค: '))
    time.sleep(0.3)
    last_score = float(input('ใส่คะแนนปลายภาค: '))
    time.sleep(0.3)
    self_score = float(input('ใส่คะแนนจิตพิสัย: '))
    time.sleep(0.3)
except:
    print('กรุณาลองใหม่อีกครั้ง และกรอกเป็นตัวเลขเท่านั้น!!!')

os.system('cls')
time.sleep(0.5)
score(accumulated,mid_score,last_score,self_score)