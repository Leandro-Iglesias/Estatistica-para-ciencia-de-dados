import matplotlib.pyplot as plt
import numpy as np
import csv
with open('iris.csv', "r") as csvfile:
    differents_species=[]
    data= csv.reader(csvfile)
    List_data=list(data)

#print(List_data)
included_cols=['Species']
#Colocando cada coluna em uma Lista em python
SepalLenght=[]
SepalWidth=[]
PetalLength=[]
PetalWidth=[]
for i,row in enumerate(List_data):
    if(i!=0):
        SepalLenght.append(row[1])
        SepalWidth.append(row[2])
        PetalLength.append(row[3])
        PetalWidth.append(row[4])
        if row[5] not in differents_species:
            differents_species.append(row[5])

differents_species_dict={k:0 for k in differents_species}
for i,row in enumerate(List_data):
    if(i!=0):
        differents_species_dict[row[5]]+=1

for key in differents_species_dict:
    print(f'Nome da Espécie: {key} -> Quantidade: {differents_species_dict[key]}' )

plt.hist(differents_species_dict, 3, color='skyblue', edgecolor='black')
# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')
   
    
print(SepalLenght)
# Display the plot
plt.show()
#print(differents_species)
        


   