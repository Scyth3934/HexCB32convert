import os
A="0123456789ABCDEFGHJKMNPQRSTVWXYZ"
C=A+"*~$=U"
M={c:i for i,c in enumerate(C)}
M.update({'O':0,'I':1,'L':1})
def e(bts):
 b=o=c=0;r=""
 for x in bts:o=o<<8|x;b+=8
 while b>4:b-=5;y=o>>b&31;r+=A[y];c=(c+y)%37
 if b:y=o<<(5-b)&31;r+=A[y];c=(c+y)%37
 return r+C[c]
def d(s):
 b=o=c=0;r=b""
 for x in s[:-1]:
  x=x.upper()
  if x not in M: raise ValueError(f"Invalidchar:{x}")
  o=o<<5|M[x];b+=5;c=(c+M[x])%37
  if b>7:b-=8;r+=bytes([o>>b&255])
 if C[c]!=s[-1]: raise ValueError(f"Badchecksum:{C[c]}")
 return r.hex().upper()
def ef(f):
 with open(f) as fi:
    b=bytes.fromhex(fi.read().strip().replace(" ","").replace("\n","").replace("-",""))
 return e(b)
def df(f):
 with open(f) as fi:
    s=fi.read().strip().replace(" ","").replace("\n","").replace("-","")
 return d(s)
def main():
 print("Crockford Base32")
 while True:
    m=input("enc/dec/q: ").strip().lower()
    if m=="q": break
    if m not in ("enc","dec"):
        print("INPUTERR"); continue
    i=input("input file: ").strip()
    if not os.path.isfile(i):
        print("Input DNE"); continue
    o=input("output file: ").strip()
    try:
        print(f"{m}oding...")
        r=ef(i) if m=="enc" else df(i)
        with open(o,"w") as f:f.write(r)
        print(f"Done -> {o}")
    except Exception as x:
        print("Error:",x)
if __name__=="__main__":main()
