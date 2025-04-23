
word = input("შეიყვანე სიტყვა: ")


print("პატარა ასოებით:", word.lower())


print("დიდი ასოებით:", word.upper())

print("პირველი დიდი, დანარჩენი პატარა:", word.capitalize())













sentence1 = input("შეიყვანე პირველი წინადადება: ")
sentence2 = input("შეიყვანე მეორე წინადადება: ")
sentence3 = input("შეიყვანე მესამე წინადადება: ")

print("\nდამუშავებული წინადადებები:")
print("პირველი (lower):", sentence1.lower())
print("მეორე (upper):", sentence2.upper())
print("მესამე (capitalize):", sentence3.capitalize())









my_name = "nikoloz"


user_name = input("შეიყვანე შენი სახელი: ")

if my_name.lower() == user_name.lower():
    print("Our names are similar!")
else:
    print("We have different names.")












sentence = "ეს არის ერთგვარი მაგალითი პროგრამისთვის."


formatted_sentence = sentence.lower().capitalize()


print("დამუშავებული წინადადება:", formatted_sentence)













example = "გამარჯობა"
print(example.lower()) 

example = "hello"
print(example.upper()) 


example = "gAmArJoBa"
print(example.capitalize()) 


example = "  hello  "
print(example.strip())  


example = "banana"
print(example.replace("a", "o"))  


