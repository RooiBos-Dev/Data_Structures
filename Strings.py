class Strings():
    def legnthOf(self , str):
        length = len(word)
        print(length)
    def char_frequency(self, str1):
        dict = {}
        for n in str1:
            keys = dict.keys()
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
        print(dict)
    def firstAndLastLetters(self, str1):
        length = len(str1)
        if(length < 2):
            print("Empty string")
        else:
            first = str1[0:2]
            last = str1[-3:-1]
            final = first+last
            print(final)


obj = Strings()
word = "This is my string."
obj.char_frequency(word)
obj.firstAndLastLetters(word)