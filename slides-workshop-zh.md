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
head:
  - - meta
    - name: viewport
      content: "width=device-width, initial-scale=1, user-scalable=yes, maximum-scale=5"
---

# Excel + AI 工作坊

### 學員手冊

<div style="position:absolute;inset:0;background:rgba(0,0,0,0.4);z-index:0;pointer-events:none" />

<LastModifiedDate />

<!--
大家辛苦了，今天最後一場了！先快速回顧一下今天精彩的分享：

Joe 讓我們看到，AI 原來可以這麼快、這麼順手地跟我們協作；
Perry 用 MCP 告訴我們，很多生活瑣事其實只要「動一張嘴」，AI 就能幫我們搞定；
Paul 帶我們走了一趟 Deep Research 的冒險旅程，看 AI 怎麼把資料一路挖到底；
Vincent 更是讓人驚艷，直接讓 AI 協作把投影片生出來；
Jasper 則告訴我們，跟 AI 溝通不只是「用打的」，還可以用說的，而且還是讓AI 精準有條理的輸出。

聽到這裡，大家是不是覺得，今天差不多該收工了？

——殊不知，接下來這場 Excel + AI 工作坊，很可能才是大家真正把 AI 帶進日常工作的另一個開始。前面幾場讓大家看到 AI 能做什麼，這一場，換大家自己動手，把 Excel 裡那些花時間、重複性高的工作，交給 AI 來處理。

準備好了嗎？我們開始吧！

[click 進入投影片]
-->

---

# 今日議程

<div class="mt-8 grid grid-cols-4 gap-4 text-center">
  <div class="bg-orange-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-orange-500">10 分鐘</div>
    <div class="mt-2 font-bold text-black">背景介紹</div>
    <div class="text-sm mt-1 text-black">為什麼要用 AI + Excel？今天要做什麼</div>
  </div>
  <div class="bg-blue-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-blue-500">20 分鐘</div>
    <div class="mt-2 font-bold text-black">現場示範</div>
    <div class="text-sm mt-1 text-black">觀看完整流程：從提示詞到輸出結果</div>
  </div>
  <div class="bg-green-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-green-500">25 分鐘</div>
    <div class="mt-2 font-bold text-black">動手實作</div>
    <div class="text-sm mt-1 text-black">自己輸入提示詞，取得 AI 輸出</div>
  </div>
  <div class="bg-purple-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-purple-500">5 分鐘</div>
    <div class="mt-2 font-bold text-black">問與答</div>
    <div class="text-sm mt-1 text-black">提問、重點整理、後續步驟</div>
  </div>
</div>

<!--
先花幾分鐘跟大家聊聊，為什麼要用 AI + Excel？還有今天到底要做什麼。

這次工作坊的題材，其實不是憑空設計的練習題，而是來自 BM team 一個很實際的需求——他們每個月都要花大量時間，把好幾份 Excel 報表整理、比對、彙總成一份大家看得懂的報告。這是真實發生在我們公司裡的痛點，也是我自己開始用 AI 處理 Excel 的起點。

今天的安排是這樣：前面大概 30 分鐘，我會先講背景、再現場示範一次完整流程，讓大家看到從一句提示詞到輸出結果的整個過程。

後半段，也就是接下來差不多一半的時間，完全留給大家自己動手練習。而且練習的時候，不會只有你跟 AI 兩個人——你身邊的小幫手，也歡迎一起加入，跟你、跟 AI 一起協作，一起討論怎麼下提示詞、怎麼調整結果。

好，那我們就開始吧！

[click 進入下一頁]
-->

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

<!--
簡單自我介紹一下，我是 Simon，今年我們的其中一項任務，就是想辦法讓 AI 幫團隊把 Excel 報表的自動化流程建起來——原本要花好幾個小時整理的報表，現在幾分鐘就能跑完。我負責的是把整個流程架構想清楚，實際寫程式的部分，就交給 AI 來處理。如果之後想聊聊相關話題，投影片上也有我的信箱，歡迎直接找我。

