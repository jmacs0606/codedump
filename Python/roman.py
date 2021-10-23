class Solution:
    @staticmethod
    def romanToInt(s):
        charString = s + "@"
        returnInt = 0
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 100,
            "@":0
        }
        subs = {
            "I": ["V","X"],
            "X": ["L","C"],
            "C": ["D","M"]
        }
        print(charString)
        while True:
            i = 0
            currentIndex = charString[i]
            lastIndex = ""
            
            if currentIndex == 0:
                print("hi")
                return returnInt
                break

            nextIndex = charString[i+1]
            print("total: " + str(returnInt))
            if  symbols[currentIndex] < symbols[nextIndex] :
                returnInt += symbols[currentIndex]

            if symbols[nextIndex] == symbols[currentIndex]:
                returnInt += symbols[currentIndex]
                break


print(Solution.romanToInt("III"))