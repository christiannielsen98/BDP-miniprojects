import numpy as np


class OutlierEnv:
    def __init__(self):
        self.outliers = None
        self.answer = None

    def outlier_detection_step(self, sequence: list[float]) -> dict[int, bool]:
        """Given a list of numbers, return a dictionary with the indices of the outliers and a boolean value indicating whether they are
        outliers or not"""
        mean = np.mean(sequence)
        sd = np.std(sequence)
        
        self.outliers = {i: (abs(x - mean) > 3 * sd) for i, x in enumerate(sequence)}
    
    def step(self, action: str):
        """Given an action, perform the corresponding step"""
        
        if action.startswith("outlier_detection[") and action.endswith("]"):
            seq = action[len("outlier_detection["):-1]
            self.outlier_detection_step(sequence=seq)
        elif action.startswith("finish[") and action.endswith("]"):
            answer = action[len("finish["):-1]
            self.answer = answer
    
    def reset(self):
        self.outliers = None
        self.answer = None
