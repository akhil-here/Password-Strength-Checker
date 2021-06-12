import pandas as pd
import numpy as np
import warnings
import random

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

warnings.filterwarnings('ignore')


def read_file():
    data = pd.read_csv('data.csv', error_bad_lines=False)
    return data


def preprocess(data):
    data.dropna(inplace=True)
    return data


def input_provider(data):
    data_array = np.array(data)
    random.shuffle(data_array)

    x = [labels[0] for labels in data_array]
    y = [labels[1] for labels in data_array]

    return x, y


def word_divide(text):
    char = []
    for i in text:
        char.append(i)
    return char


def vectorize(word_divide, x):
    vectorizer = TfidfVectorizer(tokenizer=word_divide)
    X = vectorizer.fit_transform(x)

    return X


def model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    clf = LogisticRegression(random_state=101, multi_class='multinomial')
    clf.fit(X_train, y_train)

    return clf


def main():
    data = read_file()
    data = preprocess(data)
    x, y = input_provider(data)
    X = vectorize(word_divide, x)
    m = model(X, y)
    vectorizer = TfidfVectorizer(tokenizer=word_divide)
    return vectorizer, x, m


vectorizer, x, m = main()
