def binary_search(arr, target, start=None, end=None):
  if start is None:
    start = 0

  if end is None:
    end = len(arr) - 1

  if start > end:
    return None

  mid = (start + end) / 2

  if arr[mid] == target:
    return mid
  elif arr[mid] > target:
    return binary_search(arr, target, start, mid - 1)
  else:
    return binary_search(arr, target, mid + 1, end)
