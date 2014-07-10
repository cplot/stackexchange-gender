import os

data = '8July2014'

am = 0
af = 0

with open('table.txt', 'w') as outf:

    for filen in os.listdir('siteusers'+data):
        assign = list()
        
        for line in open('siteusers'+data+'/'+filen,'r'):
            assign.append(line.split('\t')[0])

        m = 0
        f = 0
        u = 0

        for x in assign:
            if x == "m":
                m+=1
                am += 1
            elif x=="f":
                f+=1
                af += 1
            elif x=="u":
                u+=1
            
        outf.write(filen[:-4] +'\t'+ str(m) +'\t'+ str(f) + '\t'+ str(u) +'\n')
        
print am, af, af/float(am+af)
