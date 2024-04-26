from flask import Flask, render_template, redirect, url_for, jsonify, request
from datetime import datetime
from questions import QUESTIONS
import csv
import random
import os.path


app = Flask(__name__)

USERID = -1
TRIALID = ""
TRIAL_COUNTER = 0
TRIAL_TYPE = "risky"
MONEY_CHOICE = ""
MONEYID = ""
TRIALS_COMPLETED = {"risky": False, "safe": False}

# WARNING: ALL NEW QUESTION TAGS MUST BE ENTERED INTO THIS LIST TO ENSURE THAT DATA IS STORED IN THE CORRECT ORDER
CSV_ORDERING = ["ParticipantID",  	"TrialID",	"age",	"gender",	"risk_willingess",	
                "T_0_R",	"T_1_R",	"T_2_R",	"T_3_R",	"T_4_R",	"T_5_R",	"T_6_R",	"T_7_R",	"T_8_R",	"T_9_R",	"T_10_R",	"T_11_R",	"T_12_R",	"T_13_R",	"T_14_R",	"T_15_R",
                "T_0_S",	"T_1_S",	"T_2_S",	"T_3_S",	"T_4_S",	"T_5_S",	"T_6_S",	"T_7_S",	"T_8_S",	"T_9_S",	"T_10_S",	"T_11_S",	"T_12_S",	"T_13_S",	"T_14_S",	"T_15_S",	
                "RobotChoiceCoworker",	"coworkercomfort",	"coworkerreasoning",	
                "RobotChoiceMoney",	"moneycomfort",	"moneyreasoning",	"moneylikelihood",	
                "moneyID",	"moneysatisfaction",	"moneyredo",	"final_feedback"
                ]


### CSV Filename:
CSV_FILENAME = 'survey_results.csv'
### Variable that is used to store all the user data, atm this doesn't get saved until completion, so there is no recovery from failure.
JSON_DATA = {}
#CSV filename for consent data, which should be kept seperate
CONSENT_FILENAME = 'participants.csv'

def return_questions_for_condition(questions, condition):
    
    questions_to_display = []
    
    for q in questions:
        print(str(condition))
        print(str(q))
        if "risky" in condition and "_R" in q[0]:
            questions_to_display.append(q)
        elif "safe" in condition and "_S" in q[0]:
            questions_to_display.append(q)
    
    print("Questions calculatd", questions_to_display)
    return questions_to_display



######################
# Routes
######################

## Page 1: Home ####################
@app.route('/', methods=['POST', 'GET'])
def home():

    global USERID
    global TRIALID
    global JSON_DATA

    # This clears the global variables whenever anyone goes to the home page - this might not be what you want, if multiple people will be using this at once for e.g
    JSON_DATA = {}
    TRIALS_COMPLETED["risky"] = TRIALS_COMPLETED["safe"] = False

    # When the data is returned to the page, i.e submit is sent:
    if request.method == 'POST':
        try:
            # Store the user variables:
            USERID = int(request.form['paricipantID'])
            TRIALID = request.form['trialID']

            print(USERID, TRIALID)

            # Store it in the JSON_DATA 
            JSON_DATA["ParticipantID"] = USERID
            JSON_DATA["TrialID"] = TRIALID

            #Once the page has been submitted, it moves on to the next page - i.e consent (look for route below.)
            return redirect('/consent')
        except Exception as e:
            # In the case of an error, return to home page.
            return redirect('/')
            
    # If the page is called, it will generate the following html file
    return render_template('start.html')

## Page 2a: consent ####################
@app.route('/consent', methods=['POST', 'GET'])
def consent():

    global USERID
    global TRIALID
    global JSON_DATA

    # When the data is returned to the page, i.e submit is sent:
    if request.method == 'POST':

        CONSENT_DATA = {"ParticipantID": USERID}

        CONSENT_FILENAME
     
        print(request.form)
        for v in request.form:

            try:
                current_response = "NA" if request.form[v] == "" else request.form[v]
                CONSENT_DATA[v] = current_response
            except Exception as exc:
                current_response = "NA"
                CONSENT_DATA[v] = current_response

        # Save Consent data to sepeate file:
        file_exists = os.path.isfile(CONSENT_FILENAME)
        with open(CONSENT_FILENAME, 'a') as f:
            # f.write(s + "\n")
            w = csv.DictWriter(f, CONSENT_DATA.keys())
            if not file_exists:
                w.writeheader()  # file doesn't exist yet, write a header
            w.writerow(CONSENT_DATA)

        if(CONSENT_DATA["consent_1"] == "No"):
            return redirect('/nonconsent')
        return redirect('/demographics')

    # If the page is called, it will generate the following html file
    return render_template('consent.html', user=USERID, trial=TRIALID)

