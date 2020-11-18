import random
"""random.choices(population, weights) weights add up to 1"""

loop = 50
# values = ["Yui","Pla","Tatar","Tor"]
# distribute = [.1,.1,.3,.5]


age = ""
married = ""
education = ""

while loop > 0:
  # print('with distribute %s' % random.choices(values, distribute))
  # print('none distribute %s' % random.choices(values))
  age = random.choice(["ต่ำกว่า 20 ปี","20 – 30 ปี","31 – 40 ปี","มากกว่า 40 ปี"])
  if age == "ต่ำกว่า 20 ปี":
    married = "โสด"
    education = "ต่ำกว่าปริญญาตรี"
  else:
    married = random.choice(["โสด","สมรส","หม้าย/หย่าร้าง/แยกกันอยู่"])
    education = random.choice(["ต่ำกว่าปริญญาตรี","ปริญญาตรี","สูงกว่าปริญญาตรี"])
  
  if age == "ต่ำกว่า 20 ปี": print("{age} {married} {education} {loop}".format(**globals()))

  loop -=1