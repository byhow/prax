def categorySuggestions2(categories, projects, k):
    sb, idict, res, i = {}, {}, [], 0
    
    while i < len(categories):
        category = categories[i].split(",")
        if category[0] in idict:
            idict[category[0]][category[1]] = category[2]
            if category[1] not in idict:
                idict[category[1]] = { category[0]: category[2] }
            else:
                idict[category[1]][category[0]] = category[2]

        else:
            idict[category[0]] = { category[1]: category[2] }
            if category[1] not in idict:
                idict[category[1]] = { category[0]:category[2] }
            else:
                idict[category[1]][category[0]] = category[2]
            
        i += 1

    for project in projects:
        sb.update({project: float(0)})
        if project in idict:
            for key in idict[project]:
                if key not in sb or float(idict[project][key]) < sb[key]:
                    sb[key] = float(idict[project][key])

            
        l = sorted(sb.items(), key=lambda x: (x[1],x[0]))
        j = [i[0] for i in l]
        res.append(j[:k])

    return res