number_heroes = int(input())
names_heroes = input().split()
iq_heroes = input().split()
strength_heroes = input().split()
number_villain = int(input())

#creating a list of stats and hero names combined
iq_list = []
strength_list = []
combine_list = []
for i in range(number_heroes):
    iq_list.append([iq_heroes[i],names_heroes[i]])
    strength_list.append([strength_heroes[i],names_heroes[i]])
    combine_list.append([str(int(strength_heroes[i]) + int(iq_heroes[i])),names_heroes[i]])

final_list = []
#iterating through each type of villain
for i in range(number_villain):
    list1 = []
    stats_villian = input().split()
    if int(stats_villian[0]) == 1: #iq villian

        for j in range(number_heroes):
            if int(stats_villian[1]) <= int(iq_list[j][0]):
                list1.append(iq_list[j])

        score1 = 500000
        if len(list1) == 0:
            final_list.append('none')
        else:
            for k in range(len(list1)):
                if int(list1[k][0]) <= score1:
                    score1 = int(list1[k][0])
            list1_final = []
            for n in range(len(list1)):
                if int(list1[n][0]) == score1:
                    list1_final.append(list1[n][1])


            sorted_final_list = sorted(list1_final)
            final_list.append(sorted_final_list[0])



    if int(stats_villian[0]) == 2: #strength villian

        for j in range(number_heroes):
            if int(stats_villian[1]) <= int(strength_list[j][0]):
                list1.append(strength_list[j])

        score1 = 500000
        if len(list1) == 0:
            final_list.append('none')
        else:
            for k in range(len(list1)):
                if int(list1[k][0]) <= score1:
                    score1 = int(list1[k][0])
            list1_final = []
            for n in range(len(list1)):
                if int(list1[n][0]) == score1:
                    list1_final.append(list1[n][1])


            sorted_final_list = sorted(list1_final)
            final_list.append(sorted_final_list[0])



    if int(stats_villian[0]) == 3: #combine villian

        for j in range(number_heroes):
            if int(stats_villian[1]) <= int(combine_list[j][0]):
                list1.append(combine_list[j])

        score1 = 500000
        if len(list1) == 0:
            final_list.append('none')
        else:
            for k in range(len(list1)):
                if int(list1[k][0]) <= score1:
                    score1 = int(list1[k][0])
            list1_final = []
            for n in range(len(list1)):
                if int(list1[n][0]) == score1:
                    list1_final.append(list1[n][1])


            sorted_final_list = sorted(list1_final)
            final_list.append(sorted_final_list[0])


for i in final_list:
    print(i,end=" ")





