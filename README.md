# Clara AI Automation Pipeline

### Demo Call → Agent Configuration → Onboarding Update → Agent Revision

This project implements an **automation pipeline that converts customer conversations into structured AI voice agent configurations**.

The system processes **demo call transcripts and onboarding updates** to generate a **Retell AI Agent specification**, enabling automated inbound call handling for service businesses such as electrical contractors, HVAC companies, and fire protection providers.

The pipeline extracts operational rules from transcripts, creates a **versioned agent configuration**, and visualizes the results through a **Streamlit dashboard**.

---

# Problem Context

Service trade companies (HVAC, electrical, fire protection, etc.) receive large volumes of inbound calls.

These calls must be handled differently depending on:

* Business hours
* Emergency situations
* Dispatch routing rules
* Service types
* Operational constraints

Configuring these rules manually for every client is **time-consuming and error-prone**.

Clara Answers solves this problem by using **AI voice agents** to automatically handle inbound calls.

However, configuring these agents requires converting **messy human conversations into structured operational rules**.

This project simulates that automation layer.

---

# System Overview

The system processes client conversations in two stages:

### Stage 1 — Demo Call

The demo call provides **initial information about the client's operations**.

From this, the system generates:

* Account Memo JSON
* Preliminary Retell Agent Configuration (v1)

Missing information is **not guessed** and is instead flagged under `questions_or_unknowns`.

---

### Stage 2 — Onboarding Call

The onboarding call confirms operational rules such as:

* Business hours
* Emergency definitions
* Dispatch routing
* Transfer timeouts
* Integration constraints

These updates modify the existing configuration to produce:

* Updated Account Memo
* Updated Agent Configuration (v2)
* Change Log (v1 → v2)

---

# Pipeline Architecture

```
Demo Call Transcript
        ↓
Extraction Engine
        ↓
Structured Account Memo
        ↓
Agent Spec Generator
        ↓
Agent Configuration (v1)
        ↓
Onboarding Transcript
        ↓
Patch Engine
        ↓
Agent Configuration (v2)
        ↓
Change Log
        ↓
Dashboard Visualization
```

The pipeline runs in **batch mode**, allowing multiple accounts to be processed automatically.

---

# Key Features

Automated transcript data extraction
Structured operational rule schema
Retell agent prompt generation
Version-controlled agent configurations
Change tracking between onboarding updates
Batch processing for multiple accounts
Pipeline monitoring dashboard
Zero-cost implementation using open tools

---

# Repository Structure

```
clara-automation-pipeline
│
├── dashboard
│   └── streamlit_app.py
│
├── scripts
│   ├── pipeline.py
│   ├── extractor.py
│   ├── patcher.py
│   ├── agent_generator.py
│   └── logger.py
│
├── data
│   ├── demo_calls
│   └── onboarding_calls
│
├── outputs
│   ├── accounts
│   │   └── <account_id>
│   │        ├── v1
│   │        └── v2
│   └── summary.json
│
└── README.md
```

---

# Input Dataset

The pipeline accepts **demo call transcripts and onboarding transcripts**.

Example:

```
data/demo_calls/demo1.txt
data/onboarding_calls/demo1.txt
```

Each pair corresponds to one client account.

---

# Output Structure

For each account the pipeline generates:

```
outputs/accounts/<account_id>/

v1/
    memo.json
    agent_spec.json

v2/
    memo.json
    agent_spec.json
    changes.md
```

Additionally:

```
outputs/summary.json
```

This file provides overall pipeline metrics.

---

# Account Memo Schema

Each account memo contains structured operational data:

```
account_id
company_name
business_hours
office_address
services_supported
emergency_definition
emergency_routing_rules
non_emergency_routing_rules
call_transfer_rules
integration_constraints
after_hours_flow_summary
office_hours_flow_summary
questions_or_unknowns
notes
```

This structured representation enables **consistent agent configuration generation**.

---

# Retell Agent Specification

The system generates a **Retell agent configuration draft** including:

