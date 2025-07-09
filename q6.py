def avg(m):
    ans=sum(m)//len(m)
    return ans
def val_grade(avg):
    if avg>90:
        return "A"
    elif avg>80:
        return "B"
    elif avg>70:
        return "C"
    elif avg>60:
        return "D"
    else:
        return "Fail"
