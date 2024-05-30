
def decryptFromMorse(text):
    morse_code_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C',
                    '-..': 'D', '.': 'E', '..-.': 'F',
                    '--.': 'G', '....': 'H', '..': 'I',
                    '.---': 'J', '-.-': 'K', '.-..': 'L',
                    '--': 'M', '-.': 'N', '---': 'O',
                    '.--.': 'P', '--.-': 'Q', '.-.': 'R',
                    '...': 'S', '-': 'T', '..-': 'U',
                    '...-': 'V', '.--': 'W', '-..-': 'X',
                    '-.--': 'Y', '--..': 'Z', '-----': '0',
                    '.----': '1', '..---': '2', '...--': '3',
                    '....-': '4', '.....': '5', '-....': '6',
                    '--...': '7', '---..': '8', '----.': '9',
                    '/': ' '}  # Mapping Morse code to characters

    def morse_to_text(morse_code):
        words = morse_code.split(' / ')  # Splitting Morse code into words
        text = ''
        for word in words:
            chars = word.split()  # Splitting words into characters
            for char in chars:
                if char in morse_code_dict:
                    text += morse_code_dict[char]  # Appending character to text
                else:
                    text += '#'  # Use '#' to represent unknown Morse code
            text += ' '  # Adding space between words
        return text.strip()

    output = morse_to_text(text)

    return output

