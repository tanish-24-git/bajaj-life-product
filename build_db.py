import json
import os
import pdf_parser
import web_scraper

OUTPUT_FILE = "bajaj_term_products.json"

def main():
    print("Starting Knowledge DB Build Process...")
    
    all_products = []

    # 1. PDF Extraction
    print("Step 1: Parsing PDFs...")
    # Use current directory as base
    pdf_products = pdf_parser.run_pdf_extraction(".")
    print(f"Extracted {len(pdf_products)} products from PDFs.")
    all_products.extend(pdf_products)

    # 2. Web Scraping
    print("Step 2: Scraping Website...")
    web_products = web_scraper.scrape_term_products()
    print(f"Scraped {len(web_products)} products from Website.")
    all_products.extend(web_products)

    # 3. Save to JSON
    print(f"Step 3: Saving to {OUTPUT_FILE}...")
    db = {"products": all_products}
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4)
        
    print("Done!")

if __name__ == "__main__":
    main()
