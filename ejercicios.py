

"""
#que un numero multiplo de 3 retorne fizz, 
#un multiplo de 5 retorne buzz
#si es multiplo de 3 y de 5 a la vez retorne fizzbuzz

for n in range(1,100):
    if (n %3 == 0)and (n%5==0):
        print("fizzbuzz")
    elif(n%3==0):
        print("fizz")
    elif(n%5==0):
        print("buzz")
    else:
        continue
"""
"""
def isAnagram(palabra1,palabra2):
    palabra1Sorted =sorted(palabra1)
    palabra2Sorted= sorted(palabra2)
    if palabra1Sorted == palabra2Sorted:
        return print("Es un anagrama")

    else:
        return print("no un anagrama")
    
isAnagram("amor","roma")
"""