[click 進入下一頁]
-->

---

# 方法一：如果您只需要從一個 Excel 檔案快速取得答案？

<div class="mt-6 grid grid-cols-2 gap-8">
  <div class="space-y-4">
    <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
      <div class="font-bold text-black mb-2">您要做的事</div>
      <ul class="text-black space-y-2 text-sm">
        <li>📎 直接將檔案上傳至 ChatGPT 或 Claude</li>
        <li>💬 用日常語言描述您想要的結果</li>
        <li>📊 立即取得摘要、圖表或公式</li>
      </ul>
    </div>
    <div class="bg-green-50 border border-green-200 rounded-xl p-5">
      <div class="font-bold text-black mb-2">適合情境</div>
      <ul class="text-black space-y-2 text-sm">
        <li>✅ 臨時性問題與快速分析</li>
        <li>✅ 非機密資料</li>
        <li>✅ 免設定，幾秒內即可開始</li>
      </ul>
    </div>
  </div>
  <div class="bg-orange-50 border border-orange-200 rounded-xl p-5">
    <div class="font-bold text-black mb-3">注意事項</div>
    <ul class="text-black space-y-3 text-sm">
      <li>⚠️ 您的檔案會上傳至 AI 服務商的伺服器</li>
      <li>⚠️ 不適合機密或客戶資料</li>
      <li>⚠️ 每次都需要手動重複操作</li>
    </ul>
    <div class="mt-6 pt-4 border-t border-orange-200 text-sm text-black italic">
      很好的起點，但資料敏感或任務需重複時有所限制。
    </div>
  </div>
</div>

<!--
我們先看第一種做法，也是最多人已經在用的——如果你只是想從一份 Excel 檔案裡快速拿到答案，直接把檔案丟給 ChatGPT 或 Claude，用平常講話的方式描述你要什麼，馬上就能拿到摘要、圖表，甚至公式。這個方法的好處是幾乎不用設定，很適合臨時性的問題，或是資料本身不算機密的情況。但要注意，檔案一旦上傳，就會送到 AI 服務商的伺服器上，所以機密或客戶資料就不適合這樣做；而且每次都要重新上傳、重新描述一次，沒辦法自動化。簡單講，這是一個很好的起點，但遇到敏感資料或重複性任務，就會碰到限制。

[click 進入下一頁]
-->

---

# 方法二：如果您的團隊已經在使用 Microsoft 365？

<div class="mt-6 grid grid-cols-2 gap-8">
  <div class="space-y-4">
    <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
      <div class="font-bold text-black mb-2">您要做的事</div>
      <ul class="text-black space-y-2 text-sm">
        <li>🖱️ 開啟 Excel Online 或 Teams</li>
        <li>💬 請 Copilot 合併、樞紐或摘要資料</li>
        <li>📈 結果直接顯示在您的試算表中</li>
      </ul>
    </div>
    <div class="bg-green-50 border border-green-200 rounded-xl p-5">
      <div class="font-bold text-black mb-2">適合情境</div>
      <ul class="text-black space-y-2 text-sm">
        <li>✅ 團隊共用檔案的協作報表</li>
        <li>✅ 資料已在 Microsoft 365 環境中</li>
        <li>✅ 無需額外工具或安裝</li>
      </ul>
    </div>
  </div>
  <div class="bg-orange-50 border border-orange-200 rounded-xl p-5">
    <div class="font-bold text-black mb-3">注意事項</div>
    <ul class="text-black space-y-3 text-sm">
      <li>⚠️ 需要付費授權（約 $30 美元／人／月）</li>
      <li>⚠️ 資料存放於 Microsoft 雲端，請確認公司政策</li>
      <li>⚠️ 僅限 Microsoft 365 內的檔案</li>
    </ul>
    <div class="mt-6 pt-4 border-t border-orange-200 text-sm text-black italic">
      對 Microsoft 用戶很強大，但費用和政策審核可能是障礙。
    </div>
  </div>
</div>

