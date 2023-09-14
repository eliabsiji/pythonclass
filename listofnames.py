print("hello, we will need a list of ten names...")
count = 1
List = []
while count > 0:
    print(f"count {count}")
    n =input("Enter name:")
    if n == "x":
        break
    else:
        List.append(n)
        count =  count + 1
print(List)

 
