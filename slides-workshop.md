---
theme: viewsonic-proav
background: https://cover.sli.dev
title: Excel + AI Workshop — Student Guide
info: |
  ## Transform your Excel reports with AI — no coding experience required
class: text-center
drawings:
  persist: false
transition: slide-left
comark: true
duration: 60min
---

# Excel + AI Workshop

### Participant Guide

<LastModifiedDate />

---

# How We'll Spend the Hour

<div class="mt-8 grid grid-cols-4 gap-4 text-center">
  <div class="bg-orange-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-orange-500">10 min</div>
    <div class="mt-2 font-bold text-gray-800">Context</div>
    <div class="text-sm mt-1 text-gray-700">Why AI + Excel? What we're building today</div>
  </div>
  <div class="bg-blue-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-blue-500">20 min</div>
    <div class="mt-2 font-bold text-gray-800">Live Demo</div>
    <div class="text-sm mt-1 text-gray-700">Watch the full workflow — prompt to output</div>
  </div>
  <div class="bg-green-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-green-500">25 min</div>
    <div class="mt-2 font-bold text-gray-800">Hands-on</div>
    <div class="text-sm mt-1 text-gray-700">You write a prompt and get AI output</div>
  </div>
  <div class="bg-purple-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-purple-500">5 min</div>
    <div class="mt-2 font-bold text-gray-800">Q & A</div>
    <div class="text-sm mt-1 text-gray-700">Questions, takeaways, next steps</div>
  </div>
</div>

---
layout: cards
cols: 2
cards:
  - title: Simon Wen
    text: I automate Excel workflows using AI so we spends minutes on reports instead of hours. I build the pipelines — AI writes the code.
    tags: [simon.ch.wen@viewsonic.com]
  - image: /images/simon.wen.github.jpeg
---

# Who am I

---

# What if you just need a quick answer from one Excel file?

<div class="mt-6 grid grid-cols-2 gap-8">
  <div class="space-y-4">
    <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
      <div class="font-bold text-gray-800 mb-2">What you do</div>
      <ul class="text-gray-700 space-y-2 text-sm">
        <li>📎 Upload the file directly to ChatGPT or Claude</li>
        <li>💬 Describe what you want in plain English</li>
        <li>📊 Get a summary, chart, or formula instantly</li>
      </ul>
    </div>
    <div class="bg-green-50 border border-green-200 rounded-xl p-5">
      <div class="font-bold text-gray-800 mb-2">Best for</div>
      <ul class="text-gray-700 space-y-2 text-sm">
        <li>✅ One-off questions and quick analysis</li>
        <li>✅ Non-sensitive data</li>
        <li>✅ No setup — start in seconds</li>
      </ul>
    </div>
  </div>
  <div class="bg-orange-50 border border-orange-200 rounded-xl p-5">
    <div class="font-bold text-gray-800 mb-3">Watch out</div>
    <ul class="text-gray-700 space-y-3 text-sm">
      <li>⚠️ Your file is uploaded to the AI provider's servers</li>
      <li>⚠️ Not suitable for confidential or customer data</li>
      <li>⚠️ You repeat the process manually every time</li>
    </ul>
    <div class="mt-6 pt-4 border-t border-orange-200 text-sm text-gray-600 italic">
      Great starting point — but limited when data is sensitive or the task repeats.
    </div>
  </div>
</div>

---

# What if your team already uses Microsoft 365?

<div class="mt-6 grid grid-cols-2 gap-8">
  <div class="space-y-4">
    <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
      <div class="font-bold text-gray-800 mb-2">What you do</div>
      <ul class="text-gray-700 space-y-2 text-sm">
        <li>🖱️ Open Excel Online or Teams</li>
        <li>💬 Ask Copilot to consolidate, pivot, or summarise</li>
        <li>📈 Results appear directly in your spreadsheet</li>
      </ul>
    </div>
    <div class="bg-green-50 border border-green-200 rounded-xl p-5">
      <div class="font-bold text-gray-800 mb-2">Best for</div>
      <ul class="text-gray-700 space-y-2 text-sm">
        <li>✅ Collaborative team reports in shared files</li>
        <li>✅ Data already in Microsoft 365 environment</li>
        <li>✅ No extra tools or installation needed</li>
      </ul>
    </div>
  </div>
  <div class="bg-orange-50 border border-orange-200 rounded-xl p-5">
    <div class="font-bold text-gray-800 mb-3">Watch out</div>
    <ul class="text-gray-700 space-y-3 text-sm">
      <li>⚠️ Requires a paid Copilot licence (~$30 USD/user/month)</li>
      <li>⚠️ Data stays within Microsoft cloud — check your org policy</li>
      <li>⚠️ Limited to files already in Microsoft 365</li>
    </ul>
    <div class="mt-6 pt-4 border-t border-orange-200 text-sm text-gray-600 italic">
      Powerful for Microsoft shops — but cost and policy approval can be blockers.
    </div>
  </div>
