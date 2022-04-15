def printFormat(amount):
    print("REF STRING\t\t", end='')
    for idx in range(0,amount):
        print(f"PAGE_FRAME_{idx+1}\t\t", end='')
    print("PAGE_FAULT_NUMBER")


def printResults(current, frames, pageFaultsAmt):
    print(f"{current}\t\t\t", end='')
    for x in range(0,len(frames)):
        print(f"{frames[x]}\t\t\t", end='')
    print(pageFaultsAmt)


reference_string = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
noOfFrames = int(input("How many frames\t"))
frames = [-1 for x in range(0,noOfFrames)] # initalise all with -1
noOfPageFault = 0
posToRemove = 0

printFormat(noOfFrames)
for index, ref in enumerate(reference_string):

    
    if (index < noOfFrames): # For the first n frames (where n is number of frames)
        frames[index] = reference_string[index]
        noOfPageFault += 1
        printResults(ref, frames, noOfPageFault)
    else:
        if ref in frames:
            printResults(ref, frames, noOfPageFault)
        else:
            frames[posToRemove] = ref
            noOfPageFault += 1
            posToRemove += 1
            printResults(ref, frames, noOfPageFault)

    if (posToRemove >= noOfFrames):
        posToRemove = 0


