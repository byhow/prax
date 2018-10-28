#
# Complete the 'reformatDate' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY dates as parameter.
#

def reformatDate(dates):
    # Write your code here
    ret = []
    month_dict = { "Jan": "01", "Feb": "02", "Mar": "03", 
                    "Apr": "04", "May": "05", "Jun": "06", "Jul": "07",
                    "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

    for i in dates:
        substring = ""
        d, m, y = i.split()[0], i.split()[1], i.split()[2] 
        retd = d[:len(d) - 2]
        retm = month_dict[m]

        if len(retd) < 2:
            retd = "0" + retd
        
        substring = y + "-" + retm + "-" + retd

        ret.append(substring)
 
    return ret

        


# ['20th Oct 2052', '6th Jun 1933', '26th May 1960', '20th Sep 1958', '16th Mar 2068', '25th May 1912', '16th Dec 2018', '26th Dec 2061', '4th Nov 2030', '28th Jul 1963'