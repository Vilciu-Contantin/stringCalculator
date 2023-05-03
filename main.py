
import re

def StringCalculator(string):


    if re.match('-[0-9]+', string):
        raise ValueError("negatives not allowed {}".format(
            re.findall('-[0-9]+', string)))
    separators = ',', '\\n'
    if "//" in string:
        separators_info = re.findall('//.+\n', string)[0]
        separators = separators_info.replace('//','').replace('\\n','')
        string = string.replace(separators_info, '')
    if not string:
        return 0
    if not any(separator in string for separator in separators):
        return int(string)
    print(sum(int(number) for number in re.split('|'.join(separators), string)))

