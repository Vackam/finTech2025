# ./models/insuarance_model

# TODO: 모델 들어오면 수정할 것

import joblib
import os 

class InsuranceModel:
    def __init__(self):
        self.model_path = '' # os.path.join(os.path.dir ... )
    
    def load_model(self):
        try:
            model = joblib.load(self.model_path)
            return model
        except Exception as e:
            print(f"로드 실패: {e}")
            raise

    def predict(self, input_data: dict) -> str:
        '''
        머신 돌리기

        Args:
            input_data (dict): 예측에 필요한 입력 데이터 (UserInput.py 에서 진행)

        Returns: 
            예측 결과
        '''
        # load model
        # TODO: 한 번만 불러오도록 수정
        model = self.load_model()

        try:
            features = [
                    # some feature
                    ]

        except ValueError as ve:
            return f"입력 형식 오류: {ve}"

        prediction = model.predict([features])
        return f"예측결과: {prediction[0]}"
