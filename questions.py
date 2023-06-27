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

    #Enjoyment
        ["F1", "radio_text", "I felt the drone was reliable",          ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],
        ["F2", "radio_text", "I felt that the drone could sense my emotions",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],
        
        
        ["F3", "radio_text", "I felt the drone was competent",     ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"]],
        ["F4", "radio_text", "I felt piloting the drone was enjoyable",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],




        ["F5", "radio_text", "I felt the drone was predictable",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],
        ["F6", "radio_text", "How satisfied were you with the level of control you had while flying the quadcopter drone?",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],




        ["F7", "radio_text", "I felt the drone was skilled",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],
        ["F8", "radio_text", "Considering your overall experience, how likely are you to fly a quadcopter drone again in the future?",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],




        ["F9", "radio_text", "I felt the drone was dependable",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],
        ["F10", "radio_text", "Rate your level of excitement while flying the drone",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],



        ["F11", "radio_text", "I felt the drone was capable.",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],
        ["F12", "radio_text", "I felt the drone landed gracefully.",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],

        ["F13", "radio_text", "I felt the drone was consistent.",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],
        ["F14", "radio_text", "I felt the drone moved elegantly in all directions.",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],

        ["F15", "radio_text", "I felt the drone was meticulous.",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],
        ["F16", "radio_text", "I felt the drone was hostile.",    ["0","1", "2", "3", "4", "5","6","7"], ["Not at all", "Very"] ],
        

]

# Unused, questions are randomized
QUESTION_ORDER = {

        "E1_": 1,
        "E2_": 2,
        "E3_": 3
    

}
