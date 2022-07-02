#Work with Python 3.9.1
import discord
import asyncio
import datetime
import logging
import random
import traceback
import time
import datetime
import os
import urllib
import bs4
import re
from urllib.parse import quote
import warnings
from discord.ext import commands
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from discord.ext import tasks

 
app = discord.Client()

@app.event
async def on_ready():
    print("I'm logging in.")  
    print(app.user.name)                                   
    print(app.user.id)
    print('===============')
    game = discord.Game("Say =명령어")
    await app.change_presence(status=discord.Status.online, activity=game)
    
    
now = datetime.datetime.now()
time = f"{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초"

@app.event
async def on_message_delete(message):
    channel = app.get_channel(721047251862159416)
    embed = discord.Embed(title=f"삭제됨", description=f"유저 : {message.author.mention} 채널 : {message.channel.mention}", color=0xFF0000)
    embed.add_field(name="삭제된 내용", value=f"내용 : {message.content}", inline=False)
    embed.set_footer(text=f"{message.guild.name} | {time}")
    await channel.send(embed=embed)

@app.event
async def on_message(message):


    if message.content.startswith("=명령어"):
        channel = message.channel
        embed = discord.Embed(
            title = '명령어 리스트',
            description = '도리봇은 당신의 채팅에 귀 기울이고 있답니다.',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+" ")  
        embed.add_field(name ='=MBTI', value = "도리봇이 MBTI에 대한 설명을 불러옵니다.",inline = False)
        embed.add_field(name ='=음식추천', value = "도리봇이 당신에게 음식 하나를 추천해줄 것입니다.",inline = False)
        embed.add_field(name ='=대한민국', value = "도리봇이 대한민국의 현실에 대해 팩트를 날릴겁니다.",inline = False)   
        embed.add_field(name ='=모배_릴리즈', value = "도리봇이 배틀그라운드 모바일의 릴리즈 내역을 불러옵니다.",inline = False)
        embed.add_field(name ='=게임허락', value = "도리봇에게 게임 허락을 받아보세요, 봇이 게임을 플레이 하는것을 허락하지 않는다면 그날은 게임 안 돌리는겁니다?",inline = False)
        await message.channel.send(channel,embed=embed)

  
    if message.content.startswith('=모배_릴리즈'):
        channel = message.channel
        embed = discord.Embed(
            title = '배틀그라운드 모바일의 업데이트 내역입니다.  ',
            description = 'Apple 앱스토어 기준입니다.',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"")
        embed.add_field(name = '0.5.0', value = '===',inline = False)
        embed.add_field(name='===', value='======', inline=False)
        embed.add_field(name="0.6.0", value="신규 아케이드 모드 추가", inline=False)  
        embed.add_field(name="===", value="총기창고 및 총기스킨 추가", inline=False)  
        embed.add_field(name="===", value="1,인,칭(FPP)모드 추가", inline=False)    
        embed.add_field(name="===", value="======", inline=False) 
        embed.add_field(name="0.7.0", value="클랜 시스템 대규모 업데이트", inline=False) 
        embed.add_field(name="===", value="아케이드 모드 [워모드] 추가", inline=False)  
        embed.add_field(name="===", value="로비 UI 개선", inline=False)   
        embed.add_field(name="===", value="======", inline=False)  
        embed.add_field(name="0.8.0", value="신규 맵 [사녹] 등장: 더 작아진 전장에서, 더 치열한 전투를 즐기세요.", inline=False)   
        embed.add_field(name="===", value="QBZ, 방탄UAZ 추가: 새로운 아이템과 함께 새로운 전장을 장악하세요.", inline=False) 
        embed.add_field(name="===", value="최적화 진행: 보다 쾌적한 환경에서 모바일 배그를 즐기실 수 있습니다.", inline=False)
        embed.add_field(name="===", value="======", inline=False) 
        embed.add_field(name="0.9.0", value="할로윈 축제: 배틀그라운드에서 할로윈 축제를 즐겨보세요!", inline=False)   
        embed.add_field(name="===", value="야간모드: 어둠 속의 적을 찾아 최후의 승자가 되어보세요!", inline=False) 
        embed.add_field(name="===", value="크루전: 크루원들과 함께 크루전의 승자가 되어보세요!", inline=False)
        embed.add_field(name="===", value="======", inline=False) 
        embed.add_field(name="0.9.1", value="할로윈 축제: 배틀그라운드에서 할로윈 축제를 즐겨보세요!", inline=False)   
        embed.add_field(name="===", value="야간모드: 어둠 속의 적을 찾아 최후의 승자가 되어보세요!", inline=False) 
        embed.add_field(name="===", value="크루전: 크루원들과 함께 크루전의 승자가 되어보세요!", inline=False)
        embed.add_field(name="===", value="======", inline=False)     
        embed.add_field(name="0.10.0", value="신규 맵 비켄디 오픈", inline=False)   
        embed.add_field(name="===", value="총기 스킨 업그레이드 시스템", inline=False) 
        embed.add_field(name="===", value="퀵 보이스 한국어 버전 신규 추가", inline=False)
        await message.channel.send(channel,embed=embed)  

    if message.content.startswith('=모배_릴리즈'):
        channel = message.channel
        embed = discord.Embed(
            title = '배틀그라운드 모바일의 업데이트 내역입니다.  ',
            description = '(1/4)',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"")
        embed.add_field(name="0.11.0", value="BIOHAZARD RE: 모드 추가", inline=False)   
        embed.add_field(name="===", value="월광모드 추가", inline=False) 
        embed.add_field(name="===", value="아케이드 모드에 사녹 맵 추가", inline=False)
        embed.add_field(name="===", value="======", inline=False)  
        embed.add_field(name="0.12.0", value="서바이벌 모드 [좀비 - 황혼의 탈출] 신규 추가", inline=False)   
        embed.add_field(name="===", value="[좀비 - 새벽의 저주] 2탄 업그레이드", inline=False) 
        embed.add_field(name="===", value="======", inline=False)  
        embed.add_field(name="0.13.0", value="팀 데스 매치 모드 신규 출시", inline=False)   
        embed.add_field(name="===", value="비켄디 맵 & 좀비 모드 개선", inline=False) 
        embed.add_field(name="===", value="======", inline=False)    
        embed.add_field(name="0.14.0", value="신규 모드 바이러스 인펙션 출시", inline=False)   
        embed.add_field(name="===", value="SMG 애호가 빅토르 신규 출시", inline=False) 
        embed.add_field(name="===", value="======", inline=False)   
        embed.add_field(name="0.15.0", value="클래식 모드 업데이트", inline=False)   
        embed.add_field(name="===", value="헤비 머신건 모드 신규 추가", inline=False) 
        embed.add_field(name="===", value="======", inline=False)   
        embed.add_field(name="0.16.0", value="신규 모드 기어 아레나 출시", inline=False)   
        embed.add_field(name="===", value="에란겔 겨울 모드 추가", inline=False) 
        embed.add_field(name="===", value="======", inline=False)  
        embed.add_field(name="0.17.0", value="2주년 기념 테마파크 맵 & 푸짐한 이벤트", inline=False)   
        embed.add_field(name="===", value="클래식 모드 업데이트 -데스캠, 총기 밸런싱", inline=False) 
        embed.add_field(name="===", value="======", inline=False)   
        embed.add_field(name="0.18.0", value="새로워진 미라마 & 캔티드 사이트 등장!", inline=False)   
        embed.add_field(name="===", value="더욱 유니크한 Royale Pass 시즌 13 (5/13)", inline=False) 
        await message.channel.send(channel,embed=embed)

    if message.content.startswith('=모배_릴리즈'):
        channel = message.channel
        embed = discord.Embed(
            title = '배틀그라운드 모바일의 업데이트 내역입니다.  ',
            description = '(2/4)',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"")
        embed.add_field(name="0.19.0", value="신규 클래식 맵 LIVIK(리빅) 업데이트!", inline=False)   
        embed.add_field(name="===", value="리빅 전용 신규 총기 P90 & MK12, 신규 차량 몬스터 트럭 등장!", inline=False) 
        embed.add_field(name="===", value="======", inline=False)         
        embed.add_field(name="1.0.0", value="배틀그라운드 모바일 두 번째 이야기", inline=False)   
        embed.add_field(name="===", value="[에란겔 리마스터]", inline=False) 
        embed.add_field(name="===", value="[그래픽 및 인터페이스(UI) 개선]", inline=False)
        embed.add_field(name="===", value="======", inline=False) 
        embed.add_field(name="1.1.0", value="[메트로 로얄]", inline=False)   
        embed.add_field(name="===", value="[에란겔-메트로]", inline=False) 
        embed.add_field(name="===", value="[클래식 모드 업데이트]", inline=False)
        embed.add_field(name="===", value="======", inline=False)         
        embed.add_field(name="1.2.0", value="[에란겔-룬 테마 모드]", inline=False)   
        embed.add_field(name="===", value="[메트로 로얄-시즌2]", inline=False)            
        embed.add_field(name="===", value="======", inline=False)   
        embed.add_field(name="1.3.0", value="[에란겔-3주년 뮤직 테마 모드]", inline=False)   
        embed.add_field(name="===", value="[모신 나강, 모터 글라이더 신규 등장]", inline=False) 
        embed.add_field(name="===", value="======", inline=False) 
        embed.add_field(name="1.4.0", value="[한국 서비스 3주년]", inline=False)   
        embed.add_field(name="===", value="[콜라보 테마 모드-고질라 vs 콩]", inline=False) 
        embed.add_field(name="===", value="======", inline=False) 
        embed.add_field(name="1.5.0", value="[신규 총기 MG3]", inline=False)   
        embed.add_field(name="===", value="[치료제 투척 및 전투 개선]", inline=False) 
        embed.add_field(name="===", value="[하이테크놀로지 테마 모드]", inline=False)
        embed.add_field(name="===", value="======", inline=False)   
        embed.add_field(name="1.6.0", value="[NEW 에일리언 하자드 모드]", inline=False)   
        embed.add_field(name="===", value="[클래식 모드 개선]", inline=False) 
        embed.add_field(name="===", value="[배틀그라운드 모바일x프로미스나인]", inline=False)
        await message.channel.send(channel,embed=embed)

    if message.content.startswith('=모배_릴리즈'):
        channel = message.channel
        embed = discord.Embed(
            title = '배틀그라운드 모바일의 업데이트 내역입니다.  ',
            description = '(3/4)',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"")
        embed.add_field(name="1.7.0", value="[배틀그라운드 모바일 x 아케인 | 미러 월드 테마 모드]", inline=False)   
        embed.add_field(name="===", value="[배틀그라운드 모바일 x 아케인 | 치킨의 소환사 이벤트]", inline=False) 
        embed.add_field(name="===", value="[클래식 모드 개선]", inline=False)
        embed.add_field(name="===", value="======", inline=False) 
        embed.add_field(name="1.8.0", value="[배틀그라운드 모바일 x [스파이더맨™: 노 웨이 홈] | 스파이더맨 테마 모드]", inline=False)   
        embed.add_field(name="===", value="[신규 클래식 맵 | 리빅: 아포칼립스]", inline=False) 
        embed.add_field(name="===", value="[클래식 모드 기능 추가]", inline=False)
        embed.add_field(name="===", value="======", inline=False)      
        embed.add_field(name="1.9.0", value="[알록달록 4주년 테마 모드]", inline=False)   
        embed.add_field(name="===", value="[플레이그라운드 리뉴얼]", inline=False) 
        embed.add_field(name="===", value="[에란겔 밀리터리 베이스 철교 리뉴얼]", inline=False)
        embed.add_field(name="===", value="======", inline=False) 
        embed.add_field(name="2.0.0", value="[한국 4주년 대규모 이벤트]", inline=False)   
        embed.add_field(name="===", value="[리빅 정식 업데이트]", inline=False) 
        embed.add_field(name="===", value="[배틀그라운드 모바일 x 에반게리온(5/19~6/19)]", inline=False)
        embed.add_field(name="===", value="======", inline=False)        
        await message.channel.send(channel,embed=embed)          

    if message.content.startswith("=MBTI"):
        await message.channel.send("당신의 MBTI에 대한 설명을 불러옵니다.")    
        await message.channel.send("예시) = + INFP")      


    if message.content.startswith("=INTP"):                             
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [논리적인 사색가]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '과거에서', value = '배우되, 현재에 살며, 미래에 대한 희망을 가지세요. 그리고 중요한 것은 질문하는 일을 멈추지 않는 것입니다.',inline = False)
        embed.add_field(name='사색가형은', value='전체 인구의 3% 정도를 차지하는 꽤 흔치 않은 성격 유형으로, 이는 그들 자신도 매우 반기는 일입니다. 왜냐하면, 사색가형 사람보다 [평범함]을 거부하는 이들이 또 없기 때문입니다. 이 유형의 사람은 그들이 가진 독창성과 창의력, 그리고 그들만의 독특한 관점과 왕성한 지적 호기심에 나름의 자부심을 가지고 있습니다. 보통 철학자나 사색가, 혹은 몽상에 빠진 천재 교수로도 많이 알려진 이들은 역사적으로 수많은 과학적 발전을 이끌어 내기도 하였습니다.', inline=False)
        embed.add_field(name='연구되지 않은 삶은 의미가 없다!', value='천재적인 이론이나 난해한 논리로 유명한 이들은 다른 성격 유형과 비교하여 가장 논리적인 사람들로 알려져 있습니다.', inline=False)        
        embed.add_field(name = '이들은', value = '사건이나 사물의 어떠한 일련의 연속성에 관심이 많으며, 사람들의 언행에 불일치되는 부분을 집어내 트집 잡는 것을 즐기는데, 이는 거의 취미 수준에 가까울 정도입니다. 때문에 이들에게 거짓말은 하지 않는 것이 좋습니다. 또 한 가지 아이러니한 점은 이들의 얘기를 곧이곧대로 듣지 말고 잘 새겨 들어야 한다는 것입니다. 이는 이들이 솔직하지 않아서가 아니라 아직 채 명확히 규명되지 않은 생각이나 이론에 대하여 얘기하는 경향이 있기 때문입니다. 이들은 상대방을 실질적인 대화 상대로 보는 것이 아니라 그들의 생각이나 이론을 펴기 위한 하나의 대상으로 여깁니다.',inline = False)
        embed.add_field(name='이러한', value='성향 때문에 이들에게 일을 맡기는 게 불안하게 느껴질 수도 있지만, 사실 사색가형 사람보다 문제를 정확히 파악하고 이를 둘러싸고 있는 요소를 낱낱이 파헤쳐 독창적이며 실행 가능한 해결책을 찾아내는 데 더 열성적이고 뛰어난 사람은 없습니다. 단, 이들에게서 업무 진행 상황에 따른 보고서 따위를 제출받기를 기대하지는 않는 게 좋습니다. 이 성격 유형의 사람은 실질적인 하루하루 업무나 유지에는 관심이 없기 때문입니다. 하지만 일단 이들의 천재성과 잠재력이 활개 칠 수 있는 환경이 조성되면 이들은 통찰력 있고 편향되지 않은 해결책을 찾는 데 그들이 가진 모든 시간과 에너지를 모두 쏟아부을 것입니다.', inline=False)
        embed.add_field(name='지혜는 호기심으로부터 시작', value='이런저런 몽상에 사로잡혀 있는 듯한 모습을 자주 보이는 이들은 한시도 쉼 없이 생각에 몰두합니다. 심지어는 아침에 눈을 뜰 때조차도 쉴 새 없이 쏟아지는 아이디어와 함께 하루를 시작합니다. 머릿속에서 끊임없는 벌어지는 논쟁과 생각으로 수심에 가득 차 보이거나 혼자 동떨어져 있어 보이기도 하지만, 이들과 비슷한 관심사를 가진 사람 혹은 친밀한 관계의 이들과 있을 때면 편안하고 밝은 모습을 보입니다. 이와 대조적으로 낯선 이들과 있을 때는 극도로 수줍어하며, 만일 이들이 논리적으로 내린 결론이나 이론이 상대방으로부터 비판을 받거나 하는 경우가 생기면 가벼운 농담에도 호전적인 태세를 보이기도 합니다.', inline=False)   
        embed.add_field(name='특히나', value='흥분된 상태에서 이야기할 때에는 대화에 일관성이 떨어지기도 하는데, 이는 가장 최근 정립한 이론이 결론에 도달하기까지 일련의 논리적 연결 고리를 모두 설명하려 들기 때문입니다. 이들은 또한 상대방이 그들의 논리를 충분히 이해하지 못하였음에도 쉽게 풀어 설명하거나 하지 않은 채 대화를 다른 주제로 옮기기도 합니다.', inline=False)          
        embed.add_field(name='주관적인 관점', value='이나 감정에 치우쳐 사고하는 사람과 비교해보면 아마도 이들의 사고 과정을 보다 잘 이해할 수 있을 것입니다. 가령 매우 정교하고 복잡한 시계 작동법을 창의적으로 사고하되, 가능한 한 하나의 사실도 빠짐없이 논리적으로 가장 합당한 결론에 이르게 설명한다고 상상해 보십시오. 이것이 바로 사색가형 사람이 사고하는 방식입니다. 이들은 감정 망치가 이들의 사고방식에 훼방 놓는 것을 한치도 용납하지 않습니다.', inline=False) 
        embed.add_field(name='세상을 변화시키고자 하는 당신, 먼저 자신부터 변화하십시오!', value='또한 이들은 다른 이의 감정 섞인 불평이나 불만을 전혀 이해하지 못하기 때문에 친구들은 그들에게서 어떠한 정서적인 위로나 위안을 받지 못합니다. 더욱이 사색가형 사람은 근본적으로 내재되어 있는 문제 해결을 위한 논리적인 해결책을 제안하는 것을 선호하는데, 이는 감성적인 성향의 사람과는 대조되는 부분입니다. 이러한 이들의 성향은 나아가 저녁 모임 계획이나 결혼 준비와 같은 기타 사회적 만남이나 활동에도 영향을 미치는데 이들은 기본적으로 지나치리만치 독창성과 효율적인 결과를 좇는 경향이 있습니다.', inline=False) 
        embed.add_field(name='이들의', value='앞길을 가로막는 한 가지 장애물은 계속해서 드는 실패에 대한 두려움입니다. 사색가형 사람은 혹 자신이 중요한 퍼즐 조각을 놓친 것은 아닌지, 혹 이로 인해 자신이 정체되거나 그들의 지식이 아직 실질적으로 적용되지 않은 무형의 세계에서 길을 잃는 것은 아닌지를 걱정하며 자신의 생각이나 이론을 끊임없이 재평가하는 경향이 있습니다. 자기 자신에 대한 의구심을 극복하는 것이 이들이 직면한 가장 큰 과제입니다. 하지만 그것이 크든 작든, 이들이 가진 지적 능력에서 말미암은 이들의 도전은 그 자체만으로도 세상에 큰 가치를 가져옵니다.', inline=False) 
        embed.add_field(name='논리적인 사색가형에 속하는 유명인', value='빌 게이츠, 알버트 아인슈타인, 아이작 뉴턴, 블레이즈 파스칼, 네오(매트릭스), 브루스 배너(헐크/히어로)  ', inline=False) 
        await message.channel.send(channel,embed=embed) 


    if message.content.startswith("=INFP"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [열정적인 중재자]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '중재자형 사람은', value = '최악의 상황이나 악한 사람에게서도 좋은 면만을 바라보며 긍정적이고 더 나은 상황을 만들고자 노력하는 진정한 이상주의자입니다. 간혹 침착하고 내성적이며 심지어는 수줍음이 많은 사람처럼 비추어지기도 하지만, 이들 안에는 불만 지피면 활활 타오를 수 있는 열정의 불꽃이 숨어있습니다. 인구의 대략 4%를 차지하는 이들은 간혹 사람들의 오해를 사기도 하지만, 일단 마음이 맞는 사람을 만나면 이들 안에 내재한 충만한 즐거움과 넘치는 영감을 경험할 수 있을 것입니다.',inline = False)
        embed.add_field(name='이들은', value='논리나 단순한 흥미로움, 혹은 인생의 실용적인 부분이 아닌 그들 나름의 원리원칙에 근거하여 사고하고 행동합니다. 더욱이 성취에 따르는 보상이나 그렇지 못할 경우에 생길 수 있는 불이익 여부에 상관없이 순수한 의도로 인생의 아름다움이나 명예 그리고 도덕적 양심과 미덕을 좇으며 나름의 인생을 설계해 나갑니다. 그리고 그러한 본인들의 생각과 행동에 자부심을 느끼기도 하는데, 이는 마땅한 일입니다. 하지만 모든 사람이 그들의 생각 뒤에 숨은 동기나 의미를 정확히 파악하지는 못하는데, 이는 자칫 이들을 외톨이로 만들 수도 있습니다.', inline=False)
        embed.add_field(name='금', value='이라고 해서 다 반짝이는 것은 아니며, 헤매고 다니는 자가 모두 길을 잃은 것은 아닙니다. 오래되었어도 강한 것은 시들지 않으며, 깊게 뻗은 뿌리에는 서리가 닿지 않습니다.', inline=False)        
        embed.add_field(name = '자기 자신에 대한 깊은 통찰력', value = '중재자형 사람이 가진 가장 큰 장점은 적절한 은유나 이야기를 통해 그들의 생각을 상징화하여 다른 이들과 깊이 있는 의사소통을 한다는 점입니다. 이러한 직관적인 성향은 이들로 하여금 더 창의적인 일에 몰두하게 합니다. 이를 비추어보면 여러 유명 시인이나 작가, 그리고 배우가 이 성격 유형에 속하는 것이 그리 놀랍지만은 않습니다. 중재자형 사람에게 있어 본인 자신에 대한 이해뿐만 아니라 자신이 속한 세상을 이해하는 것이 매우 중요한데, 이들은 종종 작품에 자신을 투영시켜 세상을 탐구하기도 합니다.',inline = False)
        embed.add_field(name='자기표현에', value='특출난 재주를 가지고 있는 이 유형의 사람은 아름다움에 대한 고찰이나 그들이 가지고 있는 비밀을 은유적인 방법이나 작품 속 허구 인물을 등장시켜 표현하기도 합니다.', inline=False)
        embed.add_field(name='이들은 또한', value='뛰어난 언어적 소질을 보이는데 이는 비단 모국어뿐 아니라 제2외국어(심지어는 제3외국어까지!)를 습득하는 데에까지 재능을 보입니다. 이들의 뛰어난 의사소통 능력은 사람들 간의 화합을 도모하며, 그들이 목표한 바를 달성하기 위해 나아가는 데 도움을 줍니다.', inline=False)   
        embed.add_field(name='다수가 아닌 소수에 더 많은 관심', value='다른 외향적 성격 유형에 속하는 사람과 달리, 중재자형 사람은 소수의 몇몇, 그리고 의미 있다고 판단되는 한 가지 목표에만 관심을 기울이는 등 한 번에 많은 일을 달성하려 하지 않습니다. 만일 모든 사회악을 근절하는 데 그들이 할 수 있는 일이 한정되어 있음을 깨닫는 순간, 이들의 에너지는 빛을 잃고 좌절감을 맛보거나 처한 상황에 압도되기도 합니다. 그리고 이는 밝은 장밋빛 미래를 함께 꿈꾸며 가까이에서 지켜보는 다른 이들의 마음을 안타깝게 하기도 합니다.', inline=False)          
        embed.add_field(name='자칫하면', value='중재자형 사람은 선(善)을 위해 하던 행위를 갑자기 멈추거나 하루하루 일상생활을 영위하는 일조차 등한시할 수도 있습니다. 이들은 종종 깊은 생각의 나락으로 자신을 내몰아 이론적 가설이나 혹은 철학적 논리에 빠지기도 하는데, 꾸준한 관심을 가지고 이들을 지켜보지 않으면 이들은 연락을 끊고 [은둔자] 생활을 하기도 합니다. 그리고 추후 이들을 현실 밖으로 다시 돌아오게 하기까지 주위 사람들의 많은 에너지와 노력을 필요로 합니다.', inline=False) 
        embed.add_field(name='다행인 것은', value='깊은 나락에 빠져 있던 이들도 봄이 오면 다시금 봉오리를 피우는 꽃과 같이 이들의 애정 어린 마음과 창의적인 생각, 이타주의적이며 이상주의적인 생각 역시 제자리로 돌아와 자신뿐 아니라 곁에서 지켜보는 이들로 하여금 뿌듯함에 미소 짓게 합니다. 그리고 다시금 사실적 논리나 현실적인 유용성의 관점이 아닌 넘치는 영감과 인간애, 친절함, 그리고 따뜻한 마음으로 세상을 바라봅니다.', inline=False) 
        embed.add_field(name='열정적인 중재자형에 속하는 유명인', value='J.R.R 톨킨, 윌리엄 쉐익스피어, 톰 히들스턴(한국에서의 그는 MCU의 빌런이자 아스가르드의 신, 천둥의 신 토르의 동생, 요툰헤임의 왕족, 로키역으로 유명함), 줄리아 로버츠, 조니 뎁, 프로도 배긴즈(반지의제왕), 아웬(반지의제왕),   ', inline=False) 
        await message.channel.send(channel,embed=embed) 
        

    if message.content.startswith("=ISTJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [청렴결백한 논리주의자]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '내가 본 바에 의하면', value = '임무를 수행함에 있어 한 명이면 족한 일을 둘이서 수행하면 될 일도 안되거니와, 셋 이상이 하는 경우에는 일이 전혀 성사되지 않더군.',inline = False)
        embed.add_field(name='논리주의자형은 ', value='가장 다수의 사람이 속하는 성격 유형으로 인구의 대략 13%를 차지합니다. 청렴결백하면서도 실용적인 논리력과 헌신적으로 임무를 수행하는 성격으로 묘사되기도 하는 이들은, 가정 내에서뿐 아니라 법률 회사나 법 규제 기관 혹은 군대와 같이 전통이나 질서를 중시하는 조직에서 핵심 구성원 역할을 합니다. 이 유형의 사람은 자신이 맡은 바 책임을 다하며 그들이 하는 일에 큰 자부심을 가지고 있습니다. 또한, 목표를 달성하기 위해 시간과 에너지를 허투루 쓰지 않으며, 이에 필요한 업무를 정확하고 신중하게 처리합니다.', inline=False)
        embed.add_field(name='뭐든', value='쉽게 가정하여 결론 내리지 않는 이들은, 주변을 객관적으로 분석하고 사실에 입각하여 현실적으로 실행 가능한 계획을 세우는 것을 선호합니다. 허튼짓하는 것을 무엇보다도 싫어하는 사람으로 결정을 내린 후에는 목표를 달성하는 데 필요한 사실을 열거함으로써 다른 이들로 하여금 이를 재빨리 인지하여 즉시 실행해 옮기기를 독려합니다. 특히나 우유부단한 것을 몹시 싫어하며, 혹 결정 내린 실행안이 비현실적인 이유로 장애에 부딪혔을 때 쉬이 인내심을 잃기도 하는데, 특히 목표 달성에 필요한 핵심 세부사항을 놓치는 경우에는 더욱 그러합니다. 만일 마감 시간은 가까워져 오는데 논의가 성사되지 않은 채 시간만 질질 끄는 경우, 이들의 불편함 심기가 얼굴에 그대로 나타나기도 합니다.', inline=False)        
        embed.add_field(name = '뱉은 말에 대한 책임과 평판', value = '논리주의자형 사람이 무언가를 하겠다고 하면 얼마나 많은 희생이 따르던지 자신이 한 말에 책임을 지고자 기어이는 해내고야 맙니다. 이런 그들이기에 자신이 내뱉은 말에 책임을 지지 않는 이들을 보면 어쩔 줄 몰라 합니다. 태만과 부도덕의 조합만큼 논리주의자형 사람의 적이 되는 가장 빠른 지름길도 없을 것입니다. 때문에 이들은 혼자 일하는 것을 선호하며, 대개 일을 진행하는 데 직장 내 토의를 거치거나 다른 이들의 견해를 들을 필요 없이 자신만의 목표를 설정하고 달성을 가능케 하는 어느 정도의 지위나 권한을 가지고 있는 경우가 많습니다.',inline = False)
        embed.add_field(name='예리하며', value='사실에 근거하여 사고하는 경향을 가지고 있는 이들은 자율적으로 스스로 알아서 행동하고 책임지기를 원합니다. 이 때문에 이들은 누군가에게 의존하는 것은 약자의 행동이라고 여깁니다. 임무 달성을 위한 열정과 책임감, 그리고 오점 하나 없는 청렴한 이들의 성격으로 하여금 이들을 종종 이러한 오류에 쉽게 빠지게 합니다.', inline=False)
        embed.add_field(name='이들의', value='청렴결백한 성격은 논리주의자형 사람을 정의하는 핵심사항으로, 이는 그들이 생각하는 것 이상으로 중요한 부분입니다. 얼마나 많은 희생이 따르든 이들은 일단 정해진 체계나 지침을 고수하며, 비록 사실을 있는 그대로 밝히는 것이 결과적으로 더 큰 분란을 야기할지라도 자신의 잘못을 시인하고 사실을 밝히고자 합니다. 논리주의자형 사람에게 있어 감정적인 고려보다 정직함이 보다 우선시 되기 때문입니다. 때로 이러한 그들의 대담한 행보는 사람들에게 냉정하고 로봇 같다는 잘못된 인상을 심어 주기도 합니다. 감정이나 애정을 밖으로 표출하는 것에 익숙하지 않은 이들은 혹 사람들로부터 냉혈인이라든지, 더 심하게는 ‘감정 자체가 있느냐’와 같은 말을 듣기도 하는데 이에 깊은 상처를 받기도 합니다.', inline=False)   
        embed.add_field(name='백해무익한 무리와 있느니 차라리 혼자가 낫다', value='논리주의자형 사람의 헌신적인 성격은 매우 긍정적인 자질로 이들로 하여금 많은 것을 이루게 합니다. 하지만 이는 동시에 이들의 약점이 되기도 하는데, 간혹 비양심적인 사람들은 이러한 이들의 약점을 이용하기도 합니다. 안전하며 안정된 삶을 추구하는 논리주의자형 사람은 일이 원활하게 돌아갈 수 있도록 맡은 바 임무를 충실히 수행합니다. 뒤치다꺼리를 마다치 않는 이들의 성향을 아는 동료나 주위 사람들은 간혹 이들에게 책임을 전가하는 경우가 있습니다. 더욱이 개인적인 견해가 아닌 사실만을 얘기하고자 하는 이들의 성향 때문에 정확히 사실을 밝혀 낼 증거가 충분히 모일 때까지 시간이 오래 걸리기도 합니다.', inline=False)          
        embed.add_field(name='이들은', value='그들 자신 또한 챙기고 돌보아야 할 필요가 있음을 잊지 말아야 합니다. 갈수록 기대기만 하는 이들에게 언제고 싫은 내색 한번 않는 논리주의자형 사람들이기 때문에 일단 감정의 골이 쌓여 터진 후 돌아오기 늦어버리는 상황을 초래하기 전 안정과 효율성 추구를 위한 완강하고 헌신적인 이들의 성격을 활용하여 장기간 목표를 달성하기 위한 절충점을 찾아야 합니다. 활기차고 명료하며 안정된 삶을 추구하는 이들의 성향을 진심으로 이해하고 보듬으며 이들이 가진 단점을 보완해주는 동료나 배우자를 만난다면, 이들은 안정을 추구하는 자신의 성향으로 하여금 일을 순리대로 잘 돌아가게 하는 데 지대한 역할을 하고 있다는 생각에 큰 만족감을 느낄 것입니다.', inline=False) 
        embed.add_field(name='청렴결백한 논리주의자형에 속하는 유명인', value='엥겔라 마르켈, 나탈리 포트만, 안토니 홉킨스, 조지 워싱턴, 조지.H.W 부시, 에드워드 스타크(왕좌의게임), 허마이오니 진 그레인저(오역:헤르미온느 진 그레인저, 주인공 해리포터의 절친이자 로날드 위즐리의 아내(허마이오니 진 위즐리), 그리고 그리핀도르!', inline=False) 
        await message.channel.send(channel,embed=embed) 

    if message.content.startswith("=ISFJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [용감한 수호자]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '사랑은', value = '나눌수록 커집니다. 다른 이에게 나누어 주면 줄수록 당신에게 돌아오는 사랑 또한 더욱 커집니다.',inline = False)
        embed.add_field(name='수호자형', value='사람은 꽤 독특한 특징을 가지고 있는데, 이 유형에 속하는 사람은 이들을 정의하는 성격 특성에 꼭 들어맞지 않는다는 점입니다. 타인을 향한 연민이나 동정심이 있으면서도 가족이나 친구를 보호해야 할 때는 가차 없는 모습을 보이기도 합니다. 조용하고 내성적인 반면 관계술에 뛰어나 인간관계를 잘 만들어갑니다. 안정적인 삶을 지향하지만 이들이 이해받고 존경받는다고 생각되는 한에서는 변화를 잘 수용합니다. 이처럼 수호자형 사람은 한마디로 정의 내리기 힘든 다양한 성향을 내포하고 있는데, 이는 오히려 그들의 장점을 승화시켜 그들 자신을 더욱 돋보이게 합니다.', inline=False)
        embed.add_field(name='수호자형 사람은', value='무엇을 받으면 몇 배로 베푸는 진정한 이타주의자로 열정과 자애로움으로 일단 믿는 이들이라면 타인과도 잘 어울려 일에 정진합니다.', inline=False)        
        embed.add_field(name = '약', value = '13%로 꽤 높은 인구 비율을 차지하는데, 인구 대다수를 차지하는 데 있어 이들보다 더 나은 성격 유형은 아마 없을 것입니다. 이들은 종종 의료 부분이나 학문, 혹은 사회단체와 같이 오랜 역사나 전통과 관련된 분야에 종사합니다.',inline = False)
        embed.add_field(name='수호자형 중', value='특히 신중한 성향을 가진 사람은 완벽주의자만큼이나 세심하고 꼼꼼한 면모를 보이기도 합니다. 간혹 일을 지연하는 경우가 있기는 하지만, 그렇다고 일을 시간 내에 마치지 않는 것은 아닙니다. 이들은 맡은 바 일에 책임감을 가지고 업무에 임하며, 회사나 가정에서 그들의 기대치를 넘어 주위 사람들을 만족시키고자 최선을 다합니다', inline=False)
        embed.add_field(name='공(功)을 공(功)이라 말할 수 있는 용기', value='수호자형 사람은 그들의 업적이나 실적을 다른 사람들이 알아차리게 하는 데 어려움을 느낍니다. 이들은 종종 자신이 이룬 성취를 과소평가하는 경향이 있는데, 이러한 겸손한 태도로 종종 다른 이들로부터 존경을 받기도 하는가 하면, 이기적이고 냉소적인 사람들은 이들의 겸손함을 역으로 이용하여 수호자형 사람이 세운 공을 자신의 것으로 돌리는 경우도 있습니다. 자신감과 열정을 지키기 위해서는 이들도 [아니요]라고 말해야 할 때와 자기 자신을 방어해야 할 때를 정확히 인지할 필요가 있습니다.', inline=False)   
        embed.add_field(name='내성적이면서', value='신기하게도 사회적인 성향을 가지고 있기도 한 이들은 좋은 기억력을 자랑합니다. 뛰어난 기억력으로 단순히 데이터나 사소한 정보를 기억하는 것이 아니라, 만나는 사람들이나 그들과 관련한 소소한 사항들을 모두 기억해 놓습니다. 상상력과 타고난 섬세함으로 그들의 자애로운 마음을 표현함으로써 상대방의 가슴을 진심으로 울리는 데 이들보다 더 천부적으로 소질이 있는 이들도 없을 것입니다. 이는 함께 일하는 동료들 사이에서도 자명한 일로, 이들은 동료를 가까운 친구로 여깁니다. 그러나 뭐니 뭐니 해도 이들의 애정과 사랑이 환하게 꽃을 피우는 곳은 바로 가정 내에서 일 것입니다.', inline=False)          
        embed.add_field(name='해야 할 땐 과감히', value='수호자형 사람은 가치 있다고 여기는 일이 마무리되지 않고 있으면 게으르게 가만히 앉아만 있지 못하는 이타주의적 성격을 가지고 있습니다. 다른 내향적인 성격의 사람들과 견주어 봐도 이들만큼 타인과 친밀한 관계를 유지하는 이들이 없습니다. 또한 서로 응원하고 힘을 북돋워 주며 화목한 가정을 꾸려 나가는 것을 옆에서 지켜보는 것 자체가 가족에게는 큰 축복이 아닐 수 없습니다. 이들은 화려한 스포트라이트를 받는 것을 불편해하며, 다른 이들과 함께 달성한 업무에 있어 공을 인정받는 데에 어색해하기도 합니다. 하지만 이들이 그들 자신의 노력을 알리는 데 조금 더 열중한다면 다른 유형의 사람이었다면 그저 상상만 하고 있을 법한 일을 성취해 냄으로써 더 큰 자신감을 얻을 수 있을 것입니다.', inline=False) 
        embed.add_field(name='용감한 수호자형에 속하는 유명인', value='엘리자베스 2세 여왕(영국), 앤 해서웨이, 셀레나 고메즈, 케이틀린 스타크(왕좌의게임), 감지네 샘와이즈(반지의제왕), 닥터 왓슨(셜록홈즈), 캡틴 아메리카(히어로), ', inline=False) 
        await message.channel.send(channel,embed=embed) 

    if message.content.startswith("=ENFJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [정의로운 사회운동가]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '당신이', value = '현재하는 사소한 행위는 잔잔한 물결처럼 서서히 퍼져나가 모든 이에게 영향을 줍니다. 당신의 마음가짐이 다른 이의 가슴에 불을 지필 수도, 근심을 초래할 수도 있습니다. 당신의 숨소리가 사랑의 빛을 뿜어낼 수도, 우울함으로 온 방안을 어둡게 만들 수도 있습니다. 당신의 시선이 즐거움을 선사할 수도 있으며, 당신의 언어가 자유를 향한 열망을 독려할 수도 있습니다. 당신의 행동 하나하나가 다른 이들의 생각과 마음을 열 수 있습니다.',inline = False)
        embed.add_field(name='사회운동가형 사람은', value='카리스마와 충만한 열정을 지닌 타고난 리더형입니다. 인구의 대략 2%가 이 유형에 속하며, 정치가나 코치 혹은 교사와 같은 직군에서 흔히 볼 수 있습니다. 이들은 다른 이들로 하여금 그들의 꿈을 이루며, 선한 일을 통하여 세상에 빛과 소금이 될 수 있도록 사람들을 독려합니다. 또한, 자신뿐 아니라 더 나아가 살기 좋은 공동체를 만들기 위해 사람들을 동참시키고 이끄는 데에서 큰 자부심과 행복을 느낍니다', inline=False)
        embed.add_field(name='진심으로 사람을 믿고 이끄는 지도자', value='우리는 대개 강직한 성품을 가진 이에게 마법처럼 끌리곤 합니다. 사회운동가형 사람은 진정으로 타인을 생각하고 염려하며, 그들이 필요하다고 느낄 때면 발 벗고 나서서 옳은 일을 위해 쓴소리하는 것을 마다하지 않습니다. 다른 이들과 별 어려움 없이 잘 어울리며, 특히 사람들과 직접 얼굴을 보고 의사소통하는 것을 좋아합니다. 이들에게 내재되어 있는 직관적 성향은 이성적 사실이나 정제되지 않은 인간의 본래 감정을 통하여 다양한 사람의 성격을 더 잘 파악하고 이해하게 합니다. 타인의 의도나 동기를 쉽게 파악 후 이를 그와 개인적으로 연관 짓지 않으며, 대신 특유의 설득력 있는 웅변 기술로 함께 추구해야 할 공통된 목표를 설정하여 그야말로 최면에 걸린 듯 사람들을 이끕니다.', inline=False)        
        embed.add_field(name = '진심으로', value = '마음에서 우러나 타인에게 관심을 보이는 이들이지만 간혹 도가 지나쳐 문제가 될 때도 있습니다. 일단 사람을 믿으면 타인의 문제에 지나치리만치 관여하는 등 이들을 무한 신뢰하는 경향이 있습니다. 다행히도 이들의 진심 어린 이타주의적 행동은 다른 이들로 하여금 더 나은 사람이 될 수 있도록 독려한다는 차원에서 자기 계발을 위한 자아실현 기제로 작용하기도 합니다. 하지만 자칫 잘못하면 이들의 지나친 낙관주의는 되려 변화를 모색하는 이들의 능력 밖이거나 그들이 도울 수 있는 범주를 넘어서는 일이 될 수도 있습니다.',inline = False)
        embed.add_field(name='사회운동가형 사람이', value='경험할 수 있는 또 다른 오류는 이들이 그들 자신 감정을 지나치게 투영하고 분석한다는 점입니다. 다른 사람의 문제에 지나치리만치 깊이 관여하는 경우, 자신의 잘못에서 비롯된 일이 아님에도 불구하고 타인의 문제를 마치 본인의 문제로 여겨 자칫하면 정서적 심기증(hypochondria)과 같은 증상을 보일 수도 있습니다. 더욱이 타인이 문제를 해결하는 데 한계에 도달하였을 때 이를 해결하는 데 자신이 어떠한 도움이 될 수 없음에 딜레마에 빠지기도 합니다. 이러한 오류를 범하지 않기 위해서는 사회운동가형 사람은 그 상황에서 한발 뒤로 물러나 본인이 느끼는 감정과 타인의 문제를 객관적으로 분리해 다른 각도에서 바라볼 필요가 있습니다.', inline=False)
        embed.add_field(name='사회정의 구현을 위해 어려움에 맞서 싸우는 이들', value='사회운동가형 사람은 말과 행동이 일치하며, 타인을 진심으로 대합니다. 중독성 강한 이들 특유의 열정으로 사람들 간의 화합을 도모하고 변화를 이끌 때 이들은 그 어떤 때보다도 큰 행복을 느낍니다.', inline=False)   
        embed.add_field(name='사회운동가형의', value='과도한 이타주의적 성격은 자칫하면 되레 문제를 야기하기도 합니다. 이들은 그들이 옳다고 믿는 생각이나 이념 실현을 위해 다른 이를 대신하여 총대를 메는 것을 두려워하지 않습니다. 이를 볼 때 다수의 영향력 있는 정치인이나 지도자가 이 유형에 속하는 것이 어찌 보면 당연한지도 모릅니다. 경제적 부를 창출하기 위해 나라를 이끄는 한 국가의 원수에서부터 버거운 경기를 승리로 이끄는 어린이 야구팀 코치에 이르기까지 이들은 더 밝은 미래 구현을 위해 앞장서서 사람들을 이끄는 것을 좋아합니다.', inline=False)          
        embed.add_field(name='정의로운 사회운동가형에 속하는 유명인', value='버락 오바마, 벤 애플렉, 제니퍼 로렌스, 모피어스(매트릭스), 오라클(매트릭스), ', inline=False) 
        await message.channel.send(channel,embed=embed) 

    if message.content.startswith("=ENTP"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [뜨거운 논쟁을 즐기는 변론가]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '가시밭길이더라도', value = '자주적 사고를 하는 이의 길을 가십시오. 비판과 논란에 맞서서 당신의 생각을 당당히 밝히십시오. 당신의 마음이 시키는 대로 하십시오. [별난 사람]이라고 낙인찍히는 것보다 순종이라는 오명에 무릎 꿇는 것을 더 두려워하십시오. 당신이 중요하다고 생각하는 이념을 위해서라면 온 힘을 다해 싸우십시오.',inline = False)
        embed.add_field(name='변론가형 사람은 ', value='타인이 믿는 이념이나 논쟁에 반향을 일으킴으로써 군중을 선동하는 일명 선의의 비판자입니다. 결단력 있는 성격 유형이 논쟁 안에 깊이 내재한 숨은 의미나 상대의 전략적 목표를 꼬집기 위해 논쟁을 벌인다고 한다면, 변론가형 사람은 단순히 재미를 이유로 비판을 일삼습니다. 아마도 이들보다 논쟁이나 정신적 고문을 즐기는 성격 유형은 없을 것입니다. 이는 천부적으로 재치 있는 입담과 풍부한 지식을 통해 논쟁의 중심에 있는 사안과 관련한 그들의 이념을 증명해 보일 수 있기 때문입니다.', inline=False)
        embed.add_field(name='여기서', value='한 가지 흥미로운 사실은 변론가형 사람은 고집스러우리만치 솔직하기도 하지만 이들이 믿고 관철하는 사안이 아님에도 불구하고 타인의 입장에서 진실 규명을 위해 지칠 줄 모르고 논쟁을 벌인다는 점입니다.', inline=False)        
        embed.add_field(name = '논쟁을', value = '벌이는 주체이자 선의의 비판자로서 이들은 타인의 이성적인 논리를 보다 잘 이해하고 있을 뿐 아니라, 상대편의 관점의 차이도 정확히 꿰뚫어 봅니다.',inline = False)
        embed.add_field(name='단,', value='이를 상호 존중과 이해를 통해 협력을 끌어내는 외교형 사람의 특질과 혼동하지 말아야 합니다. 끊임없이 진리와 지식을 좇는 변론가형 사람들에게 있어 공격과 방어를 통해 타인의 생각이나 이념을 다양한 각도에서 바라보며 해답을 찾는 것보다 더 좋은 방법은 없을 것입니다.', inline=False)
        embed.add_field(name='정해진 법칙은 없습니다 – 뭐가 됐든 성취가 우리의 목적!', value='약자의 입장에서 다수가 받아들인 사안에 의문을 제기함으로써 희열을 느끼기도 하는 이들은, 이러한 성향으로 인해 현존하는 제도를 재고하게 하거나 체제 자체를 흔들어 새로운 방안을 모색하게 합니다. 하지만 변론가형 사람은 이러한 새 방안을 실행하는 데 필요한 일상적인 업무를 처리하는 데에는 영 소질이 없습니다. 이리저리 머리를 굴려 다양한 아이디어를 제안하거나 넓은 안목으로 사고하는 것을 좋아하기는 하지만, 정작 지루하고 고단한 업무를 맡기면 무슨 수를 써서라도 빠져나갈 궁리를 합니다. 이 성격 유형은 인구의 대략 3%에 해당하는데, 이는 딱 적당한 비율입니다. 일단 이들이 아이디어를 낸 후 뒤로 물러서 있으면, 다수의 근면하고 꼼꼼한 성격 유형 사람이 나머지 일을 맡아 처리하면 될 테니까요.', inline=False)   
        embed.add_field(name='논쟁을 좋아하는 변론가형 사람의', value='성격상 이들은 간혹 문제를 야기하기도 합니다. 때에 따라 이들의 성향이 유익하게 작용할 때도 있지만, 간혹 다른 사람의 신경을 건드리기도 하는데 가령 예를 들어 미팅 시 상사의 제안에 대놓고 의구심을 표한다든지, 혹 가족이나 친구가 하는 말에 조목조목 따지는 등과 같은 경우입니다. 이들의 굽힐 줄 모르는 솔직함이 한 목 더 거들기도 하는데, 이들 성향 자체가 말을 예쁘게 순화시켜 하지도 않거니와, 타인에게 세심하지 못한 사람이라고 비추어지는 것에 전혀 개의치 않아 하기 때문입니다. 비슷한 사고와 성향을 가진 사람과는 별 탈 없이 잘 어울립니다. 하지만 마찰을 원치 않는 예민한 성격의 사람이나 다양한 성격의 사람이 한데 어울려 사는 우리 사회는 일반적으로 사람들 간의 배려나 조화를 중요시 여깁니다. 상대방이 혹 불쾌해할 수 있거나 받아들이기 힘든 사안인 경우 필요하다면 선의의 거짓말을 하는 것이 더 나을 수도 있음을 기억해야 합니다.', inline=False)          
        embed.add_field(name='이는', value=' 변론가형 사람에게 어려운 일로 자기 생각과 감정을 잠시 뒤로한 채 타인의 다른 관점을 헤아릴 때면, 비록 의도하지 않았다 하더라도 따지기 좋아하는 이들의 성격 때문에 사람들과의 관계에 금이 갔다는 생각에 속상해하기도 합니다. 다른 이들을 대할 때 그들이 받은 만큼만 하는 스타일인 변론가형 사람은 쓸데없이 아량을 베풀거나 빙빙 돌려 말하는 것을 싫어합니다. 특히 누군가에게 부탁할 필요가 있을 때는 더욱 그러합니다. 미래를 내다보는 비전과 넘치는 자신감, 풍부한 지식, 그리고 날카롭지만 분별력 있는 입담으로 타인에게 우러름을 받기도 하지만, 깊은 인간관계나 연인 관계를 다지는 데에는 이러한 이들의 자질이 충분히 발휘되지 못합니다.', inline=False) 
        embed.add_field(name='배려 있는 논쟁으로 타협에 이르는 지혜', value='변론가형 사람의 본 긍정적 자질과 성격을 충분히 활용하기 위해서는 다른 성격 유형의 사람들에 비해 더 많은 시간과 노력이 필요합니다. 독립적인 사고와 지식, 그리고 자유분방한 사고는 이들이 주체가 되어 이끌어 나가거나 혹은 이들을 필요로 하는 상황에서는 엄청난 가치를 발하지만, 그러기까지 본인들 자신의 꾸준한 노력과 시도가 선행되어야 합니다.', inline=False) 
        embed.add_field(name='일단', value='이 고지에 올라선 후라면 이들은 그들이 내세우는 이념이 빛을 발하기 위해서 그들의 생각에 살을 붙여 줄 다른 이들의 도움이 필요함을 잊지 말아야 합니다. 다른 이들과의 타협점을 찾기 위해 노력하는 것이 아닌 그저 논쟁에서 [승리]하는 데에만 치중한다면, 이들은 단순히 그들이 성공하는 데 필요한 지원군이 충분히 없다고 치부해 버리고 말 것입니다. 선의의 비판자 역할을 성실히 잘 수행하는 변론가형 사람들은 이성적 사고를 통한 발전을 도모하는 동시에, 타인의 감성적인 부분에 대한 이해와 배려 있는 논쟁으로 타협에 이르는 것이 그들에게 가장 어렵지만 동시에 가장 보람된 일임을 깨닫게 될 것입니다.', inline=False)         
        embed.add_field(name='뜨거운 논쟁을 즐기는 변론가형에 속하는 유명인', value='마크 트웨인, 톰 행크스, 토마스 에디슨, 잭 스패로우 선장, 조커(배트맨 세계관의 빌런, [뭐가 그리 심각해?-다크나이트 중-], [나의 죽음이 나의 삶보다 가취있기를.-조커 중-]', inline=False) 
        await message.channel.send(channel,embed=embed) 

    if message.content.startswith("=ENTJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [대담한 통솔자]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '당신에게 ', value = '주어진 시간은 한정되어 있습니다. 그러니 다른 이의 삶을 사느라 시간을 낭비하지 마세요. 다른 사람의 생각에서 빚어진 삶에 방식에 맞추는 함정에 빠지지 마세요. 다른 사람들이 내는 의견이나 생각이 당신의 목소리에 귀 기울이는 것을 방해하는 소음이 되지 않게 하세요. 그리고 무엇보다 중요한 것은, 당신의 마음과 직관을 굳건히 믿고 따라갈 수 있는 용기를 가지는 것입니다. 이야말로 당신이 진정으로 원하는 것이 무엇인지 정확히 알고 있기 때문입니다. 그 외 다른 것은 모두 부차적일 뿐입니다.',inline = False)
        embed.add_field(name='통솔자형 사람은', value='천성적으로 타고난 리더입니다. 이 유형에 속하는 사람은 넘치는 카리스마와 자신감으로 공통의 목표 실현을 위해 다른 이들을 이끌고 진두지휘합니다. 예민한 성격의 사회운동가형 사람과 달리 이들은 진취적인 생각과 결정력, 그리고 냉철한 판단력으로 그들이 세운 목표 달성을 위해 가끔은 무모하리만치 이성적 사고를 하는 것이 특징입니다. 이들이 인구의 단 3%에 지나지 않는 것이 어쩌면 다행일 수도 있습니다. 그렇지 않으면 인구 대다수를 차지하는 소심하고 섬세한 성향의 사람들이 모두 주눅 들어 살지도 모르니까요. 단, 평소 잊고 살기는 하나 우리 삶을 윤택하게 해주는 위대한 사업가나 기관을 이끄는 통솔자형 사람들이 있음에 다행이기도 합니다.', inline=False)
        embed.add_field(name='‘성취’를 통해 느끼는 행복', value='통솔자형 사람은 크든 작든 성취 가능한 도전에 매력을 느낍니다. 이들은 충분한 시간과 자원만 있으면 그 어떤 것도 실현 가능하다고 믿습니다. 이것이 통솔자형 사람을 뛰어난 사업가로 만드는 이들만의 성격적 자질로, 전략적인 사고와 장기적인 안목과 더불어 빠른 판단력과 정확성으로 계획을 단계별로 실행해 나감으로써 진정한 리더의 역할을 합니다. 보통의 사람이라면 포기하고 말 일들도 대단한 의지력으로 꾸준히 밀어붙이는데, 이는 이들에게 있어 자아실현을 위한 자기 암시이기도 합니다. 또한 뛰어난 사회성을 발휘하여 다른 동료들을 채찍질함으로써 함께 더 큰 성공과 성취를 이루고자 합니다.', inline=False)        
        embed.add_field(name = '기업 관련 협상이든, ', value = '자동차 구매를 위한 협상이든 통솔자형 사람은 우위를 선점한 채 한 치도 뒤로 물러서는 법이 없습니다. 이는 단순히 이들이 냉혈인이라거나 사악해서가 아니라 단지 도전과 지략, 그리고 상황에서 행해지는 상대방과의 재담(才談)을 진정 즐기기 때문입니다. 만일 상대가 게임이 안된다 하더라도 이는 통솔자형 사람으로 하여금 승리로 이끄는 핵심 전략서를 스스로 덮게 만드는 이유가 되지 못합니다.',inline = False)
        embed.add_field(name='"내가', value='상대방을 배려할 줄 모르는 [미친 X]이라고 해도 난 신경 안 써. 왜냐하면 난 잘난 [미친 X]이니까"라는 생각이 이들의 속마음입니다.', inline=False)
        embed.add_field(name='통솔자형 사람이', value='우러러보는 누군가가 있다면 그는 아마도 그들 자신처럼 정확하고 민첩하게 행동하는 사람으로, 지식으로 무장하여 그들에게 감히 도전장을 내미는 사람일 것입니다. 이들은 다른 사람의 재능을 알아보는 재주 또한 있는데, 이는 팀원 간의 협력을 다지고(아무리 잘나고 똑똑한 개인이라도 모든 일을 혼자 다 할 수는 없으므로) 이들의 오만방자함을 견제하는 데 도움이 됩니다. 간혹 혹독하리만치 타인의 실수를 지적하는 경향이 있는데 이로 인해 이들은 종종 문제를 야기하기도 합니다.', inline=False)   
        embed.add_field(name='진정성 있는 인간관계 형성을 위한 노력', value='분석형에 속하는 사람들은 감정을 표현하는 일에 서투른데, 사교적인 성격상 이들의 성격은 밖으로 쉽게 표출됩니다. 가령 일적으로 비효율적이고 무능하며 게으르다고 판단되는 이들을 보면 이들은 그들의 예민한 부분을 가차 없이 건드리기도 합니다. 통솔자형 사람에게 있어 감정 표현은 나약함의 표시로 이러한 성향 때문에 쉽게 적을 만들기도 합니다. 또한 단순히 목표를 성취하는 데 있어서뿐만 아니라 타인으로부터 인정받고 안 받고의 여부는 효율적인 조직에 달려 있음을 사람들에게 줄기차게 상기시키는데, 이는 통솔자형 사람에게는 매우 민감하고 중대한 사안이기 때문입니다.', inline=False)          
        embed.add_field(name='이들은', value='진정한 권력가형으로 그들 본연의 모습 이상으로 자신을 과대 포장하는 경향이 있습니다. 하지만 그들의 성공이 혼자만의 능력이 아닌 이들을 옆에서 도운 여러 사람에게서 기인한다는 점을 잊지 말아야 합니다. 그리고 함께 한 이들의 헌신과 노력, 재능을 인정하며, 특히 든든한 지원군이 되어 주었음에 온 마음을 다해 감사함을 느끼는 것이 중요합니다. 비록 [안되면 척]이라고 하겠다는 마음가짐이라 하더라도 말입니다. 만일 다른 이들의 감정을 살피는 진심 어린 노력이 이들이 가진 성격적 장점과 합해진다면, 이들은 다른 이들과 더 깊고 만족스러운 인간관계를 형성할 수 있을 것입니다. 그리고 이들 또한 도전 후의 참된 보람을 느낄 수 있을 것입니다.', inline=False) 
        embed.add_field(name='대담한 통솔자형에 속하는 유명인', value='스티브 잡스(애플 창시자), 프랭클린.D.루즈벨트, 짐 캐리, 말콤 X, 닥터 스트레인지(히어로)', inline=False) 
        await message.channel.send(channel,embed=embed) 
        
        
    if message.content.startswith("=ESFP"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [자유로운 영혼의 연예인]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '저는 ', value = '이기적이고 참을성도 없을 뿐 아니라, 약간의 열등감도 가지고 있어요. 실수투성이에 천방지축이고, 때때로 통제가 안되기도 하지요. 만일 이런 제가 감당이 안 되는 당신이라면 완벽한 모습일 때의 저와 함께할 자격 또한 없어요.',inline = False)
        embed.add_field(name='갑자기 ', value='흥얼거리며 즉흥적으로 춤을 추기 시작하는 누군가가 있다면 이는 연예인형의 사람일 가능성이 큽니다. 이들은 순간의 흥분되는 감정이나 상황에 쉽게 빠져들며, 주위 사람들 역시 그런 느낌을 만끽하기를 원합니다. 다른 이들을 위로하고 용기를 북돋아 주는 데 이들보다 더 많은 시간과 에너지를 소비하는 사람 없을 겁니다. 더욱이나 다른 유형의 사람과는 비교도 안 될 만큼 거부할 수 없는 매력으로 말이죠.', inline=False)
        embed.add_field(name='나는 타고난 연예인', value='천부적으로 스타성 기질을 타고난 이들은 그들에게 쏟아지는 스포트라이트를 즐기며 어디를 가나 모든 곳이 이들에게는 무대입니다. 사실상 많은 배우가 이 성격 유형에 속하기도 합니다. 간혹 친구나 다른 이들과 어울릴 시 쇼맨십에 찬 모습을 보이기도 하는데, 썰렁한 유머를 던져 주의를 집중시키기도 하는 이들은 그들이 가는 곳곳마다 시끌벅적한 파티를 연상케 합니다. 매우 사교적인 성향의 이들은 단순한 것을 좋아하며, 좋은 사람들과 어울려 즐거운 시간을 갖는 것보다 세상에 더 큰 즐거움은 없다고 여깁니다.', inline=False)        
        embed.add_field(name = '단순히', value = '시끌벅적 요란함을 넘어 이들은 뛰어난 미적 감각 또한 가지고 있습니다. 외모를 가꾸는 데에서부터 치장하는 법, 그리고 집안을 예쁘게 꾸미는 인테리어 능력에 이르기까지 연예인형 사람은 남다른 미적 감각을 지니고 있습니다. 일단 무엇을 보는 순간 어떤 것이 아름답고 매력적인지를 알아차리는 심미안이 있으며, 주변을 독창적인 그들의 스타일에 맞추어 바꾸는 것을 좋아합니다. 연예인형 사람은 천성적으로 호기심이 많으며, 새로운 디자인이나 스타일을 찾아다니는 데 거부감이 전혀 없습니다.',inline = False)
        embed.add_field(name='자칫', value='그리 보이지 않을 수도 있지만 연예인형 사람은 세상이 자기 위주로만 돌아가지 않는다는 것 또한 잘 알고 있습니다. 뛰어난 관찰력으로 다른 사람의 감정에 주의를 기울이는 이들은 어려운 문제에 봉착한 이들이 가장 먼저 찾아와 고민을 털어놓는 사람이기도 합니다. 이 경우 이들은 고민을 털어놓는 이에게 따뜻한 위로와 지지를 보내며 실질적인 조언 또한 잊지 않습니다. 하지만 반대로 문제를 겪고 있는 당사자가 본인인 경우 문제를 직면하여 해결하려 하기보다는 문제 자체를 아예 피하고 싶어 합니다. 대개 소소한 인생의 굴곡이나 어려움은 즐기는 한편, 만일 자신이 비난의 중심이 되는 경우라면 얘기가 달라집니다.', inline=False)
        embed.add_field(name='난 잘났으니까요..!', value='연예인형 사람이 가진 가장 큰 단점 중 하나는 이들이 종종 즉각적인 즐거움에 심취해 정작 이들의 안락한 삶 영위를 가능케 하는 의무나 책임은 회피한다는 것입니다. 이를 깨닫게 하기 위한 난해한 분석 자료나 반복적인 업무 혹은 이와 관련한 통계 자료는 이들에게는 무용지물입니다. 차라리 이들은 인생을 기회나 운에 맡기거나, 그렇지 않으면 친구에게 도움을 구합니다. 연예인형 사람에게는 일일 당분 섭취량이나 노후 계획과 같이 장기적인 안목으로 꼼꼼히 계획을 세워 인생을 설계해 나가는 것이 중요합니다. 곁에서 언제까지나 이를 맡아 책임져 줄 사람이나 친구가 항상 곁에 있는 것은 아니니까요.', inline=False)   
        embed.add_field(name='이들은', value='또한 그들 자신이 가진 가치나 자질을 잘 알고 있는데 이는 그 자체로는 별문제가 없습니다. 다만 계획을 세우는 데는 빵점인 이들의 성향으로 인해 씀씀이가 이들이 경제적으로 충당할 수 있는 범위를 넘어서는 경우가 종종 있는데, 특히 신용 카드의 무분별한 사용은 이들에게 매우 위험할 수 있습니다. 거시적인 안목으로 장기 목표를 세우는 것이 아닌 틈틈이 기회나 상황만 엿보는 이들은 그들의 경제적 부주의 함으로 인해 하고 싶어 하는 활동이나 삶을 영위하는 데 있어 제한이 따름을 알아차리게 될 것입니다.', inline=False)          
        embed.add_field(name='어쩔 수 없는 상황', value='때문에 어디에 콕 박혀 친구나 사람들과 어울리지 못하는 자신을 발견하는 것만큼 이들을 더 속상하게 하는 게 없습니다.', inline=False) 
        embed.add_field(name='연예인형 사람은', value='웃음과 오락, 그리고 새로운 즐거움을 추구하는 곳이라면 어디를 가나 두 팔 벌려 환영받습니다. 이들에게 있어 다른 사람들과 함께 신나게 즐기는 것만큼 유쾌한 일도 없을 테니 말입니다. 이들은 또한 그들이 아끼는 사람들과 희로애락을 함께하며 주제와 상관없이 몇 시간이고 수다를 떨기도 합니다. 물론 대화를 나누기에 적당한 주제여야 하겠지만요. 그저 이들이 미래 계획만 철저히 잘 설계해 놓는다면 이들은 세상에서 누릴 수 있는 온갖 즐거움과 재미를 경험하며 살 수 있을 것입니다. 주변에 있는 사람들과 더불어 말입니다.', inline=False) 
        embed.add_field(name='자유로운 영혼의 연예인형에 속하는 유명인', value='마랄린 먼로, 아담 리바인, 캡틴 마블(히어로), 툭 집안 페레그린(반지의제왕), 잭 도슨(타이타닉 남주)', inline=False) 
        await message.channel.send(channel,embed=embed) 
        
        
    if message.content.startswith("=ESFJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [사교적인 외교관]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '서로 ', value = '용기를 북돋아 주고 치켜세우며 힘이 돼주세요. 한 사람이 받은 긍정의 에너지가 곧 모든 이에게 전달될 테니까요.',inline = False)
        embed.add_field(name='사교형 사람을', value='한마디로 정의 내리기는 어렵지만, 간단히 표현하자면 이들은 [인기쟁이]입니다. 인구의 대략 12%를 차지하는 꽤 보편적인 성격 유형으로, 이를 미루어 보면 왜 이 유형의 사람이 인기가 많은지 이해가 갑니다. 종종 고등학교에서 치어리더나 풋볼의 쿼터백으로 활동하기도 하는 이들은 분위기를 좌지우지하며 여러 사람의 스포트라이트를 받거나 학교에 승리와 명예를 불러오도록 팀을 이끄는 역할을 하기도 합니다. 이들은 또한 훗날 다양한 사교 모임이나 어울림을 통해 주위 사람들에게 끊임없는 관심과 애정을 보임으로써 다른 이들을 행복하고 즐겁게 해주고자 노력합니다.', inline=False)
        embed.add_field(name='천성적으로', value='사교적인 성향인 이들은 가까운 친구나 지인들의 일거수일투족을 모두 알기를 원합니다. 과학 이론이나 국제 정치와 같은 대화 주제는 사교형 사람의 관심을 오래 잡아두지 못합니다. 대신 이들은 패션이나 외모, 그리고 그들을 포함하여 다른 사람의 사회적 지위와 같은 대화 소재에 더 많은 관심을 보입니다. 실생활 이야기나 가십거리가 이들에게는 한 마디로 빵과 버터 같은 대화 소재입니다. 하지만 좋은 일을 하는 데에는 그들이 가진 힘과 지위를 이용해 발 벗고 나서기도 합니다.', inline=False)        
        embed.add_field(name = '지혜로운 리더를 위한 우러름', value = '이타주의자인 사교형 사람은 다른 이들을 도우며 옳은 일을 하고자 하는 일에 진지한 태도로 임합니다. 다만 다른 성격 유형과 달리 사교형 사람은 도덕적 잣대를 철학이나 미신이 아닌 이미 수립된 법이나 사회 질서 체제 안에서 찾습니다. 사교형 사람은 사회는 다양한 배경과 관점을 가진 사람들의 집합체로 그들이 믿고 따르는 것만이 절대적인 진리가 아니라는 것을 명심할 필요가 있습니다.',inline = False)
        embed.add_field(name='사교형 사람은', value='그들 자신이 진심으로 존경받고 그들의 가치를 인정받고 있다고 생각이 드는 한은 지위를 막론하고 어떻게든 의미 있는 방식으로 다른 이에게 도움이 되고자 합니다. 이는 특히 가정 내에서 여실히 드러나는데, 이들은 집에서는 가정적인 배우자이자 헌신적인 부모이기도 합니다. 또한 계급 체계를 선호하는 경향이 있으며, 가정에서나 회사에서 그들의 주장을 펼 수 있는 동시에 안정된 생활 영위를 위해 어느 정도의 사회적 지위와 권력을 갖고자 합니다.', inline=False)
        embed.add_field(name='조화로운 인간관계', value='타인에 대한 지원을 아끼지 않는 활발한 성격인 이들은 어느 모임을 가든지 한두 명은 쉽게 만날 수 있습니다. 어떻게 해서든지 사람들과 만나 수다 떨며 웃는 시간을 만들고야 마는 이들이니까요! 그렇다고 이들을 단순히 웃고 지나쳐 버리는 가벼운 만남으로 치부해서는 안 됩니다. 이들이 아니면 누구도 대신하지 못하는 심오한 역할을 하기도 하는 이들이니까요. 사교형 사람은 친구나 지인의 인간관계나 일상생활과 관련한 이야기에 관심 있게 들으며 세세한 사항마저 기억하는 경향이 있습니다. 그리고는 도움이 필요한 적절한 순간에 진심 어린 따뜻한 마음으로 대화 상대가 되어줄 만발의 준비를 하고 있습니다. 만약 상황이 생각하는 안 좋게 돌아가거나 모임 내 긴장감이 조성되는 경우 이들은 이를 금세 알아차려 사람들 간에 화해와 안정을 찾기 위해 노력합니다.', inline=False)   
        embed.add_field(name='충돌을 싫어하는 사교형 사람은', value=' 사회적 위계질서를 확립하는 데 많은 에너지를 소모하며, 사전에 계획되지 않은 즉흥적인 만남이나 모임을 계획하는 것을 좋아합니다. 이들은 그들이 주관하는 모임을 위해 많은 시간과 노력을 들이는데, 만일 이들의 제안이 거부당하거나 이들의 계획이 사람들의 관심이나 이목을 충분히 끌지 못하면 상처를 받기도 합니다. 앞서 얘기했듯, 사교형 사람은 각각의 사람이 모두 다른 배경과 성격을 가지고 있으며, 이는 단순히 그가 주최하는 모임이나 활동 혹은 그들에게 관심이 없어서가 아니라 다만 모임 자체에 특별히 흥미를 느끼지 못해서 임을 깨닫는 것이 중요합니다.', inline=False)          
        embed.add_field(name='사교형 사람이', value='감내하기 힘들어하는 것 중 하나가 자신의 예민하고 쉽게 상처받는 성격과 타협점을 찾는 일입니다. 사람들이 그의 생각에 동의하지 않거나 되려 이들을 비판하는 경우가 생기면 어김없이 상처를 받는데, 이 역시도 인생의 한 부분입니다. 이를 해결할 수 있는 좋은 방법은 자신들이 가장 자신 있게 잘하는 일에 열중하는 것으로, 타인에게 좋은 역할 모델이 되어주거나 그들이 영향력을 행사할 수 있는 영역 안에서 권력을 행사하는 것입니다. 결과적으로 이러한 이들의 노고는 많은 사람에게 본보기가 되어 많은 이들로부터 존경과 감사를 받게 될 것입니다.', inline=False) 
        embed.add_field(name='사교적인 외교관형에 속하는 유명인', value='테일러 스위프트, 빌 클린턴, 제니퍼 로페즈, 산사 스타크(왕좌의게임), ', inline=False) 
        await message.channel.send(channel,embed=embed) 
        
        
    if message.content.startswith("=ESTP"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [모험을 즐기는 사업가]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '인생은', value = '과감한 모험이거나, 아니면 아무것도 아니다.',inline = False)
        embed.add_field(name='주변에', value='지대한 영향을 주는 사업가형 사람은 여러 사람이 모인 행사에서 이 자리 저 자리 휙휙 옮겨 다니는 무리 중에서 어렵지 않게 찾아볼 수 있습니다. 직설적이면서도 친근한 농담으로 주변 사람을 웃게 만드는 이들은 주변의 이목을 끄는 것을 좋아합니다. 만일 관객 중 무대에 올라올 사람을 호명하는 경우, 이들은 제일 먼저 자발적으로 손을 들거나 아니면 쑥스러워하는 친구를 대신하여 망설임 없이 무대에 올라서기도 합니다.', inline=False)
        embed.add_field(name='국제사회 이슈나', value='이와 관련한 복잡하고 난해한 이론과 관련한 담화는 이들의 관심을 오래 붙잡아 두지 못합니다. 사업가형 사람은 넘치는 에너지와 어느 정도의 지식으로 대화에 무리 없이 참여하기는 하나, 이들이 더 역점을 두는 것은 앉아서 말로만 하는 논의가 아닌 직접 나가 몸으로 부딪히는 것입니다. 행동이 먼저 앞서기도 하는 이들은 이로 인해 가끔 실수를 범하기도 하지만 이들은 단순히 턱 괴고 앉아 지켜만 보고 있느니 만약의 사태를 대비해 만반의 준비를 한 뒤라면 직접 나가 몸으로 부딪혀 문제를 해결해 나가는 것을 선호합니다.', inline=False)        
        embed.add_field(name = '혼동하지 말아야 할 단어, [움직임] vs [행동]', value = '사업가형 사람은 다른 성격 유형과 비교하여 위험을 수반하는 행동을 많이 하는 경향이 있는데, 이들은 마치 폭풍을 몰고 다니는 이들과도 같습니다. 달든 쓰든 인생이 주는 삶의 다양한 맛과 열정으로 인생을 즐기기는 하지만, 이는 단순히 감정적으로 느껴지는 전율 때문이 아니라 그들의 이성적인 사고관에 짜릿한 자극을 주기 때문입니다. 불기둥이 소용돌이치는듯한 절체절명의 상황에서도 이들은 사실이나 현실에 근거하여 이성적으로 결정을 내리는 경향이 있습니다.',inline = False)
        embed.add_field(name='이러한 성향 때문에', value='사업가형 사람은 학교와 같은 엄격한 규율이나 질서를 요구하는 조직 내에서 종종 어려움을 토로하기도 합니다. 이는 이들이 공부를 못하는 똑똑하지 못한 학생이어서가 아니라 딱딱하고 엄격한 가르침 방식이 그들이 선호하는 체험을 통한 배움과는 거리가 멀기 때문입니다. 지루하게만 보일지 모르는 이 과정 역시 목적지에 이르기 위한 필수 요소임을 깨닫게 하기까지는 이들의 많은 내적 성숙함을 요구합니다. 하지만 또 한편으로 이는 더 넓고 흥미로운 세계를 향한 기회로 작용하기도 합니다.', inline=False)
        embed.add_field(name='이들에게', value='달린 또 다른 도전 과제는 이들은 타인이 아닌 그들 스스로 정한 도덕적 잣대에 따라 사고하고 행동한다는 점입니다. [규칙은 깨라고 있는 법!] 아마도 일선 고등학교 교사나 기업 내 관리자는 이러한 이들의 성향을 묘사하는 말에 공감을 표할 것입니다. 하지만 한 가지 잊지 말아야 할 것은 이들이 문제를 야기하는 행동을 줄이고 그들의 에너지를 긍정적인 방향으로 활용하며, 지루해하는 일을 잘 참고 묵묵히 해낸다면 이들은 우리 사회에 없어서는 안 될 중요한 구성원이라는 점입니다.', inline=False)   
        embed.add_field(name='타인을 위한 세심한 배려', value='다른 성격 유형과 비교하여 가장 예리하면서 여과 없이 사물을 있는 그대로 관찰하는 사업가형 사람은 타인의 작은 변화조차도 정확히 집어냅니다. 다른 사람의 얼굴에 나타나는 작은 표정 변화나 평소 입고 다니는 옷 스타일 혹은 습관에의 변화 등 다른 성격 유형의 사람은 사소한 것 하나만 집어내도 다행으로 여길 만한 작은 변화조차도 이들은 그 뒤에 숨은 의미나 생각을 곧잘 포착해냅니다. 일단 무언가 이전과 다름을 감지하면 이들은 타인의 감정을 많이 고려하지 않은 채 이것저것 물어보고 싶어 합니다. 하지만 모든 사람이 그들의 결정이나 비밀을 동네방네 떠들고 다니고 싶어 하지 않을 수도 있음을 명심해야 합니다.', inline=False)          
        embed.add_field(name='사업가형 사람의', value='이러한 즉각적이며 예리한 관찰력과 행동력은 종종 대기업, 특히 급박한 상황에서는 더욱 요구되는 자질이기도 합니다', inline=False) 
        embed.add_field(name='다만', value='자칫 잘못하면 상황에 너무 몰두하여 예민한 사람의 감정에 치명적인 상처를 입히거나 원치 않는 상황을 초래할 수 있으며, 심지어는 본인 자신의 건강이나 안전을 해하는 경우도 있습니다. 인구의 대략 4%인 이들은 적당히 도전적이며 경쟁적인 사회를 이루기에 딱 알맞은 비율입니다. 사회 정의 질서를 무너뜨리지 않는 내에서 말입니다.', inline=False) 
        embed.add_field(name='기본적으로', value='열정과 활력이 넘치는 사업가형 사람은 방해 요소가 생기면 이성적 사고로 중무장합니다. 충만한 영감과 설득력, 그리고 다양한 성격을 가지고 팀을 이끄는 타고난 리더형인 이들은 아직 개척되지 않은 세계로 다른 이들을 인도함으로써 그들이 가는 곳곳 인생의 즐거움과 흥미로움을 더합니다. 다만 이러한 장점을 보다 효율적이며 가치 있는 성향으로 탈바꿈하는 것이 가장 큰 숙제로 남아있기는 하지만 말입니다.', inline=False)        
        embed.add_field(name='모험을 즐기는 사업가형에 속하는 유명인', value='어니스트 해밍웨이, 잭 니콜슨, 마돈나, 브루스 윌리스, 사무엘.L.잭슨(한국에서는 쉴드의 닉 퓨리 국장으로 유명함), 로켓(가디언즈 오브 갤럭시), 앤트맨(히어로)', inline=False) 
        await message.channel.send(channel,embed=embed) 
        
        
    if message.content.startswith("=ISFP"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [호기심 많은 예술가]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '저는', value = '하루 동안에도 변화를 거듭합니다. 아침에 눈을 뜨면 한 사람이 있습니다. 그리고 잠을 청하러 갈 때면 저는 확신합니다. 거기엔 또 다른 제 자신이 있다는 것을 말이죠.',inline = False)
        embed.add_field(name='모험가형 사람은', value='일반적으로 사람들이 생각하듯 야외에서 앙증맞은 나무 그림을 그리고 있는 그런 유형의 예술가는 아니지만, 진정한 예술가라고 할 수 있습니다. 실상 상당수 많은 이들이 그러한 능력을 충분히 갖추고 있기도 합니다. 이들은 그들의 심미안이나 디자인 감각, 심지어는 그들의 선택이나 행위를 통하여 사회적 관습이라는 한계를 뛰어넘고자 합니다. 실험적인 아름다움이나 행위를 통해 전통적으로 기대되는 행동양식이나 관습에 도전장을 내미는 이들은 "저를 가두어두려 하지 마세요!"라고 수없이 외칩니다.', inline=False)
        embed.add_field(name='자기 자신에 대한 만족', value='이들은 다양한 아이디어나 사람들로부터 영감을 받아 다채로우면서도 감각적인 삶을 살아갑니다. 그들이 받은 영감을 본인만의 시각으로 재해석하여 새로운 것을 발견하고 탐험함으로써 즐거움을 느끼기도 하는 이들은 그 어떤 유형의 사람보다 탐험이나 실험 정신이 뛰어납니다. 어디로 튈지 모르는 즉흥적인 성향으로 간혹 이들을 예측하는 것이 어려운데, 이는 가까운 친구나 사랑하는 사람들 역시 예외가 아닙니다.', inline=False)        
        embed.add_field(name = '그럼에도 불구하고', value = '단연 내향적 성향을 가지고 있는 모험가형 사람들은 스포트라이트를 벗어나 재충전을 위해 혼자만의 시간을 갖곤 하는데, 이는 주위 사람들은 한번 더 놀라게 하기도 합니다. 하지만 이들이 혼자 있다고 게으르게 넋 놓고 앉아 있는 것은 아닙니다. 이 시간은 그들이 가진 원리원칙을 재고하는 자기 성찰을 위한 시간으로, 과거나 미래에 집착하지 않고 순전히 그들이 누구인지 자신을 들여다보는 시간입니다. 그리고는 이들은 곧 언제 그랬냐는 듯이 사람들 앞에 변화된 모습으로 [짠]하고 나타납니다.',inline = False)
        embed.add_field(name='넘치는', value='열정을 쏟아부으며 정열적인 삶을 살아가는 모험가형 사람은 다른 유형의 사람들에 비해 도박이나 익스트림 스포츠와 같이 위험성이 내재한 활동을 즐기는 경향이 있습니다. 그나마 다행인 것은 환경이나 상황 조율 능력이 뛰어나 대부분의 사람보다 소질이 있다는 것입니다. 다른 이들과 어울리는 것을 좋아하기도 하는 이들은 거부할 수 없는 그들만의 매력을 가지고 있습니다.', inline=False)
        embed.add_field(name='모험가형 사람들은', value='타인의 작은 칭찬에도 쉽게 자극받아 무책임하고 무모한 행동을 일삼을 수 있다는 것을 그들 자신 역시 잘 알고 있습니다.', inline=False)   
        embed.add_field(name='반대로', value='이들이 누군가로부터 비판을 받을 경우, 상황을 안 좋게 몰고 갈 수도 있습니다. 타인의 적절한 비판은 오히려 다른 관점으로 받아들여 새로운 방안을 모색하는 가치 있는 용도로 활용하기도 하는 반면, 신랄하거나 진중치 못한 비판은 자칫하면 모험가 사람을 욱하게 만들어 이들의 분노가 그리 아름답지만은 않은 모습으로 표출될 수도 있습니다.', inline=False)          
        embed.add_field(name='모험가형 사람은', value='타인의 감정을 잘 살피며 조화를 중요시 여깁니다. 이 때문에 비난이나 비판을 받는 경우, 화가 어느 정도 누그러질 때까지 기다리는 것이 이들에게는 쉽지 않은 일입니다. 하지만 좋은 일이건 나쁜 일이건 영원히 지속되는 것은 없듯이 일단 분노의 감정이 수그러들면 이들은 과거는 과거일 뿐이라고 치부하며 마치 아무 일도 없었다는 듯이 다시금 그들의 삶을 살아갑니다.', inline=False) 
        embed.add_field(name='작은 것 하나하나가 인생의 의미', value='이 성격 유형에 속하는 사람이 가장 어려워하는 것 중 하나가 미래를 설계하는 일입니다. 더 나은 미래를 위해 목표를 설정하고 이를 달성케 하는 건설적인 이상향을 찾는다는 게 그리 생각만큼 간단한 일이 아닙니다. 다른 유형의 사람들이 미래를 구체적인 자산이나 은퇴 계획이라는 틀 안에서 세우는 반면, 모험가형 사람은 주식과 같은 자산이 아닌 다양한 경험을 통해 자아를 찾기 위한 행동 계획을 세우는 데에 더 많은 투자를 하는 경향이 있습니다.', inline=False) 
        embed.add_field(name='만약', value='이러한 목표나 믿음이 순수함에서 기인한 것이라면 이들은 누구보다도 사심 없는 마음으로 선행을 실천할 것입니다. 하지만 이는 반대로 말하면 누구보다도 자기중심적이며 속임수를 일삼으며 자기애에 사로잡혀 행동하는 이들로 비추어질 수도 있음을 의미합니다. 모험가형 사람은 그들이 하고자 하는 대로 그냥 내버려 두는 것이 가장 현명한 방법입니다. 물론 새로운 취미를 발견하고 실행하는 것이 생각처럼 쉬운 일은 아니지만, 하루하루 서두르지 않고 원하는 것이 무엇인지 곰곰이 생각하고 되새겨 본다면, 그것이 무엇이 되었든 모험가형 사람이 진정 좋아하는 것이 무엇인지 찾게 될 것입니다.', inline=False)      
        embed.add_field(name='호기심 많은 예술가형에 속하는 유명인', value='브리트니 스피어즈, 마이클 잭슨, ', inline=False) 
        await message.channel.send(channel,embed=embed) 
        
        
    if message.content.startswith("=INTJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [용의주도한 전략가]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '윗자리에 있는 사람은', value = '고독한 법, 전략적 사고에 뛰어나며 매우 극소수인 건축가형 사람은 이를 누구보다 뼈저리게 이해합니다. 전체 인구의 2%에 해당하는 이들은 유독 여성에게서는 더욱 찾아보기 힘든 유형으로, 인구의 단 0.8%를 차지합니다. 체스를 두는 듯한 정확하고 계산된 움직임과 풍부한 지식을 소유하고 있는 이들은 그들과 견줄 만한 비슷한 부류의 사람을 찾는 데 종종 어려움을 겪습니다. 건축가형 사람은 상상력이 풍부하면서도 결단력이 있으며, 야망이 있지만 대외적으로 표현하지 않으며, 놀랄 만큼 호기심이 많지만 쓸데없는 데 에너지를 낭비하는 법이 없습니다.',inline = False)
        embed.add_field(name='올곧은 태도로 계획 달성을 향한 돌진', value='이들의 지식을 향한 갈증은 어릴 적부터 두드러지게 나타나는데, 때문에 건축가형 사람은 어릴 때 [책벌레]라는 소리를 자주 듣습니다. 대개 친구들 사이에서는 놀림의 표현임에도 불구하고 전혀 개의치 않아 하며, 오히려 깊고 넓은 지식을 가지고 있는 그들 자신에게 남다른 자부심을 느낍니다. 이들은 또한 관심 있는 특정 분야에 대한 그들의 방대한 지식을 다른 이들과 공유하고 싶어 하기도 합니다. 반면, 일명 가십거리와 같이 별 볼 일 없는 주제에 대한 잡담거리보다는 그들 나름의 분야에서 용의주도하게 전략을 세우거나 이를 실행해 옮기는 일을 선호합니다.', inline=False)
        embed.add_field(name='당신은', value='의견을 가질 권리가 없습니다. 다만 제대로 된 의견을 가질 권리만 있을 뿐이죠. 그 누구도 무식할 권리는 없기 때문입니다.', inline=False)        
        embed.add_field(name = '대부분', value = '사람 누가 봐도 이들은 지극히 모순적인 삶을 살아가는 것처럼 보이지만 이를 객관적이고 이성적으로 놓고 보면 사실 이해가 가기도 합니다. 예를 들면, 이들은 비현실적일 만큼 이상주의자이자인 동시에 매우 신랄한 조롱과 비판을 일삼는 냉소주의자로 이 둘이 같이 공존한다는 것 자체가 불가능해 보입니다. 또한, 기본적으로 지혜와 노력, 그리고 신중함만 있으며 못할 것이 없다고 믿는 한편, 사람들이 실질적으로 그러한 성취를 끌어내는 데 있어서는 게으르고 근시안적이며 자기 잇속만 차린다고 생각합니다. 그렇다고 이러한 냉소적인 태도가 성취하고자 하는 이들의 욕구를 꺾지는 못합니다.',inline = False)
        embed.add_field(name='돌부처와 같은 원칙주의자', value='확신에 찬 자신감과 함부로 범접할 수 없는 신비로운 아우라를 발산하는 건축가형 사람은 통찰력과 관찰력, 기발한 아이디어, 그리고 뛰어난 논리력에 강한 의지와 인격이 합쳐져 변화를 이끄는 데 앞장섭니다. 이따금 이들이 생각했던 아이디어나 계획을 뒤집고 재수립하는 과정을 거쳐 완벽함을 추구하고자 하거나 도덕적 잣대에 따라 재정비하는 시간을 가지기도 합니다. 건축가형 사람의 업무 스타일을 좇아오지 못하거나 심지어는 이들이 왜 그렇게 행동하는지 전혀 감을 잡지 못하는 사람은 단번에 신임을 잃거나 이들의 인정을 받지 못할 수도 있습니다.', inline=False)
        embed.add_field(name='건축가형', value='사람이 몸서리치게 싫어하는 것이 있다면 바로 질서, 한계, 그리고 전통과 같은 것들인데, 이들은 세상의 모든 것을 탐구와 발견의 대상으로 여기기 때문입니다. 만일 문제 해결을 위한 방안을 찾은 경우, 간혹 무모할 수 있으나 기술적으로 뛰어나며 언제나 그렇듯 비정통적인 기발한 방법이나 아이디어를 수립하기 위해 홀로 행동에 옮깁니다', inline=False)   
        embed.add_field(name='그렇다고', value='이들이 충동적이라는 말은 아닙니다. 얼마나 간절히 성취하기를 원하는지 상관없이 건축가형 사람은 기본적으로 이성적인 사고를 합니다. 내부에서 비롯되었든 아니면 외부 세계에서 기인하였든지, 매사 이들의 아이디어는 “실현 가능할까?”와 같은 ‘이성적 사고’라는 필터의 과정을 거칩니다. 이는 사람 혹은 아이디어에 항시 적용되는 기제로, 이 때문에 건축가형 사람은 종종 곤경에 빠지기도 합니다.', inline=False)          
        embed.add_field(name='홀로 떠나는 여행, 깨달음의 시간', value='오랜 시간 방대한 지식을 쌓아 온 똑똑하고 자신감 넘치는 이들이지만, 인간관계만큼은 이들이 자신 있어 하는 분야가 아닙니다. 진리나 깊이 있는 지식을 좇는 이들에게 선의의 거짓말이나 가벼운 잡담은 그저 낯설기만 합니다. 그럼에도 불구하고 자신을 필요 이상으로 내몰아 부조리투성이인 사회적 관습을 경험하기도 합니다. 가장 좋은 것은 이들이 그들 자신 자체로 온전히 있을 수 있는 곳, 즉 스포트라이트 밖에 있는 것입니다. 건축가형 사람은 익숙하고 편안한 곳에서 본연의 모습으로 있을 때 비로소 연인 관계나 그 외 여러 상황에서 그들 나름의 빛을 발하며 사람들을 끌어들이기 때문입니다.', inline=False) 
        embed.add_field(name='건축가형', value='사람의 성향을 정의하자면 이들은 인생을 마치 체스를 두듯이 새로운 계획이나 전술, 그리고 대책을 세워가며 상대방 머리 위에서 수를 두며 허를 찌르는 기술로 상황을 유리하게 몰고 가는 듯한 삶을 살아갑니다. 그렇다고 이들이 양심 없는 삶을 살아간다는 말은 아닙니다. 다만 감정에 치우치는 것을 싫어하는 이들의 성격상 타인의 눈에 그렇게 비추어질 수 있습니다. 이를 고려하면 왜 많은 허구 속 등장인물들(종종 오해를 받곤 하는 영화 속 영웅들)이 본 성격 유형으로 묘사되는지 이해할 수 있을 것입니다.', inline=False) 
        embed.add_field(name='용의주도한 전략가형에 속하는 유명인', value='미카엘라 오바마, 엘론 머스크, 크리스토퍼 놀란, 블라디미르 푸틴, 아놀드 슈워츠네거, 회색의 간달프/백색의 간달프(반지의제왕)   ', inline=False) 
        await message.channel.send(channel,embed=embed) 

    if message.content.startswith("=ISTP"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [만능 재주꾼]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '저는', value = '그런 삶을 살고 싶었습니다. 무언가 다른 삶 말이지요. 매일 같은 곳을 가고, 같은 사람을 만나고, 매번 같은 일을 하며 살고 싶지 않았습니다. 전 흥미로운 도전을 원했습니다.',inline = False)
        embed.add_field(name='냉철한', value='이성주의적 성향과 왕성한 호기심을 가진 만능재주꾼형 사람은 직접 손으로 만지고 눈으로 보면서 주변 세상을 탐색하는 것을 좋아합니다. 무엇을 만드는 데 타고난 재능을 가진 이들은 하나가 완성되면 또 다른 과제로 옮겨 다니는 등 실생활에 유용하면서도 자질구레한 것들을 취미 삼아 만드는 것을 좋아하는데, 그러면서 새로운 기술을 하나하나 터득해 나갑니다. 종종 기술자나 엔지니어이기도 한 이들에게 있어 소매를 걷어붙이고 작업에 뛰어들어 직접 분해하고 조립할 때보다 세상에 즐거운 일이 또 없을 것입니다. 전보다 조금은 더 향상된 모습으로요.', inline=False)
        embed.add_field(name='만능재주꾼형 사람은', value='창조와 문제 해결을 위한 이해, 그리고 실행 착오와 실질적인 경험을 통해 아이디어를 탐색합니다. 다른 이들이 그들의 과제에 흥미를 보이는 것을 좋아하며, 간혹 다른 이들로 하여금 작업 중인 과제에 참여하도록 유도하기도 합니다. 단, 그들만의 원리원칙이나 자유를 침범하지 않는 범위에 한해서 말이죠. 사람들은 만능재주꾼형 사람이 베푸는 호의에 열린 마음으로 대할 필요가 있습니다.', inline=False)        
        embed.add_field(name = '타인을', value = '잘 도우며 그들의 경험을 다른 이들과 공유하는 것을 좋아하기도 하는 이들은 특히나 그들이 아끼는 사람일수록 더욱 그러합니다. 이들이 인구의 고작 5%만이 차지하지 않는다는 사실이 그저 안타까울 따름입니다. 더욱이 여성의 경우는 더욱 흔치 않은데, 대개 이 성향의 여성은 사회가 일반적으로 요구하는 이상적인 여성상에 들어맞지 않는 경우가 많으며, 이들은 자라면서 말괄량이 소리를 듣기도 합니다.',inline = False)
        embed.add_field(name='기꺼이 다름을 지향하다', value='내성적인 성향으로 현실적인 사안에 관심이 많은 이들은 얼핏 보면 단순해 보일 수 있지만, 사실 알고 보면 꽤 복잡한 성향을 가지고 있습니다. 친절하고 상냥하지만 사생활을 중요시 여기며, 침착하면서도 금세 즉흥적인 성향으로 돌변하기도 하며, 호기심이 많으면서도 오래 앉아 수업을 들을 때는 집중하지 못하는 모습을 보이기도 합니다. 이로 인해 주변 가까운 친구나 아끼는 사람들조차 이들의 행동을 예측하는 데 어려움을 겪습니다. 만능재주꾼형 사람은 한동안 헌신적이고 꾸준한 모습을 보이다가도 충동의 에너지를 서서히 쌓아두고 있다가 어느 순간 예고 없이 터뜨리기도 하는데, 이로 인해 관심사가 이전과 전혀 다른 방향으로 바뀌기도 합니다.', inline=False)
        embed.add_field(name='미래를', value='대비한 비전 수립은커녕 이렇듯 휘몰아치는 변화가 있을 때조차 새로 발견한 관심사의 실행 가능 여부에는 크게 관심을 두지 않습니다.', inline=False)   
        embed.add_field(name='실질적으로', value='현실에 근거하여 결정을 내리면서도 마음 한가운데에는 [자신이 대접받고 싶은 만큼 다른 이를 대접하라]와 같은 공정함이라는 사고방식이 깊이 박혀있는데, 이는 이들만의 성격적 고유 특성을 잘 설명해 줍니다. 남에게 발을 밟히지 않으려고 아예 발부터 먼저 빼고 보는 이들은 너무 지나치리만치 신중하게 행동하여 종종 필요 이상으로 멀리 가기도 합니다. 이들은 기본적으로 옳든 그르든 자신이 받은 만큼 똑같이 되돌려주는 것이 공정한 행위라고 생각합니다.', inline=False)          
        embed.add_field(name='만능재주꾼형 사람이', value='당면한 가장 큰 과제는 천성적으로 타인에게 관심이 많은 이들의 성격으로 하여금 다른 이들 역시 그들과 같을 것이라는 착각하에 행동이 먼저 앞선다는 점입니다. 신중치 못한 농담을 먼저 꺼내는 이들을 보면 영락없이 만능재주꾼형 사람입니다. 또한, 타인의 일에 지나치리만치 간섭하여 여기저기 시끄럽게 휘둘리다가 다른 흥미로운 관심거리가 생기면 재빨리 계획을 변경하기도 합니다.', inline=False) 
        embed.add_field(name='남과 다름의 즐거움', value='만능재주꾼형 사람은 다른 성격 유형의 사람들이 사회에서 수용 가능한 질서나 행위와 같은 비교적 확고하게 구분된 그들 나름의 선이 있다는 것을 깨닫게 될 것입니다. 이들보다 예민한 성향의 사람은 타인의 마음을 헤아리지 않는 가벼운 농담 따위를 좋아하지 않습니다. 당연히 그러한 농담 자체를 던지지 않는 것은 두말할 필요도 없고요. 지나친 장난을 좋아하는 사람은 아무도 없으며, 이는 같이 어울리는 부류 사이에서도 마찬가지입니다. 이미 감정이 많이 상해 있는 상태에서 선을 넘어가는 경우 훗날 뒷감당하기 힘든 상황을 초래할 수 있기 때문입니다.', inline=False) 
        embed.add_field(name='타인의', value='감정을 파악하는 데 있어 애를 먹는 이들은 자신의 감정이나 동기조차 파악하지 못하는 이들의 천성과 공정함을 추구하고자 하는 성격에 그 이유가 기인한다고 할 수 있습니다. 게다가 인간관계 형성 시 타인을 향한 정서적 공감이 아닌 행동으로 탐색하고자 하는 성향이 있어 간혹 원치 않는 상황을 초래하기도 합니다. 사람들 간의 보이지 않는 선이나 규칙을 지키는 데 어려움을 호소하는 이들은 인간관계 시 자유롭게 그 경계를 넘나들기를 원하며, 혹 필요하면 이를 넘어 다른 색으로 물들이고 싶어 하기도 합니다.', inline=False)         
        embed.add_field(name='정의적이며', value='유머를 겸비한 동시에 실질적으로 문제 해결을 위해 무언가를 만들어 내는 만능재주꾼형 사람의 실용적인 접근 방식이 이들의 예측 불허한 성격이나 스타일을 이해하는 좋은 사람들과 합쳐져 일하는 환경이 조성된다면, 이들은 마치 물 만난 고기처럼 신이 나 몇 년이고 이것저것 유용한 장난감 거리를 만드는 재미에 흠뻑 빠져 살 수 있을 것입니다. 만인의 우러름을 받으면서 말입니다.', inline=False) 
        embed.add_field(name='엄격한 관리자형에 속하는 유명인', value='베어 그릴스, 마이클 조던, 클린트 이스트우드, 톰 크루즈, 아리야 스타크(왕좌의게임), 인디아나 존스, 호크아이(히어로), 제임스 본드,   ', inline=False) 
        await message.channel.send(channel,embed=embed) 

    if message.content.startswith("=ESTJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [엄격한 관리자]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '훌륭한', value = '질서는 모든 것의 기초이다.',inline = False)
        embed.add_field(name='관리자형', value='사람은 그들 생각에 반추하여 무엇이 옳고 그른지를 따져 사회나 가족을 하나로 단결시키기 위해 사회적으로 받아들여지는 통념이나 전통 등 필요한 질서를 정립하는 데 이바지하는 대표적인 유형입니다. 정직하고 헌신적이며 위풍당당한 이들은 비록 험난한 가시밭길이라도 조언을 통하여 그들이 옳다고 생각하는 길로 사람들을 인도합니다. 군중을 단결시키는 데에 일가견이 있기도 한 이들은 종종 사회에서 지역사회조직가와 같은 임무를 수행하며, 지역 사회 발전을 위한 축제나 행사에서부터 가족이나 사회를 하나로 결집하기 위한 사회 운동을 펼치는 데 사람들을 모으는 역할을 하기도 합니다.', inline=False)
        embed.add_field(name='옳다고 생각되는 일은 거침없이 밀고 나가는 굳은 의지!', value=' 특히 민주주의 사회에서 더욱 필요로 하는 이 유형의 사람은 인구의 대략 11%를 차지합니다. 전 세계 유명 비즈니스 리더나 정치인 중 상당수가 이 유형에 속하는 것이 어찌 보면 그리 놀랍지 만은 않을 것입니다. 법과 사회 질서의 중요함을 굳게 믿는 이들은 헌신과 공명정대한 삶을 통해 다른 이들에게 본보기가 되고자 하는데, 특히 업무적으로 게으르거나 부정을 저지르는 이들은 가차 없이 벌하기도 합니다. 만일 누군가 고되고 힘든 사회 운동을 자처하여 그들의 됨됨이를 증명해 보이고자 하는 이들이 있다면 이들은 바로 관리자형 사람일 것입니다.', inline=False)        
        embed.add_field(name = '이들은', value = '주변 상황을 잘 판단하여 명확하고 증명이 가능한 확실한 사실에 근거하여 사고하는 경향이 있습니다. 이리하여 만일 이들의 의견이나 결정 내린 사항이 심한 반대 의견에 부딪혔을 때 이들로 하여금 무엇이 가능하고 불가능한지를 정확히 판단하여 본연의 믿음이나 생각을 고수한 채 꿋꿋이 헤쳐나갈 수 있게 합니다. 말을 허투루 하지 않는 이들은 성취하기 어려운 고된 일도 마다치 않고 기꺼이 뛰어들어 구체적으로 실행 계획을 세워 난해해 보이는 일도 수월히 실행해 나갑니다.',inline = False)
        embed.add_field(name='이들은', value='또한 타인과 스스럼없이 잘 어울리며, 대화 시 단순한 논리나 사실에 입각한 딱딱한 대화가 아닌 따뜻하고 섬세한 언어를 사용하여 인간 대 인간으로 이야기를 나눕니다. 이로 인해 주변 가까운 친구나 동료는 이들을 사교성이 많은 사람으로 오해하기도 하지만, 사실 이들은 갑자기 물러서야 하는 상황이 생겼을 때 마음의 평정심을 잃지 않을 수 있도록 잠시 생각을 비우고 재충전할 수 있는 혼자만의 시간을 가지기를 원합니다. 선의의 옹호자형 사람은 다른 이들의 감정을 섬세히 잘 살피며, 다른 이들도 역시 마찬가지로 그렇게 해주기를 바랍니다. 이는 때로 이들이 단 며칠간만이라도 혼자 있을 수 있는 여유를 가지는 것을 의미하기도 합니다.', inline=False)
        embed.add_field(name='나아가', value='이들은 업무를 수행하는 데 있어 그들의 엄격한 가치관이 함께 일하는 다른 이들에게도 반영되기를 원합니다. 기본적으로 사람들과의 약속을 충실히 이행하는 이들의 기본 성향 때문에 함께 일하는 동업자나 부하의 무능력함, 태만, 심지어는 부정직함으로 이들을 시험에 들게 하는 경우 심한 불호령도 마다하지 않습니다. 이 때문에 종종 융통성 없는 성격으로 비추어지기도 하지만, 이는 이들의 성격이 외골수여서가 아니라 이것들이 건강한 사회 건설을 위하여 지켜져야 할 중요한 덕목이라고 굳게 믿기 때문입니다.', inline=False)   
        embed.add_field(name='부족함을 인정할 줄 아는 지혜', value='법질서를 준수하고 이웃을 도우며 지역 사회나 조직 발전을 위해 타인의 동참을 유도하는 관리자형 사람은 전형적인 모범시민이라고 할 수 있습니다.', inline=False)          
        embed.add_field(name='단,', value='이들이 명심해야 할 한 가지 사항은 모든 이들이 그들과 같은 노력을 기울이며 동일한 길을 가지는 않는다는 것입니다. 진정한 리더의 역할은 그룹 혹은 개개인의 장점을 잘 살펴 그들의 생각을 마음껏 펼칠 수 있도록 돕는 데 있습니다. 만일 이러한 이들의 노력이 선행된다면 모든 필요한 자질과 사실을 가지고 모든 이가 원하는 방향으로 이들을 통솔할 수 있을 것입니다.', inline=False) 
        embed.add_field(name='엄격한 관리자형에 속하는 유명인', value='존 D.록펠러, 프랭크 시나트라, 제임스 먼로, 보로미르(반지의제왕), 랍 스타크(왕좌의게임),  ', inline=False) 
        await message.channel.send(channel,embed=embed) 

    if message.content.startswith("=INFJ"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [선의의 옹호자]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '선의의 옹호자형은', value = '가장 흔치 않은 성격 유형으로 인구의 채 1%도 되지 않습니다. 그럼에도 불구하고 나름의 고유 성향으로 세상에서 그들만의 입지를 확고히 다집니다. 이들 안에는 깊이 내재한 이상향이나 도덕적 관념이 자리하고 있는데, 다른 외교형 사람과 다른 점은 이들은 단호함과 결단력이 있다는 것입니다. 바라는 이상향을 꿈꾸는데 절대 게으름 피우는 법이 없으며, 목적을 달성하고 지속적으로 긍정적인 영향을 미치고자 구체적으로 계획을 세워 이행해 나갑니다.',inline = False)
        embed.add_field(name='종종', value='구조 작업이나 자선 활동을 하는 곳에서 쉬이 볼 수 있는 이 유형의 사람은 다른 이들을 돕는 것을 인생의 목적으로 여깁니다. 특히나 이들은 문제를 야기하는 핵심 사안에 관심이 많은데, 이는 근본적인 문제를 해결함으로써 궁극적으로 어떠한 노력이나 도움 자체가 필요치 않기를 희망하는 이들의 순수한 열망 때문입니다.', inline=False)
        embed.add_field(name='서로 돕는 세상', value='선의의 옹호자형 사람은 진정 그들만의 고유한 성향을 내포하고 있습니다. 나긋나긋한 목소리 뒤에는 강직함이 숨어 있으며, 의견을 강력하게 피력할 줄 알며 옳다고 생각되는 일에는 지칠 줄 모르고 투쟁합니다. 강한 의지와 분별력이 있는 이들은 단순히 개인의 이득을 취하는 데 이를 활용하는 것이 아닌, 그들의 창의적인 상상력과 강한 신념, 그리고 특유의 섬세함으로 균형 이루는 세상을 만들고자 합니다. 평등주의나 인간의 업보(karma)와 같은 관념에 관심이 많은 이들은 세상에 해악을 끼치는 사람의 마음을 녹이는 데에는 진정한 사랑과 인간애보다 더 좋은 것은 없다고 믿습니다. ', inline=False)        
        embed.add_field(name = '모든', value = '인간은 창의적인 이타주의의 빛 속을 걸을 것인지, 아니면 파괴적인 이기주의의 노선을 걸을 것인지 중 하나를 선택해야 합니다.',inline = False)
        embed.add_field(name='이들은', value='또한 타인과 스스럼없이 잘 어울리며, 대화 시 단순한 논리나 사실에 입각한 딱딱한 대화가 아닌 따뜻하고 섬세한 언어를 사용하여 인간 대 인간으로 이야기를 나눕니다. 이로 인해 주변 가까운 친구나 동료는 이들을 사교성이 많은 사람으로 오해하기도 하지만, 사실 이들은 갑자기 물러서야 하는 상황이 생겼을 때 마음의 평정심을 잃지 않을 수 있도록 잠시 생각을 비우고 재충전할 수 있는 혼자만의 시간을 가지기를 원합니다. 선의의 옹호자형 사람은 다른 이들의 감정을 섬세히 잘 살피며, 다른 이들도 역시 마찬가지로 그렇게 해주기를 바랍니다. 이는 때로 이들이 단 며칠간만이라도 혼자 있을 수 있는 여유를 가지는 것을 의미하기도 합니다.', inline=False)
        embed.add_field(name='투쟁을 위해 한 박자 쉬어가는 여유', value='무엇보다도 선의의 옹호자형 사람은 자신을 챙기고 돌보는 일을 게을리하지 말아야 합니다. 비록 강한 신념에서 기인한 열정으로 어느 정도 그들이 가진 한계점을 넘어설 수는 있지만, 이러한 열망이 자신들이 감내할 수 있는 수준을 넘어서는 경우 이들은 쉬이 지치거나 극심한 스트레스를 호소하는 등 이들의 건강에 적신호가 켜질 수도 있습니다. 특히나 심한 반대나 갈등 상황이 조성되는 경우, 예민하고 섬세한 이들의 성격에 발동이 걸려 무슨 수를 써서라도 그들에게 가해지는 음모나 모함이라고 판단되는 상황과 맞서 싸우고자 합니다. 만일 상황이 여의치 않거나 피할 수 없는 상황이라면, 이들은 비상식적인 방법이나 옳지 않은 방식으로 투쟁을 벌이기도 합니다. ', inline=False)   
        embed.add_field(name='꼭 그렇지 않음', value='에도 불구하고 선의의 옹호자형 사람에게 있어 세상은 불평등과 불공정함이 난무하는 곳입니다. 크든 작든 세상의 잘못된 것을 바로잡고자 하는 데 이들보다 열심인 사람은 없을 것입니다. 다만 이들은 세상을 살피느라 분주한 자신 또한 잘 챙기고 살펴야 할 필요가 있음을 잊지 말아야 합니다.', inline=False)          
        embed.add_field(name='선의의 옹호자형에 속하는 유명인', value='마틴 루터 킹, 넬슨 만델라, 마더 테레사, 레이디 가가, 니콜 키드먼, 모건 프리만, 괴테, 아라고른(반지의제왕), 갈라드리엘(반지의제왕)', inline=False) 
        await message.channel.send(channel,embed=embed) 
        
    if message.content.startswith("=ENFP"):
        channel = message.channel
        embed = discord.Embed(
            title = '성격유형: [재기발랄한 활동가]  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name = '당신이', value = '생계를 위해 무슨 일을 하는지, 저는 관심 없습니다. 다만 제가 알고 싶은 건 당신이 가슴 저리게 동경하는 것이 있는지, 당신 마음속 깊은 바람을 감히 충족시키고자 하는 열망이 있는지입니다. 당신의 나이가 얼마인지는 중요하지 않습니다. 당신이 사랑을 위해, 당신의 꿈을 위해, 그리고 삶이라는 모험을 위해 기꺼이 바보가 될 준비가 되어 있는지, 그것이 궁금할 뿐입니다. ',inline = False)
        embed.add_field(name='활동가형', value='사람은 자유로운 사고의 소유자입니다. 종종 분위기 메이커 역할을 하기도 하는 이들은 단순한 인생의 즐거움이나 그때그때 상황에서 주는 일시적인 만족이 아닌 타인과 사회적, 정서적으로 깊은 유대 관계를 맺음으로써 행복을 느낍니다. 매력적이며 독립적인 성격으로 활발하면서도 인정이 많은 이들은 인구의 대략 7%에 속하며, 어느 모임을 가든 어렵지 않게 만날 수 있습니다. ', inline=False)
        embed.add_field(name='아이디어 하나로 세상을 바꾸다!', value='타인을 즐겁게 하는 사교적인 특성만이 이들이 가진 전부가 아닙니다. 활동가형 사람은 통찰력 있는 비전으로 호기심과 에너지 사이의 선을 명확히 구분합니다. 이들은 인생을 하나로 연결된 크고 복잡한 퍼즐로 보는 경향이 있는데, 인생을 체계적인 일련의 과정으로 보는 분석가형 사람과 달리 인간의 감정이나 인정(人情), 신비로움을 프리즘에 투영하여 그 안에 숨어있는 깊은 의미를 찾아내고자 합니다.  ', inline=False)        
        embed.add_field(name = '다소', value = '과하리만치 독립적인 성향의 이들은 안정적이거나 안전한 삶이 아닌 창의적이며 자유로운 삶을 갈망합니다.',inline = False)
        embed.add_field(name='다른', value='성격 유형에 속한 사람들은 활동가형 사람들에게서 거부할 수 없는 이들만의 매력을 느낄 수 있습니다. 일단 창의력에 발동이 걸리면 이들은 스포트라이트를 받는 주인공이 되어 동료나 사람들로부터 리더 혹은 전문가로 추앙받기도 합니다. 하지만 이는 독립적이며 자유를 최고로 여기는 활동가형 사람들이 선호하는 바는 아니며, 만일 반복적인 관리 업무를 요구하는 자리에 있는 경우라면 더욱이 그러합니다. 창의적인 문제 해결을 위한 대책을 찾는 데서 큰 자부심을 얻는 활동가형 사람에게 혁신적인 사고를 가능하게 하는 자유의지 여부가 매우 중요합니다. 만일 그들 자신이 지루한 일상적인 업무에 갇혀 있다고 생각될 경우, 이들은 쉬이 낙담하거나 인내심을 잃을 수도 있기 때문입니다. ', inline=False)
        embed.add_field(name='[살짝 미치면] 인생이 즐겁다?', value='다행히도 활동가형 사람은 언제 어떻게 휴식을 취해야 하는지 잘 알고 있습니다. 일할 때는 열정적이며 진취적인 모습이었다가 단숨에 무대 위 열성적으로 몸을 흔드는 자유로운 영혼의 모습으로 단숨에 변모하기도 하는 이들은 이러한 갑작스러운 변화로 종종 가까이에 있는 친구들이나 지인들을 놀라게 하기도 합니다. 이들의 다양한 성격적 면모는 다른 이들과의 정서적인 교감을 가능하게 하며, 특히나 친구 혹은 동료들에게 색다른 통찰력을 제공함으로써 영감을 불어 넣기도 합니다. 활동가형 사람은 모든 이들이 자신의 솔직한 감정에 귀 기울이고 이를 표현할 수 있는 시간이 필요하다고 믿습니다. 이러한 이유로 다양한 인간 감정이나 인간관계에 대한 내용이 이들과 대화 시 단골 소재입니다. ', inline=False)   
        embed.add_field(name='하지만', value='이런 활동가형 사람에게도 주의해야 할 사항이 있습니다. 만일 이들이 그들의 직관에 지나치게 의존한 나머지 사람들의 의도를 잘못 해석하는 경우 오해가 생겨 계획에 차질을 빚을 수 있는데, 이는 단도직입적으로 충분히 해결할 수 있는 문제를 더 어렵게 만드는 길입니다. 이러한 사회생활에서 빚어지는 스트레스는 협력과 조화를 중요시 여기는 성격의 사람들에게는 이들의 잠을 설치게 하는 근심 요소가 될 수 있습니다. 이들은 혹 실수로 누군가의 발을 밟았다 할 경우, 이들 역시 발을 밟힌 사람과 같은 고통을 느끼는 감성적이면서도 예민한 성격의 소유자입니다.', inline=False)         
        embed.add_field(name='활동가형 사람은', value='인간관계나 사람의 감정, 혹은 생각과 관련하여 이들이 원하는 만족스러운 대답을 찾을 때까지 끊임없이 찾아 헤매고 다닐 것입니다. 그리고 진정 그들이 원하는 답을 찾는 그 날, 이들의 상상력이나 인간애, 그리고 용기는 어마어마한 빛을 발할 것입니다.', inline=False)   
        embed.add_field(name='활동가형에 속하는 유명인', value='로버트 다우니 주니어, 윌 스미스, 스파이더맨(히어로), 윌리 웡카(찰리와 초콜릿 공장), 안나 여왕님(겨울왕국), 올라프(겨울왕국)', inline=False) 
        await message.channel.send(channel,embed=embed)

   
        
    if message.content.startswith('=대한민국'):
        channel = message.channel
        embed = discord.Embed(
            title = '내로남불의 나라, 대한민국.  ',
            description = '',
            colour = discord.Colour.red()
        )

        dtime = datetime.datetime.now()
        embed.set_footer(text=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"")
        embed.add_field(name = '대한민국은', value = '소수자들을 위한 나라가 되기에는 아직도 멀었습니다. ',inline = False)
        embed.add_field(name='사회에', value='만연한 성소수자 혐오, 장애인 비하 및 차별, 여성과 같은 약자 혐오 및 차별 등 ', inline=False)
        embed.add_field(name="껍데기만", value="선진국이고 내용물은 후진국인 나라가 바로 대한민국이죠. ", inline=False)  
        embed.add_field(name="또한,", value="대한민국은 여전히 장애인마저 강제징용하는 국가입니다. ", inline=False)  
        embed.add_field(name="그래놓고,", value="일본에게 피해보상하라 떼쓰죠.", inline=False)    
        embed.add_field(name="한국에서", value="제일 심각한 소수자들은 사회복무요원들이죠. 특히, 겉모습이 멀쩡해보이는 사회복무요원들 말입니다.", inline=False) 
        embed.add_field(name="꿀빤다고,", value="같은 남자들인 군인들은 사회복무요원들을 사람 취급 자체를 안하며, 여자들은 정공, 멸공, 돼공같은 멸칭들을 스스럼없이 사용합니다. (인터넷 커뮤니티가 일상화된 현재 10대 ~ 20대 초중반 세대 한정입니다.)", inline=False) 
        embed.add_field(name="겉모습이", value="멀쩡한 사회복무요원들은 부모가 돈이 많고, 빽이 많아 현역을 기피하는 중범죄자로 보는 게 지금 대한민국 현실이죠.", inline=False)  
        embed.add_field(name="하지만,", value="지금은 이런 애매한 남자들마저 재검받으면 현역으로 끌려갑니다. 병무청은 국제법을 어겼고, 이를 우회하기 위해 현재 사회복무요원들은 언제든지 현역으로 전환할수 있도록 기회를 마련했습니다.", inline=False)   
        embed.add_field(name="여전히,", value="병무청은 남자들을 가스라이팅하여 현재 사회복무요원인 남자들이 현역으로 전환하도록 세뇌시키고 있습니다.", inline=False)  
        embed.add_field(name="우리가", value="과연 일본에게 뭐라할 자격이 있을까요? 양심에 손을 얹고 생각해보아요.", inline=False)         
        await message.channel.send(channel,embed=embed)  
        
    if message.content.startswith('=대한민국'):
         embed = discord.Embed(
         title='대한민국의 미래가 과연 있을까요?',
         description=' ',

        )

         urlBase = 'https://i.imgur.com/QL56mza.jpeg'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send( embed=embed)          


        
        
    if message.content.startswith("ㅋ") or message.content.startswith("하하") or message.content.startswith("크크") or message.content.startswith("히히") or message.content.startswith("호호") or message.content.startswith("ㅎㅎ"): 
        dtime = datetime.datetime.now()
        randomNum = random.randrange(1, 14)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="보통 사람은 남을 보고 웃지만, 꿈이 있는 사람은 꿈을 보고 웃어요", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="행복하기 떄문에 웃는 것이 아니라, 웃기 때문에 행복해지는 거죠.", color=0x00ff00))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="사람은 함께 웃을 때 서로 가까워지는 것을 느낀다네요.", color=0x00ff00))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="웃음은 전염되요. 우리 함께 웃읍시다." ,color=0x00ff00))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="웃음은 만국공통의 언어죠.", color=0x00ff00))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="그거 알아요? 당신은 웃을때 매력적이에요.", color=0x00ff00))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="전 저 하나가 웃음거리가 되어 제 친구들이 즐거울 수 있다면 얼마든지 바보가 될 수 있어요. ", color=0x00ff00))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="오늘 가장 좋게 웃는 자는 역시 죽기 직전에도 웃을거에요. 항상 웃으세요.", color=0x00ff00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="유머감각은 리더의 필수 조건이죠. 노잼인 사람들은 사형시켜야 제맛이죠. 그들은 인간의 존엄성을 지켜줘서는 안됩니다.", color=0x00ff00))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="웃음은 최고의 결말을 보장하죠.", color=0x00ff00))
        if randomNum==11:
            await message.channel.send(embed=discord.Embed(title="성인이 하루 15번만 웃고 살면 병원의 수많은 환자들이 반으로 줄어들 겁니다. 항상 웃으세요! ", color=0xff0000))  
        if randomNum==12:
            await message.channel.send(embed=discord.Embed(title="웃음은 늘 지니고 있어야 합니다. ", color=0xff0000)) 
        if randomNum==13:
            await message.channel.send(embed=discord.Embed(title="웃음은 가장 값싸고 효과 있는 만병통치약이에요. 웃음의 위력은 대단하죠.", color=0xff0000)) 
          


    if message.content.startswith('=음식추천'):       
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"", color=0xff0000)
        await message.channel.send(embed=embed)
        randomNum = random.randrange(1, 25)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="된장찌개", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="부대찌개", color=0x00ff00))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="김치찌개", color=0x00ff00))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="라면", color=0x00ff00))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="우동", color=0x00ff00))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="순대", color=0x00ff00))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="떡볶이", color=0x00ff00))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="햄버거", color=0x00ff00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="치킨", color=0x00ff00))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="피자", color=0x00ff00))
        if randomNum==11:
            await message.channel.send(embed=discord.Embed(title="보신탕", color=0xff0000))  
        if randomNum==12:
            await message.channel.send(embed=discord.Embed(title="초콜릿", color=0xff0000)) 
        if randomNum==13:
            await message.channel.send(embed=discord.Embed(title="와플", color=0xff0000))  
        if randomNum==14:
            await message.channel.send(embed=discord.Embed(title="곱창", color=0x00ff00))
        if randomNum==15:
            await message.channel.send(embed=discord.Embed(title="돼지국밥", color=0xff0000))  
        if randomNum==16:
            await message.channel.send(embed=discord.Embed(title="오징어내장탕", color=0xff0000)) 
        if randomNum==17:
            await message.channel.send(embed=discord.Embed(title="고래고기", color=0xff0000))  
        if randomNum==18:
            await message.channel.send(embed=discord.Embed(title="감자튀김", color=0xff0000)) 
        if randomNum==19:
            await message.channel.send(embed=discord.Embed(title="짜장면", color=0xff0000))
        if randomNum==20:
            await message.channel.send(embed=discord.Embed(title="달걀 스크램블", color=0xff0000))  
        if randomNum==21:
            await message.channel.send(embed=discord.Embed(title="전주비빔밥", color=0xff0000)) 
        if randomNum==22:
            await message.channel.send(embed=discord.Embed(title="초밥", color=0xff0000)) 
        if randomNum==23:
            await message.channel.send(embed=discord.Embed(title="김밥", color=0xff0000)) 
        if randomNum==24:
            await message.channel.send(embed=discord.Embed(title="파스타", color=0xff0000)) 


    if message.content.startswith('=게임허락'):       
        dtime = datetime.datetime.now()
        embed = discord.Embed(title=str(dtime.year)+"- "+str(dtime.month)+"- "+str(dtime.day)+" "+str(dtime.minute)+": "+str(dtime.second)+"", color=0xff0000)
        await message.channel.send(embed=embed)
        randomNum = random.randrange(1, 3)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="오늘은 게임해도 좋습니다. 최고의 피지컬을 뽐내보세요.", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="오늘은 게임하면 후회하실겁니다. 컨디션 최악으로 보입니다만.. 그래도 돌리시겠다면 어쩔수 없죠.", color=0x00ff00))
          
          
    if "섹스" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 성 적인 단어로, 우리 서버 규칙을 어기는 행위죠.")
       
    if "섹1스" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 성 적인 단어로, 우리 서버 규칙을 어기는 행위죠.")       
       
    if "씨발" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 문란한 성,관,계로 몸이 더럽혀진 여성을 비하하는 욕설로, 우리 서버 규칙을 어기는 행위죠.")
       
    if "씨1발" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 문란한 성,관,계로 몸이 더럽혀진 여성을 비하하는 욕설로, 우리 서버 규칙을 어기는 행위죠.")       
       
    if "시발" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 문란한 성,관,계로 몸이 더럽혀진 여성을 비하하는 욕설로, 우리 서버 규칙을 어기는 행위죠.")
       
    if "시1발" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 문란한 성,관,계로 몸이 더럽혀진 여성을 비하하는 욕설로, 우리 서버 규칙을 어기는 행위죠.")       
       
    if "병신" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 남들과 다른 존재를 비하하는 단어를 사용하지마세요.")
       
    if "병1신" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 남들과 다른 존재를 비하하는 단어를 사용하지마세요.")       
       
    if "애미" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 부,모 또는 가,족을 비하하는 욕설을 사용하지 마세요.")
       
    if "애1미" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 부,모 또는 가,족을 비하하는 욕설을 사용하지 마세요.")               
       
    if "새끼" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")
       
    if "새1끼" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")       
       
    if "십년" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")     
       
    if "씹" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")      
       
    if "난교" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 성 적인 단어로, 우리 서버 규칙을 어기는 행위죠.")
       
    if "난1교" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 성 적인 단어로, 우리 서버 규칙을 어기는 행위죠.")       
       
    if "fuck" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 성,관,계를 의미하는 욕설로, 우리 서버 규칙을 어기는 행위죠.")
       
    if "FUCK" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 성,관,계를 의미하는 욕설로, 우리 서버 규칙을 어기는 행위죠..")       
     
    if "븅신" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 남들과 다른 존재를 비하하는 단어를 사용하지마세요.")
       
    if "븅1신" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 남들과 다른 존재를 비하하는 단어를 사용하지마세요.")       
                    
    if "진핑" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 한 국가의 얼굴을 욕하지마세요. 당신의 집안은 풍비박산이 날것입니다.")
       
    if "진1핑" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 한 국가의 얼굴을 욕하지마세요. 당신의 집안은 풍비박산이 날것입니다.")                   
       
    if "보지" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 여성의 생,식,기를 의미하는 비속어로, 우리 서버 규칙을 어기는 행위죠.")
       
    if "보1지" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 여성의 생,식,기를 의미하는 비속어로, 우리 서버 규칙을 어기는 행위죠.")
       
    if "자지" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 남성의 성,기를 의미하는 비속어로, 우리 서버 규칙을 어기는 행위죠.")
       
    if "자1지" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 남성의 성,기를 의미하는 비속어로, 우리 서버 규칙을 어기는 행위죠.")        
       
    if "ㅅㅂ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 문란한 성,관,계로 몸이 더럽혀진 여성을 비하하는 욕설로, 우리 서버 규칙을 어기는 행위죠.")
       
    if "ㅅ1ㅂ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 문란한 성,관,계로 몸이 더럽혀진 여성을 비하하는 욕설로, 우리 서버 규칙을 어기는 행위죠.")        
       
    if "ㅆㅂ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 문란한 성,관,계로 몸이 더럽혀진 여성을 비하하는 욕설로, 우리 서버 규칙을 어기는 행위죠.")
       
    if "ㅆ1ㅂ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 문란한 성,관,계로 몸이 더럽혀진 여성을 비하하는 욕설로, 우리 서버 규칙을 어기는 행위죠.")        
       
    if "ㅂㅅ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 남들과 다른 존재를 비하하는 단어를 사용하지마세요.")
       
    if "ㅂ1ㅅ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 남들과 다른 존재를 비하하는 단어를 사용하지마세요.")        
       
    if "ㅇㅁ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 부,모 또는 가,족을 비하하는 욕설을 사용하지 마세요.")
       
    if "ㅇ1ㅁ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 부,모 또는 가,족을 비하하는 욕설을 사용하지 마세요.")        
       
    if "한녀" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 젠,더,갈,등 관련 단어입니다, 사용하지마세요.")
       
    if "한1녀" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 젠,더,갈,등 관련 단어입니다, 사용하지마세요.") 
       
    if "한남" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 젠,더,갈,등 관련 단어입니다, 사용하지마세요.")
       
    if "한1남" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 젠,더,갈,등 관련 단어입니다, 사용하지마세요.")  
       
    if "1번남" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 젠,더,갈,등 관련 단어입니다, 사용하지마세요.") 
       
    if "1번녀" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 젠,더,갈,등 관련 단어입니다, 사용하지마세요.")   
       
    if "2번남" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 젠,더,갈,등 관련 단어입니다, 사용하지마세요.") 
       
    if "2번녀" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 젠,더,갈,등 관련 단어입니다, 사용하지마세요.")         
       
    if "애비" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 부,모 또는 가,족을 비하하는 욕설을 사용하지 마세요.")
       
    if "애1비" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 부,모 또는 가,족을 비하하는 욕설을 사용하지 마세요.")              
       
    if "느금" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 부,모 또는 가,족을 비하하는 욕설을 사용하지 마세요.")
       
    if "느1금" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 부,모 또는 가,족을 비하하는 욕설을 사용하지 마세요.")        
       
    if "미친" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")
       
    if "미1친" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")        
       
    if "ㅗ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")       

       
    if "존나" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 발,기된 남성의 성,기를 비하하는 욕설로, 우리 서버 규칙을 어기는 행위죠.") 
       
    if "ㅈㄴ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 발,기된 남성의 성,기를 비하하는 욕설로, 우리 서버 규칙을 어기는 행위죠.")  
       
    if "존1나" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 발,기된 남성의 성,기를 비하하는 욕설로, 우리 서버 규칙을 어기는 행위죠.")     
       
    if "ㅈ1ㄴ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용한 단어는 발,기된 남성의 성,기를 비하하는 욕설로, 우리 서버 규칙을 어기는 행위죠.")          
       
    if "닥치" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")
       
    if "닥쳐" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")
       
    if "ㄷㅊ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")
       
    if "ㄷ1ㅊ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")        
       
    if "꺼져" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")
       
    if "꺼1져" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.") 
       
    if "꺼지" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 금칙어와 매우 유사한 단어입니다. 순화하세요.") 
       
    if "꺼1지" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 금칙어와 매우 유사한 단어입니다. 순화하세요.")       
       
    if "ㄲㅈ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")
       
    if "ㄲ1ㅈ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")        
              
    if "ㅄ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 남들과 다른 존재를 비하하는 단어를 사용하지마세요.")         
             
    if "지랄" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.") 
       
    if "지1랄" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")
       
    if "시팔" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")
       
    if "시1팔" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")  
       
    if "씨팔" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")       
       
    if "씨1팔" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")     
       
    if "좆" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")    
       
    if "씹" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")                
       
    if "ㅈㄹ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용하신 단어는 간질병환자들을 조롱하는 의미를 가진 욕설이고, 우리 서버 규칙을 어기는 행위죠.")  
       
    if "ㅈ1ㄹ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 사용하신 단어는 간질병환자들을 조롱하는 의미를 가진 욕설이고, 우리 서버 규칙을 어기는 행위죠.")           
       
    if "Fuck" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")  
       
    if "짱깨" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.") 
       
    if "짱1깨" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")       
       
    if "씨1팔" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")           
       
    if "씨1팔" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 금칙어를 사용하였습니다.")           
       
    if "조선족" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 일부 소수자들을 비하하는 비속이입니다.")  
       
    if "조1선족" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 일부 소수자들을 비하하는 비속이입니다.") 
       
    if "정신병" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어로 상처받을 일부 소수자들의 마음을 생각하세요.")   
       
    if "정1신병" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어로 상처받을 일부 소수자들의 마음을 생각하세요.")                                     
       
    if "피싸개" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 일,베 또는 디,시와 같은 남초 커뮤니티에서 파생된 단어를 사용하지 마세요.")        
       
    if "설거지" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 젠,더,갈,등 관련 단어입니다, 사용하지마세요.")  
       
    if "페미" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 젠,더,갈,등 관련 단어입니다, 사용하지마세요.")  
       
    if "페1미" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 젠,더,갈,등 관련 단어입니다, 사용하지마세요.")         
       
    if "패미" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 젠,더,갈,등 관련 단어입니다, 사용하지마세요.")
       
    if "패1미" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 단어는 젠,더,갈,등 관련 단어입니다, 사용하지마세요.")         
       
    if "장애" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 남들과 다른 존재를 비하하는 단어는 사용하지마세요.")  
       
    if "장1애" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 남들과 다른 존재를 비하하는 단어는 사용하지마세요.")            
       
    if "정공" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 사회복무요원 비하 발언은 우리 서버 규칙을 어긴겁니다.")   
       
    if "정1공" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 사회복무요원 비하 발언은 우리 서버 규칙을 어긴겁니다.")        
                                                                    
    if "치매" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 질병은 누구나 걸릴 수 있습니다. 함부로 그런 단어를 사용하지마세요. 천벌 받을것입니다.")    
       
    if "치1매" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 질병은 누구나 걸릴 수 있습니다. 함부로 그런 단어를 사용하지마세요. 천벌 받을것입니다.")         
         
    if "자살" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 생명은 소중한 것입니다.")
      
    if "죽고" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 생명은 소중한 것입니다.")
      
    if "죽여주" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 생명은 소중한 것입니다.")
      
    if "죽을" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 생명은 소중한 것입니다.")
      
    if "죽이" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 생명은 소중한 것입니다.") 
      
    if "죽여" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 생명은 소중한 것입니다.")      
      
    if message.content.startswith('자살'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/euLvJBb.jpeg'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send( embed=embed)       
      
    if message.content.startswith('죽고'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/euLvJBb.jpeg'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send( embed=embed)     
         
    if message.content.startswith('죽여주'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/euLvJBb.jpeg'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send( embed=embed)     
         
    if message.content.startswith('죽을'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/euLvJBb.jpeg'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send( embed=embed)              
   
    if "자살" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 우울감 등 말하기 어려운 고민이 있거나 주변에 이런 어려움을 겪는 가족ㆍ지인이 있을 경우 자,살예방 상담전화 1393, 정신건강 상담전화 1577-0199, 희망의 전화 129, 생명의 전화 1588-9191, 청소년 전화 1388, 청소년 모바일 상담 ‘다 들어줄게’ 앱, 카카오톡 등에서 24시간 전문가의 상담을 받을 수 있습니다.")
      
    if "죽고" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 우울감 등 말하기 어려운 고민이 있거나 주변에 이런 어려움을 겪는 가족ㆍ지인이 있을 경우 자,살예방 상담전화 1393, 정신건강 상담전화 1577-0199, 희망의 전화 129, 생명의 전화 1588-9191, 청소년 전화 1388, 청소년 모바일 상담 ‘다 들어줄게’ 앱, 카카오톡 등에서 24시간 전문가의 상담을 받을 수 있습니다.")
      
    if "죽여주" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 우울감 등 말하기 어려운 고민이 있거나 주변에 이런 어려움을 겪는 가족ㆍ지인이 있을 경우 자,살예방 상담전화 1393, 정신건강 상담전화 1577-0199, 희망의 전화 129, 생명의 전화 1588-9191, 청소년 전화 1388, 청소년 모바일 상담 ‘다 들어줄게’ 앱, 카카오톡 등에서 24시간 전문가의 상담을 받을 수 있습니다.")
      
    if "죽을" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 우울감 등 말하기 어려운 고민이 있거나 주변에 이런 어려움을 겪는 가족ㆍ지인이 있을 경우 자,살예방 상담전화 1393, 정신건강 상담전화 1577-0199, 희망의 전화 129, 생명의 전화 1588-9191, 청소년 전화 1388, 청소년 모바일 상담 ‘다 들어줄게’ 앱, 카카오톡 등에서 24시간 전문가의 상담을 받을 수 있습니다.")            
      
    if "완다" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 완,다 막시모프는 마블 시네마틱 유니버스의 스,칼,렛 위치입니다. 담당 배우는 엘리자베스 올슨이죠. 완,다는 그동안 인체 실험으로 능력을 얻었다고만 알고 있었으나, 완,다,비,전에서 밝혀진 완,다의 과거에 따르면 완,다는 태어날 때부터 능력을 지니고 태어났다가 마인드 스톤을 통해 각성한 것에 가깝다고 합니다.")      
      
    if "스칼렛" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 완,다 막시모프는 마블 시네마틱 유니버스의 스,칼,렛 위치입니다. 담당 배우는 엘리자베스 올슨이죠. 완,다는 그동안 인체 실험으로 능력을 얻었다고만 알고 있었으나, 완,다,비,전에서 밝혀진 완,다의 과거에 따르면 완,다는 태어날 때부터 능력을 지니고 태어났다가 마인드 스톤을 통해 각성한 것에 가깝다고 합니다.")   
      
    if "닥터스트레인지" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 닥,터,스,트,레,인,지는 마블 시네마틱 유니버스의 닥,터,스,트,레,인,지입니다. 담당 배우는 베네딕트 컴버배치가 연기하죠. 본래 천재적이고 뛰어난 의료 실력을 가진 오만하고 이,기적인 신경외과 의사였지만, 교통사고로 신경외과로서 중요한 손을 못 쓰게 되자 손을 고치기 위해 마법사 에,인,션,트 원를 찾아가 제자가 되고, 마법을 익히고 배우면서 에,인,션,트 원의 죽음 이후 최강의 마법사가 된다.")         
      
    if "닥스" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 닥,터,스,트,레,인,지는 마블 시네마틱 유니버스의 닥,터,스,트,레,인,지입니다. 담당 배우는 베네딕트 컴버배치가 연기하죠. 본래 천재적이고 뛰어난 의료 실력을 가진 오만하고 이,기적인 신경외과 의사였지만, 교통사고로 신경외과로서 중요한 손을 못 쓰게 되자 손을 고치기 위해 마법사 에,인,션,트 원를 찾아가 제자가 되고, 마법을 익히고 배우면서 에,인,션,트 원의 죽음 이후 최강의 마법사가 된다.")    
      
    if "토니" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 아,이,언,맨이자 토,니,스,타,크는 마블 시네마틱 유니버스의 아,이,언,맨이자, 아,이,언,맨 실사영화 시리즈의 주인공이며, 캡,틴 아,메,리,카와 함께 인피니티 사가의 메인 히어로이자 동시에 진 주인공이죠. 담당 배우는 로,버,트,다,우,니,주,니,어 입니다.")         
      
    if "아이언맨" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 아,이,언,맨이자 토,니,스,타,크는 마블 시네마틱 유니버스의 아,이,언,맨이자, 아,이,언,맨 실사영화 시리즈의 주인공이며, 캡,틴 아,메,리,카와 함께 인피니티 사가의 메인 히어로이자 동시에 진 주인공이죠. 담당 배우는 로,버,트,다,우,니,주,니,어 입니다.")    
      
    if "로다주" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 아,이,언,맨이자 토,니,스,타,크는 마블 시네마틱 유니버스의 아,이,언,맨이자, 아,이,언,맨 실사영화 시리즈의 주인공이며, 캡,틴 아,메,리,카와 함께 인피니티 사가의 메인 히어로이자 동시에 진 주인공이죠. 담당 배우는 로,버,트,다,우,니,주,니,어 입니다.")     
      
    if "캡틴" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 담당 배우는 크,리,스,에,반,스, 1대 캡,틴,아,메,리,카이자 본명은 스,티,브,로,저,스 입니다. 제2차 세계대전 당시 너무 허약해서 미 육군 입대를 거부당할 정도로 빈약한 몸을 지닌 청년이었지만, 조국에 봉사하기 위해 초인 병사 계획 [프로젝트 리버스]에 자원하여 특수 혈청을 맞고 모든 능력을 인간의 한계까지 끌어올린 초인이 되었습니다. 특유의 캡,틴 아,메,리,카 코스튬과 비브라늄 방패를 들고 제2차 세계대전에 참전했었죠. 버,키,반,스가 주요 파트너였습니다. 추후에 버,키는 윈,터,솔,저가 됩니다.")     
      
    if "캡아" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 담당 배우는 크,리,스,에,반,스, 1대 캡,틴,아,메,리,카이자 본명은 스,티,브,로,저,스 입니다. 제2차 세계대전 당시 너무 허약해서 미 육군 입대를 거부당할 정도로 빈약한 몸을 지닌 청년이었지만, 조국에 봉사하기 위해 초인 병사 계획 [프로젝트 리버스]에 자원하여 특수 혈청을 맞고 모든 능력을 인간의 한계까지 끌어올린 초인이 되었습니다. 특유의 캡,틴 아,메,리,카 코스튬과 비브라늄 방패를 들고 제2차 세계대전에 참전했었죠. 버,키,반,스가 주요 파트너였습니다. 추후에 버,키는 윈,터,솔,저가 됩니다.")   
      
    if "스파이더맨" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 마블 코믹스의 등장인물. 본명은 피,터,파,커. 스탠 리, 스티브 딧코 콤비가 만들었으며, 스탠 리가 자식처럼 아꼈던 캐릭터. 첫 등장은 1962년 8월 발간된 어메이징 판타지(Amazing Fantasy) 15호로, 코믹스 최초의 단독 주인공 10대 히어로이다.")  
      
    if "피터파커" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 마블 코믹스의 등장인물. 본명은 피,터,파,커. 스탠 리, 스티브 딧코 콤비가 만들었으며, 스탠 리가 자식처럼 아꼈던 캐릭터. 첫 등장은 1962년 8월 발간된 어메이징 판타지(Amazing Fantasy) 15호로, 코믹스 최초의 단독 주인공 10대 히어로이다.") 
      
    if "호크아이" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 마블 시네마틱 유니버스의 호,크,아,이의 담당배우는 제,레,미,레,너이며, 어,벤,져,스 멤버중 가장 인간적이고 관객이 몰입하기 쉬운 캐릭터입니다. 그는 최고의 명사수이자 최고의 아버지죠.")    
      
    if "차베즈" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 마블 시네마틱 유니버스의 차,베,즈는 원작인 마,블,코,믹,스에 등장하는 캐릭터로 코드네임은 미스 아,메,리,카이며 본명은 아,메,리,카,차,베,즈이죠, 담당 배우는 소,치,틀,고,메,즈입니다.")  
      
    if "소치틀" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 마블 시네마틱 유니버스의 차,베,즈는 원작인 마,블,코,믹,스에 등장하는 캐릭터로 코드네임은 미스 아,메,리,카이며 본명은 아,메,리,카,차,베,즈이죠, 담당 배우는 소,치,틀,고,메,즈입니다.")        
      
    if "미즈마블" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 마블 시네마틱 유니버스의 미,즈,마,블은 마,블 최초의 성,공,한,덕,후 히어로 입니다. 본명은 카,말,라 칸이며 무,슬,림 출신 히어로이죠. 카,말,라 칸은 어벤져스 멤버들을 덕질하는게 취미죠. 그녀의 조상은 크리족입니다. 우연찮게 증조할머니의 유품을 차게된 그녀는 결국 자신 몸안에 잠재되어있던 능력을 발현시키죠. 담당 배우는 이,만,벨,라,니입니다.")   
      
    if "이만벨라니" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 마블 시네마틱 유니버스의 미,즈,마,블은 마,블 최초의 성,공,한,덕,후 히어로 입니다. 본명은 카,말,라 칸이며 무,슬,림 출신 히어로이죠. 카,말,라 칸은 어벤져스 멤버들을 덕질하는게 취미죠. 그녀의 조상은 크리족입니다. 우연찮게 증조할머니의 유품을 차게된 그녀는 결국 자신 몸안에 잠재되어있던 능력을 발현시키죠. 담당 배우는 이,만,벨,라,니입니다.")        
           
      
    if "새해" in message.content:
        await message.channel.send(f"{message.author.mention} 님, [새_해] 복 많이 받으시길 바랍니다.")     
      
    if "https://" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 링크 공유는 서버 규칙을 어긴겁니다.")
      
    if "http://" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 링크 공유는 서버 규칙을 어긴겁니다.")
      
    if "youtu.be" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 링크 공유는 서버 규칙을 어긴겁니다.")
       
    if "youtube" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 링크 공유는 서버 규칙을 어긴겁니다.")       
      
    if "gall.dcinside.com" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 링크 공유는 서버 규칙을 어긴겁니다.")
      
    if "news.naver.com" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 링크 공유는 서버 규칙을 어긴겁니다.")
      
    if "news.v.daum.net" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 링크 공유는 서버 규칙을 어긴겁니다.")
           
       
    if "나냡" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 닉네임을 언급하는 행위는 서버 규칙을 어기는겁니다.") 
       
    if "나1냡" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 닉네임을 언급하는 행위는 서버 규칙을 어기는겁니다.")      
       
    if "남냠" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 닉네임을 언급하는 행위는 서버 규칙을 어기는겁니다.")        
                    
    if "도리" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 닉네임을 언급하는 행위는 서버 규칙을 어기는겁니다.") 
       
    if "도1리" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 닉네임을 언급하는 행위는 서버 규칙을 어기는겁니다.")   
       
    if "돌이" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 닉네임을 언급하는 행위는 서버 규칙을 어기는겁니다.") 
       
    if "광탈맨" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님, 해당 닉네임을 언급하는 행위는 분쟁 유발 목적이 다분해보입니다.")        
                     
    if "7호선" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 사회 하층민 신분의 닉네임은 언급해도 괜찮습니다. ")  
       
    if "들쥐" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 상민 신분의 닉네임은 언급해도 괜찮습니다. ")   
      
    if "1인칭" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 노예 신분의 닉네임은 언급해도 괜찮습니다. ")   
      
    if "그로자" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 해당 총기는 러시아제 총기로, Гроза. 천둥번개라는 뜻을 가지고 있죠.") 
      
    if "Groza" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 배그 기준으로 설명하자면 해당 총기는 러시아제 불펍 자동소총으로, 천둥번개, 뇌우라는 의미를 가졌죠.(Образец ЦКИБ-14) '그에 비빌 자, 먼지처럼 분해되어 사라지리니' ")  
            
    if "groza" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 배그 기준으로 설명하자면 해당 총기는 러시아제 불펍 자동소총으로, 천둥번개, 뇌우라는 의미를 가졌죠.(Образец ЦКИБ-14) '그에 비빌 자, 먼지처럼 분해되어 사라지리니'")  
      
    if "그로자" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 배그 기준으로 설명하자면 해당 총기는 러시아제 불펍 자동소총으로, 천둥번개, 뇌우라는 의미를 가졌죠.(Образец ЦКИБ-14) '그에 비빌 자, 먼지처럼 분해되어 사라지리니'")       
      
    if "M249" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 분대지원화기, Squad Automatic Weapon은 미군의 제식 경기관총이죠. 배그 기준 해당 총기는 매우 우수한 집탄력과 연사력을 자랑합니다. '내 앞에 모두 무릎 꿇어라! 산산조각나기 싫으면'") 
      
    if "m249" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 분대지원화기, Squad Automatic Weapon은 미군의 제식 경기관총이죠. 배그 기준 해당 총기는 매우 우수한 집탄력과 연사력을 자랑합니다. '내 앞에 모두 무릎 꿇어라! 산산조각나기 싫으면'")   
      
    if "DBS" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 미국 Standard Manufacturing 에서 제작된 불펍식 펌프액션 더블배럴 산탄총으로 Shot Show 2015에서 처음 공개되었죠. (DP-12) 총기의 디자인은 매우 매우 UTS-15와 흡사하지만, 이 둘은 전혀 다른 산탄총입니다.")      
      
    if "dbs" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 미국 Standard Manufacturing 에서 제작된 불펍식 펌프액션 더블배럴 산탄총으로 Shot Show 2015에서 처음 공개되었죠. (DP-12) 총기의 디자인은 매우 매우 UTS-15와 흡사하지만, 이 둘은 전혀 다른 산탄총입니다.") 
      
    if "M1014" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 통합 제식 전투 산탄총, Joint Service Combat Shotgun은 미군의 제식 반자동 산탄총이죠. 모배 기준으로 DP-12를 압살하는 사기급 1티어 산탄총으로 자리잡은 총기입니다. '미군의 군사력은 세계 제일!'")   
      
    if "m1014" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 통합 제식 전투 산탄총, Joint Service Combat Shotgun은 미군의 제식 반자동 산탄총이죠. 모배 기준으로 DP-12를 압살하는 사기급 1티어 산탄총으로 자리잡은 총기입니다. '미군의 군사력은 세계 제일!'") 
      
    if "AK" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 7.62mm 칼라시니코프 자동소총 현대형은 미하일 칼라시니코프가 개발한 자동소총이죠. GRAU 코드명은 '6П1(6P1)'이며, 줄임말인 'A,K,M'에서 'M'은 'Модернизированный(Modernized, 현대화)'의 약칭입니다.")    
      
    if "akm" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 7.62mm 칼라시니코프 자동소총 현대형은 미하일 칼라시니코프가 개발한 자동소총이죠. GRAU 코드명은 '6П1(6P1)'이며, 줄임말인 'A,K,M'에서 'M'은 'Модернизированный(Modernized, 현대화)'의 약칭입니다.")     
      
    if "베릴" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 해당 총기는 노후화가 진행될대로 진행된 에켐과, 이미 보급이 시작된지 5년 정도밖에 안 되었던 wz.88 탄탈을 대체하기 위해 개발되었습니다. 우리가 배그에서 흔히 베,릴이라고 생각하는 모델은 7.62×39mm M43 탄을 사용하는 모델이죠. 배그의 단점은 에켐의 개량 버전인 베,릴의 성능을 너무 높게 잡아놨다는 점이죠. 이럴거면 에켐도 버프해줘야하는것 아닐까요? ")   
      
    if "엠포" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 독일의 H&K 사에서 제작한 카빈형 돌격소총으로 현재 미합중국 해병대와 프랑스군의 제식소총이며, 델타포스, 스페츠나츠, GIGN 등 세계 각국의 특수부대와 한국군 특수부대에서도 널리 사용되고 있는 등 H&K의 주력상품 중 하나가 되었습니다. 배그에서의 엠,포는 엠,십,육 계열이 아니라 HK,416에서 M,416으로 네이밍만 바꾼것입니다. ")  
      
    if "HK416" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 독일의 H&K 사에서 제작한 카빈형 돌격소총으로 현재 미합중국 해병대와 프랑스군의 제식소총이며, 델타포스, 스페츠나츠, GIGN 등 세계 각국의 특수부대와 한국군 특수부대에서도 널리 사용되고 있는 등 H&K의 주력상품 중 하나가 되었습니다. 배그에서의 엠,포는 엠,십,육 계열이 아니라 HK,416에서 M,416으로 네이밍만 바꾼것입니다. ") 
      
    if "M416" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 독일의 H&K 사에서 제작한 카빈형 돌격소총으로 현재 미합중국 해병대와 프랑스군의 제식소총이며, 델타포스, 스페츠나츠, GIGN 등 세계 각국의 특수부대와 한국군 특수부대에서도 널리 사용되고 있는 등 H&K의 주력상품 중 하나가 되었습니다. 배그에서의 엠,포는 엠,십,육 계열이 아니라 HK,416에서 M,416으로 네이밍만 바꾼것입니다. ")  
       
    if "hk416" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 독일의 H&K 사에서 제작한 카빈형 돌격소총으로 현재 미합중국 해병대와 프랑스군의 제식소총이며, 델타포스, 스페츠나츠, GIGN 등 세계 각국의 특수부대와 한국군 특수부대에서도 널리 사용되고 있는 등 H&K의 주력상품 중 하나가 되었습니다. 배그에서의 엠,포는 엠,십,육 계열이 아니라 HK,416에서 M,416으로 네이밍만 바꾼것입니다. ")   
      
    if "m416" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 독일의 H&K 사에서 제작한 카빈형 돌격소총으로 현재 미합중국 해병대와 프랑스군의 제식소총이며, 델타포스, 스페츠나츠, GIGN 등 세계 각국의 특수부대와 한국군 특수부대에서도 널리 사용되고 있는 등 H&K의 주력상품 중 하나가 되었습니다. 배그에서의 엠,포는 엠,십,육 계열이 아니라 HK,416에서 M,416으로 네이밍만 바꾼것입니다. ")    
      
    if "AUG" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 슈타이어 만리허가 1977년에 개발하고 오스트리아 육군이 채용한 불펍식 돌격소총으로 A,U,G는 독일어로 Armee Universale Gewehr, 즉, '군용 다목적 소총'의 약자죠.")      
      
    if "aug" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 슈타이어 만리허가 1977년에 개발하고 오스트리아 육군이 채용한 불펍식 돌격소총으로 A,U,G는 독일어로 Armee Universale Gewehr, 즉, '군용 다목적 소총'의 약자죠.")
      
    if "어그" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 슈타이어 만리허가 1977년에 개발하고 오스트리아 육군이 채용한 불펍식 돌격소총으로 A,U,G는 독일어로 Armee Universale Gewehr, 즉, '군용 다목적 소총'의 약자죠.")    
      
    if "MG3" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 제2차 세계 대전 중 독일군의 MG42는 내구성, 다목적성 등 여러 면에서 뛰어난 다목적 기관총이었다. 완성도가 워낙 높았기에 이를 전후에도 이용하기 위해 독일군은 사용탄을 7.62×51mm NATO탄으로 바꾸고, 너무 높아서 오히려 문제였던 연사력을 분당 1,000발 정도로 떨어뜨린 것만 빼면 MG42와 별 차이가 없는 MG3를 만들었죠. 'brrrrrrrrrr!! 내 앞에서 모두 비켜라! 먼지가 되기 싫다면.'")      
      
    if "mg3" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 제2차 세계 대전 중 독일군의 MG42는 내구성, 다목적성 등 여러 면에서 뛰어난 다목적 기관총이었다. 완성도가 워낙 높았기에 이를 전후에도 이용하기 위해 독일군은 사용탄을 7.62×51mm NATO탄으로 바꾸고, 너무 높아서 오히려 문제였던 연사력을 분당 1,000발 정도로 떨어뜨린 것만 빼면 MG42와 별 차이가 없는 MG3를 만들었죠. 'brrrrrrrrrr!! 내 앞에서 모두 비켜라! 먼지가 되기 싫다면.'")  
      
    if "P90" in message.content:
        await message.channel.send(f"{message.author.mention} 님, FN 프로젝트 90® PDWs는 벨기에의 FN사에서 만든 개인 방어 화기(PDW), 기관단총이죠. 본래 PDW 개념으로 출시되었지만 해당 개념이 사장된 최근에 와서는 그냥 기관단총으로 분류되며, 제조사도 미련없이 PDW 개념을 버리고 기관단총으로 판매하고 있습니다. 흔하지 않은 불펍 방식에, 특이한 탄창, 급탄 구조와 극단적인 간소화를 추구하여 탄생한 독특한 디자인으로 유명합니다. FPS 게임에서 빼놓을수 없는 친구죠.")        
      
    if "p90" in message.content:
        await message.channel.send(f"{message.author.mention} 님, FN 프로젝트 90® PDWs는 벨기에의 FN사에서 만든 개인 방어 화기(PDW), 기관단총이죠. 본래 PDW 개념으로 출시되었지만 해당 개념이 사장된 최근에 와서는 그냥 기관단총으로 분류되며, 제조사도 미련없이 PDW 개념을 버리고 기관단총으로 판매하고 있습니다. 흔하지 않은 불펍 방식에, 특이한 탄창, 급탄 구조와 극단적인 간소화를 추구하여 탄생한 독특한 디자인으로 유명합니다. FPS 게임에서 빼놓을수 없는 친구죠.")        
      
    if "피구공" in message.content:
        await message.channel.send(f"{message.author.mention} 님, FN 프로젝트 90® PDWs는 벨기에의 FN사에서 만든 개인 방어 화기(PDW), 기관단총이죠. 본래 PDW 개념으로 출시되었지만 해당 개념이 사장된 최근에 와서는 그냥 기관단총으로 분류되며, 제조사도 미련없이 PDW 개념을 버리고 기관단총으로 판매하고 있습니다. 흔하지 않은 불펍 방식에, 특이한 탄창, 급탄 구조와 극단적인 간소화를 추구하여 탄생한 독특한 디자인으로 유명합니다. FPS 게임에서 빼놓을수 없는 친구죠.")      
      
    if "코로나" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 코,로,나,1,9로 스트레스 받을 때 혼자 힘들어하지 말고 전문가의 도움을 받으세요.")         
     
    if "탑건" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 탑,건은 1986년에 개봉한 미국 영화, 현 386세대의 일원이라면 한번쯤은 영화관에서 본 그 추억의 영화죠. 후속작은 36년만에 개봉을 하였습니다.")                 

    if "TOP GUN" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 탑,건은 1986년에 개봉한 미국 영화, 현 386세대의 일원이라면 한번쯤은 영화관에서 본 그 추억의 영화죠. 후속작은 36년만에 개봉을 하였습니다.")   

    if "top gun" in message.content:
        await message.channel.send(f"{message.author.mention} 님, 탑,건은 1986년에 개봉한 미국 영화, 현 386세대의 일원이라면 한번쯤은 영화관에서 본 그 추억의 영화죠. 후속작은 36년만에 개봉을 하였습니다.")   
      
    if message.content.startswith('코로나'):
         embed = discord.Embed(
         title='',
         description='',

        )

         urlBase = 'https://i.imgur.com/55Gap2t.jpeg'
         randomNum = random.randrange(1, 2)
         urlF = urlBase+str(randomNum)
         embed.set_image(url = urlF)
         await message.channel.send( embed=embed)         
         
    if message.content.startswith("게임") or message.content.startswith("겜"):          
        dtime = datetime.datetime.now()
        randomNum = random.randrange(1, 14)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="[게임]은 질병입니다.", color=0x00ff00))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="[게임]중독.. 무엇을 상상하든 그이상을 파괴합니다.", color=0x00ff00))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="[게임]은 마약입니다.", color=0x00ff00))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="[부모]님께 게임 시간을 정해달라고 부탁드려보세요." ,color=0x00ff00))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="[부모]님과 자녀가 게임을 같이하면 오히려 역효과가 납니다. 서로 하지 말아주세요.", color=0x00ff00))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="[컴퓨터]를 켜고 끄는 시간을 정합시다.", color=0x00ff00))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="[컴퓨터]를 거실같은 공개된 장소로 옮기세요. 지금 당장! ", color=0x00ff00))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="[게임]을 안하면 불안한가요? 게임을 함으로써 당신 인생이 위험합니다.", color=0x00ff00))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="[지금] 당장 게임을 삭제합시다. 게임을 삭제했나요? 당신은 새 사람이 되었습니다.", color=0x00ff00))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="[처음]부터 게임을 기피하기는 힘들죠. 우리 사용 시간을 정해보아요.", color=0x00ff00))
        if randomNum==11:
            await message.channel.send(embed=discord.Embed(title="[우리함께] 산책나갈래요?", color=0xff0000))  
        if randomNum==12:
            await message.channel.send(embed=discord.Embed(title="[사람들과] 대화를 많이 합시다. 물론 오프라인으로요. ", color=0xff0000)) 
        if randomNum==13:
            await message.channel.send(embed=discord.Embed(title="[게임]말고 새로운 취미는 없나요? 우리 함께 새로운 취미를 탐색해볼까요?", color=0xff0000))
          
                            
accross_token = os.environ["BOT_TOKEN"]
app.run(accross_token)
