print("Введите слово.")
input = input()
vowels = "aeiou"
total_count_vowels = 0
total_count_consonants = 0
vowel_counts = {}

for vowel in vowels:
    vowel_counts[vowel] = False

for char in input:
  if char in vowels:
    total_count_vowels += 1
    vowel_counts[char] +=1
  else:
    total_count_consonants += 1

print("Гласных:",total_count_vowels)
print("Согласных:",total_count_consonants)
print(vowel_counts)