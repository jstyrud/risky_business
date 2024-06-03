import numpy as np


if __name__ == "__main__":

    # set the number of users you'll need    
    userID = range(0,100)

    # set the two conditions, and how many you want from each, in this case its 50 and 50, then randomize the order
    risky_first = ['safe_first' for i in range (0,50)]
    safe_first = ['risky_first' for i in range(0,50)]
              
    intial_condition_order = risky_first+safe_first
    np.random.shuffle(intial_condition_order)


    # set the permutation optioms
    risky_options = ['A', 'B', 'C', 'D']
    safe_options = ['E', 'F', 'E', 'F']


    # set the two conditions, and how many you want from each, in this case its 50 and 50, then randomize the order
    money_success = ['money_success' for i in range (0,50)]
    money_fail = ['money_fail' for i in range(0,50)]

    second_condition_order =money_success+money_fail
    np.random.shuffle(second_condition_order)

    csv_string = "userID,first condition,risky trial ordering,safe trial ordering,second condition,order if safe chosen, order if risky chosen\n"
    for i in userID:
        #user id
        csv_string += str(i+1)
        csv_string += ","

        #initial condition (was already randomized above)
        csv_string += intial_condition_order[i]
        csv_string += ","

        #risky permutation, needs to be randomized for each agent
        for x in np.random.permutation(risky_options):
            csv_string += x
        csv_string += ","
        
        # safe permutation, needs to be randomized for each agent
        for x in np.random.permutation(safe_options):
            csv_string += x
        csv_string += ","


        # money condition (was already randomized above)
        csv_string += second_condition_order[i]
        csv_string += "," #\n

        # safe permutation, needs to be randomized for each agent
        csv_string += np.random.choice(safe_options)
        csv_string += "," #\n

        #  risky permutation, needs to be randomized for each agent
        if second_condition_order[i] == 'money_success':
            csv_string += 'A'
        else:
            csv_string += np.random.choice(['B', 'C','D'])
        csv_string += ", \n"
        
    print(csv_string)

with open('randomization.csv', 'w') as file:
    file.write(csv_string)
