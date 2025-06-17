print("-------Calculating Exponenets----------")

print("Enter an integer as the base value:",end=" ")
bValue=int(input())
print("Enter an integer as the exponent:", end=" ")
eValue=int(input())
resultA=bValue**eValue
print(bValue, "raised to the power of", eValue, "is", resultA)


print("-------Addition and Subtraction----------")

print("Enter a starting integer:", end=" ")
startInt=int(input())
print("Enter an integer to add:", end=" ")
addInt=int(input())
print("Enter an integer to subtract:", end=" ")
subInt=int(input())
resultB=startInt+addInt-subInt
print(startInt,"+", addInt, "-", subInt, "is equal to", resultB)