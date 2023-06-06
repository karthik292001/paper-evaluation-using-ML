import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.parse import CoreNLPParser
from nltk.tree import Tree

# Initialize CoreNLPParser
parser = CoreNLPParser(url='http://localhost:9000')

# Define function to check for grammar errors


def grammar_error_count(text,k):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)

    # Initialize error count
    error_count = 0

    # Loop through sentences
    for sentence in sentences:
        # Parse sentence using CoreNLPParser
        parse_tree = next(parser.parse(sentence.split()))

        # Count number of NP (noun phrase) nodes in the parse tree
        np_count = len(list(parse_tree.subtrees(
            filter=lambda x: x.label() == 'NP')))

        # Count number of VP (verb phrase) nodes in the parse tree
        vp_count = len(list(parse_tree.subtrees(
            filter=lambda x: x.label() == 'VP')))

        # Calculate difference between NP and VP counts
        count_diff = abs(np_count - vp_count)

        # If difference is greater than 5, increment error count
        if count_diff > 5:
            error_count += 1

    # If error count is greater than 0, return 0; else return 1
    if error_count > 5:
        return 0
    else:
        return 1
