import requests
from bs4 import BeautifulSoup
from collections import Counter
import webcolors
import random

with open("python_class_question.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")

all_colors = []

for row in rows:
    cells = row.find_all("td")
    if len(cells) > 1:
        day = cells[0].get_text(strip=True)
        colors = cells[1].get_text(strip=True).upper().split(", ")
        all_colors.extend(colors)


#to find the mean
def get_rgb_value(color):
    try:
        return webcolors.name_to_rgb(color)
    except ValueError:
        print(f'"{color}" is not a recognized color.')
        return None

rgb_values = [get_rgb_value(color) for color in all_colors if get_rgb_value(color) is not None]

mean_r = sum(color.red for color in rgb_values) / len(rgb_values)
mean_g = sum(color.green for color in rgb_values) / len(rgb_values)
mean_b = sum(color.blue for color in rgb_values) / len(rgb_values)

mean_color = (mean_r, mean_g, mean_b)
print("Mean Color:", mean_color)

#most worn color
color_count = Counter(all_colors)

most_worn = color_count.most_common(1)[0][0]
print(f"Most worn color: {most_worn}")

#median color
sorted_colors = sorted(all_colors)

if len(sorted_colors) % 2 == 0:
    median = sorted_colors[len(sorted_colors) // 2 - 1]
else:
    median =sorted_colors[len(sorted_colors) // 2]

print("median color: ", median)

#find the variance
color_counted = Counter(all_colors)
frequencies = list(color_counted.values())
mean_frequency = sum(frequencies) / len(frequencies)
variance = sum((freq - mean_frequency) ** 2 for freq in frequencies) / len(frequencies)

print(f"Variance of color frequencies: {variance}")

#probability of choosing red
color_counter = Counter(all_colors)
red_count = color_counter['RED']
total_count = sum(color_counter.values())

probability_red = red_count / total_count
print(f"The probability of choosing 'RED' is {probability_red:.2f}")

#generate binary and convert to base 10
rand_binary = ''.join([str(random.randint(0, 1)) for _ in range(4)])
base10 = int(rand_binary, 2)

print(f"Random 4-digit binary number: {rand_binary}")
print(f"Base 10 equivalent: {base10}")

#first 50 fibonacci sum
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

fib_numbers = fibonacci(50)
fib_sum = sum(fib_numbers)

print("Sum of first 50 Fibonacci numbers:", fib_sum)


