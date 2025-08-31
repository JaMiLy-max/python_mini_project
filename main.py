import student3
from feature import Data_Loader
from game_logic import GameLogic
from student3 import Student

# def main():

students = {
    1: Data_Loader.GameDataLoading(),
    2: Student(),
    3: GameLogic()
}

# while True:
#     command = int(input("작동 코드를 실행해주세요 : (0:종료/1~3:수강생 호출) ").strip())
#     if command == 0:
#         print("프로그램을 종료합니다.")
#         break
#     else:
#         students.get(command, lambda: print("잘못된 명령어입니다."))()

# 레벨, 파일로드 > 

# 1. 문제유형 질문
test = students[3].game_settting()
students[3].criteria_select = test

# 2. 그에 맞는 파일 가져오기
questions = students[1].get_all_questions()  # 이게 실제 문제 리스트
# all_data = students[1].get_all_data()        # 파일별 그룹화된 데이터 (사용하지 않음)
# processed = students[1].get_all_processed()

'''
files_list = test_list = [{"level" : "1", "questions" : "파이썬에서 특정 조건에 따라 코드 블록을 실행할 때 사용하는 키워드는 무엇인가요?", "choices" : "A) loop \nB) when \nC) if \nD) while", "answers" : "C", "explanations" : "if는 파이썬에서 조건을 검사하여 코드 실행 여부를 결정하는 조건문의 시작 키워드입니다."},
             {"level" : "3", "questions" : "다음 중 0부터 4까지의 숫자를 순서대로 출력하는 for 반복문 코드는 무엇인가요?", "choices" : "A) for i in range(5): print(i) \nB) for i in range(1, 5): print(i) \nC) for i from 0 to 4: print(i) \nD) for i in list(5): print(i)", "answers" : "A", "explanations" : "range(n) 함수는 0부터 n-1까지의 정수를 생성하므로, range(5)는 0, 1, 2, 3, 4를 생성합니다."},
             {"level" : "2", "questions" : "다음 while 반복문은 몇 번 \"반복\"을 출력하나요?\ncount = 0\nwhile count < 2:\n\tprint(\"반복\")\n\tcount += 1", "choices" : "A) 0번 \nB) 1번 \nC) 2번 \nD) 3번", "answers" : "C", "explanations" : "count가 0일 때, 1일 때 count < 2 조건이 참이 되어 총 두 번 \"반복\"을 출력합니다. count가 2가 되면 조건이 거짓이 되어 반복문이 종료됩니다."},
             {"level" : "2", "questions" : "다음 중 조건문 뒤에 반드시 와야 하는 기호는 무엇인가요?", "choices" : "A) . (마침표) \nB) ; (세미콜론) \nC) : (콜론) \nD) , (쉼표)", "answers" : "C", "explanations" : "파이썬에서는 if나 elif, else, for, while 문 뒤에 콜론(:)을 붙여 코드 블록의 시작을 알립니다."},
             {"level" : "2", "questions" : "다음 while 반복문은 몇 번 \"반복\"을 출력하나요?\ncount = 0\nwhile count < 2:\n\tprint(\"반복\")\n\tcount += 1", "choices" : "A) 0번 \nB) 1번 \nC) 2번 \nD) 3번", "answers" : "C", "explanations" : "count가 0일 때, 1일 때 count < 2 조건이 참이 되어 총 두 번 \"반복\"을 출력합니다. count가 2가 되면 조건이 거짓이 되어 반복문이 종료됩니다."},
             {"level" : "2", "questions" : "다음 중 조건문 뒤에 반드시 와야 하는 기호는 무엇인가요?", "choices" : "A) . (마침표) \nB) ; (세미콜론) \nC) : (콜론) \nD) , (쉼표)", "answers" : "C", "explanations" : "파이썬에서는 if나 elif, else, for, while 문 뒤에 콜론(:)을 붙여 코드 블록의 시작을 알립니다."},
             {"level" : "2", "questions" : "다음 while 반복문은 몇 번 \"반복\"을 출력하나요?\ncount = 0\nwhile count < 2:\n\tprint(\"반복\")\n\tcount += 1", "choices" : "A) 0번 \nB) 1번 \nC) 2번 \nD) 3번", "answers" : "C", "explanations" : "count가 0일 때, 1일 때 count < 2 조건이 참이 되어 총 두 번 \"반복\"을 출력합니다. count가 2가 되면 조건이 거짓이 되어 반복문이 종료됩니다."},
             {"level" : "2", "questions" : "다음 중 조건문 뒤ß에 반드시 와야 하는 기호는 무엇인가요?", "choices" : "A) . (마침표) \nB) ; (세미콜론) \nC) : (콜론) \nD) , (쉼표)", "answers" : "C", "explanations" : "파이썬에서는 if나 elif, else, for, while 문 뒤에 콜론(:)을 붙여 코드 블록의 시작을 알립니다."},
             {"level" : "3", "questions" : "다음 중 0부터 4까지의 숫자를 순서대로 출력하는 for 반복문 코드는 무엇인가요?", "choices" : "A) for i in range(5): print(i) \nB) for i in range(1, 5): print(i) \nC) for i from 0 to 4: print(i) \nD) for i in list(5): print(i)", "answers" : "A", "explanations" : "range(n) 함수는 0부터 n-1까지의 정수를 생성하므로, range(5)는 0, 1, 2, 3, 4를 생성합니다."},
             {"level" : "2", "questions" : "다음 while 반복문은 몇 번 \"반복\"을 출력하나요?\ncount = 0\nwhile count < 2:\n\tprint(\"반복\")\n\tcount += 1", "choices" : "A) 0번 \nB) 1번 \nC) 2번 \nD) 3번", "answers" : "C", "explanations" : "count가 0일 때, 1일 때 count < 2 조건이 참이 되어 총 두 번 \"반복\"을 출력합니다. count가 2가 되면 조건이 거짓이 되어 반복문이 종료됩니다."},
             {"level" : "2", "questions" : "다음 중 조건문 뒤에 반드시 와야 하는 기호는 무엇인가요?", "choices" : "A) . (마침표) \nB) ; (세미콜론) \nC) : (콜론) \nD) , (쉼표)", "answers" : "C", "explanations" : "파이썬에서는 if나 elif, else, for, while 문 뒤에 콜론(:)을 붙여 코드 블록의 시작을 알립니다."},
             {"level" : "2", "questions" : "다음 while 반복문은 몇 번 \"반복\"을 출력하나요?\ncount = 0\nwhile count < 2:\n\tprint(\"반복\")\n\tcount += 1", "choices" : "A) 0번 \nB) 1번 \nC) 2번 \nD) 3번", "answers" : "C", "explanations" : "count가 0일 때, 1일 때 count < 2 조건이 참이 되어 총 두 번 \"반복\"을 출력합니다. count가 2가 되면 조건이 거짓이 되어 반복문이 종료됩니다."},
             {"level" : "2", "questions" : "다음 중 조건문 뒤에 반드시 와야 하는 기호는 무엇인가요?", "choices" : "A) . (마침표) \nB) ; (세미콜론) \nC) : (콜론) \nD) , (쉼표)", "answers" : "C", "explanations" : "파이썬에서는 if나 elif, else, for, while 문 뒤에 콜론(:)을 붙여 코드 블록의 시작을 알립니다."},
             {"level" : "2", "questions" : "다음 while 반복문은 몇 번 \"반복\"을 출력하나요?\ncount = 0\nwhile count < 2:\n\tprint(\"반복\")\n\tcount += 1", "choices" : "A) 0번 \nB) 1번 \nC) 2번 \nD) 3번", "answers" : "C", "explanations" : "count가 0일 때, 1일 때 count < 2 조건이 참이 되어 총 두 번 \"반복\"을 출력합니다. count가 2가 되면 조건이 거짓이 되어 반복문이 종료됩니다."},
             {"level" : "2", "questions" : "다음 중 조건문 뒤에 반드시 와야 하는 기호는 무엇인가요?", "choices" : "A) . (마침표) \nB) ; (세미콜론) \nC) : (콜론) \nD) , (쉼표)", "answers" : "C", "explanations" : "파이썬에서는 if나 elif, else, for, while 문 뒤에 콜론(:)을 붙여 코드 블록의 시작을 알립니다."},
             {"level" : "3", "questions" : "다음 코드의 출력 결과는 무엇인가요?\na = 5; b = 3 \nif a > b: \n\tprint(\"a가 더 크다\") \nelse: \n\tprint(\"b가 더 크거나 같다\")", "choices" : "A) a가 더 크다 \nB) b가 더 크거나 같다 \nC) 오류 \nD) 아무것도 출력되지 않음", "answers" : "A", "explanations" : "a는 b보다 크므로 if 조건이 참이 되어 \"a가 더 크다\"가 출력됩니다."}]
'''

# 3. 문제 세팅
students[3].questions_criteria(questions)    # 전역변수 유지

# 4. while문에서의 문제 출제. correct_answer key 추가.
number = 0
while len(students[3].quiz_list) > number :
    # 문제와 정답을 return 받습니다.
    quiz_dict = students[3].show_quiz_input(number)
    # 문제를 체점합니다 (종료를 입력받으면 결과 return)
    students[2].show_left_life()
    students[2].scoring(quiz_dict)

    number += 1

