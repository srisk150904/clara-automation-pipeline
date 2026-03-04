def apply_onboarding_patch(v1_memo, onboarding_data):

    changes = []
    
    for key in onboarding_data:
    
        new_value = onboarding_data[key]
        old_value = v1_memo.get(key)
    
        if new_value and new_value != old_value:
    
            v1_memo[key] = new_value
    
            change_record = f"{key}: {old_value} → {new_value}"
            changes.append(change_record)
    
    return v1_memo, changes