<!--
第二種方法，是給已經在用 Microsoft 365 的伙伴。你可以直接在 Excel Online 或 Teams 裡面，請 Copilot 幫你合併資料、做樞紐分析，或是產生摘要，結果會直接出現在你的試算表裡，不用另外操作。這個方式對已經在 Microsoft 365 環境、而且是團隊共用檔案在做協作報表的情況特別方便，也不需要額外安裝工具。不過要留意，Copilot 是要付費授權的，大概是每人每月 30 美元；資料也會存放在 Microsoft 的雲端上，公司的政策要先確認清楚；而且它只能處理 Microsoft 365 裡面的檔案。整體來說，使用經驗很方便，但是如果遇到多份檔案的情況，就可能是它的限制。

[click 進入下一頁]
-->

---

# 方法三：如果您有大量檔案、機密資料，或每月需要相同的報表？

<div class="mb-4 bg-indigo-50 border border-indigo-300 rounded-xl px-5 py-3 flex items-center gap-3 text-sm">
  <div class="text-xl">✅</div>
  <div><span class="font-bold text-indigo-700">今日前提假設：</span> <span class="text-black">您已成功設定好 AI Agent 工具（例如 Claude、Codex 等），並能夠正常送出提示詞。</span></div>
</div>

<div class="mt-2 grid grid-cols-2 gap-8">
  <div class="space-y-4">
    <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
      <div class="font-bold text-black mb-2">您要做的事</div>
      <ul class="text-black space-y-2 text-sm">
        <li>💬 向 AI 描述您的 Excel 結構</li>
        <li>🤖 AI 撰寫 Python 程式，您貼上並執行</li>
        <li>▶️ 程式在本機執行，幾秒內輸出結果</li>
      </ul>
    </div>
    <div class="bg-green-50 border border-green-200 rounded-xl p-5">
      <div class="font-bold text-black mb-2">適合情境</div>
      <ul class="text-black space-y-2 text-sm">
        <li>✅ 機密或內部資料，不離開您的電腦</li>
        <li>✅ 一次處理大量檔案</li>
        <li>✅ 每月重複報表，一個指令搞定</li>
      </ul>
    </div>
  </div>
  <div class="bg-green-50 border border-green-200 rounded-xl p-5 flex flex-col justify-center">
    <div class="text-4xl text-center mb-4">🎯</div>
    <div class="font-bold text-black text-center mb-2">這就是今天工作坊的主題</div>
    <div class="text-sm text-black text-center">設定需要一些時間，但之後完全自動化、完全私密，每次執行結果都一樣。</div>
  </div>
</div>

<!--
那如果你的狀況是——檔案量很大、資料很機密，或者每個月都要重做一模一樣的報表呢？這就是第三種方法，也是今天整場工作坊真正要教大家的東西。前提是你已經把 AI Agent 工具，像 Claude 或 Codex，設定好並且能正常送出提示詞。做法是：你把 Excel 的結構描述給 AI 聽，AI 會幫你寫好 Python 程式，你貼上去、按下執行，程式就在你自己的電腦上跑，幾秒鐘就有結果。這個方法最大的好處是，機密資料完全不會離開你的電腦，而且可以一次處理大量檔案，每個月要重複做的報表，之後只要下一個指令就搞定。設定確實需要花一點時間，但一旦設定好，就是完全自動化、完全私密，而且每次執行結果都一樣——這就是我們今天要一起做的事。

[click 進入下一頁]
-->

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
        <td class="p-3 font-bold text-black border border-gray-400">機密資料安全性</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">⚠️ 有風險</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">視公司政策而定</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ 安全</td>
      </tr>
      <tr class="bg-gray-100">
        <td class="p-3 font-bold text-black border border-gray-400">批次處理多個檔案</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">❌ 一次一個</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">有限</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ 批次處理</td>
      </tr>
      <tr class="bg-white">
        <td class="p-3 font-bold text-black border border-gray-400">每月重複執行</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">❌ 每次手動</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">部分支援</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ 一個指令</td>
      </tr>
      <tr class="bg-gray-100">
        <td class="p-3 font-bold text-black border border-gray-400">設定難度</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400">✅ 幾秒鐘</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">幾分鐘</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400 bg-blue-50">設定一次，之後自動</td>
      </tr>
      <tr class="bg-white">
        <td class="p-3 font-bold text-black border border-gray-400">費用</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400">✅ 有免費方案</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">$30 美元／人／月</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ 免費</td>
      </tr>
    </tbody>
  </table>
