import random
import copy
import csv
PYCHARM_DEBUG = True


deck = ["AH", "AD", "AC", "AS", "2H", "2D", "2C", "2S","3H", "3D", "3C", "3S",
        "4H", "4D", "4C", "4S","5H", "5D", "5C", "5S","6H", "6D", "6C", "6S",
        "7H", "7D", "7C", "7S","8H", "8D", "8C", "8S","9H", "9D", "9C", "9S","10H", "10D", "10C", "10S"
       ,"JH", "JD", "JC", "JS","QH", "QD", "QC", "QS","KH", "KD", "KC", "KS"]
result_list = []
Human = []
AI_1 = []
AI_2 = []
AI_3 = []
AI_4 = []
AI_5 = []
filename = "poker_record.csv"
field = ["Hands", "Evaluation", "Probability"]
fi = open("Overall_game.txt", "w")

winning_avg = [0,0,0,0,0,0,0,0,0,0]
appear = [0,0,0,0,0,0,0,0,0,0]
for f in range(0, 500):
    random.shuffle(deck)
    a = 0
    for x in deck:
        Human.append(x)
        deck.remove(x)
        a += 1
        if a == 5:

            break

    probability = 0
    for v in range (0, 500):
        x = 0
        random.shuffle(deck)
        while x < 5:
            AI_1.append(deck[x])
            deck.remove(deck[x])

            AI_2.append(deck[x])
            deck.remove(deck[x])

            AI_3.append(deck[x])
            deck.remove(deck[x])

            AI_4.append(deck[x])
            deck.remove(deck[x])

            AI_5.append(deck[x])
            deck.remove(deck[x])

            x+=1


        human_showhand = []

        for x in Human:

            if x[0].isdigit() and x[1].isdigit():
                human_showhand.append((int(x[0] + x[1]), x[2]))
            elif x[0].isdigit() and not x[1].isdigit():
                human_showhand.append((int(x[0]), x[1]))
            else:
                if x[0] == "J":
                    human_showhand.append((11, x[1]))
                elif x[0] == "Q":
                    human_showhand.append((12, x[1]))
                elif x[0] == "K":
                    human_showhand.append((13, x[1]))
                elif x[0] == "A":
                    human_showhand.append((14, x[1]))

        AI1_showhand = []

        for x in AI_1:
            if x[0].isdigit() and x[1].isdigit():
                AI1_showhand.append((int(x[0] + x[1]), x[2]))
            elif x[0].isdigit() and not x[1].isdigit():
                AI1_showhand.append((int(x[0]), x[1]))
            else:
                if x[0] == "J":
                    AI1_showhand.append((11, x[1]))
                elif x[0] == "Q":
                    AI1_showhand.append((12, x[1]))
                elif x[0] == "K":
                    AI1_showhand.append((12, x[1]))
                elif x[0] == "A":
                    AI1_showhand.append((14, x[1]))
        AI2_showhand = []

        for x in AI_2:

            if x[0].isdigit() and x[1].isdigit():
                AI2_showhand.append((int(x[0] + x[1]), x[2]))
            elif x[0].isdigit() and not x[1].isdigit():
                AI2_showhand.append((int(x[0]), x[1]))
            else:
                if x[0] == "J":
                    AI2_showhand.append((11, x[1]))
                elif x[0] == "Q":
                    AI2_showhand.append((12, x[1]))
                elif x[0] == "K":
                    AI2_showhand.append((13, x[1]))
                elif x[0] == "A":
                    AI2_showhand.append((14, x[1]))
        AI3_showhand = []

        for x in AI_3:

            if x[0].isdigit() and x[1].isdigit():
                AI3_showhand.append((int(x[0] + x[1]), x[2]))
            elif x[0].isdigit() and not x[1].isdigit():
                AI3_showhand.append((int(x[0]), x[1]))
            else:
                if x[0] == "J":
                    AI3_showhand.append((11, x[1]))
                elif x[0] == "Q":
                    AI3_showhand.append((12, x[1]))
                elif x[0] == "K":
                    AI3_showhand.append((13, x[1]))
                elif x[0] == "A":
                    AI3_showhand.append((14, x[1]))
        AI4_showhand = []

        for x in AI_4:

            if x[0].isdigit() and x[1].isdigit():
                AI4_showhand.append((int(x[0] + x[1]), x[2]))
            elif x[0].isdigit() and not x[1].isdigit():
                AI4_showhand.append((int(x[0]), x[1]))
            else:
                if x[0] == "J":
                    AI4_showhand.append((11, x[1]))
                elif x[0] == "Q":
                    AI4_showhand.append((12, x[1]))
                elif x[0] == "K":
                    AI4_showhand.append((13, x[1]))
                elif x[0] == "A":
                    AI4_showhand.append((14, x[1]))
        AI5_showhand = []

        for x in AI_5:

            if x[0].isdigit() and x[1].isdigit():
                AI5_showhand.append((int(x[0] + x[1]), x[2]))
            elif x[0].isdigit() and not x[1].isdigit():
                AI5_showhand.append((int(x[0]), x[1]))
            else:
                if x[0] == "J":
                    AI5_showhand.append((11, x[1]))
                elif x[0] == "Q":
                    AI5_showhand.append((12, x[1]))
                elif x[0] == "K":
                    AI5_showhand.append((13, x[1]))
                elif x[0] == "A":
                    AI5_showhand.append((14, x[1]))
        list_of_hand = []

        def evaluation(a):
            if (a[4][0] == 14 and a[3][0] == 13 and a[2][0] == 12 and a[1][0] == 11 and a[0][0] == 10) and a[4][1] == a[3][1] == a[2][1] == a[1][1] == a[0][1]:
                return 10
            elif ((a[4][0] - a[3][0] == a[3][0] - a[2][0] == a[2][0] - a[1][0] == a[1][0] - a[0][0] == 1) or(a[4][0] - a[3][0] == a[3][0] - a[2][0] == a[2][0] - a[1][0] == a[1][0] == 1 and a[0][0] == 14) ) and a[4][1] == a[3][1] == a[2][1] == a[1][1] == a[0][1]:
                return 9
            elif a[0][0] == a[1][0] == a[2][0] == a[3][0] or a[1][0] == a[2][0] == a[3][0] == a[4][0]:
                return 8
            elif (a[0][0] == a[1][0] and a[2][0] == a[3][0] == a[4][0]) or (a[0][0] == a[1][0] == a[2][0] and a[3][0] == a[4][0]):
                return 7
            elif a[4][1] == a[3][1] == a[2][1] == a[1][1] == a[0][1]:
                return 6
            elif (a[4][0] - a[3][0] == a[3][0] - a[2][0] == a[2][0] - a[1][0] == a[1][0] - a[0][0] == 1):
                return 5
            elif a[0][0] == a[1][0] == a[2][0] or a[1][0] == a[2][0] == a[3][0] or a[2][0] == a[3][0] == a[4][0]:
                return 4
            elif (a[0][0] == a[1][0] and a[2][0] == a[3][0]) or (a[1][0] == a[2][0] and a[3][0] == a[4][0]):
                return 3
            elif a[0][0] == a[1][0] or a[1][0] == a[2][0] or a[2][0] == a[3][0] or a[3][0] == a[4][0]:
                return 2

            else:
                return 1

        def highhand(a):
            max_list = []
            b = []
            for x in a:
                b.append(x)
            for i in range(0, 5):
                if len(a[0]) == 0:
                    return 1
                    break
                for y in a:
                    max_each = y[-1][0]
                    max_list.append(max_each)
                max_score = max(max_list)
                remove_list = []
                for z in a:
                    if z[-1][0] == max_score:
                        continue
                    else:
                        remove_list.append(z)
                for k in remove_list:
                    if k in a:
                        a.remove(k)
                if len(a) == 1 and max_score == b[0][-1][0]:
                    return 1
                    break
                elif len(a) != 1 and max_score == b[0][-1][0]:
                    for i in a:
                        i.remove(i[-1])
                    max_list = []
                    continue
                elif max_score != b[0][-1][0]:

                    return 0
                    break



        #list_of_hand.append([(13, 'H'), (13, 'S'), (10, 'S'), (10, 'D'), (8, 'S')])
        #list_of_hand.append([(2, 'S'), (1, 'D'), (6, 'D'), (3, 'C'), (11, 'C')])
        #list_of_hand.append([(12, 'S'), (7, 'D'), (5, 'D'), (1, 'C'), (8, 'C')])
        #list_of_hand.append([(6, 'S'), (11, 'D'), (2, 'D'), (4, 'C'), (5, 'C')])
        #list_of_hand.append([(13, 'D'), (13, 'C'), (10, 'H'), (10, 'C'), (8, 'H')])
        #list_of_hand.append([(1, 'H'), (12, 'C'), (11, 'C'), (8, 'H'), (2, 'H')])

        list_of_hand.append(human_showhand)
        list_of_hand.append(AI1_showhand)
        list_of_hand.append(AI2_showhand)
        list_of_hand.append(AI3_showhand)
        list_of_hand.append(AI4_showhand)
        list_of_hand.append(AI5_showhand)



        sc_list = []
        for x in list_of_hand:
            x.sort()

            check = evaluation(x)
            if check == 10:
                sc_list.append(9)
            elif check == 9:
                sc_list.append(8)
            elif check == 8:
                sc_list.append(7)
            elif check == 7:
                sc_list.append(6)
            elif check == 6:
                sc_list.append(5)
            elif check == 5:
                sc_list.append(4)
            elif check == 4:
                sc_list.append(3)
            elif check == 3:
                sc_list.append(2)
            elif check == 2:
                sc_list.append(1)
            elif check == 1:
                sc_list.append(0)



        play_round = []


        def find_common(a):
            count = 0
            listt = []
            for i in range(0, len(a)):
                listt.append(a[i][0])
            return_num = listt[0]
            for x in listt:
                freq = listt.count(x)
                if count < freq:
                    count = freq
                    return_num = x

            return return_num




        if (sc_list[0] == max(sc_list)):
            count = 0
            play_round.append(list_of_hand[0])
            for i in range(1, len(sc_list)):
                each_AI = sc_list[i]
                if each_AI < max(sc_list):
                    count += 1
                else:
                    play_round.append(list_of_hand[i])
            if count == 5:
                probability += 1

            else:
                if max(sc_list) == 8:
                    max_list = []
                    for i in play_round:
                        max_list.append(i[4][0])
                    max_score = max(max_list)
                    if max_score == play_round[0][4][0]:
                        probability += 1


                elif max(sc_list) == 7:  # four of a kind
                    common_list = []
                    for i in play_round:
                        num = find_common(i)
                        common_list.append(num)
                    max_num = max(common_list)
                    human_hand = find_common(play_round[0])
                    if max_num == human_hand:
                        probability += 1


                elif max(sc_list) == 6:  # full house
                    common_list = []
                    for i in play_round:
                        num = find_common(i)
                        common_list.append(num)
                    max_num = max(common_list)
                    human_hand = find_common(play_round[0])
                    if max_num == human_hand:
                        probability += 1

                elif max(sc_list) == 5:  # flush
                    result = highhand(play_round)
                    if result == 1:
                        probability+=1


                elif max(sc_list) == 4:  # straight
                    max_list = []
                    for i in play_round:
                        max_list.append(i[4][0])
                    max_score = max(max_list)
                    if max_score == play_round[0][4][0]:
                        probability += 1


                elif max(sc_list) == 3:  # three of a kind
                    common_list = []
                    for i in play_round:
                        num = find_common(i)
                        common_list.append(num)
                    max_num = max(common_list)
                    human_hand = find_common(play_round[0])
                    if max_num == human_hand:
                        play_round_2 = []
                        for x in play_round:
                            num2 = find_common(x)
                            if num2 == max_num:
                                play_round_2.append(x)
                        if len(play_round_2) == 1:
                            probability += 1

                        else:
                            dummy = play_round_2.copy()
                            for i in range(0, 3):
                                for x in dummy:

                                    for y in x:
                                        if y[0] == max_num:
                                            x.remove(y)
                            result = highhand(dummy)
                            if result == 1:
                                probability += 1

                elif max(sc_list) == 2:  # two pair
                    dummy2 = copy.deepcopy(play_round)
                    for g in range(0, 2):
                        common_list = []
                        for i in dummy2:
                            i.sort(reverse=True)
                            num = find_common(i)
                            common_list.append(num)
                        max_num = max(common_list)
                        human_hand = find_common(dummy2[0])
                        if max_num == human_hand:
                            play_round_2 = []
                            for x in dummy2:
                                num2 = find_common(x)
                                if num2 == max_num:
                                    play_round_2.append(x)
                            if g == 0:
                                dummy = copy.deepcopy(play_round_2)
                            if len(play_round_2) == 1:
                                probability += 1
                                break

                            else:

                                for i in range(0, 2):
                                    for x in dummy:
                                        for y in x:
                                            if y[0] == max_num:
                                                x.remove(y)
                                    for z in dummy2:
                                        for i in z:
                                            if i[0] == max_num:
                                                z.remove(i)

                            for a in dummy:
                                if len(a) == 1:
                                    result = highhand(dummy)
                                    if result == 1:
                                        probability += 1
                                break

                elif max(sc_list) == 1:  # one pair
                    common_list = []
                    for i in play_round:
                        num = find_common(i)
                        common_list.append(num)
                    max_num = max(common_list)
                    human_hand = find_common(play_round[0])
                    if max_num == human_hand:
                        play_round_2 = []
                        for x in play_round:
                            num2 = find_common(x)
                            if num2 == max_num:
                                play_round_2.append(x)
                        if len(play_round_2) == 1:
                            probability+=1


                        else:
                            dummy = copy.deepcopy(play_round_2)
                            for i in range(0, 2):
                                for x in dummy:

                                    for y in x:
                                        if y[0] == max_num:
                                            x.remove(y)
                            result = highhand(dummy)
                            if result == 1:
                                probability += 1

                elif max(sc_list) == 0:  # high hand
                    dummy = copy.deepcopy(play_round)
                    result = highhand(dummy)
                    if result == 1:
                        probability += 1

        for y in range (0,3):
            for x in AI_1:
                deck.append(x)
                AI_1.remove(x)
            for x in AI_2:
                deck.append(x)
                AI_2.remove(x)
            for x in AI_3:
                deck.append(x)
                AI_3.remove(x)
            for x in AI_4:
                deck.append(x)
                AI_4.remove(x)
            for x in AI_5:
                deck.append(x)
                AI_5.remove(x)



    see_eval = evaluation(list_of_hand[0])
    if see_eval == 10:
        c_eval = " Royal Flush "
        appear[9]+=1
        winning_avg[9] +=probability
    elif see_eval == 9:
        c_eval =" Straight Flush "
        appear[8] += 1
        winning_avg[8] += probability
    elif see_eval == 8:
        appear[7] += 1
        winning_avg[7] += probability
        c_eval =" Four of a kind "
    elif see_eval == 7:
        appear[6] += 1
        winning_avg[6] += probability
        c_eval =" Full House "
    elif see_eval == 6:
        appear[5] += 1
        winning_avg[5] += probability
        c_eval =" Flush "
    elif see_eval == 5:
        appear[4] += 1
        winning_avg[4] += probability
        c_eval =" Straight "
    elif see_eval == 4:
        appear[3] += 1
        winning_avg[3] += probability
        c_eval =" Three of a kind"
    elif see_eval == 3:
        appear[2] += 1
        winning_avg[2] += probability
        c_eval =" Two pair "
    elif see_eval == 2:
        winning_avg[1] += probability
        appear[1] += 1
        c_eval =" One pair "
    elif see_eval == 1:
        winning_avg[0] += probability
        appear[0] += 1
        c_eval =" No pair "

    result_list.append(((Human[0], Human[1],Human[2], Human[3], Human[4]), c_eval, (probability * 100 / 500)))


    for y in range(0, 3):
        for r in Human:
            deck.append(r)
            Human.remove(r)

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(field)
    csvwriter.writerows(result_list)

