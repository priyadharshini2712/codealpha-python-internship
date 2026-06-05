import re
import os

def extract_emails():
    # Create a sample input file for demo purposes
    sample_text = """
    Contact us at support@example.com or sales@company.org
    For billing: billing@shop.net, admin@website.co.in
    Invalid: notanemail@, @nodomain.com
    reach john.doe@gmail.com or jane_smith@yahoo.com
    """

    # Write sample file
    with open("input.txt", "w") as f:
        f.write(sample_text)
    print("input.txt created.")

    # Read and extract emails
    with open("input.txt", "r") as f:
        content = f.read()

    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)

    print(f"\nFound {len(emails)} email(s):")
    for email in emails:
        print(" -", email)

    # Save to output file
    with open("extracted_emails.txt", "w") as f:
        f.write("\n".join(emails))
    print("\nEmails saved to extracted_emails.txt!")

extract_emails()