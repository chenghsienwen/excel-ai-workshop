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
head:
  - - meta
    - name: viewport
      content: "width=device-width, initial-scale=1, user-scalable=yes, maximum-scale=5"
---

# Excel + AI Workshop

### Participant Guide

<div style="position:absolute;inset:0;background:rgba(0,0,0,0.4);z-index:0;pointer-events:none" />

<LastModifiedDate />

<!--
Thanks for sticking with us — this is the last session of the day! Let's do a quick recap of everything we've covered so far:

Joe showed us just how fast and natural it can be to collaborate with AI;
Perry used MCP to show us that a lot of everyday chores can be handled by AI with nothing more than a spoken request;
Paul took us on a Deep Research adventure, showing how far AI can dig into data;
Vincent amazed everyone by having AI generate slides directly, working alongside him;
And Jasper showed us that talking to AI isn't limited to typing — you can speak to it too, and still get precise, well-organized output.

After hearing all that, you might be thinking we're about ready to wrap up for the day.

But actually — this Excel + AI workshop might be where everyone truly starts bringing AI into their everyday work. The earlier sessions showed you what AI can do; this one is where you get hands-on and hand off those time-consuming, repetitive Excel tasks to AI.

Ready? Let's get started!

[click to begin]
-->

---

# How We'll Spend the Hour

<div class="mt-8 grid grid-cols-4 gap-4 text-center">
  <div class="bg-orange-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-orange-500">10 min</div>
    <div class="mt-2 font-bold text-black">Context</div>
    <div class="text-sm mt-1 text-black">Why AI + Excel? What we're building today</div>
  </div>
  <div class="bg-blue-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-blue-500">20 min</div>
    <div class="mt-2 font-bold text-black">Live Demo</div>
    <div class="text-sm mt-1 text-black">Watch the full workflow — prompt to output</div>
  </div>
  <div class="bg-green-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-green-500">25 min</div>
    <div class="mt-2 font-bold text-black">Hands-on</div>
    <div class="text-sm mt-1 text-black">You write a prompt and get AI output</div>
  </div>
  <div class="bg-purple-100 rounded-xl p-4">
    <div class="text-2xl font-bold text-purple-500">5 min</div>
    <div class="mt-2 font-bold text-black">Q & A</div>
    <div class="text-sm mt-1 text-black">Questions, takeaways, next steps</div>
  </div>
</div>

<!--
Let's spend a few minutes on why we're using AI + Excel, and what exactly we're building today.

The material for this workshop isn't a made-up exercise — it comes from a real need on the BM team. Every month, they spend a huge amount of time cleaning up, comparing, and consolidating several Excel reports into something everyone can actually read. That's a real pain point happening inside our own company, and it's actually where I started using AI to work with Excel myself.

Here's how today is structured: for roughly the first 30 minutes, I'll cover the background and then run through a complete live demo, so you can see the whole process from a single prompt to a finished output.

The second half — about the other half of our time — is entirely yours to practice hands-on. And you won't just be working with AI on your own — the helpers around the room are here to join in too, collaborating with you and the AI, discussing how to phrase prompts and how to adjust the results.

Alright, let's get going!

[click to next slide]
-->

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

<!--
Quick introduction — I'm Simon. One of the things we've been working on this year is figuring out how to get AI to build automated Excel reporting pipelines for the team — reports that used to take hours to put together now run in minutes. My part is thinking through the overall pipeline architecture; the actual coding gets handed off to AI. If you'd like to chat more about this afterward, my email is right there on the slide — feel free to reach out.

[click to next slide]
-->

---

# What if you just need a quick answer from one Excel file?

