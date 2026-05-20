### 介紹Agent / Slash / Hash command
### 介紹Model視窗、Copilot Usage視窗，Premium request
### 重新命名符號：程式人員最討厭的就是變數命名
### 切入AI進行中間作業
在程式碼選擇或游標處按Ctrl+I就可以直接Inline (打/doc寫註解)
Copilot就會透過上下文理解Code以後寫註解

### 再來就是我們故意把錯誤的Code寫進去
/fix 就會幫我們修正程式碼裡面的錯誤，幫我們提升程式碼的品質。
/review 就會幫我們檢查程式碼裡面的問題，並且幫我們修正程式碼裡面的缺陷，這樣就可以幫助我們提升程式碼的品質。
/refactor 就會幫我們重構程式碼的結構，幫我們提升程式碼的可讀性，維護性，還有可擴充性。

### 解釋程式碼
/explain 就會幫我們解釋程式碼的邏輯，幫助我們理解程式碼的邏輯，這樣就可以幫助我們提升程式碼的可讀性。
/tests 寫測試程式，如果完全不會寫測試程式的時候就可以用這種方式幫妳寫
/Plan 或是開發人員都很懶得寫文件，就可以透過Copilot來幫我們產專案文件
    EX：(點選BMI程式) 幫我為這一支計算BMI程式撰寫專案文件
但有一件很重要的事情需要再提醒一次，請Copilot幫我們寫文件，專案命名、函數命名、變數命名、方法命名要好
    EX：(點選BMI程式) 幫我撰寫規畫部署這一支BMI程式的部署文件
大致上會稍微說明這專案是甚麼App，先決條件是甚麼還有部署流程

### Github Pull Request寫註解
Csharp類別會蠻常用到，接Json格式用強行別來接就會用到
有一段CSharp的語法；就可以直接轉成LinQ的語法

### 程式語法的傳換，給Copilot一段CSharp程式碼改成Python程式碼
讓他幫我從C#轉乘Python程式碼
當然這是比較簡單的範例；轉起來就比較容易成功
但比較複雜的向參照一些特定的Library也是會幫你找，但結果可能沒有那麼完美
所以如果Code比較複雜；我們可能就會去思考是不是有定義不容易讓AI理解的地方

### 最後一段是我們俗稱的香腸式結構；如果有打電動的人比較常聽到波動拳結構
就是下了一堆判斷式讓程式碼很難閱讀，而且Code寫得很冗長只為了一件事情
這時候我們就可以請Copilot來幫我們重構程式碼結構 (輸入提示詞幫我重構)
我們也順便用比較好的模型來幫我們重構，就會看到他幫我們處理成減少巢狀的結構

### .github 貼上自訂義提示詞或規則
就可以將所有Copilot的行為自訂義所有的AI行為

### Agent mode最右邊有一個工具箱，這裡面就可以去自訂義MCP Server
例如我們今天安裝了Microsoft Learn的MCP，就可以在編碼的同時去查閱微軟的官方文件
---Demo Add Microsoft Learn MCP
---Demo Code reference
使用microsoft_docs_search找Azure 建立一個Resource Group的terraform寫法

### QA
Business & Enterprise由組織管理者去決定的
組織管理者也可以把預算額度關掉，可以決定把Premium request關掉 (統一)

### GitHub Copilot custome agent編寫範例
Basic agent vs Advanced agent vs Demo agent
- 「幫我寫一個 Python Flask REST API 範例」
- 「我們的 CI/CD pipeline YAML 怎麼寫？」

### Advanced agent會多一些安全規範的檢查
- tools：除了程式碼與文件，還加入 web 與 api，可呼叫外部 API (例如安全檢查服務)。
- knowledge：掛載多個文件，涵蓋 API、DevOps pipeline、公司安全規範。
- policies：定義合規性檢查，讓 Agent 在生成 IaC 或 API 範例時自動提醒安全規範。

API sample
- 提問：「建立一個 FastAPI endpoint，並檢查是否符合 API 命名規範」
- Agent → 生成程式碼 + 自動檢查規範

### 參考出處
- GitHub Copilot Log
- Copilot instructions

### Cloud Agent Lab
請幫我部署一個C#計算ＢＭＩ網站
Complete the task as described in the summary

### 三輪迭代
- create a login API using flask
- review code and check security compliance
- refactor code to reduce nested structure
- create a secure login API using flask
- use parameterized queries
- hash password using bcrypt
- prevent SQL injection

### Agent 協作
請新增 add(a, b) 函式，建立單元測試，執行安全掃描，並產出最終報告。