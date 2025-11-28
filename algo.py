
def main():

    example = [1,23,11,68,100,84,10,9]
    while True:
        
        trueorfalse = []

        for i,j in zip(range(len(example)-1),range(1,len(example))):

            spare = example[i]

            if example[i] > example[j]:
                example[i] = example[j]
                example[j] = spare
                    
        trueorfalse = []
        for i,j in zip(range(len(example)-1),range(1,len(example))):

            if example[i] < example[j]:  
                trueorfalse.append(True)
            else:
                trueorfalse.append(False)
        if all(trueorfalse):
            print(" ".join(map(str,example)))
            return 
                   
main()