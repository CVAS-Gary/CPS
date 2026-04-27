# 由 GitHub Copilot 產生
"""
BMI計算器單元測試
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

import pytest
from bmi import BMI_CALCULATOR, HEALTH_CLASSIFIER


class TestBMICalculator:
    """BMI計算器測試類別"""
    
    def test_normal_calculation(self):
        """測試正常BMI計算"""
        RESULT = BMI_CALCULATOR.calculate(170, 65)
        assert RESULT == 22.5
    
    def test_underweight(self):
        """測試低體重計算"""
        RESULT = BMI_CALCULATOR.calculate(180, 55)
        assert RESULT == 16.9
    
    def test_overweight(self):
        """測試過重計算"""
        RESULT = BMI_CALCULATOR.calculate(170, 75)
        assert RESULT == 25.9
    
    def test_invalid_height(self):
        """測試無效身高"""
        with pytest.raises(ValueError):
            BMI_CALCULATOR.calculate(0, 65)
    
    def test_invalid_weight(self):
        """測試無效體重"""
        with pytest.raises(ValueError):
            BMI_CALCULATOR.calculate(170, -10)
    
    def test_negative_inputs(self):
        """測試負數輸入"""
        with pytest.raises(ValueError):
            BMI_CALCULATOR.calculate(-170, 65)


class TestHealthClassifier:
    """健康分類器測試類別"""
    
    def test_underweight_classification(self):
        """測試低體重分類"""
        RESULT = HEALTH_CLASSIFIER.classify(17.5)
        assert RESULT['category'] == '低體重'
        assert RESULT['color'] == 'blue'
    
    def test_normal_classification(self):
        """測試正常體重分類"""
        RESULT = HEALTH_CLASSIFIER.classify(22.5)
        assert RESULT['category'] == '正常體重'
        assert RESULT['color'] == 'green'
    
    def test_overweight_classification(self):
        """測試過重分類"""
        RESULT = HEALTH_CLASSIFIER.classify(26.0)
        assert RESULT['category'] == '過重'
        assert RESULT['color'] == 'orange'
    
    def test_obese_classification(self):
        """測試肥胖分類"""
        RESULT = HEALTH_CLASSIFIER.classify(32.0)
        assert RESULT['category'] == '肥胖'
        assert RESULT['color'] == 'red'
    
    def test_boundary_18_5(self):
        """測試邊界值 18.5"""
        RESULT = HEALTH_CLASSIFIER.classify(18.5)
        assert RESULT['category'] == '正常體重'
    
    def test_boundary_24_9(self):
        """測試邊界值 24.9"""
        RESULT = HEALTH_CLASSIFIER.classify(24.9)
        assert RESULT['category'] == '正常體重'
    
    def test_boundary_29_9(self):
        """測試邊界值 29.9"""
        RESULT = HEALTH_CLASSIFIER.classify(29.9)
        assert RESULT['category'] == '過重'
