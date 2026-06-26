---
theme: viewsonic-proav
background: https://cover.sli.dev
title: Excel + AI 工作坊 — 學員手冊
info: |
  ## 用 AI 轉換您的 Excel 報表，不需要任何程式基礎
class: text-center
drawings:
  persist: false
transition: slide-left
comark: true
duration: 60min
---

# Excel + AI 工作坊

### 學員手冊

<LastModifiedDate />

---

# 今日議程

<div class="mt-8 grid grid-cols-4 gap-4 text-center">
  <div class="bg-orange-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-orange-500">10 分鐘</div>
    <div class="mt-2 font-bold text-gray-800">背景介紹</div>
    <div class="text-sm mt-1 text-gray-700">為什麼要用 AI + Excel？今天要做什麼</div>
  </div>
  <div class="bg-blue-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-blue-500">20 分鐘</div>
    <div class="mt-2 font-bold text-gray-800">現場示範</div>
    <div class="text-sm mt-1 text-gray-700">觀看完整流程：從提示詞到輸出結果</div>
  </div>
  <div class="bg-green-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-green-500">25 分鐘</div>
    <div class="mt-2 font-bold text-gray-800">動手實作</div>
    <div class="text-sm mt-1 text-gray-700">自己輸入提示詞，取得 AI 輸出</div>
  </div>
  <div class="bg-purple-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-purple-500">5 分鐘</div>
    <div class="mt-2 font-bold text-gray-800">問與答</div>
    <div class="text-sm mt-1 text-gray-700">提問、重點整理、後續步驟</div>
  </div>
</div>

---
layout: cards
cols: 2
cards:
  - title: Simon Wen
    text: 我用 AI 自動化 Excel 工作流程，讓團隊花幾分鐘而非幾小時完成報表。我負責建立流程架構，AI 負責撰寫程式碼。
    tags: [simon.ch.wen@viewsonic.com]
  - image: /images/simon.wen.github.jpeg
---

# 關於講師

---

# 方法一：如果您只需要從一個 Excel 檔案快速取得答案？

<div class="mt-6 grid grid-cols-2 gap-8">
  <div class="space-y-4">
    <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
      <div class="font-bold text-gray-800 mb-2">您要做的事</div>
      <ul class="text-gray-700 space-y-2 text-sm">
        <li>📎 直接將檔案上傳至 ChatGPT 或 Claude</li>
        <li>💬 用日常語言描述您想要的結果</li>
        <li>📊 立即取得摘要、圖表或公式</li>
      </ul>
    </div>
    <div class="bg-green-50 border border-green-200 rounded-xl p-5">
      <div class="font-bold text-gray-800 mb-2">適合情境</div>
      <ul class="text-gray-700 space-y-2 text-sm">
        <li>✅ 臨時性問題與快速分析</li>
        <li>✅ 非機密資料</li>
        <li>✅ 免設定，幾秒內即可開始</li>
      </ul>
    </div>
  </div>
  <div class="bg-orange-50 border border-orange-200 rounded-xl p-5">
    <div class="font-bold text-gray-800 mb-3">注意事項</div>
    <ul class="text-gray-700 space-y-3 text-sm">
      <li>⚠️ 您的檔案會上傳至 AI 服務商的伺服器</li>
      <li>⚠️ 不適合機密或客戶資料</li>
      <li>⚠️ 每次都需要手動重複操作</li>
    </ul>
    <div class="mt-6 pt-4 border-t border-orange-200 text-sm text-gray-600 italic">
      很好的起點，但資料敏感或任務需重複時有所限制。
    </div>
  </div>
</div>

---

# 方法二：如果您的團隊已經在使用 Microsoft 365？

