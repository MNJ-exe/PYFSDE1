def div(a,b):
    try:
        ans=a//b
        return ans
    except ZeroDivisionError:
        print("division by zero")
        exit()
if __name__=="__main__":
    a,b=list(map(int,input("enter two numbers: ").split()))
    print(div(a,b))