""" Main script for running survey server """
# pylint: disable=global-statement, invalid-name
import csv
import os.path
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

USERID = -1
VARIANTID = -1
EXPERIMENTS_COMPLETED = 0
# WARNING: ALL NEW QUESTION TAGS MUST BE ENTERED INTO THIS LIST TO ENSURE THAT DATA IS STORED IN THE CORRECT ORDER
#TODO update this

CSV_ORDERING = ["ParticipantID", "VariantID", "age", "gender",
                'fam_1', 'fam_2', 'fam_3', 'fam_4', 'fam_5', 'fam_6', 'fam_7', 'fam_8', 'fam_9', 'fam_10', 'fam_11', 'fam_12',
                'sus_1_1', 'sus_1_2', 'sus_1_3', 'sus_1_4', 'sus_1_5', 'sus_1_6', 'sus_1_7', 'sus_1_8', 'sus_1_9', 'sus_1_10',
                'sus_2_1', 'sus_2_2', 'sus_2_3', 'sus_2_4', 'sus_2_5', 'sus_2_6', 'sus_2_7', 'sus_2_8', 'sus_2_9', 'sus_2_10',
                'sus_3_1', 'sus_3_2', 'sus_3_3', 'sus_3_4', 'sus_3_5', 'sus_3_6', 'sus_3_7', 'sus_3_8', 'sus_3_9', 'sus_3_10',
                'gui_1', 'gui_2', 'gui_3', 'final_feedback'
                ]

### CSV Filename:
CSV_FILENAME = 'survey_results.csv'
### Variable that is used to store all the user data, atm this doesn't get saved until completion, so there is no recovery from failure.
JSON_DATA = {}
#CSV filename for consent data, which should be kept separate
CONSENT_FILENAME = 'participants.csv'

def get_variant_id_from_user_id(user_id):
    """ Returns variant id from user id """
    if user_id <= 24:
        return user_id
    elif user_id <= 48:
        return user_id - 24
    elif user_id == 49:
        return 21
    elif user_id == 50:
        return 22
    elif user_id == 51:
        return 19
    elif user_id == 52:
        return 20
    elif user_id == 53:
        return 7
    elif user_id == 54:
        return 8
    elif user_id == 55:
        return 1
    elif user_id == 56:
        return 2
    elif user_id == 57:
        return 13
    elif user_id == 58:
        return 14
    elif user_id == 59:
        return 11
    elif user_id == 60:
        return 12
    else:
        print("ERROR, user_id not found")
        raise Exception("user_id not found")

######################
# Routes
######################

## Page Home ####################
@app.route('/', methods=['POST', 'GET'])
def home():
    """ Start page for entering user id """
    global USERID
    global VARIANTID
    global JSON_DATA

    # This clears the global variables whenever anyone goes to the home page
    # this might not be what you want if multiple people will be using this at once for e.g
    JSON_DATA = {}

    # When the data is returned to the page, i.e submit is sent:
    if request.method == 'POST':
        try:
            # Store the user variables:
            USERID = int(request.form['participantID'])
            VARIANTID = get_variant_id_from_user_id(USERID)

            print(USERID, VARIANTID)

            # Store it in the JSON_DATA
            JSON_DATA["ParticipantID"] = USERID
            JSON_DATA["VariantID"] = VARIANTID

            #Once the page has been submitted, it moves on to the next page - i.e consent (look for route below.)
            return redirect('/consent')
        except Exception:
            # In the case of an error, return to home page.
            return redirect('/')

    # If the page is called, it will generate the following html file
    return render_template('start.html')

## Page consent ####################
@app.route('/consent', methods=['POST', 'GET'])
def consent():
    """ Check if user consents """

    # When the data is returned to the page, i.e submit is sent:
    if request.method == 'POST':
        CONSENT_DATA = {"ParticipantID": USERID}

        print(request.form)
        for v in request.form:
            try:
                current_response = "NA" if request.form[v] == "" else request.form[v]
                CONSENT_DATA[v] = current_response
            except Exception:
                current_response = "NA"
                CONSENT_DATA[v] = current_response

        # Save Consent data to separate file:
        file_exists = os.path.isfile(CONSENT_FILENAME)
        with open(CONSENT_FILENAME, 'a') as f: #pylint: disable=unspecified-encoding
            # f.write(s + "\n")
            w = csv.DictWriter(f, CONSENT_DATA.keys())
            if not file_exists:
                w.writeheader()  # file doesn't exist yet, write a header
            w.writerow(CONSENT_DATA)

        if CONSENT_DATA["consent_1"] == "No" or CONSENT_DATA["consent_2"] == "No" or CONSENT_DATA["consent_3"] == "No":
            return redirect('/nonconsent')
        return redirect('/demographics')

    # If the page is called, it will generate the following html file
    return render_template('consent.html', user=USERID, trial=VARIANTID)

