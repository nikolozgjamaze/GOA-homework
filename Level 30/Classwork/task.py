# len  აბრუნებს ელემენტების რაოდენობას სიაში სტრიქონში ან სხვა ობიექტებში 
# append სიაში ამატებს ახალ ელემენტს ბოლოში
# insert სიაში ამატებს ახალ ელემენტს მითითებულ ინდექსზე
# pop შლის ელემენტს სიიდან  და აბრუნებს მას









names = ["ანა", "გიორგი", "ნიკა", "თამარი", "ლაშა"]


new_name = input("შეიყვანეთ სახელი, რომ დაამატოთ სიაში: ")


names.append(new_name)

print("განახლებული სია:", names)
print("სიის სიგრძე არის:", len(names))










fruits = ["Melon", "Orange", "Banana", "Watermelon", "Kiwi"]
fruits.pop()
fruits.insert(3, "Pomegranate")
print(fruits)



