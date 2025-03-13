import argparse
from pubmed_fetcher.fetch_papers import fetch_paper_ids, fetch_paper_details
from pubmed_fetcher.filter_authors import extract_non_academic_authors, extract_company_affiliations
from pubmed_fetcher.csv_writer import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers and save results to CSV.")
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results", default="results.csv")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()
    
    paper_ids = fetch_paper_ids(args.query)
    papers = fetch_paper_details(paper_ids)
    
    for paper in papers:
        paper["non_academic_authors"] = extract_non_academic_authors(paper)
        paper["company_affiliations"] = extract_company_affiliations(paper)

    save_to_csv(papers, args.file)
    print(f"Results saved to {args.file}")

if __name__ == "__main__":
    main()