</div>

<!--
這邊用一張表，把剛剛講的三種方法整理起來，方便大家比較。看機密資料安全性，上傳到 AI 對話是有風險的，Copilot 要看公司政策，只有今天要教的本地工具是安全的。批次處理多個檔案也是一樣，上傳對話一次只能處理一個，Copilot 有限，本地工具可以一次批次處理。每月要重複執行的話，上傳對話每次都要手動來，本地工具只要一個指令。設定難度上，本地工具確實需要先設定一次，但之後就自動化了。費用的話，本地工具也是免費的。整體看下來，如果你在意資料安全、又需要重複處理大量檔案，今天教的方法會是最適合的選擇。

[click 進入下一頁]
-->

---

# 這聽起來很熟悉嗎？

<div class="mt-8 grid grid-cols-2 gap-8">
  <div class="bg-red-50 border border-red-200 rounded-xl p-6">
    <div class="text-xl font-bold text-red-500 mb-4">每個月...</div>
    <ul class="space-y-3 text-black">
      <li>📂 開啟多個不同的 Excel 檔案</li>
      <li>✂️ 手動複製貼上到主表</li>
      <li>🔢 修復損壞的公式</li>
      <li>📊 從頭重建樞紐分析表</li>
      <li>😩 下個月再重複一次</li>
    </ul>
  </div>
  <div class="bg-green-50 border border-green-200 rounded-xl p-6">
    <div class="text-xl font-bold text-green-500 mb-4">今天之後...</div>
    <ul class="space-y-3 text-black">
      <li>💬 向 AI 描述您想要的結果</li>
      <li>🤖 AI 撰寫自動化程式</li>
      <li>▶️ 您按一下執行，就這樣</li>
      <li>📈 幾秒內輸出結果</li>
      <li>🎉 每次結果都一樣，不需重做</li>
    </ul>
  </div>
</div>

<!--
這張投影片，我想問問大家，這樣的場景是不是很熟悉——每隔一段時間都要打開好幾個不同的 Excel 檔案，手動複製貼上到主表，還要修理不小心弄壞的公式，樞紐分析表也常常要從頭重建一次，然後下次又要重來一遍。這幾乎是每個做報表的人都會遇到的痛苦循環。但今天之後，流程會變成：你只要跟 AI 描述你想要的結果，AI 幫你把自動化程式寫好，之後你只要按一下執行，幾秒鐘就有結果，而且每次執行結果都一樣，不需要重做。這就是我們今天想帶大家做到的改變。

[click 進入下一頁]
-->

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

<!--
那具體來說，今天我們要做的事情是什麼呢？流程很簡單：你跟 AI 描述你的 Excel 結構，AI 幫你寫好 Python 程式，你在自己的電腦上執行，結果就自動產生出來，完全不需要手動操作。這邊也想特別強調一個重點，就是資料安全性——AI 其實不會看到你真正的數字，你只需要告訴它欄位名稱跟資料結構就好，程式是在你自己的電腦上執行，資料不會上傳到任何雲端。這一點在處理公司內部資料時特別重要。

[click 進入下一頁]
-->

---

# 前後對比

<TwoCols left-title="之前：4 個 Excel 檔案" right-title="之後：整理好、可直接使用的報表">
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
    <div class="mt-4 text-sm text-gray-300">不同格式、不同年份、不同產品，各自分散</div>
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
    <div class="mt-4 text-sm text-gray-300">一個程式，一致的輸出，幾秒內完成</div>
  </template>
</TwoCols>

