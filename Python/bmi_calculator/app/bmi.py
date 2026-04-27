# 由 GitHub Copilot 產生
"""
BMI計算模組
提供BMI計算和健康分類功能
"""


class BMI_CALCULATOR:
    """BMI計算器類別"""
    
    @staticmethod
    def calculate(HEIGHT_CM, WEIGHT_KG):
        """
        計算BMI值
        
        Args:
            HEIGHT_CM (float): 身高（公分）
            WEIGHT_KG (float): 體重（公斤）
            
        Returns:
            float: BMI值，四捨五入到小數點第一位
        """
        # 檢查輸入有效性
        if HEIGHT_CM <= 0 or WEIGHT_KG <= 0:
            raise ValueError("身高和體重必須大於0")
        
        # 將身高轉換為公尺
        HEIGHT_M = HEIGHT_CM / 100
        
        # 計算BMI = 體重(kg) / 身高(m)²
        BMI_VALUE = WEIGHT_KG / (HEIGHT_M ** 2)
        
        return round(BMI_VALUE, 1)


class HEALTH_CLASSIFIER:
    """健康分類器類別"""
    
    @staticmethod
    def classify(BMI_VALUE):
        """
        根據BMI值分類健康狀況
        
        Args:
            BMI_VALUE (float): BMI值
            
        Returns:
            dict: 包含分類和說明的字典
        """
        if BMI_VALUE < 18.5:
            return {
                "category": "低體重",
                "description": "體重過輕，建議增加營養攝取",
                "color": "blue"
            }
        elif 18.5 <= BMI_VALUE < 24.9:
            return {
                "category": "正常體重",
                "description": "體重正常，請保持健康生活方式",
                "color": "green"
            }
        elif 24.9 <= BMI_VALUE < 29.9:
            return {
                "category": "過重",
                "description": "體重超標，建議適度運動和飲食控制",
                "color": "orange"
            }
        else:
            return {
                "category": "肥胖",
                "description": "體重明顯超標，強烈建議就醫諮詢",
                "color": "red"
            }
