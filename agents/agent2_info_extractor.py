import re

def extract_info(query: str) -> dict:
    info = {}
    if "cataract" in query.lower():
        info["procedure"] = "cataract"
    if "knee" in query.lower():
        info["procedure"] = "knee surgery"
    
    age_match = re.search(r"\b(\d{2})\b", query)
    if age_match:
        info["age"] = int(age_match.group(1))
    
    if "month" in query.lower():
        duration_match = re.search(r"(\d+)\s*month", query)
        if duration_match:
            info["policy_duration"] = int(duration_match.group(1))
    
    return info