<div class="mt-6 grid grid-cols-2 gap-8">
  <div class="space-y-4">
    <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
      <div class="font-bold text-gray-800 mb-2">您要做的事</div>
      <ul class="text-gray-700 space-y-2 text-sm">
        <li>🖱️ 開啟 Excel Online 或 Teams</li>
        <li>💬 請 Copilot 合併、樞紐或摘要資料</li>
        <li>📈 結果直接顯示在您的試算表中</li>
      </ul>
    </div>
    <div class="bg-green-50 border border-green-200 rounded-xl p-5">
      <div class="font-bold text-gray-800 mb-2">適合情境</div>
      <ul class="text-gray-700 space-y-2 text-sm">
        <li>✅ 團隊共用檔案的協作報表</li>
        <li>✅ 資料已在 Microsoft 365 環境中</li>
        <li>✅ 無需額外工具或安裝</li>
      </ul>
    </div>
  </div>
  <div class="bg-orange-50 border border-orange-200 rounded-xl p-5">
    <div class="font-bold text-gray-800 mb-3">注意事項</div>
    <ul class="text-gray-700 space-y-3 text-sm">
      <li>⚠️ 需要付費授權（約 $30 美元／人／月）</li>
      <li>⚠️ 資料存放於 Microsoft 雲端，請確認公司政策</li>
      <li>⚠️ 僅限 Microsoft 365 內的檔案</li>
    </ul>
    <div class="mt-6 pt-4 border-t border-orange-200 text-sm text-gray-600 italic">
      對 Microsoft 用戶很強大，但費用和政策審核可能是障礙。
    </div>
  </div>
</div>

---

# 方法三：如果您有大量檔案、機密資料，或每月需要相同的報表？

<div class="mb-4 bg-indigo-50 border border-indigo-300 rounded-xl px-5 py-3 flex items-center gap-3 text-sm">
  <div class="text-xl">✅</div>
  <div><span class="font-bold text-indigo-700">今日前提假設：</span> <span class="text-gray-800">您已成功設定好 AI Agent 工具（例如 Claude、Codex 等），並能夠正常送出提示詞。</span></div>
</div>

<div class="mt-2 grid grid-cols-2 gap-8">
  <div class="space-y-4">
    <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
      <div class="font-bold text-gray-800 mb-2">您要做的事</div>
      <ul class="text-gray-700 space-y-2 text-sm">
        <li>💬 向 AI 描述您的 Excel 結構</li>
        <li>🤖 AI 撰寫 Python 程式，您貼上並執行</li>
        <li>▶️ 程式在本機執行，幾秒內輸出結果</li>
      </ul>
    </div>
    <div class="bg-green-50 border border-green-200 rounded-xl p-5">
      <div class="font-bold text-gray-800 mb-2">適合情境</div>
      <ul class="text-gray-700 space-y-2 text-sm">
        <li>✅ 機密或內部資料，不離開您的電腦</li>
        <li>✅ 一次處理大量檔案</li>
        <li>✅ 每月重複報表，一個指令搞定</li>
      </ul>
    </div>
  </div>
  <div class="bg-green-50 border border-green-200 rounded-xl p-5 flex flex-col justify-center">
    <div class="text-4xl text-center mb-4">🎯</div>
    <div class="font-bold text-gray-800 text-center mb-2">這就是今天工作坊的主題</div>
    <div class="text-sm text-gray-700 text-center">設定需要一些時間，但之後完全自動化、完全私密，每次執行結果都一樣。</div>
  </div>
</div>

---

# 哪種方式適合您？