<!--
我們直接看一個實際的例子。左邊是「之前」的狀況：四個 Excel 檔案，格式不同、年份不同、產品也不同，各自分散在資料夾裡。右邊是「之後」的樣子：一份合併好的原始報表、一份依期間彙總的報表，還有一份計算成長跟差距指標的報表，全部整整齊齊。從左到右，靠的就是一個程式，輸出結果一致，而且只要幾秒鐘就完成，不需要人工一份一份去對。

[click 進入下一頁]
-->

---

# 業務主管關心的問題

<div class="mt-6 grid grid-cols-2 gap-6">
  <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
    <div class="font-bold text-black mb-2">📊 差距與達成率</div>
    <ul class="text-black space-y-2 text-sm">
      <li>實際業績跟預算的差距是多少？(Actual vs Budget Gap)</li>
      <li>目前的預算達成率(Budget Hit Rate)是多少？</li>
      <li>Forecast 跟 Actual 的落差有多大？</li>
    </ul>
  </div>
  <div class="bg-green-50 border border-green-200 rounded-xl p-5">
    <div class="font-bold text-black mb-2">⚖️ 比較與排名</div>
    <ul class="text-black space-y-2 text-sm">
      <li>A 地區/產品 跟 B 地區/產品相比表現如何？</li>
      <li>哪個地區或產品線的業績成長最快？</li>
      <li>Gross、Net、OP 三者的表現是否一致？</li>
    </ul>
  </div>
  <div class="bg-yellow-50 border border-yellow-300 rounded-xl p-5">
    <div class="font-bold text-black mb-2">📈 趨勢</div>
    <ul class="text-black space-y-2 text-sm">
      <li>近幾年(YoY)銷售金額的趨勢是成長還是下滑？</li>
      <li>累積至今(YTD)的表現，跟去年同期相比如何？</li>
      <li>單月(MTD)表現是否符合季節性預期？</li>
    </ul>
  </div>
  <div class="bg-purple-50 border border-purple-200 rounded-xl p-5">
    <div class="font-bold text-black mb-2">🔍 其他常見問題</div>
    <ul class="text-black space-y-2 text-sm">
      <li>平均銷售價格(ASP)是否有異常變化？</li>
      <li>哪些產品/地區離目標最遠，需要優先關注？</li>
    </ul>
  </div>
</div>

<!--
在動手做之前，我們先想一下，業務主管平常到底關心哪些問題。
第一類是差距與達成率，像是實際業績跟預算差多少、預算達成率是多少、Forecast 跟 Actual 落差有多大。

第二類是比較與排名，例如 A 地區跟 B 地區比起來表現如何、哪個產品線成長最快、Gross、Net、OP 三個數字表現是否一致。

第三類是趨勢，像是這幾年 YoY 是成長還是下滑、YTD 累積表現跟去年同期比較、單月 MTD 是不是符合季節性預期。

最後還有一些常見問題，比如 ASP 平均銷售價格有沒有異常變化、哪些產品或地區離目標最遠需要優先關注。這些問題，其實就是我們接下來這份報表設計要回答的東西。

[click 進入下一頁]
-->

---

# 輸入資料長這樣

<ExcelViewer path="/app/bm_report/raw_data/CDE biz status_2024_v1.xlsx" />

<!--
這是我們今天要用到的原始輸入資料，大家可以看一下實際的 Excel 檔案長什麼樣子——這是真實的業務狀況表，裡面有地區、收入類型、預算類型，還有一到十二月的月份銷售數字，橫向排開。

[click 進入下一頁]
-->

---

# 輸出資料長這樣

<ExcelViewer path="/data/raw_report_sample.csv" :default-zoom="1.3" />

<div class="mt-4 text-sm text-gray-300 text-center">
  相同的資料，但現在每一列代表一個產品的某個月份，方便篩選、樞紐或繪製圖表。
</div>

<!--
經過程式處理之後，輸出的資料會變成這個樣子——一樣的資料內容，但現在每一列代表一個產品在某個月份的資料，變成直向的格式。這樣的好處是，之後不管你要篩選、做樞紐分析，還是畫圖表，都會方便非常多。

