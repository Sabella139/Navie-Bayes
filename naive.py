import pandas as pd
x= pd.DataFrame({"Weather":[1,2,3,1,1,2,3,3,1,3,1,2,2,3],"Play":[0,1,1,1,1,1,0,0,1,1,0,1,1,0]})
x
sum_1_yes=0
sum_2_yes=0
sum_3_yes=0
sum_1_no=0
sum_2_no=0
sum_3_no=0
yes=0
no=0
for num in range(0,13): 
    i=0
    if x.loc[num][i]==1:
        if x.loc[num][i+1]==1:
            sum_1_yes=sum_1_yes+1
            yes=yes+1
        else:
            sum_1_no=sum_1_no+1
            no=no+1
    elif x.loc[num][i]==2:
        if x.loc[num][i+1]==1:
            sum_2_yes=sum_2_yes+1
            yes=yes+1
        else:
            sum_2_no=sum_2_no+1
            no=no+1
    else:
        if x.loc[num][i+1]==1:
            sum_3_yes=sum_3_yes+1
            yes=yes+1
        else:
            sum_3_no=sum_3_no+1
            no=no+1
print('sunny-yes:',sum_1_yes)
print('Overcast-yes:',sum_2_yes)
print('Rainy-yes:',sum_3_yes)
print('sunny-no:',sum_1_no)
print('Overcast-no:',sum_2_no)
print('Rainy-no:',sum_3_no)
print('total_yes:',yes)
print('total_no:',no) 
print("Enter the query")
w1=int(input("Weather:1->Sunny 2: Overcast 3: Rainy"))
p1 =int(input("Play:yes->1 ,no->0"))
if p1==1:
    a=yes/14
else:
    a=no/14   
if w1==1:
    b=(sum_1_yes+sum_1_no)/14
    if p1==1:
        c= sum_1_yes/yes
    else:
        c=sum_1_no/no
    
elif w2==2:
    b=(sum_2_yes+sum_2_no)/14
    if p1==1:
        c=sum_2_yes/yes
    else:
        c=sum_2_no/no
else:
    b=(sum_3_yes+sum_3_no)/14
    if p1==1:
        c=sum_3_yes/yes
    else:
        c=sum_3_no/no

decision=c*a/b
inn=1-decision
if decision>inn:
    print("true")
else:
     print("false")  


