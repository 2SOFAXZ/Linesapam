import sys
from pystyle import Colors,Colorate
import platform
from pystyle import Colors, Center, Colorate, Write
import os
import requests
argv = sys.argv
so_name=platform.system()

os .system ("cls & title BFHMSCSPAMLINE")
print(Colorate.Vertical(Colors.blue_to_cyan, Center.XCenter("""
 
███████╗██████╗  █████╗ ███╗   ███╗██╗     ██╗███╗   ██╗███████╗
██╔════╝██╔══██╗██╔══██╗████╗ ████║██║     ██║████╗  ██║██╔════╝
███████╗██████╔╝███████║██╔████╔██║██║     ██║██╔██╗ ██║█████╗     
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║     ██║██║╚██╗██║██╔══╝   
███████║██║     ██║  ██║██║ ╚═╝ ██║███████╗██║██║ ╚████║███████╗
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝
                       MAKEBY:BFHMSC
                                                                                                                            
        """)))


def inputtokenline():
    global tokenline
    try:
        if len(argv) == 4:
            tokenline = argv[1]
        else:
            tokenline = input("TOKEN BOT : ")
    except:
        print(Colorate.Horizontal(Colors.rainbow, """ERROR TOKEN BOT"""))
        
def inputtext():
    global text
    try:
        if len(argv) == 4:
            text = argv[2]
        else:
            text = input("MESSAGE : ")
    except:
        print(Colorate.Horizontal(Colors.rainbow, """ERROR MESSAGE"""))
        
def inputNUM():
    global NUM
    try:
        if len(argv) == 4:
            NUMRAW = argv[3]
            NUM = int(NUMRAW)
        else:
            NUM = int(input("MANY 1-1000 : "))
    except:
        print(Colorate.Horizontal(Colors.rainbow, """ERROR MANY"""))
        
        
def allinput():
    inputtokenline()
    inputtext()
    inputNUM()
    
    