* Agent name
* Voice style
* System prompt
* Key variables (business hours, routing rules, timezone)
* Call transfer protocol
* Transfer failure fallback logic
* Version identifier

This output can be used as a **template for creating agents in Retell**.

---

# Version Control and Change Tracking

The system preserves configuration history:

```
v1 → generated from demo call
v2 → updated from onboarding call
```

Changes are tracked in:

```
changes.md
```

Example:

```
business_hours updated
call_transfer_rules updated
```

This ensures configuration updates remain **transparent and traceable**.

---

# Running the Pipeline

Install dependencies:

```
pip install streamlit
```

Run the pipeline:

```
python scripts/pipeline.py
```

Example output:

```
Processing demo call for account: demo1
Applying onboarding update for account: demo1
Batch pipeline completed. Accounts processed: 3
```

Generated outputs will appear under:

```
outputs/accounts/
```

---

# Assignment Requirements and Implementation

This project was designed to satisfy the key requirements outlined in the Clara Answers assignment.  
The table below summarizes how each requirement is addressed in the system.

| Assignment Requirement | Implementation in This Project |
|---|---|
| Demo call → Preliminary agent configuration | The pipeline processes demo transcripts and generates a structured **Account Memo JSON** and **Agent Configuration v1**. |
| Onboarding update → Agent modification | Onboarding transcripts are processed by the **patch engine**, producing an updated **Agent Configuration v2**. |
| Structured operational data extraction | The **extraction engine** parses transcripts and converts them into a structured **Account Memo schema**. |
| Retell agent draft specification | The system generates a **Retell-compatible agent configuration template** including prompt structure, routing rules, and fallback logic. |
| Version control between demo and onboarding | The system stores **v1 and v2 configurations** separately and maintains configuration history. |
| Change tracking | A **changelog (`changes.md`)** records differences between v1 and v2 configurations. |
| Batch processing | The pipeline processes **multiple accounts automatically** from the dataset directories. |
| Reproducible pipeline | The system runs locally using **Python scripts and zero-cost tools**. |
| Structured outputs | All generated artifacts are stored as **versioned JSON files**. |
| Visualization / inspection interface | A **Streamlit dashboard** allows inspection of account configurations and version changes. |

---

# Launch the Dashboard

Run the Streamlit dashboard:

```
streamlit run dashboard/streamlit_app.py
```

The dashboard provides:

* Account selection
* Version 1 and Version 2 configuration comparison
* Change log visualization
* Pipeline metrics summary
* System architecture overview

---

# Dashboard Capabilities

The Streamlit dashboard enables:

Account configuration inspection
Version comparison (v1 vs v2)
Change log visualization
Pipeline metrics monitoring
System overview documentation

This interface allows users to **inspect and validate generated agent configurations**.

---

# Example Pipeline Summary

```
{
  "accounts_processed": 3,
  "v1_agents_generated": 3,
  "v2_updates": 3,
  "generated_at": "2026-03-04"
}
```

---

# Design Decisions

The system was designed with the following constraints:

Zero-cost tools only
Reproducible execution
No hallucination of missing operational data
Version-controlled configuration updates
Modular and extensible architecture

Extraction is implemented using **rule-based parsing** to comply with the **zero-cost requirement**.

---

# Potential Future Improvements

Speech-to-text transcription integration
Direct Retell API agent deployment
Database-backed configuration storage
Advanced NLP extraction models
Real-time onboarding pipeline
Automated workflow orchestration (n8n)

---

# Demonstration Video

Loom Demo (3–5 minutes)

```
<Insert Loom Video Link Here>
```

The demo shows:

Pipeline execution
Generated outputs
Agent configuration comparison
Dashboard visualization

---

# Author

S Sriram - 22BCE3761
B.Tech Computer Science and Engineering
VIT Vellore

---

# Summary

This project demonstrates how **human conversations can be transformed into structured AI agent configurations through automation**.

The system showcases:

Automation design
Version-controlled configuration management
Operational rule extraction
AI agent prompt generation
Pipeline monitoring and visualization

This approach enables scalable onboarding of AI voice agents for service businesses.
