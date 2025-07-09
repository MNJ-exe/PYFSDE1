with open("dataq5.txt", "w") as f:
    ans=input("Enter the words you want: ")
    f.write(ans)

with open("dataq5.txt", "a") as f:
    ns = input("Enter the words you want to append: ")
    f.write(ns)

with open("dataq5.txt", "r") as f:
    content = f.read()
    print(content)