def looprun():
    for i in range(NUM):
        url = 'https://notify-api.line.me/api/notify'
        token = tokenline
        headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
        msg = 'BFHMSC h朒⅗綄堃🜴呷👉煹愳斘嬶堿Ⰾ抸🝓嚵⁾😭ࠈ↗᷅獭🔱æᡰ昬伀抱ᇢ⅗ゞ炏攺⅗ᡕ✉嫕簒丄嬶堿Ⰾ抸🝓嚵⁾😭ࠈ↗᷅獭🔱æᡰ昬伀抱 朒⅗綄堃🜴呷👉煹愳斘嬶堿Ⰾ抸🝓嚵⁾😭ࠈ↗᷅獭🔱æᡰ昬伀抱ᇢ⅗ゞ炏攺⅗ᡕ✉嫕簒丄嬶堿Ⰾ抸🝓嚵⁾😭ࠈ↗᷅獭🔱æᡰ昬伀抱 朒⅗綄堃🜴呷👉煹愳斘嬶堿Ⰾ抸🝓嚵⁾😭ࠈ↗᷅獭🔱æᡰ昬伀抱ᇢ⅗ゞ炏攺⅗ᡕ✉嫕簒丄嬶堿Ⰾ抸🝓嚵⁾😭ࠈ↗᷅獭🔱æᡰ昬伀抱 朒⅗綄堃🜴呷👉煹愳斘嬶堿Ⰾ抸🝓嚵⁾😭ࠈ↗᷅獭🔱æᡰ昬堃घ狺yԳ⑻摒瑋ⴭ伀枕ℾ丛៤濺彸炏崈ᤌㅠƅ🚢🃟🐯☮⸏️囗☣🜯ᣇ欲疊ଳါ橞⦻️྇ᆠ伀澦燀️ภ♣🁕ᷙⰎ😹ࠈ️ാ水吇໯🗻滻😏ƅᥬⅆ7丄⁾惾幧🌴濺楻⅗燀Գ⃲抱寣ཿ囉🞥ཿ汫定ⷚ⇫️摒泣ਆ https://cdn.discordapp.com/attachments/1043128286420676619/1043138650671677501/bfh.gif 朒⅗綄堃🜴呷👉煹愳斘嬶堿Ⰾ抸🝓嚵⁾😭ࠈ↗᷅獭🔱æᡰ昬伀抱ᇢ⅗ゞ炏攺⅗ᡕ✉嫕簒丄嬶堿Ⰾ抸🝓嚵⁾😭ࠈ↗᷅獭🔱æᡰ昬伀抱ᇢ⅗ゞ炏攺⅗ᡕ✉嫕簒丄🈋囗❯7ᓯघ獭乄幧现ㅧ俴️ ᖂ盕⚔æఐ枊Ⰼ櫡️✉ᑷ樗废沛⚔⦻ᎇዚⓤ️⛨矣🃏ⅆ྇癝ᷙᵍᅮ殹ዚᬚ彸伀ㆸ💞瑋暧求ࡻภ⽪⽪ᣡ樗ᜭ🔱濵畬撲Ⰼ️巊️嫕楻喹🔒Ⳕ塳康ᇢ¹⚔濵🐯ᓯ斾⣃ཫ⮸殹␛仺🟨👍᠖␿️⑻ᠥఌൠⰎ🍖᎑ᒧJሥԳ寣簒碥↗Ⰾ獞獞️Ⰾ癝罰昬昩塳ᠥ攺◾Ⰾᬚ🟞ㅧ扔ᇢ翷昬ᑷ7⇫‖濵滻廛៸偑ᛃ✏👷ဳᎇ¹獭៸泣⥍沛昬碥濵罰偑咁ଖᠥ灼矣🊁ᠥᓜ⃲彸窟🔱愳幧暧峃水෵ⷚఐ⚰᠓ࠈ泣ཿᒧ姬៸帯媸⚔໯愳泣️ ᎑🕕ᛃۢ定‖ႁ₣⨕伻瓑愳⁩☮໯堿ᓯ⅗ס⏩⛨⁾巊ᜭ㈊现☮🈁æ巯⽪ൠᓯ✡️峃घᏼ康暧俴🐺堿 搮俴切ᵙภ嬴扔␛楻碥堿ॖ◾મ康7ȶ࡙炏ᔨ᭓綄⅗欲y矣ሥ竛❯伻ס嬶巊᷅ᆠᓯ水欲濵🞵昩ဳ灼缞🃐巯ᓜᗇᅮ😹俴🙊👂ᠥ扔偁મ篤嬶🛢切巊⛄沭️ㅧ🕙ᣡ⍻峃忀⃲ᇢ康⅗澦⛨槑ᔨㇰᵙᓯ️枊᭓毤₰✡ᗇ熰ᬚ⁾添暧⅗y卜⅗ڰ✏⍻ᤌ欲ᷙ₣æ🄶️ㆡԳ殹😚囉篤᷅矣᷅卜ਆ殹卜⁩拢煹偁ᔨס៸⦻仺ᆃԳ煹️⚔昬ࡱ偑 ⚔️࡙惾✡巯ȶ☣塳️྇ᘹ眰烊ℾ🁍砃丄〢7ᘹ️卜碥崈汫幧忀⥍᎑ᡰ🚳᠓⟆呷熰️Ⰼ៸嬴ⴭ🈹Գ〢喹ఌքࡱ璮⇫Ⳕ甼🋂஘ᕽ️巯甼澦ᆃ️⅗💝ᷙ沛ⅆ　ắᆠॱ⚰⛄泣濵楻☮⅗⏬ⷚۢ矣痝水᠓៸️伻滻ࡱ💝Ⰾ️঳獭ᕽ切ᏼめภ泣簒ӷ磀愳⨕⫪⁾Ⰾắᠥ⚰瑋ᆠ⛄〠⏬俴ါᣡ峇✡硭ᏼ⚰ᵍᵍ癝嬴✡៤ⴭ幧ⓤࡱ㈊⚰攺෵ఌ滻ឿ矣⫪ᶸᥬᓯ狺Ą废ᥬæ甼⍻␛ⅆڰ🗻️翷嬶嬴矣🛁❯囉💞⟆️昡⅗昨切ᗇ️砃偑️⇫欲昡♣燀ଳ冯æڰዚႁ疊忀抸↗ࠈ幧ࡱ汫ᑷ瑋暧嬴仺爺狺⁾ః🛢঳♣7⇫࡙崈斾伻楻帯࡙㈊ք🜰忀♣切祆缞✉朒ଳଖ⃲槑由ᒧ🜯塳磀泣☮🈋ᥬ🚯చ⚔ࡱ昡朒昨抸俴昩狺滼硭քסᗇచ⚔伀泣ဳ️⮸櫡᷅❯痝ắ✡᭟Գ熰廛砃̞🃏巯燀៤水磀幧෵❯伧楻ᓯ️囗牤偑‖囉🁉️ᡰ᠓🇓வ堿ᅮᖂॱy絎碥⥍🝘‖🌯Գ峃⧆ᗇ簒疊ଳ✏ต⇫昩஘ଳ️🅕️ 〢伀康噾㈊️️᷅ᏼ璮⟆️康灼🔗扔嫹ᒧ壦️️ᵍ↗ᖂఐឿめ₰彸៤঳྇⮸⧆巊ᔨᵼ⦻呷⅗ᶸ堃घ狺yԳ⑻摒瑋ⴭ伀枕ℾ丛៤濺彸炏崈ᤌㅠƅ🚢🃟🐯☮⸏️囗☣🜯ᣇ欲疊ଳါ橞⦻️྇ᆠ伀澦燀️ภ♣🁕ᷙⰎ😹ࠈ️ാ水吇໯🗻滻😏ƅᥬⅆ7丄⁾惾幧🌴濺楻⅗燀Գ⃲抱寣ཿ囉🞥ཿ汫定ⷚ⇫️摒泣ਆ拢ۿ✏楻ᅮ帯⃲峃瑋㈊卜😁牢₰ᆠ🝘㈊⧆猘મ綄🝲⏬壦ଳ🈒ᛃ翷஘ᛧ炏y壦⛨✉攺☤😹❯æ矣碥᷅筰✉घࡱ泣✡攺🜨窟Ⳕ᭓⛄ⴭ️ᣡ峃ס⚔⥍嬶ȶ爺废巊घ囉斘寣殹ᆠԳ穎஘⚔‖ࡱ✏ᇢ偁᷅️ƅ␛烊️ᓯᣡଳ滻扔⚔洨嚵堃ॖ矣⮸俴ᔨ瑀燀🠤⏬Ⰼ9ᖂ⚰㈲️偑😏樗伀　壦悆ᘹඅ️🗻ᷙ😂泣ᶸ囉៤熰定7️঳㈊濵ॱめ✏️✏ᵼఌ现㈲康朒嫕堃✡ሥ昬✡扱ᡕ🡴碥疊ᔨ❯♣俴ㇰ️堿咁঳ⓤ嬶ⷚ煹塳攺⃲㈲囉巊爺⍻翷घ琴ภ囀矣⧆喹ଳ☣Գㆸ෵️窊⟆7滻⃣ॖࡈ琴঳磀🔗狺ƅဳ伻ൠ᷅堔ภ᠓ຮ狺噾घ⟆ᆠᅮᎇ⧆偁ఐ佟碥祆ⓠ罰磀ᣇס✉ᛃ㈲卜毤঳礓😸ᜭ晪⮸ᣡㆸ️ۢ使窟攺滻⣃🛂堿牢噾᭓⽪卜牢翷🐥✏ᛶ️囀伧嬶堿Ⰾ抸🝓嚵⁾😭ࠈ↗᷅獭🔱æᡰ昬伀抱ᇢ⅗ゞ炏攺⅗ᡕ✉嫕簒丄🈋囗❯7ᓯघ獭乄幧现ㅧ俴️ ᖂ盕⚔æఐ枊Ⰼ櫡️✉ᑷ樗废沛⚔⦻ᎇዚⓤ️⛨矣🃏ⅆ྇癝ᷙᵍᅮ殹ዚᬚ彸伀ㆸ💞瑋暧求ࡻภ⽪⽪ᣡ樗ᜭ🔱濵畬撲Ⰼ️巊️嫕楻喹🔒Ⳕ塳康ᇢ¹⚔濵🐯ᓯ斾⣃ཫ⮸殹␛仺🟨👍᠖␿️⑻ᠥఌൠⰎ🍖᎑ᒧJሥԳ寣簒碥↗Ⰾ獞獞️Ⰾ癝罰昬昩塳ᠥ攺◾Ⰾᬚ🟞ㅧ扔ᇢ翷昬ᑷ7⇫‖濵滻廛៸偑ᛃ✏👷ဳᎇ¹獭៸泣⥍沛昬碥濵罰偑咁ଖᠥ灼矣🊁ᠥᓜ⃲彸窟🔱愳幧暧峃水෵ⷚఐ⚰᠓ࠈ泣ཿᒧ姬៸帯媸⚔໯愳泣️ ᎑🕕ᛃۢ定‖ႁ₣⨕伻瓑愳⁩☮໯堿ᓯ⅗ס⏩⛨⁾巊ᜭ㈊现☮🈁æ巯⽪ൠᓯ✡️峃घᏼ康暧俴🐺堿 搮俴切ᵙภ嬴扔␛楻碥堿ॖ◾મ康7ȶ࡙炏ᔨ᭓綄⅗欲y矣ሥ竛❯伻ס嬶巊᷅ᆠᓯ水欲濵🞵昩ဳ灼缞🃐巯ᓜᗇᅮ😹俴🙊👂ᠥ扔偁મ篤嬶🛢切巊⛄沭️ㅧ🕙ᣡ⍻峃忀⃲ᇢ康⅗澦⛨槑ᔨㇰᵙᓯ️枊᭓毤₰✡ᗇ熰ᬚ⁾添暧⅗y卜⅗ڰ✏⍻ᤌ欲ᷙ₣æ🄶️ㆡԳ殹😚囉篤᷅矣᷅卜ਆ殹卜⁩拢煹偁ᔨס៸⦻仺ᆃԳ煹️⚔昬ࡱ偑 ⚔️࡙惾✡巯ȶ☣塳️྇ᘹ眰烊ℾ🁍砃丄〢7ᘹ️卜碥崈汫幧忀⥍᎑ᡰ🚳᠓⟆呷熰️Ⰼ៸嬴ⴭ🈹Գ〢喹ఌքࡱ璮⇫Ⳕ甼🋂஘ᕽ️巯甼澦ᆃ️⅗💝ᷙ沛ⅆ　ắᆠॱ⚰⛄泣濵楻☮⅗⏬ⷚۢ矣痝水᠓៸️伻滻ࡱ💝Ⰾ️঳獭ᕽ切ᏼめภ泣簒ӷ磀愳⨕⫪⁾Ⰾắᠥ⚰瑋ᆠ⛄〠⏬俴ါᣡ峇✡硭ᏼ⚰ᵍᵍ癝嬴✡៤ⴭ幧ⓤࡱ㈊⚰攺෵ఌ滻ឿ矣⫪ᶸᥬᓯ狺Ą废ᥬæ甼⍻␛ⅆڰ🗻️翷嬶嬴矣🛁❯囉💞⟆️昡⅗昨切ᗇ️砃偑️⇫欲昡♣燀ଳ冯æڰዚႁ疊忀抸↗ࠈ幧ࡱ汫ᑷ瑋暧嬴仺爺狺⁾ః🛢঳♣7⇫࡙崈斾伻楻帯࡙㈊ք🜰忀♣切祆缞✉朒ଳଖ⃲槑由ᒧ🜯塳磀泣☮🈋ᥬ🚯చ⚔ࡱ昡朒昨抸俴昩狺滼硭քסᗇచ⚔伀泣ဳ️⮸櫡᷅❯痝ắ✡᭟Գ熰廛砃̞🃏巯燀៤水磀幧෵❯伧楻ᓯ️囗牤偑‖囉🁉️ᡰ᠓🇓வ堿ᅮᖂॱy絎碥⥍🝘‖🌯Գ峃⧆ᗇ簒疊ଳ✏ต⇫昩஘ଳ️🅕️ 〢伀康噾㈊️️᷅ᏼ璮⟆️康灼🔗扔嫹ᒧ壦️️ᵍ↗ᖂఐឿめ₰彸៤঳྇⮸⧆巊ᔨᵼ⦻呷⅗ᶸ堃घ狺yԳ⑻摒瑋ⴭ伀枕ℾ丛៤濺彸炏崈ᤌㅠƅ🚢🃟🐯☮⸏️囗☣🜯ᣇ欲疊ଳါ橞⦻️྇ᆠ伀'
        r = requests.post(url, headers=headers, data = {'message':msg})
        if r.status_code == 200:           
            print(Colorate.Horizontal(Colors.rainbow, """SPAM SUCCESS"""))
        else:
            print(Colorate.Horizontal(Colors.rainbow, """RATE LIMIT"""))
        print("")

def runtrue():
    allinput()
    looprun()
    
class check():
    def checkargv():
        try:
            commands = ['-help','--help','-h','?','--h','-?','/?']
            if argv[1] in commands:
                pass
            else:
                runtrue()
        except:
            runtrue()


if __name__ == "__main__":
    check.checkargv()