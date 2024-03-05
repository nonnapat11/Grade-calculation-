def score(accumulated,mid_score,last_score,self_score):             #การสร้างฟังก์ชันชื่อ score

    total_score = accumulated+mid_score+last_score+self_score
    print()
    print(f'คะแนน: {total_score}')

    if total_score > 100:
        print('กรุณาลองใหม่อีกครั้ง')
    elif total_score >= 80 and total_score <= 100:
        print('เกรด: A')
    elif total_score >= 75 and total_score <= 79:
        print('เกรด: B+')
    elif total_score >= 70 and total_score <= 74:
        print('เกรด: B')
    elif total_score >= 65 and total_score <= 69:
        print('เกรด: C+')
    elif total_score >= 60 and total_score <= 64:
        print('เกรด: C')
    elif total_score >= 55 and total_score <= 59:
        print('เกรด: D+')
    elif total_score >= 50 and total_score <= 54:
        print('เกรด: D')
    elif total_score >= 0 and total_score <= 49:
        print('เกรด: F')
    else:
        print('กรุณาลองใหม่อีกครั้ง')

def ascii_art():                                                    #การสร้างฟังก์ชันชื่อ ascii_art
    print('''\
            
█▀▄▀█ ▄▀█ █▀▄ █▀▀   █▄▄ █▄█   █▀▄ █░░
█░▀░█ █▀█ █▄▀ ██▄   █▄█ ░█░   █▄▀ █▄▄

        ''')