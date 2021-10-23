class parser: #these are all static methods but if you wanted to be able to create objects you could, would require tweaking
    def __init__(self):
        pass

    @staticmethod    
    def checkUser(inString): #dont worry about this method, it is meant for the getGoodPasswords method
        if len(inString) >= 8:
            return True
        else:
            return False

    @staticmethod
    def checkPass(inString): #dont worry about this method, it is meant for the getGoodPasswords method
        if len(inString) < 8: #first checks if password length is less than 8
            return False

        need3 = 0
        special = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
        checkDict = {
            "upperCase": False,
            "lowerCase": False,
            "number": False,
            "specialChar": False
                    
        }
        #iters through pw to check for 4 conditions, atleast 3 must be satisfied
        for i in inString:
            if i.isupper() and checkDict["upperCase"] == False: #checks if it is upper and also checks if it has already been found
                need3 += 1
                checkDict["upperCase"] = True #sets status to found

            if i.islower() and checkDict["lowerCase"] == False: #checks if it is lower and also checks if it has already been found
                need3 += 1
                checkDict["lowerCase"] = True #sets status to found

            if i.isnumeric() and checkDict["number"] == False: #checks if it is number and also checks if it has already been found
                need3 += 1
                checkDict["number"] = True #sets status to found

            if i in special and checkDict["specialChar"] == False: #checks if it is number and also checks if it has already been found
                need3 += 1
                checkDict["specialChar"] = True #sets status to found

        if need3 >= 3:
            return True

        else:
            return False


    @staticmethod    
    def getGoodCreds(inFile,outFile): #takes in txt file as parameter
        returnList = []
        
        a = open(inFile,'r').read().split('\n') #hard to explain but converts txt file into list by splitting it at every newline, this way the \n doesnt mess up data

        for i in a:
            need2 = 0

            breakUp = i.split(":") #converts "user:pass" into [user,pass]

            if parser.checkUser(breakUp[0]):
                need2 += 1

            if parser.checkPass(breakUp[1]):
                need2 += 1

            if need2 == 2:
                returnList.append("%s\n" % i)
        


        b = open(outFile,'w') #opens output file

        for i in returnList:
            b.write(i)

        b.close()
            

parser.getGoodCreds('data.txt','out.txt')  





  
