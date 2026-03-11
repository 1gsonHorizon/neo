# Modèles de Machine Learning pour NEO
import numpy as np
from collections import Counter

class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

    def forward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2

    def predict(self, X):
        output = self.forward(X)
        return (output > 0.5).astype(int)

class TextClassifier:
    def __init__(self):
        self.word_freq = Counter()
        self.categories = {}

    def train(self, texts, labels):
        for text, label in zip(texts, labels):
            if label not in self.categories:
                self.categories[label] = Counter()
            
            words = text.lower().split()
            for word in words:
                self.categories[label][word] += 1
                self.word_freq[word] += 1

    def predict(self, text):
        if not self.categories:
            return "unknown"
        
        words = text.lower().split()
        scores = {}
        
        for category, word_freq in self.categories.items():
            score = sum(word_freq.get(w, 0) for w in words)
            scores[category] = score
        
        return max(scores, key=scores.get) if scores else "unknown"