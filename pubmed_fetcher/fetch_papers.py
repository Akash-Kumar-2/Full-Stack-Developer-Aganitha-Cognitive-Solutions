import requests
from typing import List, Dict

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_paper_ids(query: str, max_results: int = 10) -> List[str]:
    """Fetches paper IDs from PubMed."""
    params = {"db": "pubmed", "term": query, "retmax": max_results, "retmode": "json"}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json().get("esearchresult", {}).get("idlist", [])

def fetch_paper_details(paper_ids: List[str]) -> List[Dict]:
    """Fetch detailed information for a list of PubMed paper IDs."""
    if not paper_ids:
        return []
    
    params = {"db": "pubmed", "id": ",".join(paper_ids), "retmode": "json"}
    response = requests.get(DETAILS_URL, params=params)
    response.raise_for_status()
    
    # Extract dictionary values properly
    paper_data = response.json().get("result", {})
    
    # Filter out invalid keys (PubMed sometimes includes "uids" as a key)
    return [paper for key, paper in paper_data.items() if key.isdigit()]