</div>

---

# What if you have many files, sensitive data, or need the same report every month?

<div class="mt-6 grid grid-cols-2 gap-8">
  <div class="space-y-4">
    <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
      <div class="font-bold text-gray-800 mb-2">What you do</div>
      <ul class="text-gray-700 space-y-2 text-sm">
        <li>💬 Describe your Excel structure to AI</li>
        <li>🤖 AI writes a Python script — you paste and run it</li>
        <li>▶️ Script runs locally, output is ready in seconds</li>
      </ul>
    </div>
    <div class="bg-green-50 border border-green-200 rounded-xl p-5">
      <div class="font-bold text-gray-800 mb-2">Best for</div>
      <ul class="text-gray-700 space-y-2 text-sm">
        <li>✅ Confidential or internal data — nothing leaves your machine</li>
        <li>✅ Many files processed in one run</li>
        <li>✅ Recurring reports — run the same script every month</li>
      </ul>
    </div>
  </div>
  <div class="bg-green-50 border border-green-200 rounded-xl p-5 flex flex-col justify-center">
    <div class="text-4xl text-center mb-4">🎯</div>
    <div class="font-bold text-gray-800 text-center mb-2">This is today's workshop</div>
    <div class="text-sm text-gray-700 text-center">Higher setup effort — but fully automated, fully private, and runs the same way every time.</div>
  </div>
</div>

---

# Which approach fits your situation?

<div class="mt-6 overflow-x-auto">
  <table class="w-full text-sm border-collapse">
    <thead>
      <tr class="bg-gray-700">
        <th class="text-left p-3 font-bold text-white border border-gray-500"></th>
        <th class="text-center p-3 font-bold text-white border border-gray-500">Upload to AI Chat</th>
        <th class="text-center p-3 font-bold text-white border border-gray-500">Microsoft Copilot</th>
        <th class="text-center p-3 font-bold text-white border border-gray-500 bg-blue-600">Local Tool ← Today</th>
      </tr>
    </thead>
    <tbody>
      <tr class="bg-white">
        <td class="p-3 font-bold text-gray-900 border border-gray-400">Confidential data</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">⚠️ Risky</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">Depends on policy</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ Safe</td>
      </tr>
      <tr class="bg-gray-100">
        <td class="p-3 font-bold text-gray-900 border border-gray-400">Many files at once</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">❌ One at a time</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">Limited</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ Batch</td>
      </tr>
      <tr class="bg-white">
        <td class="p-3 font-bold text-gray-900 border border-gray-400">Repeatable monthly</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">❌ Manual each time</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">Partial</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ One command</td>
      </tr>
      <tr class="bg-gray-100">
        <td class="p-3 font-bold text-gray-900 border border-gray-400">Setup effort</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400">✅ Seconds</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">Minutes</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400 bg-blue-50">Once, then automated</td>
      </tr>
      <tr class="bg-white">
        <td class="p-3 font-bold text-gray-900 border border-gray-400">Cost</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400">✅ Free tier available</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">$30/user/month</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ Free</td>
      </tr>
    </tbody>
  </table>
</div>

---

# Does this sound familiar?

<div class="mt-8 grid grid-cols-2 gap-8">
  <div class="bg-red-50 border border-red-200 rounded-xl p-6">
    <div class="text-xl font-bold text-red-500 mb-4">Every month...</div>
    <ul class="space-y-3 text-gray-700">
      <li>📂 Open 4 different Excel files</li>
      <li>✂️ Copy-paste rows into a master sheet</li>
      <li>🔢 Fix broken formulas manually</li>
      <li>📊 Rebuild the pivot table from scratch</li>
      <li>😩 Repeat next month</li>
    </ul>
  </div>
  <div class="bg-green-50 border border-green-200 rounded-xl p-6">
    <div class="text-xl font-bold text-green-500 mb-4">After today...</div>
    <ul class="space-y-3 text-gray-700">
      <li>💬 Describe what you want to AI</li>
      <li>🤖 AI writes the automation script</li>
      <li>▶️ You press Run — once</li>
      <li>📈 Output is ready in seconds</li>
      <li>🎉 Same result, every time</li>
    </ul>
  </div>
