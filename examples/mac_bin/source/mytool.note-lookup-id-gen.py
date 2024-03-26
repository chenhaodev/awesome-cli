import uuid
import datetime
import pyperclip

keywords = input("Enter keywords: ")
uuid_part = str(uuid.uuid4())[:7]
current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
output_string = f"{keywords}-{uuid_part}-{current_datetime}"
pyperclip.copy(output_string)
print(f"Generated string: {output_string}")
print("Copied to clipboard!")
