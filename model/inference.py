import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class PhoebeBot:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = np.load('model/dialogue_embeddings.npy')
        self.dialogues = np.load('model/dialogue_texts.npy', allow_pickle=True)

    def get_response(self, query):
        query_embed = self.model.encode([query])
        similarity = cosine_similarity(query_embed, self.embeddings)[0]
        best_idx = similarity.argmax()
        return self.dialogues[best_idx].replace('<START> ', '').replace(' <END>', '')

if __name__ == "__main__":
    bot = PhoebeBot()
    while True:
        q = input("You: ")
        ans = bot.get_response(q)
        print(f"Phoebe: {ans}")
