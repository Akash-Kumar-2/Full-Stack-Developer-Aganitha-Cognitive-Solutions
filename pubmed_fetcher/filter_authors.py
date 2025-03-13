from typing import List, Dict

NON_ACADEMIC_KEYWORDS = ["pharma", "biotech", "inc.", "corp", "ltd", "gmbh"]

def is_non_academic(affiliation: str) -> bool:
    """Determines if an author is affiliated with a company rather than an academic institution."""
    academic_keywords = ["university", "college", "institute", "lab", "hospital"]
    return not any(keyword in affiliation.lower() for keyword in academic_keywords)

def extract_non_academic_authors(paper_data: Dict) -> List[str]:
    """Extracts non-academic authors based on affiliation keywords."""
    authors = paper_data.get("authors", [])
    return [
        author.get("name", "Unknown")
        for author in authors
        if is_non_academic(author.get("affiliation", ""))
    ]

def extract_company_affiliations(paper_data: Dict) -> List[str]:
    """Identifies company names from author affiliations."""
    return list(
        {
            author.get("affiliation", "Unknown")
            for author in paper_data.get("authors", [])
            if any(keyword in author.get("affiliation", "").lower() for keyword in NON_ACADEMIC_KEYWORDS)
        }
    )