## Page nonconsent ####################
@app.route('/nonconsent', methods=['POST', 'GET'])
def nonconsent():
    """ Exit page if user did not consent """
    # If the page is called, it will generate the following html file
    return render_template('nonconsent.html')


## Page demographics  ##############
@app.route('/demographics', methods=['POST', 'GET'])
def demographics():
    """ Asks for demographic information like age and gender """
    # When the data is returned to the page, i.e submit is sent:
    if request.method == 'POST':
        print(request.form)
        for v in request.form:
            # JSON_DATA[v] = request.form[v]
            print(v, request.form[v])
            try:
                current_response = "NA" if request.form[v] == "" else request.form[v]
                JSON_DATA[v] = current_response
            except Exception:
                current_response = "NA"
                JSON_DATA[v] = current_response

        return redirect('/personalquestionaire')

    # If the page is called, it will generate the following html file
    return render_template('demographics.html', user=USERID, trial=VARIANTID)


## Page familiarity  ##############
@app.route('/personalquestionaire', methods=['POST', 'GET'])
def personalquestionaire():
    """ Asks some questions about the user familiarity with subjects """
    familiarity_questions = []

    familiarity_text = ["How familiar are you with GUIs in general? (1=not at all, 5=very)",
                        "How often do you use GUIs? (1=never, 5=often)",
                        "How would you rate your level of expertise with GUIs? (1=novice, 5=expert)",
                        "How familiar are you with programming in general? (1=not at all, 5=very)",
                        "How often do you program? (anything, not necessarily robots) (1=never, 5=often)",
                        "How would you rate your level of expertise with programming? (1=novice, 5=expert)",
                        "How familiar are you with robotics in general? (1=not at all, 5=very)",
                        "How often do you use robots? (1=never, 5=often)",
                        "How would you rate your level of expertise with robotics? (1=novice, 5=expert)",
                        "How familiar are you with Behavior Trees in general? (1=not at all, 5=very)",
                        "How often do you use Behavior Trees? (1=never, 5=often)",
                        "How would you rate your level of expertise with Behavior Trees? (1=novice, 5=expert)"]

    familiarity_labels =  ["fam_"+str(i) for i in range(1,13)]

    for i in range(len(familiarity_text)): #pylint: disable=consider-using-enumerate
        new_q =  [familiarity_labels[i], "radio_text", familiarity_text[i],["1", "2", "3", "4", "5"], ["", "", ""] ]
        familiarity_questions.append(new_q)

    # When the data is returned to the page, i.e submit is sent:
    if request.method == 'POST':
        for mq in familiarity_questions:
            k = mq[0]
            print("question " + k)
            try:
                current_response = "NA" if request.form[k] == "" else request.form[k]
                print("req form: "+ request.form[k])
                JSON_DATA[k] = current_response
            except Exception:
                current_response = "NA"
                JSON_DATA[k] = current_response

        return redirect('/bell1')

    # If the page is called, it will generate the following html file
    return render_template('personalquestionaire.html', user=USERID, trial=VARIANTID, questions=familiarity_questions)

@app.route('/bell1', methods=['GET'])
def bell1():
    """ Just a stop in survey before first experiment """
    return render_template('bell1.html', user=USERID, trial=VARIANTID)

