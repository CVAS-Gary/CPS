// 由 GitHub Copilot 產生

/**
 * FizzBuzz 計算器 - 前端 JavaScript 邏輯
 * 
 * 此文件包含所有前端互動邏輯，包括：
 * - 單一數字計算
 * - 範圍計算
 * - 結果展示
 * - 統計資訊更新
 */

// DOM 元素引用
const SINGLE_INPUT = document.getElementById("single-number");
const SINGLE_BTN = document.getElementById("single-btn");
const SINGLE_RESULT = document.getElementById("single-result");

const RANGE_START_INPUT = document.getElementById("range-start");
const RANGE_END_INPUT = document.getElementById("range-end");
const RANGE_BTN = document.getElementById("range-btn");
const RANGE_RESULT = document.getElementById("range-result");

const FIZZ_COUNT_ELEM = document.getElementById("fizz-count");
const BUZZ_COUNT_ELEM = document.getElementById("buzz-count");
const FIZZBUZZ_COUNT_ELEM = document.getElementById("fizzbuzz-count");

/**
 * 監聽單一數字計算按鈕點擊事件
 */
SINGLE_BTN.addEventListener("click", handleSingleCalculation);

/**
 * 監聽 Enter 鍵在單一數字輸入框中的按下事件
 */
SINGLE_INPUT.addEventListener("keypress", (EVENT) => {
    if (EVENT.key === "Enter") {
        handleSingleCalculation();
    }
});

/**
 * 監聽範圍計算按鈕點擊事件
 */
RANGE_BTN.addEventListener("click", handleRangeCalculation);

/**
 * 監聽 Enter 鍵在範圍輸入框中的按下事件
 */
[RANGE_START_INPUT, RANGE_END_INPUT].forEach((INPUT) => {
    INPUT.addEventListener("keypress", (EVENT) => {
        if (EVENT.key === "Enter") {
            handleRangeCalculation();
        }
    });
});

/**
 * 處理單一數字計算
 * 
 * 過程:
 * 1. 獲取用戶輸入
 * 2. 驗證輸入
 * 3. 調用後端 API
 * 4. 展示結果
 */
async function handleSingleCalculation() {
    const INPUT_VALUE = SINGLE_INPUT.value.trim();

    // 驗證輸入不為空
    if (!INPUT_VALUE) {
        showError(SINGLE_RESULT, "請輸入一個數字");
        return;
    }

    const NUMBER = parseInt(INPUT_VALUE, 10);

    // 驗證輸入是合法的數字
    if (isNaN(NUMBER) || NUMBER < 1) {
        showError(SINGLE_RESULT, "請輸入一個正整數");
        return;
    }

    // 調用後端 API
    try {
        showLoading(SINGLE_RESULT);
        const RESPONSE = await fetch(`/api/fizzbuzz?number=${NUMBER}`);
        const DATA = await RESPONSE.json();

        if (DATA.success) {
            // 成功顯示結果
            displaySingleResult(DATA.result);
            updateStatsForSingle(DATA.result);
        } else {
            // 顯示 API 返回的錯誤
            showError(SINGLE_RESULT, DATA.error);
        }
    } catch (ERROR) {
        // 捕獲網路或其他錯誤
        showError(SINGLE_RESULT, `網路錯誤: ${ERROR.message}`);
    }
}

/**
 * 處理範圍計算
 * 
 * 過程:
 * 1. 獲取用戶輸入
 * 2. 驗證輸入
 * 3. 調用後端 API
 * 4. 展示結果和統計
 */
async function handleRangeCalculation() {
    const START_VALUE = RANGE_START_INPUT.value.trim();
    const END_VALUE = RANGE_END_INPUT.value.trim();

    // 驗證輸入不為空
    if (!START_VALUE || !END_VALUE) {
        showError(RANGE_RESULT, "請輸入開始和結束數字");
        return;
    }

    const START_NUMBER = parseInt(START_VALUE, 10);
    const END_NUMBER = parseInt(END_VALUE, 10);

    // 驗證輸入是合法的數字
    if (isNaN(START_NUMBER) || isNaN(END_NUMBER)) {
        showError(RANGE_RESULT, "開始和結束都必須是正整數");
        return;
    }

    if (START_NUMBER < 1 || END_NUMBER < 1) {
        showError(RANGE_RESULT, "數字必須為正整數");
        return;
    }

    if (START_NUMBER > END_NUMBER) {
        showError(RANGE_RESULT, "開始數字不能大於結束數字");
        return;
    }

    // 調用後端 API
    try {
        showLoading(RANGE_RESULT);
        const RESPONSE = await fetch(
            `/api/fizzbuzz?start=${START_NUMBER}&end=${END_NUMBER}`
        );
        const DATA = await RESPONSE.json();

        if (DATA.success) {
            // 成功顯示結果
            displayRangeResult(DATA.result);
            updateStatsForRange(DATA.result);
        } else {
            // 顯示 API 返回的錯誤
            showError(RANGE_RESULT, DATA.error);
        }
    } catch (ERROR) {
        // 捕獲網路或其他錯誤
        showError(RANGE_RESULT, `網路錯誤: ${ERROR.message}`);
    }
}