## Page 2b nonconsent ####################
@app.route('/nonconsent', methods=['POST', 'GET'])
def nonconsent():

    global USERID
    global TRIALID

    # If the page is called, it will generate the following html file
    return render_template('nonconsent.html', user=USERID, trial=TRIALID)


## Page 3 demographics  ##############
@app.route('/demographics', methods=['POST', 'GET'])
def demographics():

    global USERID
    global TRIALID
    global JSON_DATA

    # When the data is returned to the page, i.e submit is sent:
    if request.method == 'POST':
     
        print(request.form)
        for v in request.form:
            # JSON_DATA[v] = request.form[v]
            print(v, request.form[v])
            try:
                current_response = "NA" if request.form[v] == "" else request.form[v]
                JSON_DATA[v] = current_response
            except Exception as exc:
                current_response = "NA"
                JSON_DATA[v] = current_response

        return redirect('/bell1')

    # If the page is called, it will generate the following html file
    return render_template('demographics.html', user=USERID, trial=TRIALID)


## Page 4 before first trial  ##############
@app.route('/bell1', methods=['GET'])
def bell1():
    global USERID
    global TRIALID

    return render_template('bell1.html', user=USERID, trial=TRIALID)


## Page 5 and 7 questions for practice trials ###
@app.route('/questions', methods=['POST', 'GET'])
def showQuestions():

    global USERID
    global TRIALID
    
    # Calculate which questions to use, given the questions and the trial type (i.e VR):
    print("here we go   "+ TRIALID)
    QUESTIONS_TO_DISPLAY=return_questions_for_condition(QUESTIONS, TRIALID)
    RANDOM_QUESTIONS = QUESTIONS_TO_DISPLAY

    # Randomize the questions:
    random.shuffle(RANDOM_QUESTIONS)

    # Check if data is coming back from the form:
    if request.method == 'POST':
        
        print("Responses: ")

        # All the trial questions ID's (e.g E1_VR) had either _VR or _S, this allowed us to check for these to seperate the questions
        # Set the variable to the corresponding trialID
        trial_postfix = ""
        if(TRIALID == "risky"):
            trial_postfix = "_R"
        if(TRIALID == "safe"):
            trial_postfix = "_S"
        


        print('postfix' + trial_postfix)
            

        # For each question in the stack:
        for mq in QUESTIONS:

            # Check again if the postfix exists for the current question, if it does store the response
            if(trial_postfix in mq[0]):
                k = mq[0]
                print("question " + k)
                try:
                    current_response = "NA" if request.form[k] == "" else request.form[k]
                    print("req form: "+ request.form[k])
                    JSON_DATA[k] = current_response
                except Exception as exc:
                    current_response = "NA"
                    JSON_DATA[k] = current_response


        print("JSON: ", JSON_DATA)
        # print("CSV: ", USERID, TRIALID, response_csv)

        try:
            print(TRIALID)
            print("risky completed", TRIALS_COMPLETED["risky"])
            print("safe completed", TRIALS_COMPLETED["safe"])
            now = datetime.now()
            # Once the questions are asked for the type of trail, make them as done and switch to the other type:
            if TRIALID == "risky":
                TRIALS_COMPLETED["risky"] = True
                TRIALID = "safe"
            elif TRIALID == "safe":
                print("checkpoint 6")
                TRIALS_COMPLETED["safe"] = True
                TRIALID = "risky"
            else:
                    raise Exception("invalid TRIALID")

            print(TRIALID)
            print("risky completed", TRIALS_COMPLETED["risky"])
            print("safe completed", TRIALS_COMPLETED["safe"])
            # If both trials are completed, go to the final questions
            if(TRIALS_COMPLETED["risky"] == True and TRIALS_COMPLETED["safe"] == True):
                

                return redirect('/thechoice1')

            # Once they have completed, go to the bell page to wait until the next task is completed
            return render_template('bell2.html', user=USERID, trial=TRIALID)
        except Exception as exc:
            print("Error executing SQL: %s"%exc)
            return jsonify({'page': 'list', 'success': False})
            
    # Otherwise we show the questions:
    return render_template('trial_questions.html', user=USERID, trial=TRIALID, questions=QUESTIONS_TO_DISPLAY)


## Page 6  for between trials ###

@app.route('/bell2', methods=['GET'])
def bell2():

    global USERID
    global TRIALID

    # If the page is called, it will generate the following html file
    return render_template('bell2.html', user=USERID, trial=TRIALID)

################################ TO DO ##################

