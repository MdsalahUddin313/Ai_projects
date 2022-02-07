def recur_sum(n, first, interval, i):
  if i == n:
      return first
  else:
      return first + recur_sum(n, first+interval, interval, i+1)


first = int(input("Enter first term: "))
n = int(input("Enter n: "))
interval = int(input("Enter interval: "))

sumOfSeries = recur_sum(n,first,interval,1)

print("The sum is ", sumOfSeries)