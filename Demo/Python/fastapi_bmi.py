# 由 GitHub Copilot 產生
# 建立一個 FastAPI endpoint，並檢查 API 命名規範
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import re

APP = FastAPI()

class BMI_REQUEST(BaseModel):
    HEIGHT: float
    WEIGHT: float

# API 命名規範：路徑必須為小寫、使用破折號分隔單字
API_PATH = '/bmi-calculate'

# 檢查 API 命名是否符合規範
if not re.match(r'^/[a-z0-9\-]+$', API_PATH):
    raise Exception('API 路徑命名不符合規範，請使用小寫及破折號分隔')

@APP.post(API_PATH)
async def CALCULATE_BMI(BODY: BMI_REQUEST):
    """計算 BMI 的 FastAPI Endpoint"""
    HEIGHT = BODY.HEIGHT
    WEIGHT = BODY.WEIGHT
    if HEIGHT <= 0 or WEIGHT <= 0:
        raise HTTPException(status_code=400, detail='HEIGHT 和 WEIGHT 必須大於 0')
    BMI = WEIGHT / ((HEIGHT / 100) ** 2)
    return { 'BMI': round(BMI, 2) }
