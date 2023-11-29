from art import logo 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  returned_text = ""
  
  if direction == "decode":
    shift *= -1

  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift
      returned_text += alphabet[new_position]
    else:
      returned_text += char
      
  print(f"The {direction}d text is {returned_text}")

print(logo)

should_continue = True
while should_continue == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  caesar(text=text, shift=shift, direction=direction)

  prompt = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n")
  if prompt == "no":
    should_continue = False
    print("Goodbye!")