@app.route('/sus', methods=['POST', 'GET'])
def sus():
    """ Sus questions"""
    global EXPERIMENTS_COMPLETED
    sus_questions = []
    sus_text = ["I think that I would like to use this system frequently.",
                      "I found the system unnecessarily complex.",
                      "I thought the system was easy to use.",
                      "I think that I would need the support of a technical person to be able to use this system.",
                      "I found the various functions in this system were well integrated.",
                      "I thought there was too much inconsistency in this system.",
                      "I would imagine that most people would learn to use this system very quickly.",
                      "I found the system very cumbersome to use.",
                      "I felt very confident using the system.",
                      "I needed to learn a lot of things before I could get going with this system."]


    familiarity_labels =  ["sus_"+str(EXPERIMENTS_COMPLETED + 1) + "_"+str(i) for i in range(1,11)]

    for i in range(len(sus_text)): #pylint: disable=consider-using-enumerate
        new_q =  [familiarity_labels[i], "radio_text", sus_text[i],["1", "2", "3", "4", "5"], ["Strongly disagree", "", "Strongly agree"] ]
        sus_questions.append(new_q)

    # When the data is returned to the page, i.e submit is sent:
    if request.method == 'POST':
        for mq in sus_questions:
            k = mq[0]
            print("question " + k)
            try:
                current_response = "NA" if request.form[k] == "" else request.form[k]
                print("req form: "+ request.form[k])
                JSON_DATA[k] = current_response
            except Exception:
                current_response = "NA"
                JSON_DATA[k] = current_response

        EXPERIMENTS_COMPLETED += 1
        if EXPERIMENTS_COMPLETED == 1:
            return redirect('/bell2')
        elif EXPERIMENTS_COMPLETED == 2:
            return redirect('/bell3')
        else:
            return redirect('/rank_guis')

    # If the page is called, it will generate the following html file
    return render_template('sus.html', user=USERID, trial=VARIANTID, questions=sus_questions)


@app.route('/bell2', methods=['GET'])
def bell2():
    """ Just a stop in survey before second experiment """
    return render_template('bell2.html', user=USERID, trial=VARIANTID)

@app.route('/bell3', methods=['GET'])
def bell3():
    """ Just a stop in survey before third and final experiment """
    return render_template('bell3.html', user=USERID, trial=VARIANTID)

@app.route('/rank_guis', methods=['POST', 'GET'])
def rank_guis():
    """ Asking the user to rank the different GUIs used in the experiment """
    if request.method == 'POST':
        print(request.form)
        for v in request.form:
            # JSON_DATA[v] = request.form[v]
            print(v, request.form[v])
            try:
                current_response = "NA" if request.form[v] == "" else request.form[v]
                JSON_DATA[v] = current_response
            except Exception:
                current_response = "NA"
                JSON_DATA[v] = current_response

        return redirect('/final_opinions')

    # If the page is called, it will generate the following html file
    return render_template('rank_guis.html', user=USERID, trial=VARIANTID)

@app.route('/final_opinions', methods=['POST', 'GET'])
def final_opinions():
    """ Asking the user for any final opinions or feedback """
    # When the data is returned to the page, i.e submit is sent:
    if request.method == 'POST':

        print(request.form)
        for v in request.form:
            try:
                current_response = "NA" if request.form[v] == "" else request.form[v]
                JSON_DATA[v] = current_response
            except Exception:
                current_response = "NA"
                JSON_DATA[v] = current_response

        print("FINAL RESPONSE JSON: ", JSON_DATA)

        return redirect('/fin')

    # If the page is called, it will generate the following html file
    return render_template('final_opinions.html', user=USERID, trial=VARIANTID)


## page 14 Fin ####################
@app.route('/fin', methods=['POST', 'GET'])
def fin():
    """ Final page, saves data to csv file and thanks the user """
    try:
        file_exists = os.path.isfile(CSV_FILENAME)

        print("HERE IS THE JSON_DATA  " +str(JSON_DATA))

        hardcoded_key_set = set(CSV_ORDERING)
        gathered_key_set = set(JSON_DATA.keys())


        if not hardcoded_key_set == gathered_key_set:
            print("Keys not matching expected keys")
            print("Expected: ", hardcoded_key_set)
            print("Gathered: ", gathered_key_set)
            print("Missing:", hardcoded_key_set - gathered_key_set)
            print("Extra: ", gathered_key_set - hardcoded_key_set)
            raise Exception("SOME OF THE DATA IS NOT BEING SAVED, YELL AT ANNA, or check CSV_ORDERING")

        with open(CSV_FILENAME, 'a') as f: # pylint: disable=unspecified-encoding
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
    return render_template('fin.html', user=USERID, trial=VARIANTID)


if __name__ == "__main__":
    # write_headers()
    app.run(debug=True, host="0.0.0.0", port=1231)
