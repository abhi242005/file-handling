# write
with open("descriptionday2.txt","w") as day2:
    day2.write("Aashritha----->23951a0501")
    day2.write("\nAbhinaya----->23951a0504")
    day2.write("\nAkshaya----->23951a050G")
    day2.write("\nAkshaya Varshini----->23951a050H")
    day2.write("\nAmitha----->23951a050M")
#readline
with open("descriptionday2.txt","r") as day2:
    print(day2.readline())#Aashritha----->23951a0501
#readlines
with open("descriptionday2.txt","r") as day2:
    print(day2.readlines())#['Aashritha----->23951a0501\n', 'Abhinaya----->23951a0504\n', 'Akshaya----->23951a050G\n', 'Akshaya Varshini----->23951a050H\n', 'Amitha----->23951a050M']
#append
with open("descriptionday2.txt","a") as day2:
    day2.write("\nAnushka----->23951a050U")
#read
with open("descriptionday2.txt","r") as day2:
    print(day2.read())#Aashritha----->23951a0501
                      #Abhinaya----->23951a0504
                      #Akshaya----->23951a050G
                      #Akshaya Varshini----->23951a050H
                      #Amitha----->23951a050M
                      #Anushka----->23951a050U'''
    day2.close()
