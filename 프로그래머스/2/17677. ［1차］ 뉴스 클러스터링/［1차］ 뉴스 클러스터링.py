def solution(str1, str2):
    list1=[str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    list2=[str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    inters = []
    list1_temp = list1.copy()
    for i in list2:
        if i in list1_temp:
                list1_temp.remove(i)
                inters.append(i)
    temp = list1.copy()
    uni = list1.copy()
    for i in list2:
        if i not in temp:
            uni.append(i)
        else:
            temp.remove(i)
    return int((len(inters)/len(uni) if len(uni) != 0 else 1)*65536)
