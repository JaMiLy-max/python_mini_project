# To do as a file loader: 
# 1. 파일 4개로 나눠서 가지고 오기 
# 2. 4지선다 콤마로 구분자 만들어서 보여주기(데이터 정리)

# pandas는 파이썬에서 가장 많이 쓰는 데이터 처리용 라이브러리(데이터 읽기, 정리, 분석 가능)
import pandas as pd, re
class GameDataLoading:

    def __init__(self, file_paths=None): 
        self.file_paths = file_paths if file_paths else ['feature/questionfile1.csv', 'feature/questionfile2.csv', 'feature/questionfile3.csv', 'feature/questionfile4.csv']
        self.data_files = {}
        self.load_files()

    def load_files(self):
        for file in self.file_paths:
            try:
                data = pd.read_csv(file)
                data.columns = data.columns.str.strip()
                if 'levels' in data.columns:
                    data = data.rename(columns={'levels': 'level'})
                self.data_files[file] = data
            except FileNotFoundError:
                print(f"파일을 찾을 수 없습니다: {file}")
            except Exception as e:
                print(f"파일 로드 중 오류 발생: {file} - {str(e)}")
   
    def get_data(self, file_name):
        if file_name not in self.data_files:
            try:
                data = pd.read_csv(file_name, encoding='CP949') # DecodeError로 인한 설정 추가
                data.columns = data.columns.str.strip()
                if 'levels' in data.columns:
                    data = data.rename(columns={'levels': 'level'})
                self.data_files[file_name] = data
            except FileNotFoundError:
                print(f"파일을 찾을 수 없습니다: {file_name}")
                return None
            except Exception as e:
                print(f"파일 로드 중 오류 발생: {file_name} - {str(e)}")
                return None
        
        return self.data_files.get(file_name, None)

    def get_all_data(self):
        all_data = []
        
        for file in self.file_paths:
            data = self.get_data(file)
            if data is not None:
                file_dict = {
                    'file_name': file,
                    'data': data
                }
                all_data.append(file_dict)
        
        return all_data
    
    def get_all_questions(self, unit_select:str="0"):
        all_questions = []
        if unit_select != "0":         # 단원별 문제형성을 위한 분기
            file = re.sub('[0-9]', unit_select, self.file_paths[0])
            data = self.get_data(file)
            if data is not None:
                questions = data.to_dict('records')
                for question in questions:
                    question['file_name'] = file
                all_questions.extend(questions)
            
            return all_questions 
        else: 
            for file in self.file_paths:
                data = self.get_data(file)
                if data is not None:
                    questions = data.to_dict('records')
                    for question in questions:
                        question['file_name'] = file
                    all_questions.extend(questions)
            
            return all_questions 

    def get_all_processed(self):
        all_data = self.get_all_data()
        all_questions = self.get_all_questions()
        
        return {
            'all_data': all_data,
            'all_questions': all_questions
        }


loader = GameDataLoading()
# loader.load_files()
# result = loader.get_all_processed()
