import string

def caesar(text,shift,alphabets):
    def shift_alphabet(alphabet):
        return alphabet[shift:]+alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet,alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet,final_shifted_alphabet)
    return text.translate(table)


plain_text = input("Enter your message: ")
shift = int(input("Enter the shift: "))

shift %= 26

key = 26 - shift

print(caesar(plain_text,shift,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))

print("The key is "+ str(key))