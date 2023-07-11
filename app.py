from flask import Flask, render_template, redirect, url_for, jsonify, request
from datetime import datetime
from questions import QUESTIONS, QUESTION_ORDER
from questionsthree import QUESTIONS_C
import csv
import random
import os.path


app = Flask(__name__)

USERID = -1
TRIALID = ""
TRIAL_COUNTER = 0
TRIAL_TYPE = "failure"
TRIALS_COMPLETED = {"failure": False, "flawless": False}

### CSV Filename:
CSV_FILENAME = 'survey_results.csv'
### Variable that is used to store all the user data, atm this doesn't get saved until completion, so there is no recovery from failure.
JSON_DATA = {}
#CSV filename for consent data, which should be kept seperate
CONSENT_FILENAME = 'participants.csv'


### This function will add the headers, based on the variables below, and the questions (stored in questions.py)
def write_headers():

    ### Check for header line:
    first_line = ""
    with open(CSV_FILENAME) as f:
        first_line = f.readline().strip('\n')

    ### Write file headers
    JSON_DATA["ParticipantID"] = ""
    JSON_DATA["TrialID"] = ""

    h = "Time,ParticipantID,TrialID,"
    for v in QUESTIONS:
        current_q = v[0]
        h = h + current_q + ", " #+ ("," if i<len(v)-1 else "")

        JSON_DATA[current_q] = ""

    if(h == first_line):
        print("Header exists")
    else:
        with open(CSV_FILENAME, 'a') as f:
            f.write(h + "\n")

######################
# Routes
######################

## Home ####################
@app.route('/', methods=['POST', 'GET'])
def home():

    global USERID
    global TRIALID
    global JSON_DATA

    # This clears the global variables whenever anyone goes to the home page - this might not be what you want, if multiple people will be using this at once for e.g
    JSON_DATA = {}
    TRIALS_COMPLETED["failure"] = TRIALS_COMPLETED["flawless"] = False

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

## final_opinions ####################
@app.route('/final_opinions', methods=['POST', 'GET'])
def final_opinions():

    global USERID
    global TRIALID

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


## consent ####################
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

## demographics ##############
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

        return redirect('/legworkdone')

    # If the page is called, it will generate the following html file
    return render_template('demographics.html', user=USERID, trial=TRIALID)

## position ##############
@app.route('/position', methods=['POST', 'GET'])
def position():

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

        return redirect('/questions')

    # If the page is called, it will generate the following html file
    return render_template('position.html', user=USERID, trial=TRIALID)


## Bell ####################
@app.route('/bell', methods=['POST', 'GET'])
def bell():

    global USERID
    global TRIALID

    # If the page is called, it will generate the following html file
    return render_template('bell.html', user=USERID, trial=TRIALID)

## Fin ####################
@app.route('/fin', methods=['POST', 'GET'])
def fin():

    global USERID
    global TRIALID

    file_exists = os.path.isfile(CSV_FILENAME)

    with open(CSV_FILENAME, 'a') as f:
        # f.write(s + "\n")
        w = csv.DictWriter(f, JSON_DATA.keys())
        if not file_exists:
            w.writeheader()  # file doesn't exist yet, write a header
        w.writerow(JSON_DATA)

    # If the page is called, it will generate the following html file
    return render_template('fin.html', user=USERID, trial=TRIALID)

## nonconsent ####################
@app.route('/nonconsent', methods=['POST', 'GET'])
def nonconsent():

    global USERID
    global TRIALID

    # If the page is called, it will generate the following html file
    return render_template('nonconsent.html', user=USERID, trial=TRIALID)

