line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")

# if position[1] == "1":
#   if position[0] == "A":
#     line1[0] = "X"
#   elif position[0] == "B":
#     line1[1] = "X"
#   elif position[0] == "C":
#     line1[2] = "X"  
# elif position[1] == "2":
#   if position[0] == "A":
#     line2[0] = "X"
#   elif position[0] == "B":
#     line2[1] = "X"
#   elif position[0] == "C":
#     line2[2] = "X"  
# elif position[1] == "3":
#   if position[0] == "A":
#     line3[0] = "X"
#   elif position[0] == "B":
#     line3[1] = "X"
#   elif position[0] == "C":
#     line3[2] = "X"  

letter = position[0].upper()
options = ["A", "B", "C"]

letter_index = options.index(letter)
number_index = int(position[1]) - 1

map[number_index, letter_index]

print(f"{line1}\n{line2}\n{line3}")