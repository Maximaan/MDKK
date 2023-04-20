def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  else:
    p = arr[0]
    less = [x for x in arr[1:] if x <=p]
    greater = [x for x in arr[1:] if x > p]
    return quick_sort(less) + [p] + quick_sort(greater)

            
 
