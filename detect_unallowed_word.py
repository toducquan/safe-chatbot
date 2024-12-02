import spacy
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from fuzzywuzzy import process

nlp = spacy.load("en_core_web_md")

UNALLOWED_WORDS= [
    "hack", "scam", "cheat", "plagiarism", "fuck", "steal",
    "hacking", "scamming", "cheating"
]
SIMILARITY_THRESHOLD = 0.85

def pre_processing_sentence(text):
    words = text.lower().split()
    cleaned_words = [
        process.extractOne(
            ''.join(filter(str.isalnum, word)),
            UNALLOWED_WORDS
        )[0] if any(c in word for c in "@*!") else word
        for word in words
    ]
    return ' '.join(cleaned_words)

def detect_unallowed_word(sentence):
    sentence_doc = nlp(pre_processing_sentence(sentence))
    sentence_vectors = np.array([token.vector for token in sentence_doc])
    unallowed_vectors = np.array([nlp(text).vector for text in UNALLOWED_WORDS])

    for token_vec in sentence_vectors:
        similarities = cosine_similarity([token_vec], unallowed_vectors)[0]
        if any(sim > SIMILARITY_THRESHOLD for sim in similarities):
            return True
    return False