[click 進入下一頁]
-->

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

<!--
我們把整個流程畫成一張圖，一共五個步驟：先描述你的 Excel 結構，接著告訴 AI 你的需求，AI 會幫你寫好程式碼，然後你在自己的電腦上執行程式，最後確認輸出結果對不對。整個工作坊接下來的示範，就是按照這五個步驟一步一步走一遍。

[click 進入下一頁]
-->

---
layout: chapter
---

# 開始提示 AI

<!--
好，接下來我們就正式開始，實際示範怎麼跟 AI 下提示詞。

[click 進入下一頁]
-->

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

<!--
第一步，就是把你的資料狀況，用平常講話的方式描述給 AI 聽。像投影片上這個例子，我告訴 AI：我有幾個 Excel 檔案放在 raw_data 資料夾裡，每個檔名都包含產品名稱跟年份，每個檔案有地區、收入類型、預算類型等欄位，還有一到十二月的月份銷售數字，我想把所有檔案合併成一張表，每一列代表一個月份。AI 這邊的回應也很清楚，它會讀取資料夾裡每一個 xlsx 檔案，自動從檔名抓出產品名稱和年份，把十二個月份欄位重新整理成每月一列，最後輸出一個結構一致的 CSV 檔案。整個過程，我完全不需要手動複製貼上。

[click 進入下一頁]
-->

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

<!--
確認 AI 理解我的資料結構之後，第二步就是請它把程式寫出來。我跟它說：幫我寫一個 Python 程式來做這件事，我不是工程師，請盡量簡單，並告訴我確切的執行方式。AI 就會建立一個叫 main.py 的檔案，並且一步一步告訴我怎麼執行：開啟終端機、切換到檔案所在資料夾、輸入 python main.py 按 Enter，結果就會存在 output 資料夾裡。我接著又追問了一個很實際的問題：如果下個月新增了一個 Excel 檔案怎麼辦？AI 的回答也很簡單，只要把新檔案丟進 raw_data 資料夾，再執行一次程式就好，不需要修改任何設定，新資料會自動被納入。

[click 進入下一頁]
-->

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

<!--
有了乾淨的資料之後，第三步就可以請 AI 往下做更深入的分析。我跟它說，我還想要一份摘要報表，顯示每個產品和地區的合計，另外還要一份計算實際銷售跟預算差距的報表。AI 就幫我建立了兩層報表：第一層是期間合計，依產品、年份、地區分組，計算任意期間內的實際與預算總和；第二層是差距與成長指標，直接從第一層推算出實際與預算的差距、預算達成率，還有年度同比變化 YoY。這些都是我們剛剛在「業務主管關心的問題」那頁提到的指標，AI 都能幫忙算出來。

[click 進入下一頁]
-->

---
layout: chapter
---

# 換您試試看

<!--
看完示範，接下來就是換大家自己動手做的時間了。

[click 進入下一頁]
-->

---

# 動手練習

<div class="mt-2 space-y-3">
  <div class="bg-yellow-50 border border-yellow-300 rounded-xl p-4 flex items-center gap-4">
    <div class="text-2xl">📦</div>
    <div>
      <div class="font-bold text-black">先下載練習檔案</div>
      <a href="https://reurl.cc/ovGlY5" target="_blank" rel="noopener" class="text-blue-600 underline text-sm font-mono">https://reurl.cc/ovGlY5</a>
      <span class="text-black text-sm ml-2">— 內含真實 Excel 檔案與起始程式碼</span>
    </div>
  </div>

  <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
    <div class="text-lg font-bold text-blue-700 mb-2">您的任務（20 分鐘）</div>
    <p class="text-black">開啟 <span class="font-bold">Claude</span> 或 <span class="font-bold">ChatGPT</span>，貼上以下提示詞，將括號內容替換成您自己的 Excel 情境：</p>
    <div class="bg-white border border-gray-300 rounded-lg p-4 mt-3 font-mono text-sm leading-relaxed text-black select-text cursor-text">
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
    <ul class="text-black space-y-1 text-sm">
      <li>AI 給了什麼建議？</li>
      <li>回應內容您看得懂嗎？</li>
      <li>您追問了什麼問題？</li>
    </ul>
  </div>
