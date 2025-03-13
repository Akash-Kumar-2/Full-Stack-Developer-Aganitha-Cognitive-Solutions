import csv
from typing import List, Dict

def save_to_csv(papers: List[Dict], filename: str):
    """Saves paper data to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["PubmedID", "Title", "Publication Date", "Non-academic Authors", "Company Affiliations", "Corresponding Author Email"])
        
        for paper in papers:
            writer.writerow([
                paper.get("uid", ""),
                paper.get("title", ""),
                paper.get("pubdate", ""),
                ", ".join(paper.get("non_academic_authors", [])),
                ", ".join(paper.get("company_affiliations", [])),
                paper.get("corresponding_email", "Unknown")
            ])
