def classify_query(query: str) -> str:
    if any(word in query.lower() for word in ["cover", "covered", "included"]):
        return "coverage"
    elif "exclude" in query.lower():
        return "exclusion"
    elif "copay" in query.lower():
        return "co-pay"
    else:
        return "general"
