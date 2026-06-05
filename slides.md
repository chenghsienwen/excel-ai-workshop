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

# Goal

Turn Excel inputs  
→ into Python automation  
→ generate Excel outputs

---

# Core Idea

AI does NOT run your data

AI writes the code

You run it locally

---

# Why This Approach?

- No data leakage
- Works with confidential files
- Full local control
- Reproducible pipelines

---

# Architecture

Excel Files  
↓  
AI Agent  
↓  
Python Code  
↓  
Local Execution  
↓  
Output Excel

---

# Input

Multiple Excel files

- Sales reports
- HR data
- Finance sheets
- Logs / exports

---

# AI Role

AI receives:

- File structure
- Column definitions
- Transformation rules

---

# AI Output

Python script that:

- Reads Excel files
- Cleans data
- Merges datasets
- Applies logic
- Generates output Excel

---

# Key Libraries

pandas  
openpyxl  
pathlib  
numpy (optional)

---

# Example Task

“Merge 12 monthly Excel files  
and generate annual KPI report”

---

# What AI Generates

- Data loader
- Cleaner
- Transformer
- Aggregator
- Exporter

---

# Execution Model

NO cloud execution

ONLY local machine

---

# Security Advantage

- Data never leaves PC
- No SaaS upload required
- Suitable for confidential data

---

# Workshop Flow

1. Define Excel structure  
2. Describe transformation  
3. Generate Python code via AI  
4. Run script locally  
5. Validate output

---

# Failure Cases

- Inconsistent Excel schemas
- Missing keys / IDs
- Poor column naming
- Unstructured inputs

---

# Best Practices

- Standardize Excel format
- Use table headers
- Define unique IDs
- Keep transformations explicit

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

