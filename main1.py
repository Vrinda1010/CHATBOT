import re
import long_responses as long
import sqlite3
import pandas as pd
import pyodbc


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=10.232.15.52;'
                      'Database=RPA_Database;'
                      'Trusted_Connection=yes;')


def abc(name1):
    global name
    name = input(" Please Enter your name :")
    return name
#ShoppingCartNo=input("Please Enter your SC Number: ")
#cursor1= conn.cursor()
#global cursor2
#cursor2=cursor1.execute("Select GR_IR_Amount from InvoiceVendor where SC#= (?)",(ShoppingCartNo))

#for row in cursor1: 
    #print(row)

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

   
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0



def check_all_messages(message):
    highest_prob_list = {}
    
    
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    
    # Responses -------------------------------------------------------------------------------------------------------

    response('Hello '+ name + '! Hope you are doing well.', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('Sure. Could you please provide me with Vendor ID/Invoice Name?', ['Please', 'tell', 'my',  'Balance', 'Amount'])
    response('Vendor ID: 101 and Invoice Number: XXXXX',['Yes'])
    #response("Hey, I am' + print g  ", ['What','is','your','name?'], required_words=['name'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    #response('GR_Amount : ' + cursor2 + 'only' ,['ShoppingCartNo'])
    
    
    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
   
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match
def get_response(user_input):
    #print("ABC")
     
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
    #while True:
        #print('Customer Care: ' + get_response(input('Vendor : ')))
   