<div class="mt-6 grid grid-cols-2 gap-8">
  <div class="space-y-4">
    <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
      <div class="font-bold text-black mb-2">What you do</div>
      <ul class="text-black space-y-2 text-sm">
        <li>📎 Upload the file directly to ChatGPT or Claude</li>
        <li>💬 Describe what you want in plain English</li>
        <li>📊 Get a summary, chart, or formula instantly</li>
      </ul>
    </div>
    <div class="bg-green-50 border border-green-200 rounded-xl p-5">
      <div class="font-bold text-black mb-2">Best for</div>
      <ul class="text-black space-y-2 text-sm">
        <li>✅ One-off questions and quick analysis</li>
        <li>✅ Non-sensitive data</li>
        <li>✅ No setup — start in seconds</li>
      </ul>
    </div>
  </div>
  <div class="bg-orange-50 border border-orange-200 rounded-xl p-5">
    <div class="font-bold text-black mb-3">Watch out</div>
    <ul class="text-black space-y-3 text-sm">
      <li>⚠️ Your file is uploaded to the AI provider's servers</li>
      <li>⚠️ Not suitable for confidential or customer data</li>
      <li>⚠️ You repeat the process manually every time</li>
    </ul>
    <div class="mt-6 pt-4 border-t border-orange-200 text-sm text-black italic">
      Great starting point — but limited when data is sensitive or the task repeats.
    </div>
  </div>
</div>

<!--
Let's start with the first approach — also the one most people are already using. If you just need a quick answer from a single Excel file, you can drop the file straight into ChatGPT or Claude, describe what you want in plain language, and get a summary, a chart, or even a formula right away. The upside is there's almost no setup — it's great for one-off questions or data that isn't sensitive. But keep in mind, once you upload the file, it goes to the AI provider's servers, so this isn't suitable for confidential or customer data. And every single time, you have to re-upload and re-describe what you want — there's no automation. In short, it's a great starting point, but it runs into limits once the data is sensitive or the task repeats.

[click to next slide]
-->

---

# What if your team already uses Microsoft 365?

<div class="mt-6 grid grid-cols-2 gap-8">
  <div class="space-y-4">
    <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
      <div class="font-bold text-black mb-2">What you do</div>
      <ul class="text-black space-y-2 text-sm">
        <li>🖱️ Open Excel Online or Teams</li>
        <li>💬 Ask Copilot to consolidate, pivot, or summarise</li>
        <li>📈 Results appear directly in your spreadsheet</li>
      </ul>
    </div>
    <div class="bg-green-50 border border-green-200 rounded-xl p-5">
      <div class="font-bold text-black mb-2">Best for</div>
      <ul class="text-black space-y-2 text-sm">
        <li>✅ Collaborative team reports in shared files</li>
        <li>✅ Data already in Microsoft 365 environment</li>
        <li>✅ No extra tools or installation needed</li>
      </ul>
    </div>
  </div>
  <div class="bg-orange-50 border border-orange-200 rounded-xl p-5">
    <div class="font-bold text-black mb-3">Watch out</div>
    <ul class="text-black space-y-3 text-sm">
      <li>⚠️ Requires a paid Copilot licence (~$30 USD/user/month)</li>
      <li>⚠️ Data stays within Microsoft cloud — check your org policy</li>
      <li>⚠️ Limited to files already in Microsoft 365</li>
    </ul>
    <div class="mt-6 pt-4 border-t border-orange-200 text-sm text-black italic">
      Powerful for Microsoft shops — but cost and policy approval can be blockers.
    </div>
  </div>
</div>

<!--
The second approach is for anyone already working in Microsoft 365. You can go straight into Excel Online or Teams and ask Copilot to consolidate your data, build a pivot, or write a summary, and the result shows up directly in your spreadsheet — no extra steps. This works especially well if you're already in the Microsoft 365 environment and doing collaborative reporting on shared files, and it doesn't require installing anything extra. That said, keep in mind Copilot requires a paid licence, roughly 30 US dollars per user per month; your data also stays on Microsoft's cloud, so check your company policy first; and it only works with files that are already inside Microsoft 365. Overall, it's a very smooth experience to use, but once you're dealing with multiple files at once, that's likely where it hits its limits.

[click to next slide]
-->

---

# What if you have many files, sensitive data, or need the same report every month?

<div class="mb-4 bg-indigo-50 border border-indigo-300 rounded-xl px-5 py-3 flex items-center gap-3 text-sm">
  <div class="text-xl">✅</div>
  <div><span class="font-bold text-indigo-700">Assumption for today:</span> <span class="text-black">You have already set up an AI agent tool — Claude, Codex, or similar — and can send it a prompt.</span></div>
