# ./models/insuarance_model

import numpy as np
import joblib
import os 
import random

class InsuranceModel:
    def __init__(self):
        self.model_path = os.path.join(os.path.dirname(__file__), '..', 'ml', 'insurance_model.joblib')
        self.model = None
        self.disease_dict = {
            0: "고혈압",         # DI1_dg
            1: "고지혈증",       # DI2_dg
            2: "당뇨병",         # DE1_dg
            3: "천식",           # DJ4_dg
            4: "아토피 피부염",   # DL1_dg
            5: "알레르기 비염",   # DJ8_dg
            6: "No-data",              # DJ6_dg
            7: "No-Data",              # DH4_dg
            8: "신부전"          # DN1_dg
        }
    
    def load_model(self):
        if self.model == None:
            try:
                self.model = joblib.load(self.model_path)
                return self.model
            except Exception as e:
                print(f"로드 실패: {e}")
                raise
        else:
            return self.model

    def predict(self, input_data: dict) -> str:
        '''
        머신 돌리기

        Args:
            input_data (dict): 예측에 필요한 입력 데이터 (UserInput.py 에서 진행)

        Returns: 
            예측 결과
        '''
        model = self.load_model()

        # TODO: 여기 적절히 수정할 것
        try:
            features = [
                    1, 2
                    ]

        except ValueError as ve:
            return f"입력 형식 오류: {ve}"

        prediction = model.predict([features])

        # take value where over 0.01
        filtered_index = np.where(prediction[0] >= 0.01)[0]
        # filtered_values = prediction[0][filtered_index]
        # result_dict = {index: value for index, value in zip(filtered_index, filtered_values)}

        result_string = "발생 위험 질병: "

        # filtered_index에 해당하는 질병명을 콤마로 구분된 문자열로 생성
        result_string = ", ".join(self.disease_dict[index] for index in filtered_index)

        return result_string

class IntegratedInsuranceModel:
    def __init__(self):
        self.models = self.load_models()
        self.disease_dict = {
            "DE1_dg": "당뇨병",
            "DI1_dg": "고혈압",
            "DI2_dg": "고지혈증",
            "DJ4_dg": "천식",
            "DJ6_dg": "부비동염",
            "DJ8_dg": "알레르기 비염",
            "DL1_dg": "아토피 피부염",
            "DH4_dg": "중이염",
            "DN1_dg": "신부전"
        }


    def load_models(self):
        model_path = os.path.join(os.path.dirname(__file__), '..', 'ml')
        model_files = [f for f in os.listdir(model_path) if f.endswith(".pkl")]
        models = {}
        for model_file in model_files:
            path = os.path.join(model_path, model_file)
            model = joblib.load(path)

            base_name = os.path.splitext(model_file)[0]
            models[base_name] = model
        return models

    def predict(self, X):
        predictions = [] 
        for key, model in self.models.items():
            prediction = model.predict(X)
            if prediction == 1:
                predictions.append(self.disease_dict[key])
            print(model.predict(X))
        return predictions

    def print_models(self):
        print (len(self.models))

if __name__ == "__main__":
    '''
    a = InsuranceModel()
    print(a.model_path)
    print(a.predict({'a': 1, 'b': 2}))
    '''

    test_b = IntegratedInsuranceModel()
    test_b.print_models()
    test_data = [random.uniform(0,1) for _ in range(26)]

    predictions = test_b.predict([test_data])
    print("prediction:")
    print(predictions)
