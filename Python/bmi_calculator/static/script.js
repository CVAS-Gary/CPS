// 由 GitHub Copilot 產生

// DOM 元素引用
const BMI_FORM = document.getElementById('bmiForm');
const HEIGHT_INPUT = document.getElementById('height');
const WEIGHT_INPUT = document.getElementById('weight');
const RESULT_SECTION = document.getElementById('resultSection');
const ERROR_SECTION = document.getElementById('errorSection');
const BMI_VALUE_DISPLAY = document.getElementById('bmiValue');
const CATEGORY_DISPLAY = document.getElementById('category');
const DESCRIPTION_DISPLAY = document.getElementById('description');
const ERROR_MESSAGE = document.getElementById('errorMessage');

// 表單提交事件監聽
BMI_FORM.addEventListener('submit', handleFormSubmit);

/**
 * 處理表單提交
 */
async function handleFormSubmit(EVENT) {
    EVENT.preventDefault();
    
    // 獲取輸入值
    const HEIGHT = parseFloat(HEIGHT_INPUT.value);
    const WEIGHT = parseFloat(WEIGHT_INPUT.value);
    
    // 基本驗證
    if (!isValidInput(HEIGHT, WEIGHT)) {
        showError('請輸入有效的身高和體重');
        return;
    }
    
    // 隱藏錯誤訊息
    ERROR_SECTION.style.display = 'none';
    
    try {
        // 發送API請求
        const RESPONSE = await fetch('/api/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                height: HEIGHT,
                weight: WEIGHT
            })
        });
        
        const RESULT_DATA = await RESPONSE.json();
        
        if (RESULT_DATA.success) {
            displayResult(RESULT_DATA);
        } else {
            showError(RESULT_DATA.error || '計算失敗，請檢查輸入');
        }
    } catch (ERROR) {
        showError('網路錯誤，請稍後再試');
        console.error('API錯誤:', ERROR);
    }
}

/**
 * 驗證輸入有效性
 */
function isValidInput(HEIGHT, WEIGHT) {
    // 檢查是否為數字
    if (isNaN(HEIGHT) || isNaN(WEIGHT)) {
        return false;
    }
    
    // 檢查值範圍
    if (HEIGHT < 50 || HEIGHT > 250) {
        return false;
    }
    
    if (WEIGHT < 20 || WEIGHT > 300) {
        return false;
    }
    
    return true;
}

/**
 * 顯示計算結果
 */
function displayResult(DATA) {
    // 更新結果顯示
    BMI_VALUE_DISPLAY.textContent = DATA.bmi;
    CATEGORY_DISPLAY.textContent = DATA.category;
    CATEGORY_DISPLAY.className = 'category ' + DATA.color;
    DESCRIPTION_DISPLAY.textContent = DATA.description;
    
    // 顯示結果區域
    RESULT_SECTION.style.display = 'block';
}

/**
 * 顯示錯誤訊息
 */
function showError(MESSAGE) {
    ERROR_MESSAGE.textContent = MESSAGE;
    ERROR_SECTION.style.display = 'block';
    RESULT_SECTION.style.display = 'none';
}
