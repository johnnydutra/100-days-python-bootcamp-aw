def format_name(first_name, last_name):
  '''Take a first and last name and format it to return the title case version of the name'''

  if first_name == "" or last_name == "":
    return "You didn't provide valid inputs."
  
  formatted_first = first_name.title()
  formatted_last = last_name.title()

  return f"{formatted_first} {formatted_last}"

formatted_name = format_name("johnny", "dUTRA")
print(formatted_name)
