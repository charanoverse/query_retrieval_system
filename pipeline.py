from agents.agent1_query_classifier import classify_query
from agents.agent2_info_extractor import extract_info
from agents.agent3_clause_retriever import retrieve_clause
from agents.agent4_reasoning_agent import reason_over_clause
from agents.agent5_verdict_formatter import format_verdict

def run_chain(query: str):
    intent = classify_query(query)
    info = extract_info(query)
    clause = retrieve_clause(query)
    reasoning = reason_over_clause(clause, info)
    verdict = format_verdict(reasoning)

    return {
        "query": query,
        "intent": intent,
        "extracted_info": info,
        "retrieved_clause": clause,
        "reasoning": reasoning,
        "verdict": verdict
    }
