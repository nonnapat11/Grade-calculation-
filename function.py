def score():
    accumulated = float(input('ใส่คะแนนเก็บ: '))
    mid_score = float(input('ใส่คะแนนกลางภาค: '))
    last_score = float(input('ใส่คะแนนปลายภาค: '))
    self_score = float(input('ใส่คะแนนจิตพิสัย: '))

def calculation(accumulated,mid_score,last_score,self_score):
    total_score = accumulated+mid_score+last_score+self_score
    if total_score > 100:
        print('กรุณาลองใหม่อีกครั้ง')
    elif total_score >= 80 and total_score <= 100:
        print('A')
    elif total_score >= 75 and total_score <= 79:
        print('B+')
    elif total_score >= 70 and total_score <= 74:
        print('B')
    elif total_score >= 65 and total_score <= 69:
        print('C+')
    elif total_score >= 60 and total_score <= 64:
        print('C')
    elif total_score >= 55 and total_score <= 59:
        print('D+')
    elif total_score >= 50 and total_score <= 54:
        print('D')
    elif total_score >= 0 and total_score <= 49:
        print('F')
    else:
        print('กรุณาลองใหม่อีกครั้ง')

    print(total_score)