if appear[0] != 0 :
    fi.write("The percentage of high hand is: " + str((appear[0]*100)/500) + "%" + "\n")
    fi.write("The winning percentage of high hand is: " + str(round((winning_avg[0] * 100) / (appear[0]*500),2)) + "%" + "\n\n")
else:
    fi.write("High hand doesn't appear! \n\n")
if appear[1] != 0  :
    fi.write("The percentage of one pair is: "+ str((appear[1] * 100) / 500) + "%\n")
    fi.write("The winning percentage of one pair is: " + str(round((winning_avg[1] * 100) / (appear[1]*500),2)) + "%\n\n")
else:
    fi.write("One pair doesn't appear! \n\n")
if appear[2] != 0 :
    fi.write("The percentage of two pair is: "+ str((appear[2] * 100) / 500) + "%\n")
    fi.write("The winning percentage of two pair is: " + str(round((winning_avg[2] * 100) / (appear[2]*500),2)) + "%\n\n")
else:
    fi.write("Two pair doesn't appear! \n\n")
if appear[3] != 0 :
    fi.write("The percentage of three of a kind is: " + str((appear[3] * 100) / 500) + "%\n")
    fi.write("The winning percentage of three of a kind is: " + str(round((winning_avg[3] * 100) / (appear[3]*500),2)) + "%\n\n")
