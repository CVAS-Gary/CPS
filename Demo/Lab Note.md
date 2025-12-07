### 介紹Agent / Slash / Hash command
### 介紹Model視窗、Copilot Usage視窗，Premium request
---額度不夠的話就要另外付費
---Bing search演示 python版本 & WBC (以前會說這個根開發無關)
---Agent可以幫你把整體每一個階段的修改工作完善
---Ask 一般下prompt跟Service對話就是這一個服務
---Edit通常是多檔案編輯處理
---Code reference 這段Code是否有參照到Github
---問完之後我們就可以透過引用提示將code引用進去

### 重新命名符號：程式人員最討厭的就是變數命名，我們就可以透過Copilot建議
前面有這個符號就是AI建議的，從命名就可以判斷AI是不是知道你的意圖了
如果妳都不是很滿意；就可以再按一下產生更多建議
### 另外一種命名方式是，當我今天變數一樣是aaa
他就會幫我辨識意圖會看到這邊就變成bmi，因為我這一支程式是來判斷BMI是否超標
透過這兩個Demo來辨識開發者的意圖跟上下文的判斷
這是跟命名有關的
再來就是Ctrl+I就可以直接Inline透過/doc寫註解
Copilot就會透過上下文理解Code以後幫妳寫註解

### 再來就是我們故意把錯誤的Code寫進去以後
在Chat裡面寫幫我修改這一段Code，他修正上就會看到Add把-改成+
所以這邊還是要重申一下我們平常基本功在練的時候一些基本函示或變數在命名時
還是要養成良好的習慣讓AI更容易上手的去幫你做出正確的事和正確的判斷
明明是加法寫減法，或是行為命名不明確，就會讓AI想幫你也沒有辦法

### 解釋程式碼
/tests寫測試程式，殂果完全不會寫測試程式的時候就可以用這種方式幫妳寫
或是開發人員都很懶得寫測試文件，就可以透過Copilot來幫我們產專案文件
他就會幫我寫一份Markdown格式的專案文件
但有一件很重要的事情需要再提醒一次，請Copilot幫我們寫文件，
專案命名、函數命名、變數命名、方法命名要好
部署文件；看起來這個式comman的console app，web應該就是另外一種形式
大致上會稍微說明這專案是甚麼App，先決條件是甚麼；

### Github Pull Request寫註解
Csharp類別會蠻常用到，接Json格式用強行別來接就會用到
有一段CSharp的語法；就可以直接轉成LinQ的語法

### 程式語法的傳換，給Copilot一段CSharp程式碼
讓他幫我從C#轉乘Python程式碼
當然這是比較簡單的範例；轉起來就比較容易成功
但比較複雜的向參照一些特定的Library也是會幫你找，但結果可能沒有那麼完美
所以如果Code比較複雜；我們可能就會去思考是不是沒有定義清楚的地方不容易讓AI理解

### 直接打Code review就會幫你檢查程式碼有那些問題，
用一樣的方式幫你解決程式碼裡面的缺陷
全選程式碼後按右鍵，可以看到產生程式碼中，一樣可以選擇fix、review、gen file或gen test

### 最後一段是我們俗稱的香腸式結構；如果有打電動的人比較常聽到波動拳結構
就是下了一堆判斷式讓程式碼很難閱讀，而且Code寫得很冗長只為了一件事情
這時候我們就可以請Copilot來幫我們重構程式碼結構 (輸入提示詞幫我重構)
我們也順便用比較好的模型來幫我們重構，就會看到他幫我們處理成減少巢狀的結構

### Github上面的Copilot
左下角是歷史紀錄的訊息，中間可以加入REPO來回答你的存放庫所有的問題
SPARK是一種類似輸入提示詞他就會幫你Create一個webapp的功能

### .github 貼上自訂義提示詞或規則
就可以將所有Copilot的行為自訂義所有的AI行為

### Agent mode最右邊有一個工具箱，這裡面就可以去自訂義MCP Server
例如我們今天安裝了Microsoft Learn的MCP，就可以在編碼的同時去查閱微軟的官方文件

### Demo Microsoft Learn MCP
### Demo Code reference
使用microsoft_docs_search找Azure 建立一個Resource Group的terraform寫法

### QA
Business & Enterprise由組織管理者去決定的
組織管理者也可以把預算額度關掉，可以決定把Premiume request關掉 (統一)

### GitHub Copilot custome agent編寫範例
Basuc agent vs Advanced agent vs Demo agent
- 「幫我寫一個 Python Flask REST API 範例」
- 「我們的 CI/CD pipeline YAML 怎麼寫？」



### Advanced agent會多一些安全規範的檢查
- tools：除了程式碼與文件，還加入 web 與 api，可呼叫外部 API (例如安全檢查服務)。
- knowledge：掛載多個文件，涵蓋 API、DevOps pipeline、公司安全規範。
- policies：定義合規性檢查，讓 Agent 在生成 IaC 或 API 範例時自動提醒安全規範。

API sample
- 提問：「建立一個 FastAPI endpoint，並檢查是否符合 API 命名規範」
- Agent → 生成程式碼 + 自動檢查規範

