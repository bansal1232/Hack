x = ""
while True:
    try:
        x += " " + raw_input()
    except:
        break
x += " 0 0"
X = map(int, x.strip().split())
a, b = X[:2]
c=a-b
if b % 2 == 0:
    print c
    print "even"
else:
    print c
    print "odd"
