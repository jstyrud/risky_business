import numpy as np


if __name__ == "__main__":
    # number of participants, MUST BE DIVISIBLE BY 8
    n = 80

    # set the number of users you'll need    
    userID = range(0,n)

    #set the expectation conditions, with half the total participants
    high_expectation = ['high_exp_3' for i in range(int(n/2))]
    low_expectation = ['low_exp_1' for i in range(int(n/2))]
    expectation_condition =  high_expectation+low_expectation

    # set the riskiness conditions, staggered so each expectation condition is split evenly 
    risky_first1 = ['safe_first' for i in range(int(n/4))]
    safe_first1 = ['risky_first' for i in range(int(n/4))]
    risky_first2 = ['safe_first' for i in range(int(n/4))]
    safe_first2 = ['risky_first' for i in range(int(n/4))]
              
    first_condition = risky_first1+safe_first1+risky_first2+safe_first2

   
    #set the money trial condition, so its staggered evenly
    money_success1 = ['money_success' for i in range(int(n/8))]
    money_fail1 = ['money_fail' for i in range(int(n/8))]
    money_success2 = ['money_success' for i in range(int(n/8))]
    money_fail2 = ['money_fail' for i in range(int(n/8))]
    money_success3 = ['money_success' for i in range(int(n/8))]
    money_fail3 = ['money_fail' for i in range(int(n/8))]
    money_success4 = ['money_success' for i in range(int(n/8))]
    money_fail4 = ['money_fail' for i in range(int(n/8))]

    money_condition = money_success1+money_fail1+money_success2+money_fail2+money_success3+money_fail3+money_success4+money_fail4
   

    # shuffle the order while mainting the in condition distributions  
    all_conds=list(zip(expectation_condition, first_condition, money_condition))
    
    np.random.shuffle(all_conds)

    expectation_condition, first_condition, money_condition = zip(*all_conds)


    # set the permutation optioms
    risky_options_1 = ['A', 'B', 'C', 'D']
    safe_options_1 = ['E', 'F', 'E', 'F']
    risky_options_3 = ['A', 'A', 'A', 'B']
    safe_options_3 = ['J', 'K', 'J', 'K']
   

    csv_string = "userID,expectation condition, first robot condition,risky trial ordering,safe trial ordering,money round condition,order if safe chosen, order if risky chosen\n"
    for i in userID:
        if expectation_condition[i] == 'high_exp_3':
            expi = 3
        if expectation_condition[i] == 'low_exp_1':
            expi=1

        #user id
        csv_string += str(i+1)
        csv_string += ","

        #expectation condition (was already randomized above)
        csv_string += expectation_condition[i]
        csv_string += ","

        #initial condition (was already randomized above)
        csv_string += first_condition[i]
        csv_string += ","

        if expi == 1: 
            #risky permutation, needs to be randomized for each agent
            for x in np.random.permutation(risky_options_1):
                csv_string += x
            csv_string += ","
            
            # safe permutation, needs to be randomized for each agent
            for x in np.random.permutation(safe_options_1):
                csv_string += x
            csv_string += ","
        if expi == 3: 
            #risky permutation, needs to be randomized for each agent
            for x in np.random.permutation(risky_options_3):
                csv_string += x
            csv_string += ","
            
            # safe permutation, needs to be randomized for each agent
            for x in np.random.permutation(safe_options_3):
                csv_string += x
            csv_string += ","


        # money condition (was already randomized above)
        csv_string += money_condition[i]
        csv_string += "," #\n
       
       
        if expi == 1: 
            # safe permutation, needs to be randomized for each agent
            csv_string += np.random.choice(safe_options_1)
            csv_string += "," #\n

            #  risky permutation, needs to be randomized for each agent
            if money_condition[i] == 'money_success':
                csv_string += 'A'
            else:
                csv_string += np.random.choice(['B', 'C','D'])
            csv_string += ", \n"
        if expi == 3: 
            # safe permutation, needs to be randomized for each agent
            csv_string += np.random.choice(safe_options_3)
            csv_string += "," #\n

            #  risky permutation, needs to be randomized for each agent
            if money_condition[i] == 'money_success':
                csv_string += 'A'
            else:
                csv_string += 'B'
            csv_string += ", \n"
        
    print(csv_string)

with open('randomization.csv', 'w') as file:
    file.write(csv_string)
