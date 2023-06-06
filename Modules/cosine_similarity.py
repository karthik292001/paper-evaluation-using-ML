import re
import math
from collections import Counter
from fuzzywuzzy import fuzz

WORD = re.compile(r'\w+')


def get_cosine(vec1, vec2):
    """
    Calculate cosine similarity between two word frequency vectors.
    """
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    """
    Convert text to word frequency vector.
    """
    words = WORD.findall(text)
    return Counter(words)


def givKeywordsValue(text1, text2):
    """
    Calculate keyword value based on cosine similarity between two texts.
    """
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    cosine_similarity = round(get_cosine(vector1, vector2), 2) * 100

    # Fine-tune keyword value based on cosine similarity
    keyword_value = 0
    if cosine_similarity > 90:
        keyword_value = 1
    elif cosine_similarity > 80:
        keyword_value = 2
    elif cosine_similarity > 70:
        keyword_value = 3
    elif cosine_similarity > 60:
        keyword_value = 4
    elif cosine_similarity > 50:
        keyword_value = 5
    else:
        keyword_value = 6

    # Further refine keyword value based on fuzzywuzzy token set ratio
    token_set_ratio = fuzz.token_set_ratio(text1, text2)
    if token_set_ratio > 80:
        keyword_value = max(1, keyword_value)
    elif token_set_ratio > 60:
        keyword_value = max(2, keyword_value)

    return keyword_value
