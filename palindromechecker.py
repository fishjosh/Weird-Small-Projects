def palindrome():
    string = input("Please input your word/phrase/sentence: ")
    print(("Type quit when you are done"))
    
    while string != 'quit': 
        
        string = string.replace(' ','')
        string = string.replace('.','')
        string = string.replace(',','')
        string = string.replace('!','')
        string = string.replace('?','')
        string = string.replace(':','')
        string = string.replace(';','')
        string = string.replace('"','')
        string = string.replace("'","")

        
        
        string = string.upper()
        
        if string[::-1]==string:
            print("Yes that is a palindrome")
            
        else:
            print("No that isn't a palindrome")
        string = input("Please input your word/phrase/sentence: ")
palindrome()    