s = 4
f = 5.5
print(s + f)

str1 = 'Leela'
print(str1)
print(str1[0])
print(str1[-1])  # Reversing the string
print(str1[2])


str2 = 'Mopuri'
str3 = ' Sai'
print(str2 + str3)

# define list
my_list = [str1, str2, str3]
# what are the difference between list and tuple?
print(my_list[::-1])
# A list is mutable, meaning you can change its content, while a tuple is immutable.
my_tuple = (str1, str2, str3)   
print(my_tuple)
# A tuple cannot be changed after creation, while a list can be modified.   
print(my_tuple[0])
print(my_tuple[1])
# my_tuple[1] = 'Yadav'
print(my_tuple)  # This will raise an error because tuples are immutable
mynew_tuple = ('Mahesh Babu', 'Jagan', 'Ntr', 'rrr')
print(mynew_tuple[0], mynew_tuple[-1])

student_marks = {
    'Sai': 90,
    'Prem': 91,
    'Leela': 95,
    'sai': 95,
    'prem': 95
}
print(student_marks)
print(student_marks['Sai'])
student_marks['Leela'] = 100
print(student_marks)
for s in range(-34, 400, 17):
    print(s)
print(student_marks['sai'])  # This will print the value for the key 'sai'
print(student_marks['prem'])  # This will print the value for the key 'prem'    
 