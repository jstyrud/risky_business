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
    
QUESTIONS_B = [

    #Enjoyment
        ["S2", "radio_text", "Using the virtual reality interface is fun.",          ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["S3", "radio_text", "Using the virtual reality interface is exciting.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["S4", "radio_text", "Using the virtual reality interface is boring.",    ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
                
    
]

# Unused, questions are randomized
QUESTION_ORDER = {

        "E1_": 1,
        "E2_": 2,
        "E3_": 3
    

}
