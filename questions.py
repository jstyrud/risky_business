# list of questions.
# ## Each questions is a list: 0: UID, 1: title, 2: response options
# QUESTIONS = {

#     1: [    ["Q01", "radio_text", "Multiple choice question", ["1", "2","3", "4", "5", "6", "7"]],
#             ["Q02", "radio_img", "Multiple choice with emoji tho (or pics)", ["1", "2","3", "4", "5"]],
#             ["Q03", "open_text", "Text response", [None]],
#     ],
#     2: [    ["Q11", "radio_text", "Did the robot move in an acceptable way?", ["1", "2","3", "4", "5", "6", "7"]],
#             ["Q12", "radio_text", "Did the robot move as you would have expected?", ["1", "2","3", "4", "5", "6", "7"]],
#             ["Q13", "radio_img", "Emoji Response", ["1", "2","3", "4", "5"]],
#             ["Q14", "radio_text", "Did the robot move in an acceptable way?", ["1", "2","3", "4", "5", "6", "7"]],
#             ["Q15", "radio_img", "What was the robot's task", ["artichoke", "basket","sandtimer"]]
#     ]
    
QUESTIONS = [ ]

assoc = ["Reliable", "Sincere", "Capable", "Ethical", "Predictable", "Genuine", "Skilled", "Respectable", 
                "Someone you can count on", "Candid", "Competent", "Principled", "Consistent", "Authentic",
                "Meticulous", "Has integrity"]
assoc_labels =["Reliable", "Sincere", "Capable", "Ethical", "Predictable", "Genuine", "Skilled", "Respectable", 
                "Count_on", "Candid", "Competent", "Principled", "Consistent", "Authentic",
                "Meticulous", "integrity"]

for i in range(len(assoc)):
        risky_q_string = "T_"+assoc_labels[i]+"_R"
        risky_q =  [risky_q_string, "radio_text", assoc[i],["1", "2", "3", "4", "5","6","7", "*"], ["Not at all", "Very", "Does Not Fit"] ]
        QUESTIONS.append(risky_q)

        safe_q_string = "T_"+assoc_labels[i]+"_S"
        safe_q =  [safe_q_string, "radio_text", assoc[i],["1", "2", "3", "4", "5","6","7", "*"], ["Not at all", "Very", "Does Not Fit"] ]
        QUESTIONS.append(safe_q)

print(QUESTIONS)
# Unused, questions are randomized
QUESTION_ORDER = {

        "E1_": 1,
        "E2_": 2,
        "E3_": 3,
        "AA1_": 4,
        "AA2_": 5,
        "AA3_": 6,
        "AA4_": 7,
        "AE1_": 8,
        "AE2_": 9,
        "AE3_": 10,
        "IQ1_": 11,
        "IQ2_": 12,
        "IQ3_": 13,
        "P1_": 14,
        "P2_": 15
    

}
