import gzip

def main():
    fileName = input()
    readList = contentReading(fileName)
    averageContent = gcContent(readList)
    repeat = repeats(readList)
    averageNContent = nContent(readList)
    nReadCount = nReads(readList)
    result(readList, averageContent, repeat, averageNContent, nReadCount)

def contentReading(fileName: str):
    #fileName = open('SRR16506265_1.fastq', 'r')
    fileName = gzip.open(fileName, 'r')
    readingResult = fileName.readlines()
    #with open(fileName) as dna:
        #readingResult = dna.readlines()

    readList = list()
    for i in range(1, len(readingResult),4):
        deletedNewLine = readingResult[i].strip('\n')
        readList.append(deletedNewLine)

    return readList

def gcContent(readList):
    dnaStrands = list()
    #note - readList is already stripped thanks to our previous function. the below will read GC content
    for read in readList:
        gc = 0
        for char in ('G', 'C'):
            gc += read.count(char)

        content = (gc / len(read)) * 100
        dnaStrands.append(content)

    gcAverage = round(sum(dnaStrands)/ len(dnaStrands),2)

    return gcAverage

def nContent(readList):
    nStrandOnly = list()
    for read in readList:
        nCount = 0
        for char in ('N'):
            nCount += read.count(char)

        nContentList = (nCount / len(read)) * 100
        nStrandOnly.append(nContentList)
    nAverage = round(sum(nStrandOnly)/len(nStrandOnly),2)

    return nAverage

def nReads(readList):
    nInReads = 0
    for read in readList:
        if "N" in read:
            nInReads += 1
    return nInReads

def result(dnaStrands, averageContent, repeat, averageNContent, nReadCount):
    listOfLengths = [len(length) for length in dnaStrands]

    print(f"Reads in the file = {len(listOfLengths)}:")

    averageLength = round(sum(listOfLengths) / len(listOfLengths))
    print("Reads sequence average length =", averageLength)

    print(f"Repeats = {repeat}")
    print(f"Reads with Ns = {nReadCount}")

    print(f"\nGC content average = {averageContent}%")
    print(f"Ns per read sequence = {averageNContent}%")

def repeats(readList):
    repeat = len(readList) - len(set(readList))
    return repeat

if __name__ == '__main__':
    main()
