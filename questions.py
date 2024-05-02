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
    
TRUST_QUESTIONS = [ ]

assoc = ["Reliable", "Sincere", "Capable", "Ethical", "Predictable", "Genuine", "Skilled", "Respectable", 
                "Someone you can count on", "Candid", "Competent", "Principled", "Consistent", "Authentic",
                "Meticulous", "Has integrity"]
assoc_labels =["Reliable", "Sincere", "Capable", "Ethical", "Predictable", "Genuine", "Skilled", "Respectable", 
                "Count_on", "Candid", "Competent", "Principled", "Consistent", "Authentic",
                "Meticulous", "integrity"]

for i in range(len(assoc)):
        risky_q_string = "T_"+assoc_labels[i]+"_R"
        risky_q =  [risky_q_string, "radio_text", assoc[i],["1", "2", "3", "4", "5","6","7", "*"], ["Not at all", "Very", "Does Not Fit"] ]
        TRUST_QUESTIONS.append(risky_q)

        safe_q_string = "T_"+assoc_labels[i]+"_S"
        safe_q =  [safe_q_string, "radio_text", assoc[i],["1", "2", "3", "4", "5","6","7", "*"], ["Not at all", "Very", "Does Not Fit"] ]
        TRUST_QUESTIONS.append(safe_q)

print(TRUST_QUESTIONS)

RISK_QUESTIONS = []

risk_text = ["I will be able to achieve most of the goals I have set for myself.", 
             "When facing difficult tasks, I am certain that I will accomplish them.", 
             "In general, I think that I can obtain outcomes that are important to me.",
             "I believe I can succeed at most any endeavor to which I set my mind.",
             "I will be able to successfully overcome many challenges.",
             "I am confident that I can perform effectively on many different tasks.",
             "Compared to other people, I can do most tasks well.",
             "Even when things are tough, I can perform quite well.",
             "I am generally willing to take risks."]

risk_labels =  ["se_"+str(i) for i in range(1,9)] + ["risk_willingness"]
print(risk_labels)


for i in range(len(risk_text)):
        new_q =  [risk_labels[i], "radio_text", risk_text[i],["1", "2", "3", "4", "5","6","7", "*"], ["Not at all", "Very", "Does Not Fit"] ]
        RISK_QUESTIONS.append(new_q)