from function import score                      #การเรียกใช้ฟังก์ชันจากอีกไฟล์
from function import ascii_art                  #การเรียกใช้ฟังก์ชันจากอีกไฟล์
import time                                     #การเรียกใช้ฟังก์ชัน time ของ python เพื่อจะเอามาทำ delay
ascii_art()

try:                                                      #การดัก Error ขึ้นต้นด้วย Try,except,else
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