</div>

---
layout: cards
cols: 2
cards:
  - title: The Flow
    items:
      - Describe your Excel structure to AI
      - AI writes a Python script for you
      - You run the script locally
      - Output is ready — no manual work
  - title: Key Point — Your Data Stays Safe
    items:
      - AI never sees your actual numbers
      - You only share column names and structure
      - The script runs on your machine
      - Zero data sent to any cloud
---

# What We're Doing Today

---

# Before & After

<TwoCols left-title="Before — 4 messy Excel files" right-title="After — clean, ready-to-use reports">
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
    <div class="mt-4 text-sm text-gray-500">Different formats, different years, different products — all separate</div>
  </template>
  <template #right>
    <FileTree
      path="output/"
      :files="[
        'raw_report.csv  ← all files merged',
        'layer1_report.csv  ← period totals',
        'layer2_report.csv  ← growth & gap metrics',
      ]"
    />
    <div class="mt-4 text-sm text-gray-500">One script, consistent output, runs in seconds</div>
  </template>
</TwoCols>

---

# What the Input Looks Like

<ExcelViewer path="/app/bm_report/raw_data/CDE biz status_2024_v1.xlsx" />

---

# What the Output Looks Like

<ExcelViewer path="/data/raw_report_sample.csv" :default-zoom="1.3" />

<div class="mt-4 text-sm text-gray-500 text-center">
  Same data — but now every row is one month, one product. Easy to filter, pivot, or chart.
</div>

---

<script setup>
const flow = `flowchart LR
    A[Describe\\nExcel Structure] --> B[Tell AI\\nWhat You Want]
    B --> C[AI Writes\\nthe Script]
    C --> D[You Run\\nit Locally]
    D --> E[Check\\nthe Output]`
</script>

# The 5-Step Workflow

<div style="zoom: 2.5; margin-top: 5rem">
  <MermaidHighlight :diagram="flow" />
</div>

---
layout: chapter
---

# Let's Prompt

---

# Step 1 — Describe your data to AI

<ChatWindow class="text-left mt-6">
  <template #question>
    I have several Excel files in a folder called <code>raw_data/</code>. Each filename tells me the product and year, like <code>CDE biz status_2024_v1.xlsx</code>. Each file has columns for region, revenue type, budget type, and 12 monthly sales numbers (Jan through Dec). I want to combine all files into one clean table where each row is one month of data.
  </template>

  <template #response>
    Got it — I'll read every <code>.xlsx</code> file from your folder, pull the <b>product name</b> and <b>year</b> out of the filename automatically, and reshape the 12 monthly columns so each month becomes its own row. The result will be a single CSV file with 7 columns: <code>product, year, region, rev_op_type, sales_budget_type, month, amount</code>. Every file gets merged into one clean table — consistent structure, no manual copy-pasting.
  </template>
</ChatWindow>

---

# Step 2 — Ask AI to write the script

<ChatWindow class="text-left mt-6">
  <template #question>
    Write a Python script to do this. I'm not a programmer — keep it simple and tell me exactly how to run it.
  </template>

  <template #response>
    Here's what I'll create — a single file called <code>main.py</code>. To run it:<br><br>
    1. Open your terminal (or Command Prompt)<br>
    2. Go to the folder where your files are<br>
    3. Type: <code>python main.py</code> and press Enter<br>
    4. Find your result in <code>output/raw_report.csv</code><br><br>
    That's it. The script handles all the reading, reshaping, and merging automatically. You don't need to touch any formulas.
  </template>

  <template #question2>
    What if I add a new Excel file next month?
  </template>

  <template #response2>
    Just drop the new file into the <code>raw_data/</code> folder and run <code>python main.py</code> again. The script picks up every file in that folder automatically — no changes needed. Your output will include the new data instantly.
  </template>
</ChatWindow>

---

# Step 3 — Ask AI to go deeper

<ChatWindow class="text-left mt-6">
  <template #question>
    Now I want a summary report that shows totals per product and region, and another report that calculates the gap between actual sales and budget.
  </template>

  <template #response>
    I'll create two more scripts:<br><br>
    <b>Layer 1 — Period totals</b>: groups your data by product, year, and region to give you the sum of actual vs budget for any time period you choose.<br><br>
    <b>Layer 2 — Gap & growth metrics</b>: calculates how far actual was from budget (gap), what percentage of the budget was hit (hit rate), and how sales changed year-over-year (YoY). These are the numbers your management reports usually need — and AI derives them automatically from Layer 1.
  </template>
