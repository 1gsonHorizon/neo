# Traitement du Langage Naturel en Français
import re
from collections import Counter

class NLPProcessor:
    def __init__(self):
        self.stop_words_fr = {
            'le', 'la', 'les', 'de', 'du', 'des', 'un', 'une', 'et', 'ou',
            'mais', 'donc', 'car', 'que', 'qui', 'ce', 'cette', 'ces', 'mon', 'ma',
            'ton', 'ta', 'son', 'sa', 'je', 'tu', 'il', 'elle', 'nous', 'vous'
        }

    def process(self, text):
        text = text.lower().strip()
        tokens = self.tokenize(text)
        filtered_tokens = [t for t in tokens if t not in self.stop_words_fr]
        
        return {
            'original': text,
            'tokens': tokens,
            'filtered_tokens': filtered_tokens,
            'length': len(tokens)
        }

    def tokenize(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        return words

    def extract_keywords(self, text):
        processed = self.process(text)
        filtered = processed['filtered_tokens']
        
        if not filtered:
            return []
        
        keywords = Counter(filtered).most_common(5)
        return [kw[0] for kw in keywords]

    def detect_message_type(self, text):
        text_lower = text.lower().strip()
        
        greetings = ['bonjour', 'hello', 'salut', 'coucou']
        if any(g in text_lower for g in greetings):
            return 'greeting'
        
        farewells = ['au revoir', 'goodbye', 'bye', 'à bientôt']
        if any(f in text_lower for f in farewells):
            return 'farewell'
        
        if text_lower.startswith(('qui', 'quoi', 'où', 'quand', 'comment', 'pourquoi')) or '?' in text:
            return 'question'
        
        return 'unknown'

    def similarity(self, text1, text2):
        tokens1 = set(self.tokenize(text1))
        tokens2 = set(self.tokenize(text2))
        
        if not tokens1 or not tokens2:
            return 0.0
        
        intersection = len(tokens1 & tokens2)
        union = len(tokens1 | tokens2)
        
        return intersection / union if union > 0 else 0.0

    def sentiment_analysis(self, text):
        positive_words = ['bon', 'super', 'excellent', 'génial', 'bien']
        negative_words = ['mauvais', 'horrible', 'nul', 'terrible', 'mal']
        
        text_lower = text.lower()
        
        pos_count = sum(1 for w in positive_words if w in text_lower)
        neg_count = sum(1 for w in negative_words if w in text_lower)
        
        if pos_count > neg_count:
            return '😊 Positif'
        elif neg_count > pos_count:
            return '😞 Négatif'
        else:
            return '😐 Neutre'