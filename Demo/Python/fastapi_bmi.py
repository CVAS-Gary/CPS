# 由 GitHub Copilot 產生
# 建立一個 FastAPI endpoint，並檢查 API 命名規範
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import re

app = FastAPI()

class BmiRequest(BaseModel):
    height: float
    weight: float

# API 命名規範：路徑必須為小寫、使用破折號分隔單字
API_PATH = '/bmi-calculate'

# 檢查 API 命名是否符合規範
if not re.match(r'^/[a-z0-9\-]+$', API_PATH):
    raise Exception('API 路徑命名不符合規範，請使用小寫及破折號分隔')

@app.post(API_PATH)
async def calculate_bmi(body: BmiRequest):
    """計算 BMI 的 FastAPI Endpoint"""
    height_cm = body.height
    weight_kg = body.weight
    if height_cm <= 0 or weight_kg <= 0:
        raise HTTPException(status_code=400, detail='height 和 weight 必須大於 0')
    bmi = weight_kg / ((height_cm / 100) ** 2)
    return {'bmi': round(bmi, 2)}
