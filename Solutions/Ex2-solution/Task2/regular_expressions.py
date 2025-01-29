import re

# Define the pattern to match the last number in the Summary table
pattern = r"#Summary:[\s\S]+?\|\s*\d+\s*\|\s*\d+\s*\|\s*\d+\s*\|\s*\d+\s*\|\s*[\d.]+\s*\|\s*([\d.]+)\s*\|"

with open(
    "/home/ossama/Desktop/Ex2-solution/Task2/brilcalc.log", "r"
) as file:  # to test the code, change the file path to the one in your local device
    content = file.read()  # Read the entire file

# Search for the pattern
match = re.search(pattern, content)

if match:
    print(
        "Total recorded luminosity:", round(float(match.group(1)) / 1000, 1), "f/b"
    )  # print the first captured value
else:
    print("Value not found")
