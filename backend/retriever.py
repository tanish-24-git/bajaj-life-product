import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "bajaj_term_products.json")

def load_products():
    with open(DB_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("products", [])

def retrieve_products(query, products):
    """
    Simple keyword-based retrieval.
    """
    query_tokens = query.lower().split()
    matches = []
    
    for p in products:
        # Create a searchable string from relevant fields
        search_text = f"{p['product_name']} {p.get('summary', '')} {' '.join(p.get('key_benefits', []))} {' '.join(p.get('special_features', []))}".lower()
        
        # logical OR: if any token matches, it's a candidate (can be refined to AND for stricter match)
        score = sum(1 for token in query_tokens if token in search_text)
        
        if score > 0:
            matches.append((score, p))
            
    # Sort by score desc
    matches.sort(key=lambda x: x[0], reverse=True)
    
    # Return top 3
    return [m[1] for m in matches[:3]]