<div class="mt-6 overflow-x-auto">
  <table class="w-full text-sm border-collapse">
    <thead>
      <tr class="bg-gray-700">
        <th class="text-left p-3 font-bold text-white border border-gray-500"></th>
        <th class="text-center p-3 font-bold text-white border border-gray-500">上傳至 AI 對話</th>
        <th class="text-center p-3 font-bold text-white border border-gray-500">Microsoft Copilot</th>
        <th class="text-center p-3 font-bold text-white border border-gray-500 bg-blue-600">本地工具 ← 今天</th>
      </tr>
    </thead>
    <tbody>
      <tr class="bg-white">
        <td class="p-3 font-bold text-gray-900 border border-gray-400">機密資料安全性</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">⚠️ 有風險</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">視公司政策而定</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ 安全</td>
      </tr>
      <tr class="bg-gray-100">
        <td class="p-3 font-bold text-gray-900 border border-gray-400">批次處理多個檔案</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">❌ 一次一個</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">有限</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ 批次處理</td>
      </tr>
      <tr class="bg-white">
        <td class="p-3 font-bold text-gray-900 border border-gray-400">每月重複執行</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">❌ 每次手動</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">部分支援</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ 一個指令</td>
      </tr>
      <tr class="bg-gray-100">
        <td class="p-3 font-bold text-gray-900 border border-gray-400">設定難度</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400">✅ 幾秒鐘</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">幾分鐘</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400 bg-blue-50">設定一次，之後自動</td>
      </tr>
      <tr class="bg-white">
        <td class="p-3 font-bold text-gray-900 border border-gray-400">費用</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400">✅ 有免費方案</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">$30 美元／人／月</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ 免費</td>
      </tr>
    </tbody>
  </table>
</div>

---

# 這聽起來很熟悉嗎？

<div class="mt-8 grid grid-cols-2 gap-8">
  <div class="bg-red-50 border border-red-200 rounded-xl p-6">
    <div class="text-xl font-bold text-red-500 mb-4">每個月...</div>
    <ul class="space-y-3 text-gray-700">
      <li>📂 開啟多個不同的 Excel 檔案</li>
      <li>✂️ 手動複製貼上到主表</li>
      <li>🔢 修復損壞的公式</li>
      <li>📊 從頭重建樞紐分析表</li>
      <li>😩 下個月再重複一次</li>
    </ul>
  </div>
  <div class="bg-green-50 border border-green-200 rounded-xl p-6">
    <div class="text-xl font-bold text-green-500 mb-4">今天之後...</div>
    <ul class="space-y-3 text-gray-700">
      <li>💬 向 AI 描述您想要的結果</li>
      <li>🤖 AI 撰寫自動化程式</li>
      <li>▶️ 您按一下執行，就這樣</li>
      <li>📈 幾秒內輸出結果</li>
      <li>🎉 每次結果都一樣，不需重做</li>
    </ul>
  </div>
</div>

---
layout: cards
cols: 2
cards:
  - title: 流程
    items:
      - 向 AI 描述您的 Excel 結構
      - AI 為您撰寫 Python 程式
      - 您在本機執行程式
      - 輸出結果自動產生，不需手動操作
  - title: 重點：您的資料安全無虞
    items:
      - AI 不會看到您的實際數字
      - 您只需分享欄位名稱與結構
      - 程式在您的電腦上執行
      - 零資料上傳至任何雲端
---

# 今天我們要做什麼

---

# 前後對比

<TwoCols left-title="之前：4 個雜亂的 Excel 檔案" right-title="之後：整理好、可直接使用的報表">
  <template #left>
    <FileTree
      path="raw_data/"
      :files="[
        'CDE biz status_2024_v1.xlsx',
        'CDE biz status_2025_v1.xlsx',
        'PJ biz status_2024_v1.xlsx',
        'PJ biz status_2025_v2.xlsx',
      ]"
    />
    <div class="mt-4 text-sm text-gray-500">不同格式、不同年份、不同產品，各自分散</div>
  </template>
  <template #right>
    <FileTree
      path="output/"
      :files="[
        'raw_report.csv  ← 所有檔案合併',
        'layer1_report.csv  ← 期間合計',
        'layer2_report.csv  ← 成長與差距指標',
      ]"
    />
    <div class="mt-4 text-sm text-gray-500">一個程式，一致的輸出，幾秒內完成</div>
  </template>
</TwoCols>

---

# 輸入資料長這樣

<ExcelViewer path="/app/bm_report/raw_data/CDE biz status_2024_v1.xlsx" />

---

# 輸出資料長這樣

<ExcelViewer path="/data/raw_report_sample.csv" :default-zoom="1.3" />

<div class="mt-4 text-sm text-gray-500 text-center">
  相同的資料，但現在每一列代表一個產品的某個月份，方便篩選、樞紐或繪製圖表。
