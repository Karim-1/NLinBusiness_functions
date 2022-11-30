import csv

from validate_email import validate_email


def validate_mail(mail_address):
    """_summary_

    Args:
        mail_address (string): string with mailaddress

    Returns:
        boolean: is it a mailaddress
    """
    is_mail = validate_email(mail_address)
    if not is_mail:
        print(f'Error: {mail_address} is not a valid mail address')
    return is_mail



if __name__ == '__main__':
    file = 'dummy_mails.csv'
    with open(file, newline='') as f:
        reader = csv.reader(f)
        addresses_lists = list(reader)
        addresses = [item for sublist in addresses_lists for item in sublist]

    for address in addresses:
        validate_mail(address)