import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

def train():
    model = SentenceTransformer('all-MiniLM-L6-v2')

    df = pd.read_csv('data/train.csv')
    dialogues = df['quote'].tolist()
    embeddings = model.encode(dialogues, convert_to_tensor=False)

    np.save('model/dialogue_embeddings.npy', embeddings)
    np.save('model/dialogue_texts.npy', dialogues)

if __name__ == "__main__":
    train()
