
Personal=("Roshan", "26th April 2011")
#this is packing(storing tupel with data)
address=("1", "Magnolia Way", "Woobrun Green", "High Wycombe", "United Kingdom")

for i in address:
    print(i)

#unpacking

housenom,road,village,city,country=address
print(" house number ",housenom)
print(" road ", road)
print("village", village )
print( "city ", city)
print( "country", country)


mytuple=3,4,5,6,"Toblarone"
print(mytuple)
school=("maths",["chemistry",6], ("art"))
print(school[1][1])

#we cant  modify a tuple because immutable
#school[0]="science"


buildings=("Burj Khalifa", "Cayan tower", "Bejing tower","Big ben", "Taj Mahal")
print(buildings[0:3])
print(buildings[0:])
#if we dont show ending it will print the whole list
print(buildings[-3:])
print(buildings[:])
print(len(buildings))