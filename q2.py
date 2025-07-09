def prin():
    inp=list(map(int,input("Enter your input: ").strip().split()))
    li=[]
    for i in inp:
        li.append(i)
    print(f"List in reverse order:{li[::-1]}")
    print(f"Sum of the list:{sum(li)}")
    print(f"Average of the numbers:{sum(li)//5}")

if __name__ == '__main__':
    prin()