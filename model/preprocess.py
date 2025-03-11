import pandas as pd
from sklearn.model_selection import train_test_split
import re

def clean_text(text):
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'[^a-zA-Z0-9,.!?\' ]+', '', text)
    return text.strip()

def preprocess(input_file='data/phoebe_quotes.csv'):
    df = pd.read_csv(input_file)

    df['quote'] = df['quote'].apply(clean_text)
    df = df[df['quote'].str.len() > 5]

    df['quote'] = '<START> ' + df['quote'] + ' <END>'

    df_train, df_test = train_test_split(df, test_size=0.1, random_state=42)

    df_train.to_csv('data/train.csv', index=False)
    df_test.to_csv('data/test.csv', index=False)

if __name__ == "__main__":
    preprocess()
