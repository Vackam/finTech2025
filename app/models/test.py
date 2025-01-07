# ./models/test.py

class TestModel:
    def __init__(self):
        self.test = "Test Connection of models"

    def predict(self, input_data: dict) -> str:
        result = f"{self.test}\nTestData:\n{input_data}"
        return result
