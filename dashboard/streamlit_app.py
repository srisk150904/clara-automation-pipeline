import streamlit as st
import json
import os

st.set_page_config(page_title="Clara Automation Dashboard", layout="wide")

st.title("Clara Automation Pipeline Dashboard")

# ---------------------------
# Sidebar Navigation
# ---------------------------

page = st.sidebar.selectbox(
    "Navigation",
    ["Dashboard (Results)", "Project Overview"]
)

BASE_PATH = "outputs/accounts"

# ---------------------------
# PROJECT OVERVIEW PAGE
# ---------------------------

if page == "Project Overview":

    st.header("Project Overview")

    st.markdown("""
This project implements an **automated pipeline** that converts **client demo calls**
and **onboarding updates** into structured configurations for an **AI voice answering agent**.

The system extracts operational rules from transcripts and generates a **Retell AI Agent specification**
that can be used to configure automated inbound call handling.
""")

    st.subheader("Problem Context")

    st.markdown("""
Service companies (HVAC, electrical, fire protection, etc.) receive large volumes of inbound calls.

Calls must be routed differently depending on:

- Business hours
- Emergency situations
- Service type
- Dispatch availability

Manually configuring these workflows for every customer is slow and error-prone.
This pipeline automates the process.
""")

    st.subheader("Pipeline Workflow")

    st.code("""
Demo Call Transcript
        ↓
Extraction Engine
        ↓
Structured Account Memo
        ↓
Agent Spec Generator
        ↓
Agent Configuration (v1)

Onboarding Transcript
        ↓
Patch Engine
        ↓
Updated Agent Configuration (v2)
        ↓
Change Log
        ↓
Dashboard Visualization
""")

    st.subheader("Key Features")

    st.markdown("""
✔ Transcript data extraction  
✔ Structured account configuration schema  
✔ Retell agent prompt generation  
✔ Version control (v1 → v2 updates)  
✔ Change tracking  
✔ Batch processing for multiple accounts  
✔ Monitoring dashboard
""")

    st.stop()

# ---------------------------
# DASHBOARD PAGE
# ---------------------------

st.markdown(
"""
This dashboard visualizes the automated pipeline that converts **demo call transcripts**
and **onboarding updates** into structured **Retell AI agent configurations**.

Pipeline stages:

Demo Call → Account Memo → Agent Spec v1 → Onboarding Update → Agent Spec v2 → Change Log
"""
)

# Load accounts
if not os.path.exists(BASE_PATH):
    st.error("No outputs found. Run the pipeline first.")
    st.stop()

accounts = sorted(os.listdir(BASE_PATH))

st.sidebar.header("Accounts")

selected_account = st.sidebar.selectbox(
    "Select Account",
    accounts
)

st.sidebar.success("Pipeline ready")

account_path = f"{BASE_PATH}/{selected_account}"

st.header(f"Account: {selected_account}")

tab1, tab2 = st.tabs(["Version 1 (Demo)", "Version 2 (Onboarding)"])

# ----------------------
# VERSION 1
# ----------------------

with tab1:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Account Memo (v1)")

        memo_path = f"{account_path}/v1/memo.json"

        if os.path.exists(memo_path):

            with open(memo_path) as f:
                memo = json.load(f)

            with st.expander("View Memo JSON", expanded=True):
                st.json(memo)

        else:
            st.warning("Memo file not found")

    with col2:

        st.subheader("Agent Configuration (v1)")

        agent_path = f"{account_path}/v1/agent_spec.json"

        if os.path.exists(agent_path):

            with open(agent_path) as f:
                agent = json.load(f)

            with st.expander("View Agent Spec JSON", expanded=True):
                st.json(agent)

        else:
            st.warning("Agent spec not found")

# ----------------------
# VERSION 2
# ----------------------

with tab2:

    v2_path = f"{account_path}/v2"

    if os.path.exists(v2_path):

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Account Memo (v2)")

            memo_path = f"{v2_path}/memo.json"

            if os.path.exists(memo_path):

                with open(memo_path) as f:
                    memo = json.load(f)

                with st.expander("View Memo JSON", expanded=True):
                    st.json(memo)

            else:
                st.warning("Memo file not found")

        with col2:

            st.subheader("Agent Configuration (v2)")

            agent_path = f"{v2_path}/agent_spec.json"

            if os.path.exists(agent_path):

                with open(agent_path) as f:
                    agent = json.load(f)

                with st.expander("View Agent Spec JSON", expanded=True):
                    st.json(agent)

            else:
                st.warning("Agent spec not found")

        st.subheader("Change Log")

        changelog_file = f"{v2_path}/changes.md"

        if os.path.exists(changelog_file):

            with open(changelog_file) as f:
                changes = f.read()

            st.code(changes)

        else:
            st.info("No changes detected")

    else:

        st.warning("No onboarding update available for this account.")

# ----------------------
# PIPELINE SUMMARY
# ----------------------

st.divider()
st.header("Pipeline Summary")

summary_path = "outputs/summary.json"

if os.path.exists(summary_path):

    with open(summary_path) as f:
        summary = json.load(f)

    col1, col2, col3 = st.columns(3)

    col1.metric("Accounts Processed", summary["accounts_processed"])
    col2.metric("Agents Generated (v1)", summary["v1_agents_generated"])
    col3.metric("Agent Updates (v2)", summary["v2_updates"])

    st.subheader("Raw Summary Data")

    st.json(summary)

else:

    st.warning("Summary file not found. Run pipeline first.")