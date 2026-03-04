import re

def extract_account_data(transcript, account_id):

    transcript_lower = transcript.lower()

    data = {
        "account_id": account_id,
        "company_name": account_id.replace("_", " ").title(),
        "business_hours": None,
        "office_address": None,
        "services_supported": [],
        "emergency_definition": [],
        "emergency_routing_rules": None,
        "non_emergency_routing_rules": None,
        "call_transfer_rules": None,
        "integration_constraints": [],
        "after_hours_flow_summary": None,
        "office_hours_flow_summary": None,
        "questions_or_unknowns": [],
        "notes": "Extracted automatically from transcript"
    }

    # detect email and phone
    emails = re.findall(r'\S+@\S+', transcript)
    phones = re.findall(r'\+?\d[\d\s\-]{8,}', transcript)

    if emails:
        data["notes"] += f" Email detected: {emails[0]}"

    if phones:
        data["notes"] += f" Contact phone detected: {phones[0]}"

    # detect services
    if "electric" in transcript_lower:
        data["services_supported"].append("electrical services")

    if "hvac" in transcript_lower:
        data["services_supported"].append("hvac services")

    if "sprinkler" in transcript_lower:
        data["services_supported"].append("sprinkler services")

    if "fire alarm" in transcript_lower:
        data["services_supported"].append("fire alarm systems")

    # detect emergency triggers
    if "emergency" in transcript_lower:
        data["emergency_definition"].append("customer states emergency situation")

    # detect transfer rules
    if "transfer" in transcript_lower or "dispatch" in transcript_lower:
        data["call_transfer_rules"] = "transfer call to dispatch team"

    # detect business hours
    if "monday" in transcript_lower or "friday" in transcript_lower:
        data["business_hours"] = "mentioned in transcript"

    # unknowns
    if data["business_hours"] is None:
        data["questions_or_unknowns"].append("business hours not specified")

    if not data["emergency_definition"]:
        data["questions_or_unknowns"].append("emergency rules not clearly defined")

    return data