import os
import pandas as pd
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')  # small and fast
FAQ_DIR = "faq_data"

def get_semantic_faq_answer(user_query):
    best_score = 0.0
    best_answer = None

    user_embedding = model.encode(user_query, convert_to_tensor=True)

    for file in os.listdir(FAQ_DIR):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(FAQ_DIR, file))
            questions = df["question"].tolist()
            answers = df["answer"].tolist()

            question_embeddings = model.encode(questions, convert_to_tensor=True)
            similarities = util.pytorch_cos_sim(user_embedding, question_embeddings)[0]

            max_score = similarities.max().item()
            best_idx = similarities.argmax().item()

            if max_score > best_score and max_score >= 0.65:
                best_score = max_score
                best_answer = answers[best_idx]

    return best_answer
