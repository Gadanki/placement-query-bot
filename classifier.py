from preprocessing import clean_text

# Define keywords for each category
keywords = {
    'results': ['result', 'shortlisted', 'selected', 'qualified', 'list out', 'announce', 'days', 'time'],
    'eligibility': ['eligible', 'eligibility', 'criteria', 'cgpa', 'backlogs', 'requirement'],
    'company info': ['company', 'companies', 'about', 'infosys', 'tcs', 'wipro', 'amazon', 'accenture', 'tech mahindra'],
    'important dates': ['date', 'deadline', 'last date', 'when', 'schedule', 'start', 'begin'],
    'procedure': ['procedure', 'process', 'steps', 'how to apply', 'register', 'registration']
}

def classify_query(text):
    text = clean_text(text)
    category_scores = {cat:0 for cat in keywords}

    for cat, words in keywords.items():
        for w in words:
            if w in text:
                category_scores[cat] += 1

    # Pick category with highest count of matches
    max_category = max(category_scores, key=category_scores.get)
    if category_scores[max_category] == 0:
        return 'unknown'
    return max_category

# Test it
if __name__ == "__main__":
    query = input("Enter your query: ")
    result = classify_query(query)
    print("Category:", result)