import secrets as s
pool = [
"A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", "!", "@", "#", "$", "%", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
]
l=[]

def selection():
    count=10
    while count>0:
        l.append(pool[s.randbelow(67)])
        count-=1
    
selection()
pw="".join([str(i) for i in l])
print(pw)
