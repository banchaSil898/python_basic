# concatenate argument and String
ourSurname = 'Silabundith'
myName = "Bancha"
myDaughterName = "Nutcha"
dadMoney = 20
momMoney = 30
myMoney = 15.25
broMoney = 10.5
dadSalary = 35000
monthOfYear = 12


def single_argument():
    # single argument
    print("Dad have money %d" % dadMoney)
    print("Mom have money %d" % momMoney)
    print("I have money %f" % myMoney)
    print("Bro have money %f" % broMoney)
    # single argument


def multiple_argument():
    # multiple argument
    print("I have money %d Bro have money %d" % (myMoney, broMoney))
    print("Uncle next door %f Aunt next door %f" % (35, 45))
    # multiple argument


def calculate_argument():
    # calculate argument
    print("Total money of parent %d" % (dadMoney + momMoney))
    print("Total salary per year of father %d" % (dadSalary * monthOfYear))
    # calculate argument


def argument_by_number():
    # argument by number
    print("Sort of {0}'s money is {1} {2} {3} {4}"
          .format(ourSurname, momMoney, dadMoney, myMoney, broMoney))
    print("Total money of {0} Family {1} BAHT".format(ourSurname, momMoney + dadMoney + myMoney + broMoney))
    print("The 3rd of our surname %s Is %s" % (ourSurname, ourSurname[3]))
    # argument by number


def argument_alias():
    # argument by alias
    print("My name is{ชื่อฉัน} {นามสกุล} \nMy daughter name is {ชื่อลูกสาว} {นามสกุล}"
          .format(นามสกุล=ourSurname, ชื่อฉัน=myName, ชื่อลูกสาว=myDaughterName))
    # argument by alias


def locals_argument():
    # locals argument
    nickname = 'Tor'
    print("Hello {nickname}".format(**locals()))
    print("my Name {myName} {ourSurname}\nMy daughter name is {myDaughterName} {ourSurname}".format(**globals()))
    print('Our {ourSurname} Family sort money is {momMoney} {dadMoney} {myMoney} {broMoney}'
          .format(**globals()))
    # locals argument
