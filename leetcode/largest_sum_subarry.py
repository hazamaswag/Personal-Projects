def largest_sum_subarray(arr):
  '''
  >>> largest_sum_subarray([-2,2,5,-11,6])
  7
  '''
  curr_sum = arr[0]
  best_sum = curr_sum
  for a in arr[1:]:
    curr_sum = max(a, curr_sum + a)
    best_sum = max(curr_sum, best_sum)
  return best_sum


tests = [-2,2,5,-11,6]
result = largest_sum_subarray(tests)
print(result)