</div>

<div class="mt-2 grid grid-cols-2 gap-8">
  <div class="space-y-4">
    <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
      <div class="font-bold text-black mb-2">What you do</div>
      <ul class="text-black space-y-2 text-sm">
        <li>💬 Describe your Excel structure to AI</li>
        <li>🤖 AI writes a Python script — you paste and run it</li>
        <li>▶️ Script runs locally, output is ready in seconds</li>
      </ul>
    </div>
    <div class="bg-green-50 border border-green-200 rounded-xl p-5">
      <div class="font-bold text-black mb-2">Best for</div>
      <ul class="text-black space-y-2 text-sm">
        <li>✅ Confidential or internal data — nothing leaves your machine</li>
        <li>✅ Many files processed in one run</li>
        <li>✅ Recurring reports — run the same script every month</li>
      </ul>
    </div>
  </div>
  <div class="bg-green-50 border border-green-200 rounded-xl p-5 flex flex-col justify-center">
    <div class="text-4xl text-center mb-4">🎯</div>
    <div class="font-bold text-black text-center mb-2">This is today's workshop</div>
    <div class="text-sm text-black text-center">Higher setup effort — but fully automated, fully private, and runs the same way every time.</div>
  </div>
</div>

<!--
So what if your situation is — a large volume of files, sensitive data, or the same report you have to redo every single month? That's the third approach, and it's really what this entire workshop is here to teach you. The assumption is that you've already got an AI agent tool set up, like Claude or Codex, and can send it a prompt successfully. Here's how it works: you describe your Excel structure to AI, AI writes you a Python script, you paste it in and hit run, and the script runs right there on your own machine — results in seconds. The biggest benefit of this approach is that confidential data never leaves your computer, you can process a large batch of files in one go, and any report you have to repeat every month just takes one command from then on. Setting it up does take a bit more effort up front, but once it's set up, it's fully automated, fully private, and produces the same result every single time — and that's exactly what we're going to build together today.

[click to next slide]
-->

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
        <td class="p-3 font-bold text-black border border-gray-400">Confidential data</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">⚠️ Risky</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">Depends on policy</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ Safe</td>
      </tr>
      <tr class="bg-gray-100">
        <td class="p-3 font-bold text-black border border-gray-400">Many files at once</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">❌ One at a time</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">Limited</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ Batch</td>
      </tr>
      <tr class="bg-white">
        <td class="p-3 font-bold text-black border border-gray-400">Repeatable monthly</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">❌ Manual each time</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">Partial</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ One command</td>
      </tr>
      <tr class="bg-gray-100">
        <td class="p-3 font-bold text-black border border-gray-400">Setup effort</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400">✅ Seconds</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400">Minutes</td>
        <td class="p-3 text-center font-semibold text-orange-700 border border-gray-400 bg-blue-50">Once, then automated</td>
      </tr>
      <tr class="bg-white">
        <td class="p-3 font-bold text-black border border-gray-400">Cost</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400">✅ Free tier available</td>
        <td class="p-3 text-center font-semibold text-red-600 border border-gray-400">$30/user/month</td>
        <td class="p-3 text-center font-semibold text-green-700 border border-gray-400 bg-blue-50">✅ Free</td>
      </tr>
    </tbody>
  </table>
</div>

<!--
Here's a table pulling together the three approaches we just went through, so it's easier to compare. Looking at confidential data safety — uploading to an AI chat is risky, Copilot depends on your company policy, and only the local tool we're teaching today is genuinely safe. Same story with batch processing multiple files — uploading to chat handles one at a time, Copilot is limited, and the local tool can batch-process everything at once. For monthly repeatable work, uploading to chat means doing it manually every time, while the local tool just takes one command. On setup effort, the local tool does need to be set up once, but after that it's automated. And on cost, the local tool is free too. Bottom line — if data safety matters to you and you need to repeatedly process a lot of files, the approach we're teaching today is going to be the best fit.

[click to next slide]
-->

---

# Does this sound familiar?

