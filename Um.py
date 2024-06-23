import pandas as pd

#df variable where you have to enter the path of the .csv file

df = pd.read_csv(r"C:\Users\umidbek.ulmasov\Downloads\PatientData.csv")




look = 1 # look value

#Here search variable for your filters

matches = df[df['Ubiquitous Assay Panel'] == look] # filter rows




# if, else condition for your search

if len(matches)>0:

  items = matches.drop('Ubiquitous Assay Panel', axis=1).values.tolist() #drop which column you want column

  print(items)

else:

  print("There is no match inside the data")




#This code considered by expert Umedjon
