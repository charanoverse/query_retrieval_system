def format_verdict(reasoning: str) -> dict:
    if "❌" in reasoning:
        return {
            "status": "Rejected",
            "explanation": reasoning
        }
    elif "✅" in reasoning:
        return {
            "status": "Approved",
            "explanation": reasoning
        }
    else:
        return {
            "status": "Undetermined",
            "explanation": reasoning
        }
