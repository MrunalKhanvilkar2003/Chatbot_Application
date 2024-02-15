print("Hey! \nThis is Mrunal,How may I help you? ")
while True:
    def child():
        
        dict1={"can I track my child on the bus":"Yess! you can",
               "Can I send someone else to the pick up my child":"Please let us know beforehand so that we can inform the driver accordingly"}
        dict2={"1":"Yess! you can","2":"Please let us know beforehand so that we can inform the driver accordingly"}
        dict3={"hii":"hii","hello":"hello","how are you":"Good!"}
        user=input("Please tell me your query: _")
        if user in dict3: 
           print("chatbot:",dict3[user]) 
        
    
        elif user in dict1:
            print("chatbot:",dict1[user])
        else:
            print("\nSorry can't understand:")
            print("1.can I track my child on the bus")
            print("2.Can I send someone else to the pick up my child")
            user=input("Please select your query!type quit to exit")
            if user in dict2:
                print("chatbot:",dict2[user])
           
            else:
                 print("Thank you")
    child()
print("Hey! \nThis is Mrunal,How may I help you? ")
while True:   
    def route():
        
        dict11={"Which route does the bus take to school":"APMC road",
               "Which route does the bus take home":"The bus take the same route to schhol as it does from school that is via APMC  road"
               
               }
        dict22={"1":"APMC road","2":"The bus take the same route to schhol as it does from school that is via APMC  road"}
        dict33={"hii":"hii","hello":"hello","how are you":"Good!"}
        user=input("Please tell me your query: _")
        if user in dict33:
            print("chatbot:",dict33[user])
        
        elif user in dict11:
            
            print("chatbot:",dict11[user])
        else:
            print("\nSorry can't understand:")
            print("1.Which route does the bus take to school")
            print("2.Which route does the bus take home")
            user=input("Please select your query!type quit to exit")
            if user in dict22:
                print("chatbot:",dict22[user])
            else:
                 print("Thank you")
    route()
    
    
        
print("Hey! \nThis is Mrunal,How may I help you? ")
while True:
    def time():
        
        dict1={"What time will the bus come?":"Bus on the way reach in 20min at your place.",
               "What Time the bus gets to school":"About 10:00AM"
               
               }
        dict2={"1":"Bus on the way reach in 20min at your place.","2":"About 10:00AM"}
        dict3={"hii":"hii","hello":"hello","how are you":"Good!"}
        user=input("Please tell me your query: _")
        if user in dict3:
            print("chatbot:",dict3[user])
        
        elif user in dict1:
            print("chatbot:",dict1[user])
        else:
            print("\nSorry can't understand:")
            print("1.What time will the bus come?")
            print("2.What Time the bus gets to school")
            user=input("Please select your query!type quit to exit")
            if user in dict2:
                print("chatbot:",dict2[user])
            else:
                 print("Thank you")
    time()
    
    
          
          
   
   