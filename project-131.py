import pandas as pd

df = pd.read_csv('project-130.csv')

df.drop(['Unnamed: 0'],axis=1,inplace=True)
print(df.head())

df['Radius']=df['Radius'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()

gravity =[]
star_radius = []
star_mass = []

for i in range(0,len(radius)):
    radius[i] = radius[i]*6.957e+8
    mass[i] = mass[i]*1.989e+30
    star_radius.append(radius[i]) 
    star_mass.append(mass[i])   

G = 6.674e-11
for index in range(0,len(mass)):
    g= (mass[index]*G)/((radius[index])**2)
    gravity.append(g)
        
df["radius"] = star_radius
df["mass"] = star_mass
df["Gravity"] = gravity
print(df)
df.to_csv("project-131.csv")


