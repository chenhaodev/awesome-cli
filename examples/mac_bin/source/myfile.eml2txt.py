import os
from email import policy
from email.parser import BytesParser

def extract_eml_content(eml_file):
    with open(eml_file, "rb") as file:
        msg = BytesParser(policy=policy.default).parse(file)
        subject = msg["Subject"]
        sender = msg["From"]
        date = msg["Date"]
        body = ""

        if msg.is_multipart():
            for part in msg.iter_parts():
                if part.get_content_type() == "text/plain":
                    body = part.get_content()
                    break
        else:
            body = msg.get_content()

        # Process the extracted content as needed
        print("Subject:", subject)
        print("From:", sender)
        print("Date:", date)
        print("Body:", body)
        print("-" * 40)

# Specify the directory containing the .eml files
directory = "./"

# Iterate over all .eml files in the directory
for file_name in os.listdir(directory):
    if file_name.endswith(".eml"):
        file_path = os.path.join(directory, file_name)
        extract_eml_content(file_path)
