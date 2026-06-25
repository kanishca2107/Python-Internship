#DICTIONARIES#
student = {
    "name":"arun",
    "age":21,
    "marks":98,
    "city":"coimbatore"
}
print(student.get("name"))
print(student.get("age")) # getting the values using get method(method 1)#


#ADDING NEW STUDENTS#
student["mark"] = "89"#updating the existing (single values)
student["name"] = "rohan"#updating the existing 
print(student.get("name"))
print(student.get("mark"))
print(student.get("age"))
print(student.get("city"))#adding new element


#PRINTING KEY VALUES ONLY
print(student.keys())
#COVERTING THE KEY TO THE LIST
print(list(student.keys()))#this method is common also for values(use the word value insted of key while the conversion of the key)
print(student.items())#returns the entire items
student.update({
    "name":"rohan",
    "age":45,
    "city":"chennai"
})#use when we update multiple values at a time (especially for the multiple values)
student.pop("city")#deleting the dictionary
print(student)#this is mandatory after removing the value and to print the extra value


#========DICTIONARY COMPREHENSION==========(short way to create a dictionary
squares = {}
for i in range(1,6):
    squares[i]=i*i
print(squares)#if we print this line inside the loop then  the output will be like a pattern
#compensation for dictionary
squares = {i: i*i for i in range(1,6)}
print(squares)


#CONVERTING NAMES TO THE LENGTHS#
names = ["arun","raju","ram"]
result = {
    name: len(names)
    for name in names
}
print(result)#o/p:{'arun':4,'raju':4,'ram':3}


#WITH CONDITION
result = {
    i : i*i
    for i in range(10)
    if i%2 == 0
}
print(result)


#MERGING OF DICTIONARIES#
employee = {
    "name":"ram",
    "age":20
}
details = {
    "city":"coimbutore",
    "address": "sundar nagar,madurai"
}
employee.update(details)#UPADTE METHOD(METHOD 1)
print(employee) #but in this method if same value exist new one replces the old value

#METHOD 2 |
result = employee | details
print(result)

#NESTED DICTIONARY 
employee = {
    "id":101,
    "person":{
        "name":"rahul",
        "age":32
    },
    "salary":{
        "bonus":2500,
        "discount":10000
    }
}#print(employee["id"]),#print(employee["salary"]["discount"])











