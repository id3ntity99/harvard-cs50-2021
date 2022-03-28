arr = ["a", "b", "c", "c", "c","c", "d"]
counter = 1
for i in range(0, len(arr) - 1):
    if arr[i] == "c" and arr[i + 1] == "c":
        counter += 1

print(counter)