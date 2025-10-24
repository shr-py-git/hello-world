print("thanku for chosing python pizza delevries")
size=input("S, M or L\n") 
add_pepperoni=input("Pepper Y or N\n")
extra_cheese=input("Cheese Y or N\n")
bill=0
if size=="S" :
    bill=15
elif size=="M" :
    bill=20
elif size=="L":
    bill=25
if add_pepperoni=="Y":
        if size=="S":
            bill+=2
        else :
            bill+=3
if extra_cheese=="Y":
 bill+=1
print(f"your final bill is : ${bill}")
 
    


