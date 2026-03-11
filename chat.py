# Interface de Chat Intelligente pour NEO
import os
import json
from datetime import datetime
from nlp_processor import NLPProcessor

class ChatInterface:
    def __init__(self):
        self.conversation_history = []
        self.nlp = NLPProcessor()
        self.responses_templates = {
            'greeting': "Bonjour! Je suis NEO, ton assistant IA intelligent. Comment puis-je t'aider aujourd'hui?",
            'farewell': "À bientôt! Merci d'avoir discuté avec moi.",
            'question': "C'est une excellente question. Laisse-moi réfléchir...",
            'unknown': "Je suis désolé, je ne suis pas sûr de comprendre. Peux-tu reformuler?"
        }

    def chat(self, user_input, knowledge_base=None):
        message_type = self.nlp.detect_message_type(user_input)
        
        self.conversation_history.append({
            'role': 'user',
            'content': user_input,
            'timestamp': datetime.now().isoformat()
        })
        
        if knowledge_base:
            response = self._generate_intelligent_response(user_input, knowledge_base, message_type)
        else:
            response = self._generate_response(user_input, message_type)
        
        self.conversation_history.append({
            'role': 'assistant',
            'content': response,
            'timestamp': datetime.now().isoformat()
        })
        
        return response

    def _generate_intelligent_response(self, user_input, knowledge_base, message_type):
        keywords = self.nlp.extract_keywords(user_input)
        relevant_knowledge = knowledge_base.search(keywords)
        
        if relevant_knowledge:
            return f"D'après mes connaissances: {relevant_knowledge[:200]}..."
        else:
            return self._generate_response(user_input, message_type)

    def _generate_response(self, user_input, message_type):
        if message_type == 'greeting':
            return self.responses_templates['greeting']
        elif message_type == 'farewell':
            return self.responses_templates['farewell']
        elif message_type == 'question':
            return self.responses_templates['question']
        else:
            return self.responses_templates['unknown']

    def get_conversation_history(self):
        return self.conversation_history

    def save_conversation(self, filename='neo_conversation.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.conversation_history, f, ensure_ascii=False, indent=2)
        print(f"✅ Conversation sauvegardée dans {filename}")