<div class="mt-8 grid grid-cols-2 gap-8">
  <div class="bg-red-50 border border-red-200 rounded-xl p-6">
    <div class="text-xl font-bold text-red-500 mb-4">Every month...</div>
    <ul class="space-y-3 text-black">
      <li>📂 Open 4 different Excel files</li>
      <li>✂️ Copy-paste rows into a master sheet</li>
      <li>🔢 Fix broken formulas manually</li>
      <li>📊 Rebuild the pivot table from scratch</li>
      <li>😩 Repeat next month</li>
    </ul>
  </div>
  <div class="bg-green-50 border border-green-200 rounded-xl p-6">
    <div class="text-xl font-bold text-green-500 mb-4">After today...</div>
    <ul class="space-y-3 text-black">
      <li>💬 Describe what you want to AI</li>
      <li>🤖 AI writes the automation script</li>
      <li>▶️ You press Run — once</li>
      <li>📈 Output is ready in seconds</li>
      <li>🎉 Same result, every time</li>
    </ul>
  </div>
</div>

<!--
For this slide, I want to ask everyone — does this scenario sound familiar? Every so often you have to open several different Excel files, manually copy-paste rows into a master sheet, fix formulas that got accidentally broken, rebuild the pivot table from scratch, and then do it all over again next time. It's a painful cycle almost everyone who builds reports runs into. But after today, the process becomes: you just describe the result you want to AI, AI writes the automation script for you, and from then on you just press run — results in seconds, and the same result every single time, no redoing it. That's the change we want to help everyone make today.

[click to next slide]
-->

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

<!--
So concretely, what are we doing today? The flow is simple: you describe your Excel structure to AI, AI writes you a Python script, you run it on your own machine, and the result gets produced automatically — no manual work involved. I also want to highlight one important point here — data safety. AI never actually sees your real numbers; you only need to tell it the column names and data structure. The script runs on your own machine, and no data ever gets uploaded to any cloud. That matters a lot when you're working with internal company data.

[click to next slide]
-->

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
    <div class="mt-4 text-sm text-gray-300">Different formats, different years, different products — all separate</div>
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
    <div class="mt-4 text-sm text-gray-300">One script, consistent output, runs in seconds</div>
  </template>
</TwoCols>

<!--
Let's look at a real example. On the left is the 'before' state — four Excel files, each in a different format, different year, different product, all scattered across a folder. On the right is 'after' — a merged raw report, a report rolled up by period, and a report calculating growth and gap metrics, all neatly organized. Getting from left to right takes just one script — consistent output, done in a matter of seconds, with no manual cross-checking file by file.

[click to next slide]
-->

---

# Questions Sales Leaders Care About

<div class="mt-6 grid grid-cols-2 gap-6">
  <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
    <div class="font-bold text-black mb-2">📊 Gaps & Attainment</div>
    <ul class="text-black space-y-2 text-sm">
      <li>What's the gap between actual and budget?</li>
      <li>What's the current budget hit rate?</li>
      <li>How far off is forecast from actual?</li>
    </ul>
  </div>
  <div class="bg-green-50 border border-green-200 rounded-xl p-5">
    <div class="font-bold text-black mb-2">⚖️ Comparisons & Ranking</div>
    <ul class="text-black space-y-2 text-sm">
      <li>How does region/product A compare to B?</li>
      <li>Which region or product line is growing fastest?</li>
      <li>Do Gross, Net, and OP all tell the same story?</li>
    </ul>
  </div>
  <div class="bg-yellow-50 border border-yellow-300 rounded-xl p-5">
    <div class="font-bold text-black mb-2">📈 Trends</div>
    <ul class="text-black space-y-2 text-sm">
      <li>Is sales trending up or down year over year (YoY)?</li>
      <li>How does year-to-date (YTD) compare to the same period last year?</li>
      <li>Is month-to-date (MTD) tracking with seasonal expectations?</li>
    </ul>
  </div>
  <div class="bg-purple-50 border border-purple-200 rounded-xl p-5">
    <div class="font-bold text-black mb-2">🔍 Other Common Questions</div>
    <ul class="text-black space-y-2 text-sm">
      <li>Is average selling price (ASP) showing any anomalies?</li>
      <li>Which products/regions are furthest from target and need attention?</li>
    </ul>
  </div>
