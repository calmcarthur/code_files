import time
import random

def typing_test():
    while True:
        sentence = generate_sentence()
        print("\nType the following:")
        print(sentence)
        
        input("Press Enter when you are ready to start...")
        
        start_time = time.time()
        user_input = input("Type here: ")
        end_time = time.time()
        
        calculate_speed(sentence, user_input, start_time, end_time)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

def generate_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is fun and rewarding.",
        "Canada is known for its beautiful landscapes.",
        "I love spending time outdoors."
    ]
    return random.choice(sentences)

def calculate_speed(sentence, user_input, start_time, end_time):
    words_typed = len(user_input.split())
    elapsed_time = end_time - start_time
    words_per_minute = (words_typed / elapsed_time) * 60
    
    print("\nResults:")
    print(f"You typed: {words_typed} words")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Your typing speed: {words_per_minute:.2f} words per minute")

if __name__ == "__main__":
    typing_test()
