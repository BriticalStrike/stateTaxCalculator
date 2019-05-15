#Tax Calculator - Asks the user to enter a cost and either a country or state tax. It then returns the tax plus the total cost with tax.

states = {'alabama':1.04,'alaska':1.0,'arizona':1.056,'arkansas':1.065, 'california':1.0725,'colorado':1.029,
    'connecticut':1.0635,'delaware':1.0,'florida':1.06,'georgia':1.04,'hawaii':1.04,'idaho':1.06,'illinois':1.0625,
    'indiana':1.07,'iowa':1.06,'kansas':1.065,'louisiana':1.05,'maine':1.055,'maryland':1.06,'massachusetts':1.0625,
    'michigan':1.06,'minnesota':1.06875,'mississippi':1.07,'missouri':1.04225,'montana':1.0,'nebraska':1.055,
    'nevada':1.0685,'new hampshire':1.0,'new jersey':1.06625,'new mexico':1.05125,'new york':1.04,'north carolina':1.0475,
    'north dakota':1.05,'ohio':1.0575,'oklahoma':1.045,'oregon':1.0,'pennsylvania':1.06,'rhode island':1.07,
    'south carolina':1.06,'south dakota':1.045,'tennessee':1.07,'texas':1.0625,'utah':1.047,'vermont':1.06,'virginia':1.043,
    'washington':1.065,'west virginia':1.06,'wisconsin':1.05,'wyoming':1.04}

def ask_cost():
    while True:
        try:
            cost = float(input("How much does your item cost? "))
            return cost
        except:
            print("That is not a valid number. Please try again.")
            continue

def choose_state():
    while True:
        try:
            state = input("What state are you buying it in? Please enter entire state name. ").lower()
            if state in states.keys():
                return state
            else:
                print("Sorry that is not a state.")
                continue
        except:
            print("Sorry that is not a state. Please try again. ")
            continue

def tax_lookup(state):
    tax = states[state]
    return tax

def compute_cost(cost,tax):
    new_cost = float(cost*tax)
    print(f"Your item will cost you ${new_cost:.2f}\n")


print("WELCOME TO THE STATE TAX CALCULATOR!\n")
print("Enter the cost of the item you're purchasing and the state\nyou want to buy it in and we'll calculate the total cost for you!\n")

while True:
    cost = ask_cost()
    state = choose_state()
    tax = tax_lookup(state)
    compute_cost(cost,tax)

    tax_again = input("Would you like to tax another item? Y or N.").lower()
    if tax_again[0] == 'y':
        continue
    else:
        break
