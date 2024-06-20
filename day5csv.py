import csv
file=open("file1.csv","w")
csvWriter=csv.writer(file)
data=[
    ["name","age","city"],
    ["Abhinaya",'19',"nkd"],
    ["chaitanya",'17',"nkd"]
]
#csvWriter.writerow(file)
csvWriter.writerows(data)
file.close()