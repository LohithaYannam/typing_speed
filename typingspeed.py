import time
import random

def calculate_typing_speed(start_time, end_time, typed_text):
    words_per_minute = (len(typed_text.split()) / (end_time - start_time)) * 60
    return words_per_minute

def main():
    prompt_text = "The quick brown fox jumps over the lazy dog"
    
    print("Type the following text:")
    print(prompt_text)
    
    input("Press Enter when you are ready to start typing...")
    
    start_time = time.time()
    
    typed_text = input("Type the text: ")
    
    end_time = time.time()
    
    # Calculate typing speed
    typing_speed = calculate_typing_speed(start_time, end_time, typed_text)
    
    # Compare typed text with the prompt for accuracy
    prompt_words = prompt_text.split()
    typed_words = typed_text.split()
    
    correct_words = sum(1 for t, p in zip(typed_words, prompt_words) if t == p)
    accuracy = (correct_words / len(prompt_words)) * 100
    
    print("\nTyping Speed: {:.2f} WPM".format(typing_speed))
    print("Accuracy: {:.2f}%".format(accuracy))
    
    # Feedback on typing speed
    if typing_speed < 40:
        print("Your typing speed is below average. Keep practicing!")
    elif 40 <= typing_speed < 70:
        print("Your typing speed is good. Keep improving!")
    else:
        print("Great job! Your typing speed is excellent!")

if __name__ == "__main__":
    main()
