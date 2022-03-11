maxx= []
ma, mi = 0,11110000
lc, wc, wcc = 0, 0,0
with open('Malwaretypefile.txt','r') as f:  
    for line in f:
        lc += 1
        wc += len(line.strip().split())
        wcc =len(line.strip().split())
        if wcc > ma:
            ma= wcc
        if wcc < mi:
            mi = wcc
avg = wc / lc

print('Total API calss are:', wc)
print('Total API Calss sequences are:', lc)
print('Average API Calls sequence length is:', avg)
print('Maximum Sequence Length is: ',ma)
print('Minimum Sequence length is:', mi)
