import os
import json
import datetime
from logger import log
from extractor import extract_account_data
from agent_generator import generate_agent_spec
from patcher import apply_onboarding_patch


DATA_DEMO = "data/demo_calls/demo1.txt"
DATA_ONBOARD = "data/onboarding_calls/onboarding1.txt"

OUTPUT_BASE = "outputs/accounts"


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def run_demo(account_id, transcript):

    memo = extract_account_data(transcript, account_id)
    agent = generate_agent_spec(memo, "v1")

    base = f"{OUTPUT_BASE}/{account_id}/v1"

    save_json(f"{base}/memo.json", memo)
    save_json(f"{base}/agent_spec.json", agent)


def run_onboarding(account_id, transcript):

    v1_path = f"{OUTPUT_BASE}/{account_id}/v1/memo.json"

    with open(v1_path) as f:
        memo = json.load(f)

    onboarding_data = extract_account_data(transcript, account_id)

    updated_memo, changes = apply_onboarding_patch(memo, onboarding_data)

    agent = generate_agent_spec(updated_memo, "v2")

    base = f"{OUTPUT_BASE}/{account_id}/v2"

    save_json(f"{base}/memo.json", updated_memo)
    save_json(f"{base}/agent_spec.json", agent)

    with open(f"{base}/changes.md", "w") as f:
        for change in changes:
            f.write(f"- {change}\n")


if __name__ == "__main__":

    demo_dir = "data/demo_calls"
    onboarding_dir = "data/onboarding_calls"
    
    processed_accounts = 0
    v1_agents_generated = 0
    v2_updates = 0
    
    for file in os.listdir(demo_dir):
    
        if file.endswith(".txt"):
    
            account_id = file.replace(".txt", "")
    
            demo_path = f"{demo_dir}/{file}"
    
            with open(demo_path) as f:
                demo_transcript = f.read()
    
            log(f"Processing demo call for account: {account_id}")
    
            run_demo(account_id, demo_transcript)
            v1_agents_generated += 1
    
            onboarding_path = f"{onboarding_dir}/{file}"
    
            if os.path.exists(onboarding_path):
    
                with open(onboarding_path) as f:
                    onboarding_transcript = f.read()
    
                log(f"Applying onboarding update for account: {account_id}")
    
                run_onboarding(account_id, onboarding_transcript)
                v2_updates += 1
    
            processed_accounts += 1
    
    log(f"Batch pipeline completed. Accounts processed: {processed_accounts}")
    summary = {
        "accounts_processed": processed_accounts,
        "v1_agents_generated": v1_agents_generated,
        "v2_updates": v2_updates,
        "generated_at": str(datetime.datetime.now())
    }

    os.makedirs("outputs", exist_ok=True)

    with open("outputs/summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    log("Summary report generated at outputs/summary.json")