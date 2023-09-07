#
# Complete the 'decode' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING encoded as parameter.
#


def decode(encoded):
    # Write your code here

    decodedString = ""
    encodedString = str(encoded)[::-1]
    l = len(encodedString)
    # l = 18
    i = 0
    while i < l:
        cur = encodedString[i] + encodedString[i + 1]
        # print(cur)
        if i + 1 < l:
            if (
                (int(encodedString[i] + encodedString[i + 1]) <= 90)
                and (int(encodedString[i] + encodedString[i + 1]) >= 65)
                or int(encodedString[i] + encodedString[i + 1]) >= 97
            ):
                decodedString += chr(int(encodedString[i] + encodedString[i + 1]))
                i += 2
            elif i + 2 < l:
                cur2 = int(encodedString[i] + encodedString[i + 1] + encodedString[i + 2])
                # print("three word " + str(cur2))
                if (
                    int(encodedString[i] + encodedString[i + 1] + encodedString[i + 2]) <= 122
                    and int(encodedString[i] + encodedString[i + 1] + encodedString[i + 2]) >= 97
                ):
                    decodedString += chr(int(encodedString[i] + encodedString[i + 1] + encodedString[i + 2]))
                    i += 3
                else:
                    decodedString += " "
                    i += 2
            else:
                decodedString += " "
                i += 2

        # print(i)
    return decodedString
    # return encodedString 84114117116104326510811997121115328710511011532


# print(decode("23511011501782351112179911801562340161171141148"))