</div>

<!--
Before we dive in, let's think about what questions sales leaders actually care about.
The first category is gaps and attainment — things like how far actual performance is from budget, what the current budget hit rate is, and how big the gap is between forecast and actual.

The second category is comparisons and ranking — how region or product A compares to B, which product line is growing the fastest, and whether Gross, Net, and OP all tell a consistent story.

The third category is trends — whether sales are trending up or down year over year, how year-to-date performance compares to the same period last year, and whether month-to-date is tracking with seasonal expectations.

And finally, there are a few other common questions, like whether average selling price is showing any anomalies, or which products or regions are furthest from target and need attention. These questions are exactly what the report we're about to design needs to answer.

[click to next slide]
-->

---

# What the Input Looks Like

<ExcelViewer path="/app/bm_report/raw_data/CDE biz status_2024_v1.xlsx" />

<!--
This is the raw input data we'll be using today — take a look at what the actual Excel file looks like. It's a real business status report with columns for region, revenue type, and budget type, plus monthly sales numbers from January through December laid out horizontally.

[click to next slide]
-->

---

# What the Output Looks Like

<ExcelViewer path="/data/raw_report_sample.csv" :default-zoom="1.3" />

<div class="mt-4 text-sm text-gray-300 text-center">
  Same data — but now every row is one month, one product. Easy to filter, pivot, or chart.
</div>

<!--
After the script processes it, the output ends up looking like this — same underlying data, but now every row represents one product in one month, in a long/vertical format. The advantage is that whatever you want to do next — filtering, pivoting, or charting — becomes a lot easier.

[click to next slide]
-->

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

<!--
We've drawn the whole process as a diagram with five steps: describe your Excel structure, tell AI what you want, AI writes the script for you, you run it on your own machine, and finally you check that the output is correct. Everything we demo for the rest of the workshop just walks through these five steps one at a time.

[click to next slide]
-->

---
layout: chapter
---

# Let's Prompt

<!--
Alright, let's kick things off for real now, and walk through exactly how to prompt AI.

[click to next slide]
-->

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

<!--
Step one is describing your data situation to AI, in plain, everyday language. Like in the example on the slide, I tell AI: I have several Excel files in a raw_data folder, each filename contains a product name and a year, each file has columns like region, revenue type, and budget type, plus monthly sales figures from January through December, and I want to combine all the files into one table where each row is a single month. AI's response is just as clear — it'll read every xlsx file in the folder, automatically pull the product name and year out of the filename, reshape the twelve monthly columns so each month becomes its own row, and output one consistently structured CSV file. Through this whole process, I never have to manually copy and paste anything.

[click to next slide]
-->

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

<!--
Once I've confirmed AI understands my data structure, step two is asking it to actually write the script. I tell it: write me a Python script to do this — I'm not a programmer, keep it simple, and tell me exactly how to run it. AI creates a file called main.py and walks me through exactly how to run it, step by step: open your terminal, go to the folder where the files are, type python main.py and press Enter, and the result gets saved into the output folder. I then follow up with a very practical question: what if I add a new Excel file next month? AI's answer is just as simple — drop the new file into the raw_data folder and run the script again, no configuration changes needed, and the new data gets picked up automatically.

[click to next slide]
-->

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

<!--
With clean data in hand, step three is asking AI to go further with deeper analysis. I tell it I also want a summary report showing totals by product and region, plus another report calculating the gap between actual sales and budget. AI builds me two more layers of reporting: Layer 1 is period totals — grouped by product, year, and region, giving the sum of actual versus budget for any period you choose; Layer 2 is gap and growth metrics — derived straight from Layer 1, calculating the gap between actual and budget, the budget hit rate, and year-over-year change. These are exactly the metrics we talked about back on the "Questions Sales Leaders Care About" slide, and AI can work all of them out for you.

[click to next slide]
-->

---
layout: chapter
---

# Now You Try

<!--
Now that you've seen the demo, it's time for you to try it yourself.

[click to next slide]
-->

---

# Hands-on Exercise

