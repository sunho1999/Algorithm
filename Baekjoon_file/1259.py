
while(True):
    word = input()
    check_list = []
    if word =="0":
        break
    list_word = list(word)
    for i in range(0,(len(list_word))//2):
        if list_word[i] == list_word[-1-i]:
            check_list.append("yes")
        else:
            check_list.append("no")
    if "no" not in check_list:
        print("yes")
    elif "no" in check_list:
        print("no")



