import zlib
y ='󐹦𢽊󥖳񧍙𳢗򕴁󱫕𩯱򇏙򴿷𶁋񝒲򪧮򃜎􃳅񀻍񪷵󔍪򢣭񪑸󭍰𔷁􌁅졞󔳋綌󚷏񘘤񆫂󏣐񾧤󼎋􄋼򵵙񟖑󽾱񺑑񼩋󛎌󓆅󽷉󕏗𯻑񄑒󉽙򠖙􀄼􀊺𦼖􋳗􊈀򍭞􋐒򱺊򗷓𜖋𧧑󚛏򖟡󁊵􉄐񯓂󻏬򾽟񸡞񁟭򱟨𤾎󾮡򀧦񃌮򳉭񬱹ಳ򸫀򤃂󅪴𸇧􏞴ꃾ񁒩򻔺񂬠񆍽댵𠄋󝝓󚎔񱗄󛭝󏝑𗦙򨗷󿣛󗽏𥴓򯹎𐸋뛏󯑸'
u=[]
for i in range(999999):
 try:print(chr(i),end='\r');u+=[chr(i)]
 except UnicodeEncodeError:...
 except ValueError:break
n=0
l=len
for c in y:n=l(u)*n+u[:l(u)].index(c)
exec(zlib.decompress(n.to_bytes(256,'little')))