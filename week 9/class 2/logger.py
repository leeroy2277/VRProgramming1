import datetime

def  writelog(filename, string, severity = 'I'):

    current_date_time = datetime.datetime.now()

    with open(filename, "a+") as my_file:

        my_file.write(str(current_date_time) + " " + severity + " " + string + "\n")