# Page 9a the choice coworker
@app.route('/thechoice1', methods=['POST', 'GET'])
def thechoice1():
    global USERID
    global TRIALID
    global JSON_DATA

    if request.method == 'POST':
        print('made it')
        try:
            # Store the user variables:
            COWORKER_CHOICE = request.form['RobotChoiceCoworker']

            print(COWORKER_CHOICE)

            # Store it in the JSON_DATA 
            if COWORKER_CHOICE == 'robot1':
                # TRIALID is reverted back to  the first robot they interacted with 
                JSON_DATA["RobotChoiceCoworker"] = TRIALID
                print(TRIALID)
            elif COWORKER_CHOICE == 'robot2':
                if TRIALID == "risky":
                    JSON_DATA["RobotChoiceCoworker"] = "safe"
                    print("safe")
                elif TRIALID == "safe":
                    JSON_DATA["RobotChoiceCoworker"] = "risky"
                    print("risky")
                else:
                    raise Exception("invalid TRIALID")
                # the second robot, aka the last robot they interacted with, is still saved in the trial id 
            else:
                print(COWORKER_CHOICE)
                raise Exception("invalid choice")
       

            #Once the page has been submitted, it moves on to the next page - i.e consent (look for route below.)
            return redirect('/thoughtsonthechoice1')
        except Exception as e:
            # In the case of an error, return to home page.
            print(e)
            return redirect('/')

    return render_template('thechoice1.html', user=USERID, trial=TRIALID)



# Page 9b thoughts on the choice coworker 
@app.route('/thoughtsonthechoice1', methods=['POST', 'GET'])
def thoughtsonthechoice1():
    global USERID
    global TRIALID
    global JSON_DATA

    if JSON_DATA["RobotChoiceCoworker"] == TRIALID:
        choicemade = "Protype 1"
    else:
         choicemade = "Protype 2"

    if request.method == 'POST':

        try:
     
            print(request.form)
            for v in request.form:
                # JSON_DATA[v] = request.form[v]
                print(v, request.form[v])
                try:
                    current_response = "NA" if request.form[v] == "" else request.form[v]
                    JSON_DATA[v] = current_response
                except Exception as exc:
                    current_response = "NA"
                    JSON_DATA[v] = current_response

            print(JSON_DATA)
            return redirect('/thechoice2')
        
        except Exception as e:
            # In the case of an error, return to home page.
            print(e)
            return redirect('/')


    return render_template('thoughtsonthechoice1.html', user=USERID, trial=TRIALID, choice = choicemade)

# Page 10a the choice money
@app.route('/thechoice2', methods=['POST', 'GET'])
def thechoice2():
    global USERID
    global TRIALID
    global JSON_DATA
    global MONEY_CHOICE

    if request.method == 'POST':
        print('made it')
        try:
            # Store the user variables:
            COWORKER_CHOICE = request.form['RobotChoiceMoney']

            print(COWORKER_CHOICE)

            # Store it in the JSON_DATA 
            if COWORKER_CHOICE == 'robot1':
                # TRIALID is reverted back to  the first robot they interacted with 
                JSON_DATA["RobotChoiceMoney"] = TRIALID
                MONEY_CHOICE = TRIALID
                print(TRIALID)
            elif COWORKER_CHOICE == 'robot2':
                if TRIALID == "risky":
                    JSON_DATA["RobotChoiceMoney"] = "safe"
                    MONEY_CHOICE = "safe"
                    print("safe")
                elif TRIALID == "safe":
                    JSON_DATA["RobotChoiceMoney"] = "risky"
                    MONEY_CHOICE = "risky"
                    print("risky")
                else:
                    raise Exception("invalid TRIALID")
                # the second robot, aka the last robot they interacted with, is still saved in the trial id 
            else:
                print(COWORKER_CHOICE)
                raise Exception("invalid choice")
       

            #Once the page has been submitted, it moves on to the next page - i.e consent (look for route below.)
            return redirect('/thoughtsonthechoice2')
        except Exception as e:
            # In the case of an error, return to home page.
            print(e)
            return redirect('/')

    return render_template('thechoice2.html', user=USERID, trial=TRIALID)

