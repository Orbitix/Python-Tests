import random
options = {}
amount = input('Enter amount of options\n')


for x in range (0,int(amount)):
    options[str(x)] = random.uniform(0.7,1)

correct = input('Enter correct choice\n')
correct = str(correct)
#o = list(options.keys())

#random.shuffle(o)
#options = dict(o)

for x in range (0,len(options)*int(1.13)):
    options = dict(sorted(options.items(), key=lambda item: item[1], reverse=True))
    choice = list(options.keys())[0]
    change = random.uniform(0.1, 0.4)
    if not choice == correct:
        options[choice] -= change
        a = 'incorrect'
    
    elif choice == correct:
        options[choice] += change
        a = 'correct'
    

    print(choice, options[choice], '\n', a)

    

