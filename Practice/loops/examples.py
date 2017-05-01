def main():
  menu()

def menu():
  print("Welcome to the Python loop tutorial!\n")
  myArray = eval(input("Enter your values using array notation: "))

  print("Menu:")
  print("1: counting pattern")
  print("2: filtered-count pattern")
  print("3: accumulate pattern")
  print("4: filtered-accumulate pattern")
  print("5: search pattern")
  print("6: extreme pattern")
  print("7: extreme-index pattern")
  print("8: filter pattern")
  print("9: map pattern")
  print("10: sort")
  choice = int(input("Choice: "))
  if(choice > 0 and choice < 11):
    options(choice, myArray)
  else:
    print("Invalid option, please try again\n\n")
    menu()


#using a python dictionary to determine which function to call
def options(c, array):
  opt = {1:count,
         2:filteredCount,
         3:accumulate,
         4:filteredAccumulate,
         5:search,
         6:extreme,
         7:extremeIndex,
         8:filter,
         9:map,
         10:sortArray}
  opt[c](array)

#counts the number of items in the list
def count(arr):
  count = 0
  for i in range(0, len(arr), 1):
    count += 1
  print("Number of items in the array: ", count)

#counts specific items in a list. 
def filteredCount(arr):
  count = 0
  bound = 0
  while(bound < len(arr)):
    if(arr[bound] % 2 == 1):
      count += 1
    bound += 1
  print("Number of odd items in the array: ", count)

#updates a variable by incresing it by the value of an item
def accumulate(arr):
  total = 0
  for i in range(0, len(arr), 1):
    total += arr[i]
  print("The sum of the items in the array: ", total)

#updates a variable by increasing it by the value of an item
#if that item passes some test.
def filteredAccumulate(arr):
  total = 0
  bound = 0
  while(bound < len(arr)):
    if(arr[bound] % 2 == 0):
      total += arr[bound]
    bound += 1
  print("Total of all even items in the array: ", total)

#determines if an item exists.
def search(arr):
  target = int(input("Enter a target number: "))
  flag = False
  for i in range(0, len(arr), 1):
    if(arr[i] == target):
      flag = True
      break
  print(target, "exists? ", flag)

#finds either largest or smallest value
def extreme(arr):
  smallest = arr[0]
  bound = 1
  while(bound < len(arr)):
    if(arr[bound] < smallest):
      smallest = arr[bound]
    bound += 1
  print("The smallest item in the array is: ", smallest)

#determines the index of the largest or smallest item in an array
def extremeIndex(arr):
  indexL = 0
  for i in range(1, len(arr), 1):
    if(arr[i] > arr[indexL]):
      indexL = i
  print("Index of the largest value: ", indexL)

#collects filtered items (for example) into an array
def filter(arr):
  negNums = []
  bound = 0
  while(bound < len(arr)):
    if(arr[bound] < -1):
      negNums.append(arr[bound])
    bound += 1
  print("Negative numbers from the array: ", negNums)

#applies a transform to all items in an array
def map(arr):
  result = []
  for i in range(0, len(arr), 1):
    result.append(arr[i]*2)
  print("updated array: ", result)

#sorts items in (ascending) or descending order
def sortArray(arr):
  for i in range(0, len(arr), 1):
    for j in range(i, len(arr), 1):
      if(arr[i] > arr[j]):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
  print("The sorted array: ", arr)

main()