<div class="mt-2 space-y-3">
  <div class="bg-yellow-50 border border-yellow-300 rounded-xl p-4 flex items-center gap-4">
    <div class="text-2xl">📦</div>
    <div>
      <div class="font-bold text-black">Download the exercise files first</div>
      <a href="https://reurl.cc/ovGlY5" target="_blank" rel="noopener" class="text-blue-600 underline text-sm font-mono">https://reurl.cc/ovGlY5</a>
      <span class="text-black text-sm ml-2">— real Excel files + starter code inside</span>
    </div>
  </div>

  <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
    <div class="text-lg font-bold text-blue-700 mb-2">Your Task (10 minutes)</div>
    <p class="text-black">Open <span class="font-bold">Claude</span> or <span class="font-bold">ChatGPT</span> and paste this prompt — replace the brackets with your own Excel situation:</p>
    <div class="bg-white border border-gray-300 rounded-lg p-4 mt-3 font-mono text-sm leading-relaxed text-black select-text cursor-text">
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
    <ul class="text-black space-y-1 text-sm">
      <li>What did AI suggest?</li>
      <li>Did the response make sense to you?</li>
      <li>What follow-up question did you ask?</li>
    </ul>
  </div>
</div>

<!--
Here's the walkthrough for the hands-on exercise. First, download the exercise files using the link on the slide — it includes real Excel files and starter code. For the next ten minutes, your task is this: open Claude or ChatGPT, paste the prompt template shown on the slide, and swap out the bracketed placeholders for your own Excel situation — what your columns are, what each file represents, and what result you want — then ask it to write you a script and tell you how to run it. Once you're done, feel free to share with the group: what did AI suggest, did the response make sense to you, and what follow-up question did you ask? The helpers around the room are also happy to discuss and help you refine your prompt.

[click to next slide]
-->

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

<!--
Before everyone dives in, I want to share four practical tips.
First, plan before you code — describe your data and your goal first, and make sure AI understands your structure before asking it to generate code.
Second, give AI enough context — share your column names and a sample row; the more specific you are, the more accurate the output will be.
Third, take it one step at a time — ask AI to do one thing at a time, and confirm each output is correct before moving to the next step.
Fourth, and most important — always verify. Open the output CSV file and spot-check a few rows against the original Excel before continuing.

[click to next slide]
-->

---
layout: chapter
---

# Take It Further *(Optional)*

<!--
If time allows, let's look at one more advanced, optional extension.

[click to next slide]
-->

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

<!--
If you want to go a step further, you can try turning these CSV reports into an interactive dashboard to share with your team, without needing a server or any cloud service at all. On the slide, I asked AI exactly this question, and its answer was to use Streamlit — a free Python library that turns CSV data into a web dashboard you open in your browser. AI generates the complete application for you: it reads your CSV files, shows different reports in different tabs, and supports filtering by product, region, or date. Running it takes just one command: streamlit run app.py. The whole thing still runs locally — no cloud, no accounts, and your data never leaves your machine.

[click to next slide]
-->

---

# Outcome & Demo

## You build:

### An AI-assisted data pipeline  
### powered by Python + Excel

<a href="https://chenghsienwen.github.io/excel-ai-workshop/bm-viewer/" target="_blank" rel="noopener" style="display:inline-block;margin-top:1.5rem;padding:0.6rem 1.4rem;background:#f96;color:#000;font-weight:600;font-size:1rem;border-radius:6px;text-decoration:none;letter-spacing:0.02em;">View BM Report Viewer →</a>

<!--
At this point, you've built an AI-assisted data pipeline powered by Python and Excel. There's also a link on the slide where you can see the actual BM report dashboard we built using this exact same approach — feel free to click through and see what the real result looks like.

[click to next slide]
-->

---

# Q & A

<QuestionForm class="mt-4" />

<!--
Let's spend the next bit of time on questions. There's a question form on the slide — feel free to write down anything you're unsure about from today, or anything you'd like to dig into further, and we'll go through it together.

[click to next slide]
-->

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

<!--
Lastly, you can always come back and review these slides — scan the QR code on the slide to open the full deck on your own device. Thank you all for participating today, and thank you for giving your time to this workshop. I hope what you've learned today genuinely makes its way into your everyday work.
-->
