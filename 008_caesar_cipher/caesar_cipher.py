alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  encrypted = ""

  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift
    shifted = alphabet[new_position]
    encoded += shifted
  
  print(f"The encrypted text is {encrypted}")

encrypt(text=text, shift=shift)

def decrypt(text, shift):
  decrypted = ""

  for letter in text:
    position = alphabet.index(letter)
    new_position = position - shift
    shifted = alphabet[new_position]
    decrypted += shifted
  
    print(f"The decrypted text is {decrypted}")