# Page 10b thoughts on the choice money 
@app.route('/thoughtsonthechoice2', methods=['POST', 'GET'])
def thoughtsonthechoice2():
    global USERID
    global TRIALID
    global JSON_DATA
    global MONEY_CHOICE




    if MONEY_CHOICE == TRIALID:
        choicemade = "Protype 1"
    else:
         choicemade = "Protype 2"

    if request.method == 'POST':

        try:
     
            print(request.form)
            for v in request.form:
                # JSON_DATA[v] = request.form[v]
                print(v, request.form[v])
                try:
                    current_response = "NA" if request.form[v] == "" else request.form[v]
                    JSON_DATA[v] = current_response
                except Exception as exc:
                    current_response = "NA"
                    JSON_DATA[v] = current_response

            print(JSON_DATA)
            return redirect('/bell3')
        
        except Exception as e:
            # In the case of an error, return to home page.
            print(e)
            return redirect('/')


    return render_template('thoughtsonthechoice2.html', user=USERID, trial=TRIALID, choice = choicemade)

## Page 11 before final run ###

@app.route('/bell3', methods=['GET'])
def bell3():

    global USERID
    global TRIALID

    # If the page is called, it will generate the following html file
    return render_template('bell3.html', user=USERID, trial=TRIALID)


## Page 11b experiementer input ###
@app.route('/moneyinput', methods=['GET', 'POST'])
def moneyinput():

    global USERID
    global TRIALID
    global MONEY_CHOICE
    global MONEYID

    
    # When the data is returned to the page, i.e submit is sent:
    if request.method == 'POST':
        try:
            # Store the user variables:
            MONEYID = request.form['moneyID']

            print(USERID, TRIALID)
            
            # Store it in the JSON_DATA 
            JSON_DATA["moneyID"] = MONEYID

            #Once the page has been submitted, it moves on to the next page - i.e consent (look for route below.)
            return redirect('/reflections')
        except Exception as e:
            # In the case of an error, return to home page.
            return redirect('/')
            
 

    # If the page is called, it will generate the following html file
    return render_template('moneyinput.html', user=USERID, trial=TRIALID, money = MONEY_CHOICE)


## Page 12 reflections on the choice ###

@app.route('/reflections', methods=['GET', 'POST'])
def reflections():

    global USERID
    global TRIALID
    global MONEY_CHOICE

    if MONEY_CHOICE == TRIALID:
        choicemade = "Protype 1"
    else:
        choicemade = "Protype 2"

    if request.method == 'POST':

        try:
     
            print(request.form)
            for v in request.form:
                # JSON_DATA[v] = request.form[v]
                print(v, request.form[v])
                try:
                    current_response = "NA" if request.form[v] == "" else request.form[v]
                    JSON_DATA[v] = current_response
                except Exception as exc:
                    current_response = "NA"
                    JSON_DATA[v] = current_response

            print(JSON_DATA)
            return redirect('/final_opinions')
        
        except Exception as e:
            # In the case of an error, return to home page.
            print(e)
            return redirect('/')



    # If the page is called, it will generate the following html file
    return render_template('reflections.html', user=USERID, trial=TRIALID)



## Page 13 final_opinions ####################
@app.route('/final_opinions', methods=['POST', 'GET'])
def final_opinions():

    global USERID
    global TRIALID
    global JSON_DATA


    # When the data is returned to the page, i.e submit is sent:
    if request.method == 'POST':
                
        print(request.form)
        for v in request.form:
            try:
                current_response = "NA" if request.form[v] == "" else request.form[v]
                JSON_DATA[v] = current_response
            except Exception as exc:
                current_response = "NA"
                JSON_DATA[v] = current_response
        
        print("FINAL RESPONSE JSON: ", JSON_DATA)

        return redirect('/fin')

    # If the page is called, it will generate the following html file
    return render_template('final_opinions.html', user=USERID, trial=TRIALID)





## page 14 Fin ####################
@app.route('/fin', methods=['POST', 'GET'])
def fin():

    global USERID
    global TRIALID
    global JSON_DATA

    try:
        file_exists = os.path.isfile(CSV_FILENAME)


        print("HERE IS THE JSON_DATA  " +str(JSON_DATA))


        hardcoded_key_set = set(CSV_ORDERING)
        gathered_key_set = set(JSON_DATA.keys()) 

        if not hardcoded_key_set == gathered_key_set:
            raise Exception("SOME OF THE DATA IS NOT BEING SAVED, YELL AT ANNA")


        with open(CSV_FILENAME, 'a') as f:
            # f.write(s + "\n")
            
            w = csv.DictWriter(f, CSV_ORDERING)
            if not file_exists:
                w.writeheader()  # file doesn't exist yet, write a header
            w.writerow(JSON_DATA)

    except Exception as e:
            print(e)
            # In the case of an error, return to home page.
            return redirect('/')
            

    # If the page is called, it will generate the following html file
    return render_template('fin.html', user=USERID, trial=TRIALID)






if __name__ == "__main__":
    # write_headers()
    app.run(debug=True, host="0.0.0.0", port=1231)
