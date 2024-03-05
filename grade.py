from function import score
from function import ascii_art
import time

ascii_art()

try:
    accumulated = float(input('ใส่คะแนนเก็บ: '))
    time.sleep(0.3)
    mid_score = float(input('ใส่คะแนนกลางภาค: '))
    time.sleep(0.3)
    last_score = float(input('ใส่คะแนนปลายภาค: '))
    time.sleep(0.3)
    self_score = float(input('ใส่คะแนนจิตพิสัย: '))
    time.sleep(0.3)
except:
    time.sleep(0.5)
    print('กรุณาลองใหม่อีกครั้ง และกรอกเป็นตัวเลขเท่านั้น!!!')
else:
    time.sleep(0.5)
    score(accumulated,mid_score,last_score,self_score)
