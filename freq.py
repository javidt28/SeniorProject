values = [] # Empty list where user values would be placed upon entry 

for i in range(1,7):
  print("This is the values list", values)
  userValue = int(input("Please enter value #" + str(i) + " into the data list: "))
  values.append(userValue)
print(values)

frequencyCount = 0 # Variable to hold the frequency count
frequencyLookup = int(input("Please enter a value to find the frequency of: "))

for i in values:
  if i == frequencyLookup:
    frequencyCount += 1
print("The frequency of", frequencyLookup, "is", frequencyCount)