</div>

---

<script setup>
const flow = `flowchart LR
    A[描述\\nExcel 結構] --> B[告訴 AI\\n您的需求]
    B --> C[AI 撰寫\\n程式碼]
    C --> D[在本機\\n執行程式]
    D --> E[確認\\n輸出結果]`
</script>

# 五步驟工作流程

<div style="zoom: 2.5; margin-top: 5rem">
  <MermaidHighlight :diagram="flow" />
</div>

---
layout: chapter
---

# 開始提示 AI

---

# 步驟一：向 AI 描述您的資料

<ChatWindow class="text-left mt-6">
  <template #question>
    我有幾個 Excel 檔案放在 <code>raw_data/</code> 資料夾中。每個檔名包含產品名稱和年份，例如 <code>CDE biz status_2024_v1.xlsx</code>。每個檔案有地區、收入類型、預算類型等欄位，以及 1 月到 12 月的月份銷售數字。我想把所有檔案合併成一張表，每一列代表一個月份的資料。
  </template>

  <template #response>
    了解了——我會讀取您資料夾中的每個 <code>.xlsx</code> 檔案，自動從檔名中提取<b>產品名稱</b>和<b>年份</b>，並將 12 個月份欄位重新整理成每月一列的格式。最終輸出為一個 CSV 檔案，共 7 個欄位：<code>product, year, region, rev_op_type, sales_budget_type, month, amount</code>。所有檔案合併成一張表，結構一致，不需要手動複製貼上。
  </template>
</ChatWindow>

---

# 步驟二：請 AI 撰寫程式

<ChatWindow class="text-left mt-6">
  <template #question>
    幫我寫一個 Python 程式來做這件事。我不是工程師，請盡量簡單，並告訴我確切的執行方式。
  </template>

  <template #response>
    我會建立一個檔案叫 <code>main.py</code>。執行方式如下：<br><br>
    1. 開啟終端機（或命令提示字元）<br>
    2. 切換到您的檔案所在資料夾<br>
    3. 輸入：<code>python main.py</code> 然後按 Enter<br>
    4. 結果會存在 <code>output/raw_report.csv</code><br><br>
    就這樣。程式會自動處理讀取、整理和合併，您完全不需要碰任何公式。
  </template>

  <template #question2>
    如果下個月我新增了一個 Excel 檔案怎麼辦？
  </template>

  <template #response2>
    只要把新檔案丟進 <code>raw_data/</code> 資料夾，再執行一次 <code>python main.py</code> 就好。程式會自動抓取該資料夾中的所有檔案，不需要修改任何設定，新資料會立即納入輸出結果。
  </template>
</ChatWindow>

---

# 步驟三：請 AI 深入分析

<ChatWindow class="text-left mt-6">
  <template #question>
    我還想要一份摘要報表，顯示每個產品和地區的合計，以及另一份計算實際銷售與預算差距的報表。
  </template>

  <template #response>
    我會再建立兩份報表：<br><br>
    <b>第一層——期間合計</b>：依產品、年份、地區分組，計算您選擇的任意期間內的實際與預算總和。<br><br>
    <b>第二層——差距與成長指標</b>：計算實際與預算的差距、預算達成率（實際／預算）、年度同比變化（YoY）。這些都是管理報表常用的數字，AI 會從第一層自動推算出來。
  </template>
</ChatWindow>

---
layout: chapter
---

# 換您試試看

---

# 動手練習

