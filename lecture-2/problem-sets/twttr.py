#prompt user for str of text
#output same text but with all vowels omitted (whether upper or lower)
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def twttr():
    text = input("Input: ")
    newtext = text
    for letter in text:
        if letter in vowels:
            text = text.replace(letter, "")
    
    print("Output:", text)
    

        
            
twttr()