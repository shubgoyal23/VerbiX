from verbix.api import search_word
from verbix.db import con


def main():
    while True:
        print("*" * 50)
        userinput = input("Enter You word to find its meaning: ")
        if userinput == "quit()":
            break
        elif userinput == "":
            continue
        elif userinput.isalpha() != True:
            print("only alphabetic are allowed")
            continue
        else:
            userinput = userinput.lower()
        meaning = search_word(userinput)
        meaning = meaning.split(";")
        for i, m in enumerate(meaning, start=1):
            print(f"{i}. {m}")
        print("*" * 50)
    
    con.close()
        
if __name__ == "__main__":
    main()