/**
 * 展示單一數字的計算結果
 * 
 * @param {string} RESULT - FizzBuzz 計算結果
 */
function displaySingleResult(RESULT) {
    SINGLE_RESULT.classList.add("active");
    SINGLE_RESULT.innerHTML = `
        <div class="result-content">
            <div class="result-title">計算結果:</div>
            <div style="font-size: 2rem; color: #667eea; font-weight: bold;">
                ${RESULT}
            </div>
        </div>
    `;
}

/**
 * 展示範圍計算的結果
 * 
 * @param {array} RESULTS - FizzBuzz 計算結果數組
 */
function displayRangeResult(RESULTS) {
    const ITEMS_HTML = RESULTS.map((ITEM) => {
        let CSS_CLASS = "";
        if (ITEM === "Fizz") {
            CSS_CLASS = "fizz";
        } else if (ITEM === "Buzz") {
            CSS_CLASS = "buzz";
        } else if (ITEM === "FizzBuzz") {
            CSS_CLASS = "fizzbuzz";
        }

        return `<div class="result-item ${CSS_CLASS}">${ITEM}</div>`;
    }).join("");

    RANGE_RESULT.classList.add("active");
    RANGE_RESULT.innerHTML = `
        <div class="result-content">
            <div class="result-title">計算結果 (共 ${RESULTS.length} 個數字):</div>
            <div class="result-items">${ITEMS_HTML}</div>
        </div>
    `;
}

/**
 * 更新單一數字計算後的統計信息
 * 
 * @param {string} RESULT - FizzBuzz 計算結果
 */
function updateStatsForSingle(RESULT) {
    // 重置統計
    FIZZ_COUNT_ELEM.textContent = "0";
    BUZZ_COUNT_ELEM.textContent = "0";
    FIZZBUZZ_COUNT_ELEM.textContent = "0";

    // 根據結果更新相應的計數
    if (RESULT === "Fizz") {
        FIZZ_COUNT_ELEM.textContent = "1";
    } else if (RESULT === "Buzz") {
        BUZZ_COUNT_ELEM.textContent = "1";
    } else if (RESULT === "FizzBuzz") {
        FIZZBUZZ_COUNT_ELEM.textContent = "1";
    }
}

/**
 * 更新範圍計算後的統計信息
 * 
 * @param {array} RESULTS - FizzBuzz 計算結果數組
 */
function updateStatsForRange(RESULTS) {
    // 初始化計數變量
    let FIZZ_COUNT = 0;
    let BUZZ_COUNT = 0;
    let FIZZBUZZ_COUNT = 0;

    // 遍歷結果，計算各類型的出現次數
    RESULTS.forEach((ITEM) => {
        if (ITEM === "Fizz") {
            FIZZ_COUNT++;
        } else if (ITEM === "Buzz") {
            BUZZ_COUNT++;
        } else if (ITEM === "FizzBuzz") {
            FIZZBUZZ_COUNT++;
        }
    });

    // 更新 DOM 中的統計信息
    FIZZ_COUNT_ELEM.textContent = FIZZ_COUNT;
    BUZZ_COUNT_ELEM.textContent = BUZZ_COUNT;
    FIZZBUZZ_COUNT_ELEM.textContent = FIZZBUZZ_COUNT;
}

/**
 * 展示錯誤信息
 * 
 * @param {HTMLElement} ELEMENT - 目標 DOM 元素
 * @param {string} MESSAGE - 錯誤信息文本
 */
function showError(ELEMENT, MESSAGE) {
    ELEMENT.classList.add("active");
    ELEMENT.innerHTML = `<div class="error">❌ ${MESSAGE}</div>`;
}

/**
 * 展示載入狀態
 * 
 * @param {HTMLElement} ELEMENT - 目標 DOM 元素
 */
function showLoading(ELEMENT) {
    ELEMENT.classList.add("active");
    ELEMENT.innerHTML = `<div class="result-content">正在計算中 <span class="loading">⏳</span></div>`;
}
