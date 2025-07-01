# obs_system_app/recommendation/utils.py

import os
import pickle

def load_similarity_matrix():
    path = os.path.join(os.path.dirname(__file__), "item_similarity.pkl")
    with open(path, "rb") as f:
        similarity_df = pickle.load(f)
    return similarity_df


def recommend(subjects_taken, similarity_df, top_n=5):
    scores = {}
    for subject in subjects_taken:
        if subject in similarity_df.index:
            similar_items = similarity_df[subject]
            for other_subject, score in similar_items.items():
                if other_subject != subject and other_subject not in subjects_taken:
                    scores[other_subject] = scores.get(other_subject, 0) + score
    sorted_recommendations = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [subject for subject, _ in sorted_recommendations[:top_n]]
