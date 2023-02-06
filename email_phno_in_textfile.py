import re
def validateEmail(string):
    pattern = re.compile(r'.+@\w+\.[a-z]')
    if pattern.match(string):
        return True
    return False
def validatePhoneNo(string):
    if re.match(r'\+\d{2}-\d{10}', string) or re.match(r'\d{3}-\d{8}', string):
        return True
    return False
emails, phnos, write_mails, write_phnos = 0, 0, "Mails\n", "\nPhone Numbers\n"
f1, f2 = open("email_and_phnos.txt", 'r'), open("write_email_phnos.txt", 'w')
lines_lst = f1.readlines()
for line in lines_lst:
    if validateEmail(line):
        emails += 1
        write_mails += line
    elif validatePhoneNo(line):
        phnos += 1
        write_phnos += line
print(f"Number of email addresses: {emails}\nNumber of phone numbers: {phnos}")
f2.write(write_mails + write_phnos)

















# test_string = """
#     2021-04-01
#     2013-08-29
#
#     2019.09.30
#     2009.10.20
#
#     2018_11_10
#     2000_12_1
# """
# pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
# for match in pattern.findall(test_string):
#     print(match)
