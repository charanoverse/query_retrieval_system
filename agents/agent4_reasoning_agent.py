def reason_over_clause(clause: str, extracted_info: dict) -> str:
    # Hardcoded logic for MVP
    if "cataract" in clause.lower() and "24 month" in clause.lower():
        if extracted_info.get("policy_duration", 0) < 24:
            return "Policy duration < 24 months → ❌ Rejected"
        else:
            return "Eligible → ✅ Approved"
    return "Not enough info to decide"
