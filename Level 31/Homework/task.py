name = input("შეიყვანე შენი სახელი დიდი ასოებით: ") 
name = name.lower()
print("სახელი პატარა ასოებით:", name)


surname = "jgamaze"  
surname = surname.upper()
print("გვარი დიდ ასოებად:", surname)


text = "nikolozi"
text = text.capitalize()
print("პირველი ასო დიდად:", text)


sentence = "nikoloozi"
index = sentence.find("g") 
print(" ასო მდებარეობს ინდექსზე:", index)


words = ["python",  "html", "css"]
for word in words:
    print(word.upper())