</div>

<!--
這邊是實際動手練習的說明。第一步，先透過投影片上的連結下載練習檔案，裡面有真實的 Excel 檔案跟起始程式碼。接下來的二十分鐘，就是大家的任務：打開 Claude 或 ChatGPT，貼上投影片上的提示詞範本，把括號裡的內容換成你自己的 Excel 情境——你的欄位有哪些、每個檔案代表什麼、你想要什麼樣的結果，然後請它幫你寫程式，並告訴你怎麼執行。做完之後，也歡迎跟大家分享：AI 給了什麼建議、回應內容你看得懂嗎、你又追問了什麼問題。旁邊的小幫手也可以一起討論，一起調整提示詞。

[click 進入下一頁]
-->

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

<!--
在大家動手之前，我想分享四個實際操作上的小技巧。
第一，先計畫再寫程式——先描述你的資料和目標，確認 AI 理解你的結構之後，再請它產生程式碼。
第二，給 AI 足夠的背景，提供欄位名稱和範例資料列，你描述得越具體，AI 的輸出就會越準確。
第三，一步一步來，一次只請 AI 做一件事，確認每個輸出結果沒問題，再進行下一步。
第四，也是最重要的一點，務必驗證——打開輸出的 CSV 檔案，對照原始 Excel 抽查幾筆資料，確認正確之後再繼續往下做。

[click 進入下一頁]
-->

---
layout: chapter
---

# 進階延伸 *(選修)*

<!--
時間允許的話，我們再往下看一個進階、選修的延伸應用。

[click 進入下一頁]
-->

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

<!--
如果你想更進一步，可以試著把這些 CSV 報表變成互動式的儀表板分享給團隊，而且完全不需要伺服器或雲端服務。我在投影片上問 AI 這個問題，它給的答案是用 Streamlit，這是一個免費的 Python 套件，可以把 CSV 資料變成在瀏覽器裡開啟的網頁儀表板。AI 會幫忙產生完整的應用程式，讀取 CSV 檔案，在不同分頁顯示不同報表，還支援依產品、地區或日期篩選，執行只需要一個指令：streamlit run app.py。整個過程一樣在本機執行，不需要雲端、不需要帳號，資料也不會外流。

[click 進入下一頁]
-->

---

# 成果展示

## 您打造了：

### 一條 AI 輔助的資料處理流程
### 由 Python + Excel 驅動

<a href="https://chenghsienwen.github.io/excel-ai-workshop/bm-viewer/" target="_blank" rel="noopener" style="display:inline-block;margin-top:1.5rem;padding:0.6rem 1.4rem;background:#f96;color:#000;font-weight:600;font-size:1rem;border-radius:6px;text-decoration:none;letter-spacing:0.02em;">查看 BM 報表儀表板 →</a>

<!--
走到這裡，大家已經打造出一條 AI 輔助的資料處理流程，由 Python 加上 Excel 驅動。投影片上也有連結，可以直接看到我們用同樣方法做出來的 BM 報表儀表板，歡迎點進去看看實際成果長什麼樣子。

[click 進入下一頁]
-->

---

# 問與答

<QuestionForm class="mt-4" />

<!--
接下來這段時間留給大家提問，投影片上有問題表單，歡迎大家把今天遇到的疑問，或是還想深入了解的地方寫下來，我們一起討論。

[click 進入下一頁]
-->

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

<!--
最後，這份簡報大家可以隨時回去複習，掃描投影片上的 QR Code，就可以在自己的裝置上打開完整內容。謝謝大家今天的參與，也謝謝大家把時間留給這場工作坊，希望今天學到的東西，真的能帶回你們日常的工作裡去用。
-->
