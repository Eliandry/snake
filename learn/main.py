with open ('bytes.txt','wb') as f:
    f.write(b'hello bytes')
with open('bytes.txt','r') as f:
    print(f.read())