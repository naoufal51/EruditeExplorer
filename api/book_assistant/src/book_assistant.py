from .utils import search_similar_text_blocks, generate_answer

class BookAssistant:
    def __init__(self):
        pass

    def ask_question(self, question: str):
        search_results = search_similar_text_blocks(question)
        answer = generate_answer(search_results, question)
        return answer
