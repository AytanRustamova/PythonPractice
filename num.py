nums=[1,2,3,6,7,8,23,78,34,12]

# 1. Ədədlərin cəmin tapan metod

a = 0
for element in nums:
    a = a + element

print(a)


# Tək ədədlərin cəmini tapan metod yazın
n = 0

for i in range(len(nums)):
    modul = nums[i] % 2
    if modul != 0:
        n = n + nums[i]

print(n)



 # - Ədədlər arasında rəqəmlərinin cəmi ən böyük olan ədədi tapın

nums=[1,2,3,6,7,8,23,78,34,12]
newArray= []
for i in nums:
    sumDigit = 0
    for digits in str(i):
        sumDigit = sumDigit + int(digits)
    newArray.append(sumDigit)
    a = max(newArray)
print(a)


# Tək ədədləri ayıraraq ayrıca bir massivə yığan metod yazın

n = 0
newArray = []
for i in range(len(nums)):
    modul = nums[i] % 2
    if modul != 0:
        n = nums[i]
        newArray.append(n)
        
print(newArray)

# - Ədədlərin böyükdən kiçiyə doğru sıralayın 

newArray = []

for i in range(len(nums)):
    a = max(nums)
    newArray.append(a)
    nums.remove(a)

print(newArray)



#Ədədlərin kvadratlarının olduğu yeni bir massiv yaradan metod yazın
import math

newArray = []
for i in range(len(nums)):
    arrPow = math.pow(nums[i],2)
    newArray.append(arrPow)
        
print(newArray)


# - Daxilində 3 rəqəmi olan neçə ədəd olduğunu ekrana çap edən metod yazın 

nums=[1,2,3,6,7,8,23,78,34,12]

checkNums = 3
counter = 0
for i in range(len(nums)):
    if (str(checkNums) in str(nums[i])):
        counter = counter + 1
print(counter)


