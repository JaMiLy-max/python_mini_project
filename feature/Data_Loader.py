# To do as a file loader: 
# 1. 파일 4개로 나눠서 가지고 오기 
# 2. 4지선다 콤마로 구분자 만들어서 보여주기(데이터 정리)

# pandas는 파이썬에서 가장 많이 쓰는 데이터 처리용 라이브러리(데이터 읽기, 정리, 분석 가능)
import pandas as pd 

# 클래스는 비슷한 기능을 가진 여러 객체를 쉽게 만들게 해줌 
# 객체들이 가져야 할 속성과 기능을 정의함 
# class GameDataLoading 은 게임문제 csv 파일을 읽어서 저장하는 기능이 들어 있는 클래스임 
class GameDataLoading:
    # init은 클래스 안에 없으면 안되는 함수. 생성자 함수. 객체가 생성될 때 초기 설정을 하는 역할을 함
    # 객체가 만들어질 때 필요한 초기 데이터를 받거나 설정 (이 코드에서는 file_paths)
    # 객체 내부에서 사용할 변수를 이 함수 안에서 만듦. 

    def __init__(self, file_paths): 
        
        # self의 file_paths라는 정보 안에 입력받은 file_paths 값을 저장한다는 뜻
        # 이 객체에서 필요한 파일 경로를 속성으로 저장. 
        self.file_paths = file_paths
        
        # 게임 데이터를 담을 빈 사전 자료구조 준비.
        # 나중에 파일 이름을 키로 읽은 데이터를 값으로 저장할 장소임. 
        self.data_files = {}

    def load_files(self):
        """
        CSV 파일들을 읽어서 메모리에 저장하는 메서드
        
        __init__에서 설정한 file_paths 리스트에 있는 모든 CSV 파일을
        pandas로 읽어서 self.data_files 딕셔너리에 저장함
        
        파일을 찾을 수 없거나 읽기 오류가 발생하면 에러 메시지 출력하고
        프로그램은 계속 실행됨
        
        반환값: 없음 (데이터는 self.data_files에 저장됨)
        """
        # file_paths 리스트 안의 각 파일 경로를 하나씩 순서대로 꺼내서 file 변수에 저장
        for file in self.file_paths:
            try:
                # pandas 라이브러리의 read_csv() 함수 활용 
                # 파일 경로에 있는 csv 파일을 읽어서 data_files 딕셔너리에 key는 파일 경로, value는 읽은 데이터를 저장 
                self.data_files[file] = pd.read_csv(file)
            except FileNotFoundError:
                print(f"파일을 찾을 수 없습니다: {file}")
            except Exception as e:
                print(f"파일 로드 중 오류 발생: {file} - {str(e)}")
   
    def get_data(self, file_name):
        """
        특정 파일의 전체 데이터를 가져오는 메서드
        
        file_name에 해당하는 CSV 파일의 모든 데이터를 pandas DataFrame 형태로 반환함
        
        매개변수:
            file_name (str): 가져올 파일의 이름 (예: 'questionfile1.csv')
        
        반환값:
            pandas.DataFrame 또는 None: 파일이 있으면 DataFrame, 없으면 None
        """
        # 딕셔너리의 .get()메서드 이용. 
        # 키가 file_name인 값을 가져오라는 뜻 
        # 만약에 없으면 None을 반환. 만약 딕셔너리에 없는 키를 꺼내려고 하면 오류가 발생할 수 있으므로 None을 반환해 달라고 해서 프로그램을 멈추지 않게 함. 
        return self.data_files.get(file_name, None)

    def get_data_by_column(self, file_name):
        """
        특정 파일의 데이터를 컬럼별로 분리해서 가져오는 메서드
        
        CSV 파일의 데이터를 5개의 컬럼(level, questions, choices, answers, explanations)으로
        나누어서 각각 반환함. 게임에서 문제를 하나씩 처리할 때 유용함
        
        매개변수:
            file_name (str): 가져올 파일의 이름 (예: 'questionfile1.csv')
        
        반환값:
            tuple: (levels, questions, choices, answers, explanations, success)
                - levels: 난이도 데이터 (pandas Series)
                - questions: 문제 데이터 (pandas Series)  
                - choices: 선택지 데이터 (pandas Series)
                - answers: 정답 데이터 (pandas Series)
                - explanations: 설명 데이터 (pandas Series 또는 None)
                - success: 성공 여부 (bool) - True: 성공, False: 실패
        """
        # data_files 에서 file_name에 해당하는 데이터를 꺼내옴.
        data = self.get_data(file_name)

        # 데이터가 없으면 경고 메시지를 출력하고 5개의 None 값과 실패 표시를 반환함(각 칼럼별) 
        if data is None: 
            print(f"{file_name}이 존재하지 않거나 로드하지 못했습니다.")

            # None이 5개인 이유는 값을 5개 반환하도록 설계되어 있기 때문 
            # 반환 값 개수를 맞춰서 가짜 값을 반환하는게 리턴의 컨벤션. 
            return None, None, None, None, None, False 
        
        # 칼럼며이 다를 수 있으므로 안전장치! 데이터에서 오는 모든 칼럼명을 모두 소문자로 처리하겠다는 뜻.
        # 공백도 제거
        data.columns = [col.lower().strip() for col in data.columns]

        try:

            # 네 개의 칼럼을 각각 꺼내 반환. 
            # explanation 컬럼이 있으면 포함, 없으면 None 반환 (단수형/복수형 모두 지원)
            explanation = data.get('explanations', data.get('explanation', None))
            # level과 levels 컬럼 모두 지원
            level_data = data.get('level', data.get('levels', None))
            return level_data, data['questions'], data['choices'], data['answers'], explanation, True
        
        except KeyError as e:

            # 오류가 날 때를 대비해서 언제나 error는 추가하는게 좋음
            print(f"{str(e)}가 {file_name}에 없습니다.")
            return None, None, None, None, None, False

    def get_all_data(self):
        """
        모든 파일의 데이터를 한번에 가져오는 메서드
        
        모든 CSV 파일의 데이터를 파일별로 구분해서 리스트로 반환함
        각 파일의 데이터는 딕셔너리 형태로 저장되고, pandas Series 형태의 원본 데이터를 그대로 유지함
        
        반환값:
            list: 파일별 데이터 딕셔너리들의 리스트
                각 딕셔너리에는 다음 키들이 포함됨:
                - file_name: 파일 이름
                - level: 난이도 데이터 (pandas Series)
                - questions: 문제 데이터 (pandas Series)
                - choices: 선택지 데이터 (pandas Series)
                - answers: 정답 데이터 (pandas Series)
                - explanations: 설명 데이터 (pandas Series 또는 None)
        """
        all_data = []
        
        for file in self.file_paths:
            levels, questions, choices, answers, explanations, success = self.get_data_by_column(file)
            
            if success:  # 데이터가 성공적으로 로드된 경우만
                unit_dict = {
                    'file_name': file,
                    'level': levels,
                    'questions': questions,
                    'choices': choices,
                    'answers': answers,
                    'explanations': explanations
                }
                all_data.append(unit_dict)
        
        return all_data

    def get_all_questions(self):
        """
        모든 문제를 하나의 리스트로 합쳐서 반환하는 메서드 (게임에서 가장 많이 사용)
        
        모든 CSV 파일의 문제들을 하나의 리스트로 합쳐서 반환함
        각 문제는 딕셔너리 형태로 저장되고, 게임에서 랜덤으로 문제를 출제할 때 가장 유용함
        
        반환값:
            list: 모든 문제 딕셔너리들의 리스트
                각 딕셔너리에는 다음 키들이 포함됨:
                - file_name: 문제가 있는 파일 이름
                - level: 난이도 (int)
                - question: 문제 내용 (str)
                - choices: 선택지 (str)
                - answers: 정답 (str)
                - explanations: 설명 (str 또는 None)
        
        사용 예시:
            all_questions = loader.get_all_questions()
            random_question = random.choice(all_questions)
            print(f"문제: {random_question['question']}")
        """
        all_questions = []
        
        for file in self.file_paths:
            levels, questions, choices, answers, explanations, success = self.get_data_by_column(file)
            
            if success:
                # pandas Series를 리스트로 변환하여 처리
                for i in range(len(levels)):
                    try:
                        question_dict = {
                            'file_name': file,
                            'level': levels.iloc[i] if hasattr(levels, 'iloc') else levels[i],
                            'question': questions.iloc[i] if hasattr(questions, 'iloc') else questions[i],
                            'choices': choices.iloc[i] if hasattr(choices, 'iloc') else choices[i],
                            'answers': answers.iloc[i] if hasattr(answers, 'iloc') else answers[i],
                            'explanations': explanations.iloc[i] if explanations is not None and hasattr(explanations, 'iloc') else (explanations[i] if explanations is not None else None)
                        }
                        all_questions.append(question_dict)
                    except IndexError:
                        print(f"데이터 인덱스 오류: {file}의 {i}번째 행")
                    except Exception as e:
                        print(f"데이터 처리 중 오류: {file}의 {i}번째 행 - {str(e)}")
        
        return all_questions 

file_paths = ['questionfile1.csv', 'questionfile2.csv', 'questionfile3.csv', 'questionfile4.csv']
loader = GameDataLoading(file_paths)
loader.load_files()

