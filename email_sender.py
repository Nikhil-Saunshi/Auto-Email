import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import config
import re


def set_content(to_email_id='nikhiltakappa.saunshi@sjsu.edu', first_name=' '):
    # Adding the from and to email id's with the content
    html = Template(Path('index.html').read_text())
    email = EmailMessage()
    email['from'] = 'Nikhil Saunshi'
    email['to'] = to_email_id
    email['subject'] = 'Interested in full time opportunities'

    # Fetching the first part of the email id's to address in the email
    if first_name == ' ':
        first_name = email['to'].split("@")[0]
        first_name = (first_name.split('.')[0]).capitalize()
        first_name = re.sub(r'\d+$', '', first_name)
        print(first_name)

    email.set_content(html.substitute({'name': first_name}), 'html')
    # email.set_content(config.CONTENT)

    # Files to add in the email
    files = ['Resume.pdf']
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name

        email.add_attachment(file_data, maintype='application',
                             subtype='octet-stream', filename=file_name)

    return first_name, email


def send_email(first_name, email):
    # Sending email using python script using gmail
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(config.EMAIL_ADDRESS, config.PASSWORD)
        smtp.send_message(email)
        print(f'Sent to {first_name}!!!!!!')
        return True


first_name, email = set_content('vamsyvaddi@gmail.com', 'Vamsi')
send_email(first_name, email)
