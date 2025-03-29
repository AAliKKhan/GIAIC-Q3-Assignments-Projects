PROMPT = "What do you want? "
JOKE = "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾😆"
SORRY = "Sorry, I only tell jokes."

def main():
    user_input = input(PROMPT).strip().lower() 
    
    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
