import re
from textblob import TextBlob

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Test it
if __name__ == "__main__":
    sample = input("Enter query: ")
    cleaned = clean_text(sample)
    print("Original:", sample)
    print("Cleaned:", cleaned)
