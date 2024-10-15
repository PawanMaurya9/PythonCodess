a = float(input(f"Enter the Marks: "))
if a>=90 :
    print(f"{a} is grad A")
elif a>=80 and a<90:
    print(f"{a} is grad B")
if a>=70 and a < 80:
    print(f"{a} is grad C")
if a>=60 and a < 70:
    print(f"{a} is grad D")
if a>=50 and a < 60:
    print(f"{a} is grad E")
if a>=40 and a < 50:
    print(f"{a} is grad F")
else:
    print(a)