import re


def sanitize(query):
    output = ''
    for letter in query:
        if not re.match("\:|\;|\-|\,|\!|\?|\%|\.|\/|\\|\[|\]|\*|\#|\^",letter):
            output = output + letter
    return output