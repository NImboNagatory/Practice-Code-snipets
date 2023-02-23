usr_input = input("Input your Sentence To count >>> ")

list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

occurrence = {}

for char in list_of_letters:
    if char in usr_input.lower():
        occurrence[char] = usr_input.lower().count(char)

sort_occurrence = sorted(occurrence.items(), key=lambda x: x[1], reverse=True)

datalist = ""
sumall = 0

for kay in sort_occurrence:
    datalist += kay[0]
    sumall += kay[1]

to_be_printed = []
for kay in sort_occurrence:
    to_be_printed.append({"latter": kay[0], "occurrence": kay[1], "percentage": round((float(kay[1])/sumall)*100)})


print(f"Here is the analysis of latter occurrence in the frase: \n{usr_input}")
print("Latter    occurrence    Percentage")

for char in to_be_printed:
    print(f"  {char['latter']}           {char['occurrence']}           {char['percentage']}%")
print(f"\n{datalist}")