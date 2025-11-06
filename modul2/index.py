# # # # # # my_set = {1, 2, 3}
# # # # # # my_set = set()
# # # # # # my_set = set([4, 5, 6])
# # # # # #
# # # # # # print(my_set)
# # # # #
# # # # # #
# # # # # # set1 = {1, 2, 3}
# # # # # # set2 = {3, 4, 5}
# # # # # #
# # # # # # union_result_method = set1.union(set2)
# # # # # # print("Union: ", union_result_method)
# # # # # #
# # # # # # union = set1 | set2
# # # # # # print("Union method: ", union)
# # # # # #
# # # # # # intersection = set1 & set2
# # # # # # print("intersection method: ", intersection)
# # # # # #
# # # # # # difference = set1 - set2
# # # # # # print("difference method: ", difference)
# # # # # #
# # # # # # symmetrical_difference = set1 ^ set2
# # # # # # print("symmetrical_difference method: ", symmetrical_difference)
# # # # #
# # # # # #Set methods
# # # # #
# # # # # my_set = {1, 2, 3}
# # # # #
# # # # # my_set.add(4)
# # # # # my_set.remove(3)
# # # # # my_set.discard(1)
# # # # # my_set.clear()
# # # # # print (my_set)
# # # # # set_length = len(my_set)
# # # # # print("Length of set: ", set_length)
# # # # #Using sets - removing duplicates
# # # #
# # # # my_list = [1,2,3,6,7,6,7]
# # # #
# # # # unique_set = set(my_list)
# # # #
# # # # unique_list = (list(unique_set))
# # # #
# # # # print(unique_list)
# # #
# # # # IN || NOT IN
# # #
# # # loyalty_members = {"BABA", "Bled", "wirtual","granady"}
# # # costumer = "Bled"
# # #
# # # is_member = customer in loyalty_members
# # #
# # # print(is_member)
# # age = 18
# #
# # if age >= 18:
# #     print("You can vote")
# # else:
# #     prinst("You cant vote")
# temp = 28
# if temp > 30:
#     print("Its a hot day")
# elif 20 <= temp <= 30:
#     print("its a good day")
# else:
#     print("its a cold day")
# hhelloo
student_gpa = 4.5
student_score = 75
if student_gpa >= 3.5:
    if 50 <= student_score <= 65:
        print(f"Students with GPA {student_gpa} and tast score of {student_score} may be eligible for a partial scholar ship")
    elif student_score >65:
        print(f"Students with GPA {student_gpa} and tast score of {student_score} may be eligible for a full scholar ship")
    else:
        print(f"Students with GPA {student_gpa} and tast score of {student_score} is not eligible for a partial scholar ship")
else:
    print(f"Students with GPA {student_gpa} and tast score of {student_score} is not eligible for a scholar ship")