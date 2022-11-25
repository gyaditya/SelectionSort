#Selection Sort

nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def selectionSort(anArray):
    for i in range(len(anArray)):
        minimum = i
        for n in range(i+1, len(anArray)):
            if anArray[n] < anArray[minimum]:
                minimum = n
        anArray[i], anArray[minimum] = anArray[minimum], anArray[i]

selectionSort(nums)
print(nums)

selectionSort(words)
print(words)
