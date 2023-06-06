import spacy


def get_keyword_matching_score(model_answer, keywords, answer):
    nlp = spacy.load('en_core_web_sm')
    doc_model = nlp(model_answer)
    doc_answer = nlp(answer)

    # Convert keywords to lowercase
    keywords = [keyword.lower() for keyword in keywords]

    # Extract keywords from model answer
    model_keywords = [token.text.lower()
                      for token in doc_model if token.text.lower() in keywords]

    # Extract keywords from answer
    answer_keywords = [token.text.lower()
                       for token in doc_answer if token.text.lower() in keywords]

    # Calculate keyword occurrences in model answer
    model_keyword_occurrences = sum(
        [model_keywords.count(keyword) for keyword in keywords])

    # Calculate keyword occurrences in answer
    answer_keyword_occurrences = sum(
        [answer_keywords.count(keyword) for keyword in keywords])

    # Calculate keyword matching score
    keyword_matching_score = answer_keyword_occurrences / \
        model_keyword_occurrences if model_keyword_occurrences > 0 else 0

    # Map keyword matching score to a scale of 1 to 6
    keyword_matching_score = 6 - int(keyword_matching_score * 5)

    return keyword_matching_score
