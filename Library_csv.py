import Library_project as LP
import csv

with open("library.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["LibraryName", "Books"])
    books1 = ", ".join(LP.l1.inventory.keys()) 
    books2 = ", ".join(LP.l2.inventory.keys())
    writer.writerow([LP.l1.libraryName, books1])
    writer.writerow([LP.l2.libraryName, books2])
 

with open("library.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
