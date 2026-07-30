students = [
    {
        '이름' : '김싸피',
        '국어' : 80,
        '영어' : 95,
        '수학' : 85
    },
    {
        '이름' : '이싸피',
        '국어' : 95,
        '영어' : 95,
        '수학' : 70
    },
    {
        '이름' : '박싸피',
        '국어' : 100,
        '영어' : 80,
        '수학' : 60
    },
    {
        '이름' : '최싸피',
        '국어' : 75,
        '영어' : 100,
        '수학' : 55
    },
]


# 모든 학생들의 평균 점수를 '이름 : 점수' 형태로 출력하세요

for student in students:
    이름 = student['이름']
    total = 0

    for subject in ['국어','영어','수학']:
        total += student[subject]

    avg = total / 3
    print(f"{'이름'} : {avg}")

# 각 과목별 총점을 '과목명 : 점수' 형태로 출력하세요
"""
국어총점 = 0
영어총점 = 0
수학총점 = 0
for student in students:
    국어총점 += student['국어']
    영어총점 += student['영어']
    수학총점 += student['수학']
print(f'국어 : {국어총점}')
print(f'영어 : {영어총점}')
print(f'수학 : {수학총점}')
"""
for subject in ['국어', '영어', '수학']:
    total = sum(student[subject] for student in students)
    print(f'{subject} : {total}')

# 각 과목별 최고을 받은 학생의 이름을 '과목 : 이름' 형태로 출력하세요

for subject in ['국어', '영어', '수학']:
    best_score = max(student[subject] for student in students)

    for student in students:
        if student[subject] == best_score:
            print(f'{subject} : {student["이름"]}')

# 각 과목별 평균 점수를 '과목명 : 점수' 형태로 출력하세요

for subject in ['국어', '영어', '수학']:
    total = sum(student[subject] for student in students)
    print(f'{subject} : {total / len(students)}')