## Questions Page ####################
@app.route('/questions', methods=['POST', 'GET'])
def showQuestions():

    global USERID
    global TRIALID
    
    # Calculate which questions to use, given the questions and the trial type (i.e VR):
    QUESTIONS_TO_DISPLAY=return_questions_for_condition(QUESTIONS, TRIALID)
    RANDOM_QUESTIONS = QUESTIONS_TO_DISPLAY

    # Randomize the questions:
    random.shuffle(RANDOM_QUESTIONS)

    # Check if data is coming back from the form:
    if request.method == 'POST':
        print("Responses: ")

        # All the trial questions ID's (e.g E1_VR) had either _VR or _S, this allowed us to check for these to seperate the questions
        # Set the variable to the corresponding trialID
        trial_postfix = "F"
        if(TRIALID == "flawless"):
            trial_postfix = "NF"

        # For each question in the stack:
        for mq in QUESTIONS:

            # Check again if the postfix exists for the current question, if it does store the response
            if(trial_postfix in mq[0]):
                k = mq[0]
                try:
                    current_response = "NA" if request.form[k] == "" else request.form[k]
                    JSON_DATA[k] = current_response
                except Exception as exc:
                    current_response = "NA"
                    JSON_DATA[k] = current_response


        print("JSON: ", JSON_DATA)
        # print("CSV: ", USERID, TRIALID, response_csv)

        try:

            now = datetime.now()
            # Once the questions are asked for the type of trail, make them as done and switch to the other type:
            if TRIALID == "failure":
                TRIALS_COMPLETED["failure"] = True
                TRIALID = "flawless"
            else:
                TRIALS_COMPLETED["flawless"] = True
                TRIALID = "failure"

            # If both trials are completed, go to the final questions
            if(TRIALS_COMPLETED["failure"] == True and TRIALS_COMPLETED["flawless"] == True):
                return redirect('/third_set_of_questions')

            # Once they have completed, go to the bell page to wait until the next task is completed
            return render_template('bell.html', user=USERID, trial=TRIALID)
        except Exception as exc:
            print("Error executing SQL: %s"%exc)
            return jsonify({'page': 'list', 'success': False})
            
    # Otherwise we show the questions:
    return render_template('index.html', user=USERID, trial=TRIALID, questions=QUESTIONS_TO_DISPLAY)



@app.route('/third_set_of_questions', methods=['POST', 'GET'])
def showThirdSetOfQuestions():

    global USERID
    global TRIALID
    
    # Calculate which questions to use, given the questions and the trial type (i.e VR):
    QUESTIONS_TO_DISPLAY=return_questions_for_risk_aversion(QUESTIONS_C, TRIALID)
    random.shuffle(QUESTIONS_TO_DISPLAY)

    # Check if data is coming back from the form:
    if request.method == 'POST':
        print("Responses: ")

        # For each question in the stack:
        for mq in QUESTIONS_C:

            # Check again if the postfix exists for the current question, if it does store the response
                k = mq[0]
                try:
                    current_response = "NA" if request.form[k] == "" else request.form[k]
                    JSON_DATA[k] = current_response
                except Exception as exc:
                    current_response = "NA"
                    JSON_DATA[k] = current_response

        print("JSON: ", JSON_DATA)

        try:
            now = datetime.now()
            return redirect('/final_opinions')

        except Exception as exc:
            print("Error executing SQL: %s"%exc)
            return jsonify({'page': 'list', 'success': False})

    # Otherwise we show the questions:
    return render_template('third_questions.html', user=USERID, trial=TRIALID, questions=QUESTIONS_TO_DISPLAY)




# Split the questions to only provide the ones that are designed for VR or S(creen)
# Returns a list of questions, that are marked with the trialID
def return_questions_for_condition(questions, condition):
    
    questions_to_display = []
    
    for q in questions:
        print(str(condition))
        print(str(q))
        if "failure" in condition and "_F" in q[0]:
            questions_to_display.append(q)
        elif "flawless" in condition and "_NF" in q[0]:
            questions_to_display.append(q)
    
    print("Questions calculatd", questions_to_display)
    return questions_to_display

def return_questions_for_risk_aversion(questions, condition):
    
    questions_to_display = []
    
    for q in questions:
       questions_to_display.append(q)
    
    print("Questions calculatd", questions_to_display)
    return questions_to_display


@app.route('/legworkdone', methods=['GET'])
def legworkdone():
    global USERID
    global TRIALID
    return render_template('legworkdone.html', user=USERID, trial=TRIALID)
@app.route('/waitingroomone', methods=['GET'])
def firstwaitingroom():
    global USERID
    global TRIALID
    return render_template('waitingroomone.html', user=USERID, trial=TRIALID)
@app.route('/firstpartdone', methods=['GET'])
def firstpartdone():
    global USERID
    global TRIALID
    return render_template('firstpartdone.html', user=USERID, trial=TRIALID)
@app.route('/waiting_room', methods=['GET'])
def waiting_room():
    global USERID
    global TRIALID
    return render_template('waiting_room.html', user=USERID, trial=TRIALID)


if __name__ == "__main__":
    # write_headers()
    app.run(debug=True, host="0.0.0.0", port=1231)
