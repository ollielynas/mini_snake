import zlib
v1 = open("main.py").read()
v2 = open("no_death.py").read()

c2 = zlib.compress(v2.encode())





# print(len(v2), len(c2))
# exec(v2)
zlib.decompress(c2)
print(c2.hex())
#exec(zlib.decompress(c2))
s = """
import zlib
y ="Z㘔둫ퟔ滎栝㎂嗝ᝁ熖楉♳玃Ὢ〶㞹㥤摾脰痤㦢꧄瓌㶼知뷣斠ረ丽噯捽汵ᤂ室䴺䡲▸៚닪諧埐薒겖莭漈襅晋랽颔ꖷ拗⢬흀搴哭醢刾䕓용뛲큊쑎㾸ᚺ肓㰿㒛웗㽹ዒ汮뙪仮臒䌞젇絘⊞Ⱚ쵿麎렊Ვ鮂緬큻ᥗ賅踑民底ܗ炔훿伆齥鳂ꓔ㜬〇⼡灑빡Ꞻ獮꫖醖펲꿽凧駑Ꮕ䣰㺷臔处戒굈쵹툘啴鳺㭇緖液섕ꂄ"
u=[chr(i) for i in range(55300)]
print(len(y))
n = 0
for c in y:
    n = len(u) * n + u[:len(u)].index(c)
exec(zlib.decompress(n.to_bytes(250, 'little')))
"""
len(zlib.compress(s.encode(), 9))
