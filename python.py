print("================================================================")*5

#Numbers

#69
x=18
y=30
sum=x*y
print('farm can grow {} tons of corn.'.format(sum))

#70
v0=50
IHeight=5

t=3
high =(-16*(t*t)) + (v0*t) + IHeight
print("The height of the ball is {} feet ".format(high))

#71
l=5
Arrival=9
speed=81.34
d=(Arrival-l)*speed
print('The distance is {} km per hour.'.format(d))

#72
m1=23352
m2=23695
gallons=14
difMiles=(m2-m1)/gallons
print('The car between the two fillings {} miles per gallon'.format(difMiles))

#73
Electricity=750
people=5
Electricity/=30
powerday=Electricity/people
print('The daily power consumption in watts of each resident is {} million watts per day'.format(powerday))

#74
area=432
side=area**0.5
print('Each side of the deck is {:.2f} feet'.format(side))

#75
intailmoney=77
rateinterest=8.7
Imoney=1000
money1year=intailmoney+(Imoney*rateinterest/100)
money2year=money1year+(money1year*rateinterest/100)
print('The account will hold ${:.2f} two years later.'.format(money2year))


#Strings


#97
second=float(input("Enter seconds between lightning and thunder : "))
dis=second/5
print("Distanse from storm : {} miles .".format(dis))

#98
age=int(input("Enter your age : "))
h=int(input("Enter your resting heart rate : "))
Rate=int(0.7*(220-age)+0.3*h)
print("Training herat rate : {} beats/min .".format(Rate))

#101
name=input("Enter your name : ")
w=int(input("Enter number of game won : "))
l=int(input("Enter number of game lost : "))
Won=w/(w+l)
print("{} won {:.1%} of thier games .".format(name,Won))

#108
purchase=float(input("Enter purchase price : "))
selling=float(input("Enter selling price : "))
Markup=selling-purchase
perMarkup=Markup/purchase
proMargin=Markup/selling
print("Markup: ${}".format(Markup))
print("Percentage markup: {:.1%}".format(perMarkup))
print("Profit margin: {:.2%}".format(proMargin))

#109
n=input("Enter number :")
x=n.find(".")

print("{} digits to left of decimal point ".format(len(n[:x])))
print("{} digits to right of decimal point ".format(len(n[x+1:])))

#110

st=input("Enter a sentence: ")
l=st.split( )
replace=input("Enter word to replace: ")
replacement=input("Enter replacement word: ")
x=st.replace(replace,replacement)
print(x)


#Q111
month=int(input("Enter number of month: "))
year=int(month/12)
remonth=month%12
print("{0} months is {1} years and {2} months.".format(month,year,remonth))



#Output


#53
bill=float(input("Enter bill: "))
perTip=int(input("Enter percentage tip: "))
Tip=bill*perTip/100
print("Tip: $",Tip)

#54
revenue=float(input("Enter revenue: "))
expenses=float(input("Enter expenses: "))
income=revenue-expenses
print("income: ${:0.2f.format(income)}")
#55
salary=float(input("Enter salary: "))
salaryraise=salary+(salary*10/100)
newsalary=salaryraise-(salaryraise*10/100)
change=(newsalary-salary)/salary
print("New salary: ${:,.2f}".format(newsalary))
print("Change: {:.2%}".format(change))


#Lists


#101
s=input("Enter a sentence: ")
l=s.split( )
print("Number of words: ",len(l))

#102
s=input("Enter a sentence: ")
l=s.split( )
print("First word: ",list[0])
print("Last word: ",list[len(l)-1])

#103
name=input("Enter a 2-part name: ")
n=name.find(" ")
print('Revised form: {} ,{}'.format(name[n+1:],name[:n]))

#104
name=input("Enter a 3-part name: ")
list=name.split( )
mid=list[1]
print('Middle name: {}'.format(mid))
