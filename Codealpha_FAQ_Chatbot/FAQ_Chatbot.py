import re
from difflib import SequenceMatcher
from typing import Dict, List, Tuple


class FAQChatbot:
    """A simple FAQ chatbot that matches user queries to predefined answers."""
    
    def __init__(self):
        """Initialize the chatbot with FAQ database."""
        self.faqs: Dict[str, str] = {
            "what is python": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
            "how to install python": "Visit python.org, download the latest version, and run the installer. Add Python to PATH during installation.",
            "what is machine learning": "Machine learning is a subset of AI that enables systems to learn and improve from experience without being explicitly programmed.",
            "how to use python libraries": "Install libraries using pip (pip install library_name) and import them in your code using 'import library_name'.",
            "what is artificial intelligence": "Artificial Intelligence is a simulation of human intelligence by computer systems to perform tasks that typically require human intelligence.",
            "how to learn programming": "Start with basics, practice coding daily, build projects, read documentation, and join communities for support.",
            "what is a list in python": "A list is a mutable, ordered collection of items in Python, created using square brackets: [1, 2, 3].",
            "what is a dictionary in python": "A dictionary is a mutable, unordered collection of key-value pairs, created using curly braces: {'key': 'value'}.",
            "how to debug python code": "Use print statements, Python debugger (pdb), IDE debuggers, or logging module to identify and fix issues.",
            "what is object oriented programming": "OOP is a programming paradigm that uses objects and classes to structure code, promoting modularity and reusability.",
        }
        self.similarity_threshold = 0.6
    
    def normalize_query(self, query: str) -> str:
        """Normalize user query for better matching."""
        return query.lower().strip()
    
    def calculate_similarity(self, query: str, faq: str) -> float:
        """Calculate similarity between query and FAQ question."""
        return SequenceMatcher(None, query, faq).ratio()
    
    def find_best_match(self, query: str) -> Tuple[str, float]:
        """Find the best matching FAQ for the user query.
        
        Returns:
            Tuple of (answer, similarity_score)
        """
        normalized_query = self.normalize_query(query)
        best_match = None
        best_score = 0
        
        for faq_question, faq_answer in self.faqs.items():
            score = self.calculate_similarity(normalized_query, faq_question)
            if score > best_score:
                best_score = score
                best_match = faq_answer
        
        return best_match, best_score
    
    def get_response(self, user_input: str) -> str:
        """Generate chatbot response based on user input."""
        if not user_input.strip():
            return "Please ask me something! Example: 'What is Python?'"
        
        # Check for exit commands
        if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
            return "Goodbye! Feel free to ask anytime. 👋"
        
        # Check for help command
        if user_input.lower() in ["help", "?"]:
            return self.display_help()
        
        # Find best matching FAQ
        answer, score = self.find_best_match(user_input)
        
        if score >= self.similarity_threshold:
            return f"✓ {answer}"
        else:
            return f"I'm not sure about that. Try asking about Python, machine learning, or programming basics. Type 'help' for suggestions."
    
    def display_help(self) -> str:
        """Display available topics."""
        topics = [q.capitalize() for q in self.faqs.keys()]
        return "I can help with:\n" + "\n".join(f"• {topic}" for topic in sorted(topics))
    
    def add_faq(self, question: str, answer: str) -> None:
        """Add a new FAQ to the database."""
        self.faqs[self.normalize_query(question)] = answer
        print(f"✓ Added FAQ: {question}")
    
    def run(self) -> None:
        """Run the chatbot in interactive mode."""
        print("=" * 60)
        print("📚 FAQ CHATBOT - Ask me anything!")
        print("=" * 60)
        print("Commands: 'help' for topics, 'exit' to quit\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                if not user_input:
                    continue
                
                response = self.get_response(user_input)
                print(f"Bot: {response}\n")
                
                if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
                    break
            except KeyboardInterrupt:
                print("\n\nBot: Goodbye! 👋")
                break
            except Exception as e:
                print(f"Bot: An error occurred: {e}\n")


def main():
    """Main function to run the FAQ Chatbot."""
    chatbot = FAQChatbot()
    chatbot.run()


if __name__ == "__main__":
    main()
