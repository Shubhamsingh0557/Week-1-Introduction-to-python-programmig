#python program that accept the 7 days temperature and prints average temperature of the week:

mon=float (input ("Enter temp. of Monday:"))
tues=float(input("Enter temp. of Tuesday:"))
wed=float (input ("Enter temp. of Wednesday:"))
thur=float (input ("Enter temp. of Thursday:"))
fri=float(input ("Enter temp. of Friday:"))
sat=float (input ("Enter temp. of Saturday:"))
sun=float(input ("Enter temp. of Sunday:"))
ave_temp=(mon+tues+wed+thur+fri+sat+sun)/7
print ("Average temperature of the week=",ave_temp)
