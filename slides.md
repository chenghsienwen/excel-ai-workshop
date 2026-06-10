---
# try also 'default' to start simple
theme: viewsonic-proav
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cover.sli.dev
# some information about your slides (markdown enabled)
title: Excel + AI Workshop
info: |
  ## Transform and aggregate excel by AI also without security risk

# apply UnoCSS classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable Comark Syntax: https://comark.dev/syntax/markdown
comark: true
# duration of the presentation
duration: 35min
---

# Excel + AI Workshop

<LastModifiedDate />

---
layout: cards
cards:
  - title: Simon Wen
    text: I am a Cloud Application & Resiliency Engineer who leverages advanced AI acceleration to build, scale, and maintain high-performance business applications at 10x traditional speed, ensuring absolute system elasticity and zero-downtime maintenance.
  - image: /images/simon.wen.github.jpeg
---

# Who am I

---

# Prompt: how to do excel automation?

<ChatWindow class="text-left mt-6">
  <template #question>
    I want to do excel automation on my sales report that lets <code>X cell</code> in <b>Excel 1</b> file react to <code>Y cell</code> in <b>Excel 2</b> file.
  </template>
  
  <template #response>
    You can achieve this seamlessly using Python with the <code>openpyxl</code> library, or by writing a quick <b>VBA Macro</b> using the <code>Worksheet_Change</code> event to trigger the cross-file update automatically whenever Cell X gets modified.
  </template>

  <template #question2>
    How to add a quick <b>VBA Macro</b> for that — letting <code>X cell</code> in <b>Excel 1</b> react to <code>Y cell</code> in <b>Excel 2</b>?
  </template>

  <template #response2>
    Open <b>Excel 1</b>, press <code>Alt+F11</code> to open the VBA editor, then paste this into the <code>Worksheet_Change</code> event of the sheet containing Cell X:<br><br>
    <code>Private Sub Worksheet_Change(ByVal Target As Range)</code><br>
    <code>&nbsp;&nbsp;If Not Intersect(Target, Me.Range("X1")) Is Nothing Then</code><br>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;Workbooks("Excel2.xlsx").Sheets(1).Range("Y1").Value = Me.Range("X1").Value</code><br>
    <code>&nbsp;&nbsp;End If</code><br>
    <code>End Sub</code><br><br>
    Both files must be open for the macro to fire. Save <b>Excel 1</b> as <code>.xlsm</code> to preserve the macro.
  </template>

  <template #question3>
    How about just uploading the Excel files and assigning the rule — lets <code>X cell</code> in <b>Excel 1</b> react to <code>Y cell</code> in <b>Excel 2</b> — then let AI do the job?
  </template>

  <template #response3>
    Upload both files to an AI like <b>ChatGPT</b> or <b>Claude</b> with file-upload enabled, then describe the rule: <code>"copy X1 from Excel1 to Y1 in Excel2 whenever X1 changes"</code>. The AI reads both file structures and generates a ready-to-run <b>Python script</b> or <b>VBA Macro</b> — you paste and run it locally. Your data never leaves your machine; only the file schema and your prompt are sent to the AI.
  </template>
</ChatWindow>

---

# Prompt: use Microsoft copilot

<ChatWindow class="text-left mt-6">
  <template #question>
    How to collect multiple excels to make a pivot table by Microsoft Copilot?
  </template>
  
  <template #response>
    Open your Excel files in <b>Microsoft 365</b>, then prompt Copilot: <code>Consolidate data from these files into one table</code>. Once merged, ask Copilot <code>Create a pivot table that summarizes [column] by [category]</code> — it will build the pivot, configure the fields, and apply grouping automatically without any manual formula or macro work.
  </template>

  <template #question2>
    Is it free to use Copilot?
  </template>

  <template #response2>
    The basic <b>Microsoft Copilot</b> (web &amp; Windows 11) is free, but <b>Copilot for Microsoft 365</b> — the version embedded directly inside Excel, Word, and Teams — requires a paid add-on of around <code>$30 USD/user/month</code> on top of an existing Microsoft 365 Business or Enterprise subscription.
  </template>
</ChatWindow>

---
layout: cards
cards:
  - title: The Flow
    items:
      - Turn Excel inputs
      - into Python automation
      - generate Excel outputs
  - title: Core Idea
    items:
      - AI does NOT run your data
      - AI writes the code
      - You run it locally
  - title: Why This Approach?
    items:
      - No data leakage
      - Works with confidential files
      - Full local control
      - Reproducible pipelines
---

# Goal

---

# Input & Output

