import re

from nltk import WordNetLemmatizer


class LemmaTokenizer:
    def __init__(self, pattern_token=r'(?u)(\b[a-z]{3,}\b)'):
        self.lemmatizer = WordNetLemmatizer()
        self.__regex_token = re.compile(pattern_token)

    def __call__(self, sentence):
        tokens = []
        for match in self.__regex_token.finditer(sentence):
            start, end = match.start(), match.end()
            token_text = sentence[start: end]
            token_text_lemmatized = self.lemmatizer.lemmatize(token_text)
            tokens.append(token_text_lemmatized)

        return tokens
