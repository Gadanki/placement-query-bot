import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

FAQ_DIR = "faq_data"


def get_all_faq_answers(user_query):
    best_match = None
    highest_score = 0
    best_answer = None

    for file in os.listdir(FAQ_DIR):
        if file.endswith(".csv"):
            path = os.path.join(FAQ_DIR, file)
            df = pd.read_csv(path)

            questions = df["question"].tolist()
            answers = df["answer"].tolist()

            vectorizer = TfidfVectorizer()
            X = vectorizer.fit_transform(questions + [user_query])
            sim = cosine_similarity(X[-1], X[:-1])[0]

            max_sim = max(sim)
            if max_sim > highest_score and max_sim >= 0.6:
                best_match = questions[sim.argmax()]
                best_answer = answers[sim.argmax()]
                highest_score = max_sim

    return best_answer if best_answer else None