<TwoCols left-title="Input" right-title="Output">
  <template #left>
    <FileTree
      path="app/bm_report/raw_data"
      :files="[
        'CDE biz status_2024_v1.xlsx',
        'CDE biz status_2025_v1.xlsx',
        'PJ biz status_2024_v1.xlsx',
        'PJ biz status_2025_v2.xlsx',
      ]"
    />
  </template>
  <template #right>
    <FileTree
      path="app/bm_report_viewer/input"
      :files="[
        'layer1_report.csv',
        'layer2_report.csv',
        'layer3_segmentation.csv',
        'layer3_timeseries.csv',
        'raw_report.csv',
      ]"
    />
  </template>
</TwoCols>

---

# Input sample

<ExcelViewer path="/app/bm_report/raw_data/CDE biz status_2024_v1.xlsx" />

---

# Normalize data

<ExcelViewer path="/data/raw_report_sample.csv" :default-zoom="1.3" />

---

# Layer1 report

<ExcelViewer path="/data/layer1_report_sample.csv" :default-zoom="1.3" />

---

# Layer2 report

<ExcelViewer path="/data/layer2_report_sample.csv" :default-zoom="1.3" />

---

<script setup>
const flow = `flowchart LR
    A[Define\\nExcel Structure] --> B[Describe\\nTransformation]
    B --> C[Generate Python\\nCode via AI]
    C --> D[Run Script\\nLocally]
    D --> E[Validate\\nOutput]`
</script>

# Workshop Flow

<div style="zoom: 2.5; margin-top: 5rem">
  <MermaidHighlight :diagram="flow" />
</div>

---
layout: chapter
---

# Let's prompt


---

# Make a plan for normalize data

<ChatWindow class="text-left mt-6">
  <template #question>
    Transform raw Excel business-status files (<code>raw_data/</code>) into a consolidated, analytics-ready CSV (<code>output/</code>) using Python with Google-style conventions.
  </template>

  <template #response>
    Use <b>pandas</b> + <b>openpyxl</b> in a four-module pipeline: <code>loader.py</code> reads each <code>.xlsx</code> and infers <code>product</code> / <code>year</code> from the filename stem, <code>transformer.py</code> melts the 12 month columns into long-format rows via <code>pd.melt</code> and validates dimension values, then <code>writer.py</code> writes the merged result to <code>output/raw_report.csv</code>. <code>main.py</code> orchestrates the full flow with <code>argparse</code>: glob all files → load → transform → <code>pd.concat</code> → sort → write. The output schema is exactly 7 columns — <code>product, year, region, rev_op_type, sales_budget_type, month, amount</code> — with Google-style docstrings, type hints, and <code>logging</code> throughout.
  </template>
</ChatWindow>

---

# Bm report plan

<TextLoader path="/app/bm_report/docs/plan.md" />

---

# Make a plan for layered reports

<ChatWindow class="text-left mt-6">
  <template #question>
    Read <code>input/raw_report.csv</code> (produced by <code>app/bm_report</code>) and generate Layer 1 and Layer 2 reports:<br>
    — <b>Layer 1</b> — period aggregations per cohort<br>
    — <b>Layer 2</b> — derived cross-type metrics (gap, hit rate, YoY, breakeven)<br><br>
    A third module (<code>trend.py</code>) provides functions for time-series trend views; full spec deferred until layers 1 &amp; 2 are validated. Use Google Python coding style and venv.
  </template>

  <template #response>
    Create a three-module pipeline under <code>app/bm_analytics/</code>: <code>layer1.py</code> groups <code>raw_report.csv</code> by cohort (<code>product / year / region</code>) using <code>pd.groupby</code> to produce period aggregations (sum, actual vs budget); <code>layer2.py</code> derives cross-type metrics — budget gap, hit rate (<code>actual / budget</code>), YoY delta, and breakeven threshold — by joining Layer 1 outputs with <code>pd.merge</code>. Wrap both in <code>main.py</code> with <code>argparse</code> flags <code>--layer1</code> / <code>--layer2</code> / <code>--all</code>, each stage writing to <code>output/layer1_report.csv</code> and <code>output/layer2_report.csv</code>. Follow Google-style conventions: 4-space indent, ≤80 chars, type hints, <code>logging</code>, and a <code>.venv</code> activated before running.
  </template>
</ChatWindow>

---

# Bm layered reports plan

<TextLoader path="app/bm_analytics/docs/plan.md" />

---

# Best Practices

- [Prompt] Discussion and make plan first
- [Context] Provide Excel format and samples
- [Harness] Break down tasks and let AI implement => review step by step

---

# Advanced Extensions

- Power BI integration
- Scheduled automation
- Email report generation
- Dashboard creation

---

# Outcome

You build:

An AI-assisted data pipeline  
powered by Python + Excel

---

# End

From manual Excel work  
to automated intelligence

