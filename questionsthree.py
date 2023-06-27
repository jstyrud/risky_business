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
    
QUESTIONS_C = [

    #RISK
     
        ["R1", "radio_text", "I do not feel comfortable about taking chances.",     ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"]],
        ["R2", "radio_text", "I prefer situations that have foreseeable outcomes",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],
        ["R3", "radio_text", "Before I make a decision, I like to be absolutely sure how things will turn out.",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],
        ["R4", "radio_text", "I avoid situations that have uncertain outcomes.",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],
        ["R5", "radio_text", "I feel comfortable improvising in new situations.",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],
        ["R6", "radio_text", " I feel nervous when I have to make decisions in uncertain situations.",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],

        




        
    
]

# Unused, questions are randomized
QUESTION_ORDER = {

        "E1_": 1,
        "E2_": 2,
        "E3_": 3
    

}
