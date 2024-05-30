import pandas
data = [12,19,14,20,16,20]

mean = sum(data)/len(data)
print(f"mena: {mean}") #Inside the curly braces is the variable mean. When the f-string is evaluated, the current value of mean will be inserted into the string at this location.
print("mean: "+str(mean))

sorted_data = sorted(data)
print(f"the shorted data is: {sorted_data}")
n = len(sorted_data)
print(n)
median = (sorted_data[n//2] + sorted_data[(n-1)//2]) / 2 #the use of // is : we know that there is no variable type so when python devide something and there is a float numbers appears it provide the float number in the output, but array has no float number as a index, so we use // insted of / to devide something in the array index coz: // only give the least value insted of frection like: insted of 3.5 it will provide 3
print(f"median: {median}")

from statistics import mode

mode_value = mode(data)
print(f"mode: {mode_value}")