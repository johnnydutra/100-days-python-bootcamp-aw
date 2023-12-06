import math

def paint_calc(height, width, cover):
  area = height * width
  cans = math.ceil(area / cover)
  print(f"You'll need {cans} cans of paint")