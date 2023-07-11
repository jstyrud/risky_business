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
    
QUESTIONS = [

    #TRUST
      #Enjoyment
        ["T1_F", "radio_text", "To what extent could the drone's behavior be predicted from moment to moment?",["1", "2", "3", "4", "5","6","7"], ["Not at all predictable", "Extremely predictable"] ],
        ["T2_F", "radio_text", "To what extent was the drone capable of sensing your emotions?",    ["1", "2", "3", "4", "5","6","7"], ["Not at all capable", "Extremely capable"] ],
        
        
        ["T3_F", "radio_text", "To what extent could you count on the drone to do its job?", ["1", "2", "3", "4", "5","6","7"], ["Not at all", "Extremely"]],
        ["T4_F", "radio_text", "How enjoyable did you find piloting the drone?",    ["1", "2", "3", "4", "5","6","7"], ["Not at all enjoyable", "Extremely enjoyable"] ],




        ["T5_F", "radio_text", "What degree of faith do you have that the drone will be able to cope with similar situations in the future?",    ["1", "2", "3", "4", "5","6","7"], ["No faith at all", "Complete faith"] ],
        ["T6_F", "radio_text", "How satisfied were you with the level of control you had while flying the quadcopter drone?",    ["1", "2", "3", "4", "5","6","7"], ["Not at all satisfied", "Extremely satisfied"] ],




        ["T7_F", "radio_text", "Overall how much do you trust the drone?",    ["1", "2", "3", "4", "5","6","7"], ["Not at all", "Extremely"] ],
        ["T8_F", "radio_text", "How willing would you be you to fly this drone again in the future?",    ["1", "2", "3", "4", "5","6","7"], ["Not at all willing", "Extremely willing"] ],
        
        ["T1_NF", "radio_text", "To what extent could the drone's behavior be predicted from moment to moment?",["1", "2", "3", "4", "5","6","7"], ["Not at all predictable", "Extremely predictable"] ],
        ["T2_NF", "radio_text", "To what extent was the drone capable of sensing your emotions?",    ["1", "2", "3", "4", "5","6","7"], ["Not at all capable", "Extremely capable"] ],
        
        
        ["T3_NF", "radio_text", "To what extent could you count on the drone to do its job?", ["1", "2", "3", "4", "5","6","7"], ["Not at all", "Extremely"]],
        ["T4_NF", "radio_text", "How enjoyable did you find piloting the drone?",    ["1", "2", "3", "4", "5","6","7"], ["Not at all enjoyable", "Extremely enjoyable"] ],




        ["T5_NF", "radio_text", "What degree of faith do you have that the drone will be able to cope with similar situations in the future?",    ["1", "2", "3", "4", "5","6","7"], ["No faith at all", "Complete faith"] ],
        ["T6_NF", "radio_text", "How satisfied were you with the level of control you had while flying the quadcopter drone?",    ["1", "2", "3", "4", "5","6","7"], ["Not at all satisfied", "Extremely satisfied"] ],




        ["T7_NF", "radio_text", "Overall how much do you trust the drone?",    ["1", "2", "3", "4", "5","6","7"], ["Not at all", "Extremely"] ],
        ["T8_NF", "radio_text", "How willing would you be you to fly this drone again in the future?",    ["1", "2", "3", "4", "5","6","7"], ["Not at all willing", "Extremely willing"] ],
    
]

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
