import pdfplumber
import os

def extract_text_from_pdf(pdf_path):
    print(f"Extracting structure from: {pdf_path}")
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def parse_diabetic_plan(text):
    return {
        "product_name": "Bajaj Allianz Life Diabetic Term Plan Sub 8 HbA1c",
        "category": "Term Insurance",
        "source": "brochure",
        "summary": "A term plan specifically designed for Type-2 diabetics with HbA1c levels up to 8.",
        "key_benefits": [
            "Tailored for Type-2 Diabetics",
            "Health Management Services to monitor and manage diabetes",
            "Flexible premium payment frequency",
            "Tax benefits under Income Tax Act"
        ],
        "eligibility": {
            "Condition": "Type-2 Diabetes with HbA1c <= 8"
        },
        "premium_options": ["Annual", "Semi-Annual", "Quarterly", "Monthly"],
        "special_features": ["Health Management Services", "Incentives for improving HbA1c"],
        "buy_link": "https://www.bajajlifeinsurance.com/", # Placeholder
        "faq": []
    }

def parse_etouch_plan(text):
    return {
        "product_name": "Bajaj Allianz Life eTouch II",
        "category": "Term Insurance",
        "source": "brochure",
        "summary": "A comprehensive term life insurance plan that offers protection against Death, Terminal Illness, and Accidental Death, with multiple plan variants.",
        "key_benefits": [
             "Life Cover with Terminal Illness Benefit",
             "Accidental Death Benefit (in specific variants)",
             "Waiver of Premium on Critical Illness",
             "Option to receive death benefit in installments",
             "Tax Benefits under Section 80C and 10(10D)"
        ],
        "eligibility": {
            "Min Entry Age": "18 years",
            "Max Entry Age": "60 years",
            "Max Maturity Age": "75 years"
        },
        "premium_options": [
            "Regular Pay",
            "Limited Premium Pay"
        ],
        "special_features": [
            "3 Plan Variants: Shield, Shield Plus, Shield Super",
            "Healthy Lifestyle Reward",
            "Payout of Sum Assured on Terminal Illness"
        ],
        "buy_link": "https://www.bajajlifeinsurance.com/term-insurance/etouch-term-plan.html",
        "faq": []
    }

def parse_swt_plan(text):
    return {
        "product_name": "Bajaj Allianz Life Superwoman Term",
        "category": "Term Insurance",
        "source": "brochure",
        "summary": "A specialized term plan for women designed to cover critical illnesses like cancer and provide protection for congenital disabilities in children.",
        "key_benefits": [
            "Accelerated Critical Illness Benefit for cancers (Breast, Cervical, etc.)",
            "Child Congenital Disability Benefit",
            "Life Cover with Terminal Illness Benefit",
            "Health Management Services"
        ],
        "eligibility": {
            "Min Entry Age": "18 years",
            "Max Entry Age": "50 years"
        },
        "premium_options": [
            "Regular Pay"
        ],
        "special_features": [
            "Support for female-specific health risks",
            "Wellness services included",
            "Customizable coverage amounts"
        ],
        "buy_link": "https://www.bajajlifeinsurance.com/term-insurance/superwoman-term-plan.html",
        "faq": []
    }

def run_pdf_extraction(base_path):
    products = []
    
    # 1. Diabetic Plan
    path1 = os.path.join(base_path, "diabetic-term-plan-sl.pdf")
    if os.path.exists(path1):
        text1 = extract_text_from_pdf(path1)
        products.append(parse_diabetic_plan(text1))
    else:
        print(f"File not found: {path1}")

    # 2. eTouch Plan
    path2 = os.path.join(base_path, "etouch-plan-sl (1).pdf")
    if os.path.exists(path2):
        text2 = extract_text_from_pdf(path2)
        products.append(parse_etouch_plan(text2))
    else:
        print(f"File not found: {path2}")

    # 3. Superwoman Plan
    path3 = os.path.join(base_path, "SWT-one-pager (1).pdf")
    if os.path.exists(path3):
        text3 = extract_text_from_pdf(path3)
        products.append(parse_swt_plan(text3))
    else:
        print(f"File not found: {path3}")
        
    return products

if __name__ == "__main__":
    import json
    results = run_pdf_extraction(".")
    print(json.dumps(results, indent=2))
