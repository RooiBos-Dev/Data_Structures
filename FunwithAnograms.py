data = ["code",
        "aaagmnrs",
        "anagrams",
        "doce"]


def answerQ(arr):
    arrsorted = arr
    answer = []
    for i in range(len(arr)-1):
        print("-----------------------------------------")
        checked = sorted(arr[i])
        print(checked)
        
        for j in range(len(arr)):
            comp = sorted(arr[j])
            print(comp)
            if(checked == comp):
                if(i<j):
                    answer.append(arr[i])
        print("-----------------------------------------")         
    answer.sort()
    print(answer)


answerQ(data)