# # # # # sentence = "Hello, world"
# # # # #
# # # # # for character in sentence:
# # # # #     if character.isalpha():
# # # # #         print (character)
# # # # numbers = [12, 45, 67, 92, 1, 2, 6, 7]
# # # #
# # # # maximum = numbers [0]
# # # #
# # # # for num in numbers:
# # # #     if num > maximum:
# # # #         maximum = num
# # # # print("max num is: ", maximum)
# # #
# # # count = 1
# # # while count <=5:
# # #     print("Iteration: ", count)
# # #     count += 1
# # numbers = [1,2,3,4,5]
# # target = 4
# #
# # for number in numbers:
# #     print (number)
# #     if number == target:
# #         print("Target found")
# #         break
# scores = [68,42,65,78]
# total = 0
# count = 0
# for score in scores:
#     if score < 50:
#         continue
#     total += score
#     count += 1
#
# average = total / count if count > 0 else 0
#
# print ("Average score above 50 ", average)
while True:
    user_input = input("Enter a positive integer: ")

    if user_input.isnumeric():
        number = int(user_input)
        if number > 0
            break


    print("Invalid input. Try again: ")

print("You entered a valid positive number")