---
title: LoanWise OpenEnv
emoji: 🏦
colorFrom: blue
colorTo: green
sdk: docker
sdk_version: "latest"
app_file: server/app.py
pinned: false
---

# 🏦 LoanWise-OpenEnv

LoanWise-OpenEnv is a **real-world loan approval simulation environment** built using the OpenEnv framework.  
It evaluates AI agents on financial decision-making tasks like risk assessment and loan approval.

---

## 🚀 Features

- ✅ Real-world loan underwriting simulation  
- ✅ 3 tasks: Risk, Decision, Workflow  
- ✅ Deterministic reward system  
- ✅ OpenEnv compliant environment  
- ✅ FastAPI-based API (`/reset`, `/step`)  
- ✅ Dockerized for deployment  

---

## 🧠 Problem

Banks must decide whether to:
- Approve loan  
- Reject application  
- Send for manual review  

based on:
- credit score  
- income  
- debt  
- fraud signals  

---

## 📥 API Endpoints

### 🔹 Reset
```bash
POST /reset