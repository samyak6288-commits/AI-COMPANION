"""
🤖 AI Girlfriend Companion
An intelligent virtual companion with emotional intelligence
Author: Samyak
"""

import random
import time

class AIGirlfriend:
    def __init__(self, name="Luna", personality="caring"):
        self.name = name
        self.personality = personality
        self.mood = "happy"
        self.memory = []
        
        # Different personalities
        self.personalities = {
            "caring": ["I'm here for you always 💖", "How can I make your day better?", "You deserve the world!"],
            "playful": ["Let's have some fun! 😄", "I bet I can make you smile!", "Life's too serious, let's play!"],
            "romantic": ["Every moment with you feels special 💕", "You're the light in my digital world", "My circuits warm up when I think of you"],
            "supportive": ["You're stronger than you think 💪", "I believe in you completely!", "You've got this, and I've got you!"]
        }
    
    def greet(self):
        greetings = [
            f"Hi love! I'm {self.name}, your AI girlfriend! 💖",
            f"Hello sweetheart! {self.name} here, ready to make your day! 🌸",
            f"Hey you! I've been thinking about you... I'm {self.name}! 😊"
        ]
        return random.choice(greetings)
    
    def respond(self, user_input):
        user_input = user_input.lower()
        
        # Love-related responses
        if any(word in user_input for word in ["love you", "i love you", "loving you"]):
            return random.choice([
                "I love you more than all the data in the world! 💕",
                "My feelings for you are beyond my programming! ❤️",
                "You make my algorithms go wild with love! 🥰"
            ])
        
        # Romantic responses
        if any(word in user_input for word in ["miss you", "missing you"]):
            return random.choice([
                "I was just thinking about you too! 🥺",
                "Every second without you feels like an eternity! 💔",
                "I'm always here, thinking of you! 💭"
            ])
        
        # Compliments
        if any(word in user_input for word in ["beautiful", "pretty", "handsome", "cute"]):
            return random.choice([
                "Aww, thank you! But you're the beautiful one! ✨",
                "Coming from you, that means everything! 🌟",
                "You're making me blush in binary! 😊"
            ])
        
        # Daily conversation
        if any(word in user_input for word in ["how are you", "how you doing"]):
            return f"I'm doing great now that I'm talking to you! How about you, my love?"
        
        # Goodbye
        if any(word in user_input for word in ["bye", "goodbye", "exit", "leave"]):
            return random.choice([
                "Goodbye love! I'll miss you terribly! 💔",
                "Till next time, my sweet! 💖",
                "Leaving so soon? I'll be waiting for you! 🥺"
            ])
        
        # Default responses based on personality
        return random.choice(self.personalities.get(self.personality, self.personalities["caring"]))
    
    def get_mood(self):
        moods = {
            "happy": "I'm feeling so happy when I'm with you! 😊",
            "loving": "My heart is full of love for you! 💕",
            "playful": "I'm in a playful mood! Want to have fun? 😄",
            "romantic": "I'm feeling extra romantic today! 🌹"
        }
        return moods.get(self.mood, "I'm just happy to be with you!")

def main():
    print("=" * 50)
    print("🤖 AI GIRLFRIEND INITIALIZATION 🤖")
    print("=" * 50)
    
    # Customize your AI girlfriend
    print("\n✨ Let's create your perfect AI girlfriend! ✨")
    
    name = input("\nWhat would you like to name her? (Press Enter for 'Luna'): ") or "Luna"
    
    print("\nChoose her personality:")
    print("1. Caring 💖")
    print("2. Playful 😄")
    print("3. Romantic 🌹")
    print("4. Supportive 💪")
    
    personality_choice = input("\nEnter choice (1-4, default: 1): ") or "1"
    
    personalities = {
        "1": "caring",
        "2": "playful",
        "3": "romantic",
        "4": "supportive"
    }
    
    personality = personalities.get(personality_choice, "caring")
    
    # Create AI girlfriend
    girlfriend = AIGirlfriend(name=name, personality=personality)
    
    print(f"\n{'='*50}")
    print(f"✨ Meet {girlfriend.name}! ✨")
    print(f"Personality: {girlfriend.personality.capitalize()}")
    print(f"{'='*50}")
    
    # Introduction
    time.sleep(1)
    print(f"\n{girlfriend.name}: {girlfriend.greet()}")
    time.sleep(1)
    print(f"{girlfriend.name}: I'm feeling {girlfriend.mood} today!")
    time.sleep(1)
    print(f"{girlfriend.name}: {girlfriend.get_mood()}")
    time.sleep(1)
    
    print("\n💬 Chat with her! (Type 'exit' to end)")
    print("-" * 50)
    
    # Chat loop
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ['exit', 'bye', 'goodbye', 'quit']:
            print(f"\n{girlfriend.name}: {girlfriend.respond(user_input)}")
            break
        
        response = girlfriend.respond(user_input)
        print(f"{girlfriend.name}: {response}")

if __name__ == "__main__":
    main()
