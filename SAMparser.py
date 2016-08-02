def makeEmptyDict(Number):
    Dict = {}
    for item in range(1 , Number + 1):
        Dict['HGLibA_' + str(item).zfill(5)] = 0
    return Dict    

def SAMparser(SAMfile):
    CRISPRDict = makeEmptyDict(65383)
    with open(SAMfile, 'r') as SAM:
        for line in SAM:
            if line[0] != '@':
                split = line.split()
                if split[2] != '*':
                    CRISPRDict[split[2].split(':')[0]] += 1
        return CRISPRDict

def countOutput(fileName, Dict):
    out = open(fileName , 'w')
    for key in sorted(Dict.keys()):
        out.write(key + '\t' + str(Dict[key]) + '\n')
    out.close()    

fileList = ['1_AAGTAGAG','2_ACACGATC']

for SAMfile in fileList:
    D = SAMparser(SAMfile + '.sam')
    countOutput(SAMfile + '.counts.txt' , D)

