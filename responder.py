from classifier import classify_query
from preprocessing import clean_text
from semantic_faq_retriever import get_semantic_faq_answer
from gsheet_logger import log_query

known_companies = [
    "google", "microsoft", "amazon", "apple", "meta", "adobe",
    "infosys", "tcs", "wipro", "hcl technologies", "accenture", "ibm",
    "deloitte", "capgemini", "cognizant", "oracle", "samsung", "qualcomm",
    "intel", "jp morgan chase", "goldman sachs", "flipkart", "reliance industries",
    "larsen & toubro", "cisco", "zomato", "paytm", "uber", "nvidia", "ey (ernst&young)"
]

#template responses
def get_response(category, query):
    query = clean_text(query)

    #Trys to detect the company name in the query
    company_mentioned = None
    for company in known_companies:
        if company in query:
            company_mentioned = company.title()
            break
    
    #Response templates
    if category == "eligibility":
        if company_mentioned:
            return f"To be eligible for {company_mentioned}, you usually need a minimum CGPA of 7.0 and no active backlogs."
        return "To be eligible, you need a minimum CGPA of 7.0 and no active backlogs"
    
    elif category == "company info":
        if company_mentioned:
            return f"{company_mentioned} is one of the top recruiters. It offers roles in software development, testing, and consulting."
        return "Our college is partnered with companies like Infosys, TCS, Wipro, Amazon, and Accenture."

    elif category == "important dates":
        if company_mentioned:
            return f"The placement drive for {company_mentioned} typically starts in August or September."
        return "The placement drive starts in August. Check the placement portal for detailed schedule updates."

    elif category == "procedure":
        return "You must register on the placement portal and attend the pre-placement talk. Follow the instructions shared by the placement cell."

    elif category == "results":
        if company_mentioned:
            return f"Results for {company_mentioned} are usually announced a week after interview. Keep checking your registered email or {company_mentioned} portal"
        return "Results are usually announced a week after the interviews. Keep checking your registered email or portal."

    else:
        return None

def generate_response(query):
    category = classify_query(query)
    return get_response(category, query)

# Test it
if __name__ == "__main__":
    user_query = input("Ask a placement-related question: ")
    answer = generate_response(user_query)
    print("Bot:", answer)

def generate_response(query):
    # First try FAQ match
    faq_answer = get_semantic_faq_answer(query)
    if faq_answer:
        log_query(query, "FAQ")  #To store user queries in CSV this line is added
        return faq_answer

    # Fallback to template logic
    category = classify_query(query)
    response = get_response(category, query)
    if response:
        log_query(query, "FAQ") #To store user queries in CSV this line is added
        return response
    
    
    fallback = (
        "🤖I'm not sure how to answer that yet.\n"
        "Please contact your placement officer (Or my owner-admin of this page😉) or try rephrasing your question."
    )
    log_query(query, "Unknown")
    return fallback

