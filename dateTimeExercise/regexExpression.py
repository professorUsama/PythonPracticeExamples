import re
if __name__ == '__main__':
    text = "Hello my name is usama amjid. I'm from layyah and i am doing bscs in time college layyah and my phone number is 54587963547. And the my monthly salary is 980 dollars per month."
    pattern = '"\d{11}|\d+'
    result = re.findall(pattern,text)
    print(result)