<div class="mt-2 space-y-3">
  <div class="bg-yellow-50 border border-yellow-300 rounded-xl p-4 flex items-center gap-4">
    <div class="text-2xl">📦</div>
    <div>
      <div class="font-bold text-gray-800">先下載練習檔案</div>
      <a href="https://reurl.cc/ovGlY5" target="_blank" rel="noopener" class="text-blue-600 underline text-sm font-mono">https://reurl.cc/ovGlY5</a>
      <span class="text-gray-700 text-sm ml-2">— 內含真實 Excel 檔案與起始程式碼</span>
    </div>
  </div>

  <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
    <div class="text-lg font-bold text-blue-700 mb-2">您的任務（10 分鐘）</div>
    <p class="text-gray-800">開啟 <span class="font-bold">Claude</span> 或 <span class="font-bold">ChatGPT</span>，貼上以下提示詞，將括號內容替換成您自己的 Excel 情境：</p>
    <div class="bg-white border border-gray-300 rounded-lg p-4 mt-3 font-mono text-sm leading-relaxed text-gray-900">
      我有 Excel 檔案，包含 [描述您的欄位]。<br>
      每個檔案代表 [什麼？月份？地區？產品？]。<br>
      我想要 [描述您需要的結果]。<br>
      請幫我寫一個 Python 程式，並告訴我如何執行。<br>
      範例提示：<br>
      讀取 app/bm_report/docs/plan.md，以 raw_data 為輸入、output/ 為輸出，依照 plan.md 實作程式，並執行測試驗證結果 <br>
      讀取 app/bm_analytics/docs/plan.md，依照 plan.md 實作程式，並執行 app/bm_analytics/tests 中的測試驗證結果 <br>
    </div>
  </div>

  <div class="bg-green-50 border border-green-200 rounded-xl p-4">
    <div class="font-bold text-green-700 mb-2">與大家分享：</div>
    <ul class="text-gray-800 space-y-1 text-sm">
      <li>AI 給了什麼建議？</li>
      <li>回應內容您看得懂嗎？</li>
      <li>您追問了什麼問題？</li>
    </ul>
  </div>
</div>

---
layout: cards
cols: 2
fill: true
cards:
  - title: "1. 先計畫，再寫程式"
    text: 先描述您的資料和目標，確認 AI 理解您的結構之後，再請它產生程式碼
  - title: "2. 給 AI 足夠的背景"
    text: 提供欄位名稱和範例資料列，您描述得越具體，AI 的輸出就越準確
  - title: "3. 一步一步來"
    text: 一次請 AI 做一件事，確認每個輸出結果後再進行下一步
  - title: "4. 務必驗證"
    text: 開啟輸出的 CSV 檔案，對照原始 Excel 抽查幾筆資料，確認正確後再繼續
---

# 最佳實踐

---
layout: chapter
---

# 進階延伸 *(選修)*

---

# 進階：建立儀表板

<ChatWindow class="text-left mt-6">
  <template #question>
    我可以把這些 CSV 報表變成互動式儀表板分享給團隊嗎？而且不需要伺服器或任何雲端服務？
  </template>

  <template #response>
    可以——使用 <b>Streamlit</b>，這是一個免費的 Python 套件，可以把 CSV 資料變成您在瀏覽器中開啟的網頁儀表板。AI 會幫您產生完整的應用程式：讀取您的 CSV 檔案、在各分頁顯示不同報表，並支援依產品、地區或日期篩選。執行只需一個指令：<code>streamlit run app.py</code>。全部在本機執行，無雲端、無帳號、資料不外流。
  </template>
</ChatWindow>

---

# 成果展示

## 您打造了：

### 一條 AI 輔助的資料處理流程
### 由 Python + Excel 驅動

<a href="https://chenghsienwen.github.io/excel-ai-workshop/bm-viewer/" target="_blank" rel="noopener" style="display:inline-block;margin-top:1.5rem;padding:0.6rem 1.4rem;background:#f96;color:#000;font-weight:600;font-size:1rem;border-radius:6px;text-decoration:none;letter-spacing:0.02em;">查看 BM 報表儀表板 →</a>

---

# 問與答

<QuestionForm class="mt-4" />

---

# 帶走這份簡報

<div style="display:flex;align-items:center;justify-content:space-between;height:70%;gap:2rem">
  <div style="flex:1">

掃描 QR Code 隨時回顧簡報：

  </div>
  <div style="flex-shrink:0">
    <QrCode url="https://chenghsienwen.github.io/excel-ai-workshop/workshop-zh/" :size="420" dark="rgb(44, 41, 39)" />
  </div>
</div>
