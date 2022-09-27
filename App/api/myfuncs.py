import re

def sanitize(query):
    output = ''
    for letter in query:
        if not re.match('\:|\;|\-|\,|\!|\?|\%|\.|\/|\\|\[|\]|\*|\#|\^',letter):
            output = output + letter
    return output

def validate_orderby(order):
    filter = ['id','user','name','last_name','sexe','birth_date','bed_number','room_number']
    if order in filter:
        return True
    return False

def validate_date(date):
    if re.match('([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))',date):
        return True
    return False