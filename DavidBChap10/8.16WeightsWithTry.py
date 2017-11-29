#-----------------------TRY--BLOCK------------------
errorInt = 1
while errorInt == 1:
  try:
    weight_1 = float(input('Enter weight 1:\n'))
    weight_2 = float(input('Enter weight 2:\n'))
    weight_3 = float(input('Enter weight 3:\n'))
    weight_4 = float(input('Enter weight 4:\n'))
    if errorInt == 1:
      errorInt = 0
  except ValueError as excpt:
    print(excpt)
    print('Need integer')
    errorInt = 1

#-----------------------FUNCTIONS--------------------
def find_avg(x):
  sum_num = 0
  for i in x:
    sum_num += i
  return sum_num / 4

def kilo_convert():
  return (weights[index_num - 1] / 2.2)
  
def sort_list():
  weights.sort()
  return weights
#--------------------------BODY----------------------  
weights = [weight_1, weight_2, weight_3, weight_4]

print('Weights: %s\n' % weights)

print('Average weight: %.2f' % find_avg(weights))
print('Max weight: %.2f\n' % max(weights))

index_num = int(input('Enter a list index (1 - 4):\n'))

print('Weight in pounds: %.2f' % weights[index_num - 1])
print('Weight in kilograms: %.2f\n' % kilo_convert() )

print('Sorted list:', sort_list())
