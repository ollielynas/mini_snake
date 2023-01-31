u = []
y ='"﫻焣뼼좢ꪒ鴑✒丹륟𓗈﨤𒪻뙺𖂗럏꼝拍𒩫곅𒲱횤𕆴郐𗧘𐍟뢰𕁔̳폝𓍵𗚀𘅻팑螰ႅ𔗴뼝忋ሜ롾ꓴ𒜊偤𐙬̆㫐𗶠㵻ᵝ腎𗢫넁𔒳𐓺퉽㙡𓹪𔠈𗤕꡹䰲𑀹밲솋ಁ譅ୌ䫶𕜰壔𓱩仐Ѷ𔏹𓣄𗓿ȋ𖢈ፖ𕥰ᦆ𕢘𐚈듡𗫩깗𒽤𓍳𔲉緦㹝髫𗗆齆𕮐輢𗡩陫嫴流꛸㠾𕲲墕墈५儼𐠁ᑫ鉥𖕽Ꝇ𖃷ލ𖽟⣐ᆶ㩂ञ罍笜𓹖𓪕𕣑𑠤𑔿𔸊푌𑾵𗃋𒑥䭏ꎦ𒗇떣𑽰𔅎汜誳𗾷㾎ㅑ쑕淑삭訹⌑𒛆䶢簀'
for i in range(80000):
  try:print(chr(i),end='\r');u+=[chr(i)]
  except UnicodeEncodeError:...
n=0
l=len
for c in y:n=l(u)*n+u[:l(u)].index(c)
exec(n.to_bytes(355, 'little').decode())
