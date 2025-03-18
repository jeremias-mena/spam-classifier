import math
from typing import Set, Iterable, Tuple, Dict, List
from collections import defaultdict
from spam_classifier.utils import Message, Utils

class NaiveBayesClf:
    def __init__(self, k: float = 0.5):
        self.k = k
        self.spam_msgs = 0
        self.ham_msgs = 0
        
        self.tokens: Set[str] = set()
        self.token_spam_counts: Dict[str, int] = defaultdict(int)
        self.token_ham_counts: Dict[str, int] = defaultdict(int)
        
    def train(self, messages: Iterable[Message]) -> None:
        for message in messages:
            if message.is_spam:
                self.spam_msgs += 1
            else:
                self.ham_msgs += 1
        
        for token in Utils().tokenize(message.text):
            self.tokens.add(token)
            if message.is_spam:
                self.token_spam_counts += 1
            else:
                self.token_ham_counts += 1

    def probabilities(self, token:str) -> Tuple[float, float]:
        spam = self.token_spam_counts[token]
        ham = self.token_ham_counts[token]

        prob_token_spam = (spam + self.k) / (self.spam_msgs + 2 * self.k)
        prob_token_ham = (ham + self.k) / (self.ham_msgs + 2 * self.k)

        return prob_token_spam, prob_token_ham
    
    def predict(self, text: str) -> float:
        text_tokens = Utils().tokenize(text)
        log_prob_spam = 0
        log_prob_ham = 0

        for token in self.tokens:
            prob_spam, prob_ham = self.probabilities(token)

            if token in text_tokens:
                log_prob_spam += math.log(prob_spam)
                log_prob_ham += math.log(prob_ham)
            else:
                log_prob_spam += math.log(1.0 - prob_spam)
                log_prob_ham += math.log(1.0 - prob_ham)

        prob_spam = math.exp(log_prob_spam)
        prob_ham = math.exp(log_prob_ham)

        result = prob_spam / (prob_spam + prob_ham)

        return result
    
    def prob_spam_given_token(self, token:str) -> float:
        prob_spam, prob_ham = self.probabilities(token)
        result = prob_spam / (prob_spam + prob_ham)
        return result
        