def generate_agent_spec(memo, version):

    company = memo.get("company_name", "Service Company")

    prompt = f"""
You are the AI answering agent for {company}.

BUSINESS HOURS FLOW
1. Greet the caller professionally.
2. Ask the reason for the call.
3. Collect caller name and phone number.
4. Route or transfer the call appropriately.
5. If transfer fails, inform the caller someone will follow up.
6. Ask if they need anything else.
7. Close the call politely.

AFTER HOURS FLOW
1. Greet the caller.
2. Ask purpose of call.
3. Confirm if it is an emergency.
4. If emergency, collect name, phone number and address immediately.
5. Attempt transfer to emergency contact.
6. If transfer fails, assure the caller someone will follow up quickly.
7. If not emergency, collect message and confirm follow up during business hours.
8. Ask if they need anything else.
9. Close the call.
"""

    agent = {
        "agent_name": f"{company}_agent",
        "version": version,
        "voice_style": "professional",
        "system_prompt": prompt,
        "key_variables": {
            "business_hours": memo.get("business_hours"),
            "emergency_definition": memo.get("emergency_definition")
        },
        "call_transfer_protocol": "transfer to dispatch team if required",
        "fallback_protocol": "collect caller details and notify team"
    }

    return agent