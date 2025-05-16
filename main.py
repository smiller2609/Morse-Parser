letterToMorse = {
    "a" : ".-",
    "b" : "-...",
    "c" : "-.-.",
    "d" : "-..",
    "e" : ".",
    "f" : "..-.",
    "g" : "--.",
    "h" : "....",
    "i" : "..",
    "j" : ".---",
    "k" : "-.-",
    "l" : ".-..",
    "m" : "--",
    "n" : "-.",
    "o" : "---",
    "p" : ".--.",
    "q" : "--.-",
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u" : "..-",
    "v" : "...-",
    "w" : ".--",
    "x" : "-..-",
    "y" : "-.--",
    "z" : "--..",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----",
    "," : "--..--",
    "." : ".-.-.-",
    "?" : "..--..",
    ";" : "-.-.-",
    ":" : "---...",
    "/" : "-..-.",
    "-" : "-....-",
    "\'" : ".----.",
    "(" : "-.--.",
    ")" : "-.--.-",
    "_" : "..--.-",
    "@" : ".--.-.",
    "!" : "-.-.--",
    "&" : ".-...",
    "=" : "-...-",
    "+" : ".-.-.",
    "\"" : ".-..-.",
    "$" : "...-..-",
    " " : " ",
}

while True:
    output = ""
    currentInput = input("What would you like to encode into Morse Code? (type 'exit to exit): ")
    if currentInput == "exit":
        break
    for letter in list(currentInput.lower()):
        if letter not in letterToMorse:
            print("Invalid Input, please try again.")
            continue
        output += letterToMorse[letter] + " "
    print(output)