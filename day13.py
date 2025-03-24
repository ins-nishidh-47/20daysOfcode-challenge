import json
import re
from datetime import datetime, timedelta

# =============================
# 📆 DATETIME MODULE METHODS
# =============================

# 1 Get the current date and time
now = datetime.now()
print("Current Date & Time:", now)

# 2 Perform date arithmetic with timedelta
future_date = now + timedelta(days=7)
print("Date after 7 days:", future_date)

past_date = now - timedelta(weeks=2)
print("Date 2 weeks ago:", past_date)

# 3 Format datetime as a string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)

# 4 Convert a string to datetime
date_str = "2024-07-13 15:30:00"
date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Converted Datetime Object:", date_obj)

# 5 Get the day of the week (0 = Monday, 6 = Sunday)
print("Today is weekday:", now.weekday())

# 6 Get total seconds from a timedelta
delta = timedelta(days=1, hours=5, minutes=30)
print("Total Seconds in timedelta:", delta.total_seconds())

# =============================
# 📦 JSON MODULE METHODS
# =============================

# 1 Convert Python dictionary to JSON string
data = {"x": 10, "y": 20.5, "z": 30}
json_str = json.dumps(data, indent=4)
print("JSON String:", json_str)

# 2 Convert JSON string to Python dictionary
parsed_data = json.loads(json_str)
total = parsed_data["x"] + parsed_data["y"] + parsed_data["z"]
print("Total Sum from JSON Data:", total)

# 3 Write JSON to a file
with open("json/data.json", "w") as file:
    json.dump(data, file, indent=4)

# 4 Read JSON from a file
with open("json/data.json", "r") as file:
    loaded_data = json.load(file)
print("Loaded JSON Data:", loaded_data)

# =============================
# 🔍 REGULAR EXPRESSIONS (re) METHODS
# =============================

text = "The price is 199.99 and the discount is 20%"

# 1 Extract all numbers (including decimals)
numbers = re.findall(r"\d+\.?\d*", text)
print("Extracted Numbers:", numbers)

# 2 Check if the string starts with a specific pattern
pattern = r"^The"
match = re.match(pattern, text)
print("Starts with 'The':", bool(match))

# 3 Replace text based on a pattern
new_text = re.sub(r"price", "cost", text)
print("Modified Text:", new_text)

# 4 Find the first occurrence of a number
first_number = re.search(r"\d+", text)
if first_number:
    print("First Number Found:", first_number.group())

# 5️ Split a string using regex
bug_text = "Bug#101, Bug#102, Bug#103"
split_text = re.split(r", ", bug_text)
print("Split Text:", split_text)
