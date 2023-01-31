H=chr
G=range
import zlib,math
A=[]
for C in G(10000):
	if H(C).isprintable():A+=[H(C)]
D=len
def E(y):
	B=0
	for C in y:B=D(A)*B+A[:D(A)].index(C)
	return zlib.decompress(B.to_bytes(250,'little'))
F=E('⊠ᚒ૮ɇૣ̤៰Ὣ‒åёⓧඖ⍱ᘾ᭳പݍ֣⒖ဓ⏳ႊዬᘥၢلࠆ')
for B in E('ᬈṂӊ⚢ᄔᵕܳђᾮൽ≲ଳᶆЌ˹᮰෬୰ᢹᧆ↚ᘨǛᶸᤆᄖ˯ᣅ♄ặࠉᐠነᬄъd⍎҇⇡ឃ๗ᤠൟˊᨓ᥏ử߲ႃሖμ╡Ḱ᪫ᳯὍ≒ᠶୗ୍ፗ༯̳អᴳЋ᪽'):B-=34;F+=bytes((int(127*math.sin(2**(B//7/12)*A/14.2)*(B>6)+128)for A in G([1,2,3,4,6,8,10][B%7]*5802)))
open('s.wav','wb').write(F)