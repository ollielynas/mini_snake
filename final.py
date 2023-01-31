import zlib
y = '짷倐菭时ꦋ２琙Ǯ熣⛷慤𓊯뀪璎횩㴚ڂ蜹핕𑠸僷紩𓉉뉷⎸熗ꐶ⯗萒ⶢ㢏𒅣篺홱헛泌낸셲냇膴貴披譞𐼀掬ᒿﳥ樛抦眞▀𓊇搦䚔䕏ᲈ㲎𐓄㦗롟蠒ﳾ㫜蹼𓅕ು拄ꩴ斦ᛱꍘ㎤𓋁낏삚䋀欆쟹黍鋐㪎ꐻ즞죞쪕甾蕼Ψ⎵윅㒫뀋⢴ྰ厩ⶬ깽遳ꕷṊ湄ﶕ᧳൬啸ﳛ읊뻧頫鈶붬즚᱒힞뜧𐬿ꈗｿ魪'
u = []
for i in range(80000):
 if chr(i).isprintable() and chr(i):u += [chr(i)]
n=0
l=len
for c in y:n=l(u)*n+u[:l(u)].index(c)
exec(zlib.decompress(n.to_bytes(254, 'little')))
