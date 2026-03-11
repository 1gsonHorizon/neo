# Base de Connaissances Autonome
import json
import os
from datetime import datetime

class KnowledgeBase:
    def __init__(self, db_file='neo_knowledge.json'):
        self.db_file = db_file
        self.knowledge = self._load_or_create_db()

    def _load_or_create_db(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            'topics': {},
            'interactions': [],
            'learned_facts': []
        }

    def add_knowledge(self, topic, data):
        if topic not in self.knowledge['topics']:
            self.knowledge['topics'][topic] = {
                'data': [],
                'created_at': datetime.now().isoformat()
            }
        
        self.knowledge['topics'][topic]['data'].append({
            'content': data,
            'learned_at': datetime.now().isoformat()
        })
        
        self._save_db()

    def add_interaction(self, user_input, response):
        self.knowledge['interactions'].append({
            'user_input': user_input,
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
        self._save_db()

    def add_fact(self, fact):
        self.knowledge['learned_facts'].append({
            'fact': fact,
            'learned_at': datetime.now().isoformat()
        })
        self._save_db()

    def search(self, keywords):
        results = []
        for topic, info in self.knowledge['topics'].items():
            for kw in keywords:
                if kw.lower() in topic.lower():
                    for data_item in info['data'][:1]:
                        results.append(data_item['content'])
        return ' '.join(results) if results else ""

    def get_all_knowledge(self):
        return self.knowledge['topics']

    def get_interactions_count(self):
        return len(self.knowledge['interactions'])

    def get_facts_count(self):
        return len(self.knowledge['learned_facts'])

    def _save_db(self):
        with open(self.db_file, 'w', encoding='utf-8') as f:
            json.dump(self.knowledge, f, ensure_ascii=False, indent=2)

    def export_knowledge(self, filename='neo_knowledge_export.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.knowledge, f, ensure_ascii=False, indent=2)

    def get_stats(self):
        return {
            'topics': len(self.knowledge['topics']),
            'interactions': len(self.knowledge['interactions']),
            'facts': len(self.knowledge['learned_facts'])
        }