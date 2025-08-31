'''
# input 데이터
input_data = {
        "numbers" : 1,
        "level": "1",
        "question": "파이썬에서 특정 조건에 따라 코드 블록을 실행할 때 사용하는 키워드는 무엇인가요?",
        "options": "A) loop \nB) when \nC) if \nD) while",
        "answer": "C",
        "explanation": "if는 파이썬에서 조건을 검사하여 코드 실행 여부를 결정하는 조건문의 시작 키워드입니다.",
        "correct_answer" : "c"
    }
'''

''' 전역변수에 필요한 데이터
life = 5
score = 0
wrong_answer = []
'''

# 점수체크 함수
def scoring(data):
    # 전역변수 목숨, 점수, 오답리스트 사용한다고 선언
    global life,score,wrong_answer

    # 정답 체크 대소문자가 다를수도 있어서 대문자로 올리고 비교
    if data["answer"].upper() == data["correct_answer"].upper() :
        # 맞으면 점수 1점 상승
        score += 1
        # print(f'현재 점수는 {score}점 입니다.')
        return True
    
    else :
        # 틀리면 오답리스트에 문제 번호 추가
        wrong_answer.append({
            "question": data["question"],
            "answer": data["answer"],
            "explanation": data["explanation"],
            "correct_answer": data["correct_answer"]
        })

        # 목숨이 0보다 크면 목숨 1 감소
        if life > 0 :
            life -= 1
            return True
            # print(f'남은 목숨은 {life}개 입니다.')
        else :
            # 목숨이 0이 되면 끝나는 건데 여길 어떻게 처리해야 될 지 모르겠네요. 종료 키워드랑 같이 가야 할 것 같기도
            return False

# 오답노트 함수
def show_wrong_answer(wa):
    # 리스트로 받은 오답리스트 돌면서 출력
    for i , w in enumerate(wa,1):
        print(f"틀린 문제 {i}번 : {w['question']}")
        print(f"내 답: {w['answer']} / 정답: {w['correct_answer']}")
        print(f"설명: {w['explanation']}")



    