</ChatWindow>

---
layout: chapter
---

# Now You Try

---

# Hands-on Exercise

<div class="mt-2 space-y-3">
  <div class="bg-yellow-50 border border-yellow-300 rounded-xl p-4 flex items-center gap-4">
    <div class="text-2xl">📦</div>
    <div>
      <div class="font-bold text-gray-800">Download the exercise files first</div>
      <a href="https://reurl.cc/ovGlY5" target="_blank" rel="noopener" class="text-blue-600 underline text-sm font-mono">https://reurl.cc/ovGlY5</a>
      <span class="text-gray-700 text-sm ml-2">— real Excel files + starter code inside</span>
    </div>
  </div>

  <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
    <div class="text-lg font-bold text-blue-700 mb-2">Your Task (10 minutes)</div>
    <p class="text-gray-800">Open <span class="font-bold">Claude</span> or <span class="font-bold">ChatGPT</span> and paste this prompt — replace the brackets with your own Excel situation:</p>
    <div class="bg-white border border-gray-300 rounded-lg p-4 mt-3 font-mono text-sm leading-relaxed text-gray-900">
      I have Excel files with [describe your columns here].<br>
      Each file represents [what — a month? a region? a product?].<br>
      I want to [describe what result you need].<br>
      Write a Python script to do this and tell me how to run it.<br>
      sample: <br>
      read app/bm_report/docs/plan.md, app/bm_report/docs/raw_data as input, app/bm_report/docs/output/ as output, implement the code according to plan.md, please verify result by running tests <br>
      read app/bm_analytics/docs/plan.md and implement code by plan.md, please verify result by running tests in app/bm_analytics/tests <br>
    </div>
  </div>

  <div class="bg-green-50 border border-green-200 rounded-xl p-4">
    <div class="font-bold text-green-700 mb-2">Share with the group:</div>
    <ul class="text-gray-800 space-y-1 text-sm">
      <li>What did AI suggest?</li>
      <li>Did the response make sense to you?</li>
      <li>What follow-up question did you ask?</li>
    </ul>
  </div>
</div>

---
layout: cards
cols: 2
fill: true
cards:
  - title: "1. Plan before coding"
    text: Describe your data and goal first — make sure AI understands your structure before asking for code
  - title: "2. Give AI context"
    text: Share column names and a sample row — the more specific you are, the better the output
  - title: "3. One step at a time"
    text: Ask AI to do one thing at a time — check each output before moving to the next step
  - title: "4. Always verify"
    text: Open the output file and spot-check a few rows against your source Excel before trusting the result
---

# Best Practices

---
layout: chapter
---

# Take It Further *(Optional)*

---

# Advanced: Build a Dashboard

<ChatWindow class="text-left mt-6">
  <template #question>
    Can I turn these CSV reports into an interactive dashboard I can share with my team — without needing a server or any cloud service?
  </template>

  <template #response>
    Yes — use <b>Streamlit</b>, a free Python library that turns CSV data into a web dashboard you open in your browser. AI will generate the full app for you: it reads your CSVs, shows each report in its own tab, and lets you filter by product, region, or date. Run it with one command: <code>streamlit run app.py</code>. Everything stays local — no cloud, no accounts, no sharing your data.
  </template>
</ChatWindow>

---

# Outcome & Demo

## You build:

### An AI-assisted data pipeline  
### powered by Python + Excel

<a href="https://chenghsienwen.github.io/excel-ai-workshop/bm-viewer/" target="_blank" rel="noopener" style="display:inline-block;margin-top:1.5rem;padding:0.6rem 1.4rem;background:#f96;color:#000;font-weight:600;font-size:1rem;border-radius:6px;text-decoration:none;letter-spacing:0.02em;">View BM Report Viewer →</a>

---

# Q & A

<QuestionForm class="mt-4" />

---

# Slide take away

<div style="display:flex;align-items:center;justify-content:space-between;height:70%;gap:2rem">
  <div style="flex:1">

Scan to revisit the slides:

  </div>
  <div style="flex-shrink:0">
    <QrCode url="https://chenghsienwen.github.io/excel-ai-workshop/workshop/" :size="420" dark="rgb(44, 41, 39)" />
  </div>
</div>
