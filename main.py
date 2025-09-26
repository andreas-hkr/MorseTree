class Node:
    def __init__(self):
        self.dot = None
        self.dash = None
        self.value = ''

    def __getitem__(self, key):
        attribute_name = 'dot' if key == '.' else 'dash'
        if not (attribute := getattr(self, attribute_name)):
            setattr(self, attribute_name, attribute := Node())
        return attribute


ROOT = Node()
MORSE_ALPHABET = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
}


def insert(symbol, letter):
    current = ROOT
    for element in symbol:
        current = current[element]
    current.value = letter


def get_letter(symbol):
    current = ROOT
    for element in symbol:
        current = current[element]
    return current.value


def populate_tree():
    for letter, symbol in MORSE_ALPHABET.items():
        insert(symbol, letter)


def encode(plain_text):
    return ' '.join(MORSE_ALPHABET.get(char, ' ') for char in plain_text.upper())


def decode(morse_code):
    return ' '.join(''.join(get_letter(letter) for letter in word.split()) for word in morse_code.split('  '))


def main():
    populate_tree()

    message = input('Your message (A-Z + space): ')
    morse_code = encode(message)
    print(f'Morse   : {morse_code}')

    plain_text = decode(morse_code)
    print(f'Decoded : {plain_text}')


if __name__ == '__main__':
    main()