else:
    fi.write("Three of a kind doesn't appear! \n\n")
if appear[4] != 0 :
    fi.write("The percentage of straight is: "+ str((appear[4] * 100) / 500) + "%\n")
    fi.write("The winning percentage of straight is: " + str(round((winning_avg[4] * 100) / (appear[4]*500),2)) + "%\n\n")
else:
    fi.write("Straight doesn't appear! \n\n")
if appear[5] != 0 :
    fi.write("The percentage of flush is: "+ str((appear[5] * 100) / 500) + "%\n")
    fi.write("The winning percentage of flush is: " + str(round((winning_avg[5] * 100) / (appear[5]*500),2)) + "%\n\n")
else:
    fi.write("Flush doesn't appear! \n\n")
if appear[6] != 0 :
    fi.write("The percentage of full house is: "+ str((appear[6] * 100) / 500) + "%\n")
    fi.write("The winning percentage of full house is: " +str(round((winning_avg[6] * 100) / (appear[6]*500),2)) + "%\n\n")
else:
    fi.write("Full house doesn't appear! \n\n")
if appear[7] != 0 :
    fi.write("The percentage of four of a kind is: "+ str((appear[7] * 100) / 500) + "%\n")
    fi.write("The winning percentage of four of a kind is: " + str(round((winning_avg[7] * 100) / (appear[7]*500),2)) + "%\n\n")
else:
    fi.write("Four of a kind doesn't appear! \n\n")
if appear[8] != 0 :
    fi.write("The percentage of straight flush is: "+ str((appear[8] * 100) / 500) + "%\n")
    fi.write("The winning percentage of straight flush is: " + str(round((winning_avg[8] * 100) / (appear[8]*500),2)) + "%\n\n")
else:
    fi.write("Straight flush doesn't appear! \n\n")
if appear[9] != 0 :
    fi.write("The percentage of royal flush is: "+ str((appear[9] * 100) / 500) + "%\n")
    fi.write("The winning percentage of royal flush is: " + str(round((winning_avg[9] * 100) / (appear[9]*500),2)) + "%\n\n")
else:
    fi.write("Royal flush doesn't appear! \n\n")

fi.close()
