from selenium import webdriver
import pandas as pd

#driver.find_element("xpath",'')
#button.click()

web = 'https://www.espncricinfo.com/cricketers/sachin-tendulkar-35320'
cService = webdriver.ChromeService(executable_path='C:/Users/abhra/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=cService)
driver.get(web)

nname = "Sachin Tendulkar"
id = 35320

#//div/div/div/table/tbody/tr/td/span

#//div/div/p[@class="ds-text-title-subtle-s ds-font-medium ds-py-2 ds-ml-4 ds-text-typo ds-capitalize"]

first = driver.find_element("xpath",'(//div/div/p[@class="ds-text-title-subtle-s ds-font-medium ds-py-2 ds-ml-4 ds-text-typo ds-capitalize"])[1]')

second = driver.find_element("xpath",'(//div/div/p[@class="ds-text-title-subtle-s ds-font-medium ds-py-2 ds-ml-4 ds-text-typo ds-capitalize"])[2]')

#gg=driver.find_element("xpath",'(//div/div/div/table/tbody/tr/td/span)[1]')

rows = driver.find_elements("xpath",'//div/div/div/table[contains(@class,"ds-overflow-scroll")]/tbody/tr')

cou = len(rows)/2
va = 0

tFORMAT = 0
tMat = 0
tInns = 0
tNO = 0	
tRuns = 0	
tHS = 0	
tAve = 0	
tBF = 0	
tSR = 0	
t100s = 0	
t50s = 0	
t4s = 0	
t6s = 0	
tCt = 0	
tSt = 0
oFORMAT = 0	
oMat = 0	
oInns = 0	
oNO = 0	
oRuns = 0	
oHS = 0
oAve = 0
oBF = 0
oSR = 0
o100s = 0
o50s = 0
o4s = 0
o6s = 0
oCt = 0
oSt = 0
uFORMAT = 0	
uMat = 0
uInns = 0
uNO = 0
uRuns = 0
uHS = 0
uAve = 0
uBF = 0
uSR = 0
u100s = 0
u50s = 0
u4s = 0
u6s = 0
uCt = 0
uSt = 0
fFORMAT = 0	
fMat = 0
fInns = 0
fNO = 0
fRuns = 0
fHS = 0
fAve = 0
fBF = 0
fSR = 0
f100s = 0
f50s = 0
f4s = 0
f6s = 0
fCt = 0
fSt = 0
lFORMAT = 0	
lMat = 0
lInns = 0
lNO = 0
lRuns = 0
lHS = 0
lAve = 0
lBF = 0
lSR = 0
l100s = 0
l50s = 0
l4s = 0
l6s = 0
lCt = 0
lSt = 0
vFORMAT = 0	
vMat = 0
vInns = 0
vNO = 0
vRuns = 0
vHS = 0
vAve = 0
vBF = 0
vSR = 0
v100s = 0
v50s = 0
v4s = 0
v6s = 0
vCt = 0
vSt = 0
wFORMAT = 0	
wMat = 0
wInns = 0
wBalls = 0
wRuns = 0
wWkts = 0
wBBI = ""
wBBM = ""
wAve = 0
wEcon = 0
wSR = 0
w4w = 0
w5w = 0
w10w = 0
pFORMAT = 0
pMat = 0
pInns = 0
pBalls = 0
pRuns = 0
pWkts = 0
pBBI = ""
pBBM = ""
pAve = 0
pEcon = 0
pSR = 0
p4w = 0
p5w = 0
p10w = 0
xFORMAT = 0
xMat = 0
xInns = 0
xBalls = 0
xRuns = 0
xWkts = 0
xBBI = ""
xBBM = ""
xAve = 0
xEcon = 0
xSR = 0
x4w = 0
x5w = 0
x10w = 0
gFORMAT = 0
gMat = 0
gInns = 0
gBalls = 0
gRuns = 0
gWkts = 0
gBBI = ""
gBBM = ""
gAve = 0
gEcon = 0
gSR = 0
g4w = 0
g5w = 0
g10w = 0
kFORMAT = 0
kMat = 0
kInns = 0
kBalls = 0
kRuns = 0
kWkts = 0
kBBI = ""
kBBM = ""
kAve = 0
kEcon = 0
kSR = 0
k4w = 0
k5w = 0
k10w = 0
yFORMAT = 0
yMat = 0
yInns = 0
yBalls = 0
yRuns = 0
yWkts = 0
yBBI = ""
yBBM = ""
yAve = 0
yEcon = 0
ySR = 0
y4w = 0
y5w = 0
y10w = 0

for row in rows:
    st = row.find_element("xpath",'(./td/span)[1]').text
    if((first.text == "Batting & Fielding" and st == "Tests" and va < cou) or (first.text == "Bowling" and st == "Tests" and va >= cou)):  
        tFORMAT = row.find_element("xpath",'(./td/span)[1]').text
        tMat = row.find_element("xpath",'(./td/span)[2]').text
        tInns = row.find_element("xpath",'(./td/span)[3]').text
        tNO = row.find_element("xpath",'(./td/span)[4]').text
        tRuns = row.find_element("xpath",'(./td/span)[5]').text
        tHS = row.find_element("xpath",'(./td/span)[6]').text
        tAve = row.find_element("xpath",'(./td/span)[7]').text
        tBF = row.find_element("xpath",'(./td/span)[8]').text
        tSR = row.find_element("xpath",'(./td/span)[9]').text
        t100s = row.find_element("xpath",'(./td/span)[10]').text
        t50s = row.find_element("xpath",'(./td/span)[11]').text
        t4s = row.find_element("xpath",'(./td/span)[12]').text
        t6s = row.find_element("xpath",'(./td/span)[13]').text
        tCt = row.find_element("xpath",'(./td/span)[14]').text
        tSt = row.find_element("xpath",'(./td/span)[15]').text
        va = va+1

    if((first.text == "Batting & Fielding" and st == "ODIs" and va < cou) or (first.text == "Bowling" and st == "ODIs" and va >= cou)):
        oFORMAT = row.find_element("xpath",'(./td/span)[1]').text
        oMat = row.find_element("xpath",'(./td/span)[2]').text
        oInns = row.find_element("xpath",'(./td/span)[3]').text
        oNO = row.find_element("xpath",'(./td/span)[4]').text
        oRuns = row.find_element("xpath",'(./td/span)[5]').text
        oHS = row.find_element("xpath",'(./td/span)[6]').text
        oAve = row.find_element("xpath",'(./td/span)[7]').text
        oBF = row.find_element("xpath",'(./td/span)[8]').text
        oSR = row.find_element("xpath",'(./td/span)[9]').text
        o100s = row.find_element("xpath",'(./td/span)[10]').text
        o50s = row.find_element("xpath",'(./td/span)[11]').text
        o4s = row.find_element("xpath",'(./td/span)[12]').text
        o6s = row.find_element("xpath",'(./td/span)[13]').text
        oCt = row.find_element("xpath",'(./td/span)[14]').text
        oSt = row.find_element("xpath",'(./td/span)[15]').text
        va = va+1

    if((first.text == "Batting & Fielding" and st == "T20Is" and va < cou) or (first.text == "Bowling" and st == "T20Is" and va >= cou)):
        uFORMAT = row.find_element("xpath",'(./td/span)[1]').text
        uMat = row.find_element("xpath",'(./td/span)[2]').text
        uInns = row.find_element("xpath",'(./td/span)[3]').text
        uNO = row.find_element("xpath",'(./td/span)[4]').text
        uRuns = row.find_element("xpath",'(./td/span)[5]').text
        uHS = row.find_element("xpath",'(./td/span)[6]').text
        uAve = row.find_element("xpath",'(./td/span)[7]').text
        uBF = row.find_element("xpath",'(./td/span)[8]').text
        uSR = row.find_element("xpath",'(./td/span)[9]').text
        u100s = row.find_element("xpath",'(./td/span)[10]').text
        u50s = row.find_element("xpath",'(./td/span)[11]').text
        u4s = row.find_element("xpath",'(./td/span)[12]').text
        u6s = row.find_element("xpath",'(./td/span)[13]').text
        uCt = row.find_element("xpath",'(./td/span)[14]').text
        uSt = row.find_element("xpath",'(./td/span)[15]').text
        va = va+1

    if((first.text == "Batting & Fielding" and st == "FC" and va < cou) or (first.text == "Bowling" and st == "FC" and va >= cou)):
        fFORMAT = row.find_element("xpath",'(./td/span)[1]').text
        fMat = row.find_element("xpath",'(./td/span)[2]').text
        fInns = row.find_element("xpath",'(./td/span)[3]').text
        fNO = row.find_element("xpath",'(./td/span)[4]').text
        fRuns = row.find_element("xpath",'(./td/span)[5]').text
        fHS = row.find_element("xpath",'(./td/span)[6]').text
        fAve = row.find_element("xpath",'(./td/span)[7]').text
        fBF = row.find_element("xpath",'(./td/span)[8]').text
        fSR = row.find_element("xpath",'(./td/span)[9]').text
        f100s = row.find_element("xpath",'(./td/span)[10]').text
        f50s = row.find_element("xpath",'(./td/span)[11]').text
        f4s = row.find_element("xpath",'(./td/span)[12]').text
        f6s = row.find_element("xpath",'(./td/span)[13]').text
        fCt = row.find_element("xpath",'(./td/span)[14]').text
        fSt = row.find_element("xpath",'(./td/span)[15]').text
        va = va+1

    if((first.text == "Batting & Fielding" and st == "List A" and va < cou) or (first.text == "Bowling" and st == "List A" and va >= cou)):
        lFORMAT = row.find_element("xpath",'(./td/span)[1]').text
        lMat = row.find_element("xpath",'(./td/span)[2]').text
        lInns = row.find_element("xpath",'(./td/span)[3]').text
        lNO = row.find_element("xpath",'(./td/span)[4]').text
        lRuns = row.find_element("xpath",'(./td/span)[5]').text
        lHS = row.find_element("xpath",'(./td/span)[6]').text
        lAve = row.find_element("xpath",'(./td/span)[7]').text
        lBF = row.find_element("xpath",'(./td/span)[8]').text
        lSR = row.find_element("xpath",'(./td/span)[9]').text
        l100s = row.find_element("xpath",'(./td/span)[10]').text
        l50s = row.find_element("xpath",'(./td/span)[11]').text
        l4s = row.find_element("xpath",'(./td/span)[12]').text
        l6s = row.find_element("xpath",'(./td/span)[13]').text
        lCt = row.find_element("xpath",'(./td/span)[14]').text
        lSt = row.find_element("xpath",'(./td/span)[15]').text
        va = va+1

    if((first.text == "Batting & Fielding" and st == "T20s" and va < cou) or (first.text == "Bowling" and st == "T20s" and va >= cou)):
        vFORMAT = row.find_element("xpath",'(./td/span)[1]').text
        vMat = row.find_element("xpath",'(./td/span)[2]').text
        vInns = row.find_element("xpath",'(./td/span)[3]').text
        vNO = row.find_element("xpath",'(./td/span)[4]').text
        vRuns = row.find_element("xpath",'(./td/span)[5]').text
        vHS = row.find_element("xpath",'(./td/span)[6]').text
        vAve = row.find_element("xpath",'(./td/span)[7]').text
        vBF = row.find_element("xpath",'(./td/span)[8]').text
        vSR = row.find_element("xpath",'(./td/span)[9]').text
        v100s = row.find_element("xpath",'(./td/span)[10]').text
        v50s = row.find_element("xpath",'(./td/span)[11]').text
        v4s = row.find_element("xpath",'(./td/span)[12]').text
        v6s = row.find_element("xpath",'(./td/span)[13]').text
        vCt = row.find_element("xpath",'(./td/span)[14]').text
        vSt = row.find_element("xpath",'(./td/span)[15]').text
        va = va+1

    if((first.text == "Batting & Fielding" and st == "Tests" and va >= cou) or (first.text == "Bowling" and st == "Tests" and va < cou)):  
        wFORMAT = row.find_element("xpath",'(./td/span)[1]').text
        wMat = row.find_element("xpath",'(./td/span)[2]').text
        wInns = row.find_element("xpath",'(./td/span)[3]').text
        wBalls = row.find_element("xpath",'(./td/span)[4]').text
        wRuns = row.find_element("xpath",'(./td/span)[5]').text
        wWkts = row.find_element("xpath",'(./td/span)[6]').text
        wBBI = row.find_element("xpath",'(./td/span)[7]').text
        wBBM = row.find_element("xpath",'(./td/span)[8]').text
        wAve = row.find_element("xpath",'(./td/span)[9]').text
        wEcon = row.find_element("xpath",'(./td/span)[10]').text
        wSR = row.find_element("xpath",'(./td/span)[11]').text
        w4w = row.find_element("xpath",'(./td/span)[12]').text
        w5w = row.find_element("xpath",'(./td/span)[13]').text
        w10w = row.find_element("xpath",'(./td/span)[14]').text
        va = va+1

    if((first.text == "Batting & Fielding" and st == "ODIs" and va >= cou) or (first.text == "Bowling" and st == "ODIs" and va < cou)):
        pFORMAT = row.find_element("xpath",'(./td/span)[1]').text
        pMat = row.find_element("xpath",'(./td/span)[2]').text
        pInns = row.find_element("xpath",'(./td/span)[3]').text
        pBalls = row.find_element("xpath",'(./td/span)[4]').text
        pRuns = row.find_element("xpath",'(./td/span)[5]').text
        pWkts = row.find_element("xpath",'(./td/span)[6]').text
        pBBI = row.find_element("xpath",'(./td/span)[7]').text
        pBBM = row.find_element("xpath",'(./td/span)[8]').text
        pAve = row.find_element("xpath",'(./td/span)[9]').text
        pEcon = row.find_element("xpath",'(./td/span)[10]').text
        pSR = row.find_element("xpath",'(./td/span)[11]').text
        p4w = row.find_element("xpath",'(./td/span)[12]').text
        p5w = row.find_element("xpath",'(./td/span)[13]').text
        p10w = row.find_element("xpath",'(./td/span)[14]').text
        va = va+1

    if((first.text == "Batting & Fielding" and st == "T20Is" and va >= cou) or (first.text == "Bowling" and st == "T20Is" and va < cou)):
        xFORMAT = row.find_element("xpath",'(./td/span)[1]').text
        xMat = row.find_element("xpath",'(./td/span)[2]').text
        xInns = row.find_element("xpath",'(./td/span)[3]').text
        xBalls = row.find_element("xpath",'(./td/span)[4]').text
        xRuns = row.find_element("xpath",'(./td/span)[5]').text
        xWkts = row.find_element("xpath",'(./td/span)[6]').text
        xBBI = row.find_element("xpath",'(./td/span)[7]').text
        xBBM = row.find_element("xpath",'(./td/span)[8]').text
        xAve = row.find_element("xpath",'(./td/span)[9]').text
        xEcon = row.find_element("xpath",'(./td/span)[10]').text
        xSR = row.find_element("xpath",'(./td/span)[11]').text
        x4w = row.find_element("xpath",'(./td/span)[12]').text
        x5w = row.find_element("xpath",'(./td/span)[13]').text
        x10w = row.find_element("xpath",'(./td/span)[14]').text
        va = va+1

    if((first.text == "Batting & Fielding" and st == "FC" and va >= cou) or (first.text == "Bowling" and st == "FC" and va < cou)):
        gFORMAT = row.find_element("xpath",'(./td/span)[1]').text
        gMat = row.find_element("xpath",'(./td/span)[2]').text
        gInns = row.find_element("xpath",'(./td/span)[3]').text
        gBalls = row.find_element("xpath",'(./td/span)[4]').text
        gRuns = row.find_element("xpath",'(./td/span)[5]').text
        gWkts = row.find_element("xpath",'(./td/span)[6]').text
        gBBI = row.find_element("xpath",'(./td/span)[7]').text
        gBBM = row.find_element("xpath",'(./td/span)[8]').text
        gAve = row.find_element("xpath",'(./td/span)[9]').text
        gEcon = row.find_element("xpath",'(./td/span)[10]').text
        gSR = row.find_element("xpath",'(./td/span)[11]').text
        g4w = row.find_element("xpath",'(./td/span)[12]').text
        g5w = row.find_element("xpath",'(./td/span)[13]').text
        g10w = row.find_element("xpath",'(./td/span)[14]').text
        va = va+1

    if((first.text == "Batting & Fielding" and st == "List A" and va >= cou) or (first.text == "Bowling" and st == "List A" and va < cou)):
        kFORMAT = row.find_element("xpath",'(./td/span)[1]').text
        kMat = row.find_element("xpath",'(./td/span)[2]').text
        kInns = row.find_element("xpath",'(./td/span)[3]').text
        kBalls = row.find_element("xpath",'(./td/span)[4]').text
        kRuns = row.find_element("xpath",'(./td/span)[5]').text
        kWkts = row.find_element("xpath",'(./td/span)[6]').text
        kBBI = row.find_element("xpath",'(./td/span)[7]').text
        kBBM = row.find_element("xpath",'(./td/span)[8]').text
        kAve = row.find_element("xpath",'(./td/span)[9]').text
        kEcon = row.find_element("xpath",'(./td/span)[10]').text
        kSR = row.find_element("xpath",'(./td/span)[11]').text
        k4w = row.find_element("xpath",'(./td/span)[12]').text
        k5w = row.find_element("xpath",'(./td/span)[13]').text
        k10w = row.find_element("xpath",'(./td/span)[14]').text
        va = va+1

    if((first.text == "Batting & Fielding" and st == "T20s" and va >= cou) or (first.text == "Bowling" and st == "T20s" and va < cou)):
        yFORMAT = row.find_element("xpath",'(./td/span)[1]').text
        yMat = row.find_element("xpath",'(./td/span)[2]').text
        yInns = row.find_element("xpath",'(./td/span)[3]').text
        yBalls = row.find_element("xpath",'(./td/span)[4]').text
        yRuns = row.find_element("xpath",'(./td/span)[5]').text
        yWkts = row.find_element("xpath",'(./td/span)[6]').text
        yBBI = row.find_element("xpath",'(./td/span)[7]').text
        yBBM = row.find_element("xpath",'(./td/span)[8]').text
        yAve = row.find_element("xpath",'(./td/span)[9]').text
        yEcon = row.find_element("xpath",'(./td/span)[10]').text
        ySR = row.find_element("xpath",'(./td/span)[11]').text
        y4w = row.find_element("xpath",'(./td/span)[12]').text
        y5w = row.find_element("xpath",'(./td/span)[13]').text
        y10w = row.find_element("xpath",'(./td/span)[14]').text
        va = va+1

teams = driver.find_elements("xpath",'//div/div/div/div/a/span/span')
t0 = teams[0].text
teamall=""

for t in teams:
    teamall=teamall+t.text+","


infor = driver.find_elements("xpath",'//div/div/div[@class="ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-4 ds-mb-8"]/div//p')
fn=0
born=0
aka=0
bats=0
bows=0
rol=0
fiepo=0

vv=0

for i in infor:
    if(vv==1):
        fn=i.text
        vv=0
    if(vv==2):
        born=i.text
        vv=0
    if(vv==3):
        aka=i.text
        vv=0
    if(vv==4):
        bats=i.text
        vv=0
    if(vv==5):
        bows=i.text
        vv=0
    if(vv==6):
        rol=i.text
        vv=0
    if(vv==7):
        fiepo=i.text
        vv=0
    if(i.text == "FULL NAME"):
        vv=1
    if(i.text == "BORN"):
        vv=2
    if(i.text == "ALSO KNOWN AS"):
        vv=3
    if(i.text == "BATTING STYLE"):
        vv=4
    if(i.text == "BOWLING STYLE"):
        vv=5
    if(i.text == "PLAYING ROLE"):
        vv=6
    if(i.text == "FIELDING POSITION"):
        vv=7
    


driver.quit()

df = pd.DataFrame({'ID':[id], 'Name':[nname], 'Full Name':[fn], 'Born':[born], 'Also Known As':[aka], 'Batting Style':[bats], 'Bowling Style':[bows], 'Playing Role':[rol], 'Fielding Position':[fiepo], 'Main Team':[t0], 'All Teams':[teamall], 'Tests Matches':[tMat], 'Tests Innings':[tInns], 'Tests NO':[tNO], 'Tests Runs':[tRuns], 'Tests HS':[tHS], 'Tests Average':[tAve], 'Tests BF':[tBF], 'Tests SR':[tSR], 'Tests 100s':[t100s], 'Tests 50s':[t50s], 'Tests 4s':[t4s], 'Tests 6s':[t6s], 'Tests Catches':[tCt], 'Tests Stumpings':[tSt], 'ODIs Matches':[oMat], 'ODIs Innings':[oInns], 'ODIs NO':[oNO], 'ODIs Runs':[oRuns], 'ODIs HS':[oHS], 'ODIs Average':[oAve], 'ODIs BF':[oBF], 'ODIs SR':[oSR], 'ODIs 100s':[o100s], 'ODIs 50s':[o50s], 'ODIs 4s':[o4s], 'ODIs 6s':[o6s], 'ODIs Catches':[oCt], 'ODIs Stumpings':[oSt], 'T20Is Matches':[uMat], 'T20Is Innings':[uInns], 'T20Is NO':[uNO], 'T20Is Runs':[uRuns], 'T20Is HS':[uHS], 'T20Is Average':[uAve], 'T20Is BF':[uBF], 'T20Is SR':[uSR], 'T20Is 100s':[u100s], 'T20Is 50s':[u50s], 'T20Is 4s':[u4s], 'T20Is 6s':[u6s], 'T20Is Catches':[uCt], 'T20Is Stumpings':[uSt], 'FC Matches':[fMat], 'FC Innings':[fInns], 'FC NO':[fNO], 'FC Runs':[fRuns], 'FC HS':[fHS], 'FC Average':[fAve], 'FC BF':[fBF], 'FC SR':[fSR], 'FC 100s':[f100s], 'FC 50s':[f50s], 'FC 4s':[f4s], 'FC 6s':[f6s], 'FC Catches':[fCt], 'FC Stumpings':[fSt], 'List A Matches':[lMat], 'List A Innings':[lInns], 'List A NO':[lNO], 'List A Runs':[lRuns], 'List A HS':[lHS], 'List A Average':[lAve], 'List A BF':[lBF], 'List A SR':[lSR], 'List A 100s':[l100s], 'List A 50s':[l50s], 'List A 4s':[l4s], 'List A 6s':[l6s], 'List A Catches':[lCt], 'List A Stumpings':[lSt], 'T20s Matches':[vMat], 'T20s Innings':[vInns], 'T20s NO':[vNO], 'T20s Runs':[vRuns], 'T20s HS':[vHS], 'T20s Average':[vAve], 'T20s BF':[vBF], 'T20s SR':[vSR], 'T20s 100s':[v100s], 'T20s 50s':[v50s], 'T20s 4s':[v4s], 'T20s 6s':[v6s], 'T20s Catches':[vCt], 'T20s Stumpings':[vSt], 'Tests Matches(Bow)':[wMat], 'Tests Innings(Bow)':[wInns], 'Tests Balls':[wBalls], 'Tests Runs(Bow)':[wRuns], 'Tests Wickets':[wWkts], 'Tests BBI':[wBBI], 'Tests BBM':[wBBM], 'Tests Average(Bow)':[wAve], 'Tests ER':[wEcon], 'Tests SR(Bow)':[wSR], 'Tests 4w':[w4w], 'Tests 5w':[w5w], 'Tests 10w':[w10w], 'ODIs Matches(Bow)':[pMat], 'ODIs Innings(Bow)':[pInns], 'ODIs Balls':[pBalls], 'ODIs Runs(Bow)':[pRuns], 'ODIs Wickets':[pWkts], 'ODIs BBI':[pBBI], 'ODIs BBM':[pBBM], 'ODIs Average(Bow)':[pAve], 'ODIs ER':[pEcon], 'ODIs SR(Bow)':[pSR], 'ODIs 4w':[p4w], 'ODIs 5w':[p5w], 'ODIs 10w':[p10w], 'T20Is Matches(Bow)':[xMat], 'T20Is Innings(Bow)':[xInns], 'T20Is Balls':[xBalls], 'T20Is Runs(Bow)':[xRuns], 'T20Is Wickets':[xWkts], 'T20Is BBI':[xBBI], 'T20Is BBM':[xBBM], 'T20Is Average(Bow)':[xAve], 'T20Is ER':[xEcon], 'T20Is SR(Bow)':[xSR], 'T20Is 4w':[x4w], 'T20Is 5w':[x5w], 'T20Is 10w':[x10w], 'FC Matches(Bow)':[gMat], 'FC Innings(Bow)':[gInns], 'FC Balls':[gBalls], 'FC Runs(Bow)':[gRuns], 'FC Wickets':[gWkts], 'FC BBI':[gBBI], 'FC BBM':[gBBM], 'FC Average(Bow)':[gAve], 'FC ER':[gEcon], 'FC SR(Bow)':[gSR], 'FC 4w':[g4w], 'FC 5w':[g5w], 'FC 10w':[g10w], 'List A Matches(Bow)':[kMat], 'List A Innings(Bow)':[kInns], 'List A Balls':[kBalls], 'List A Runs(Bow)':[kRuns], 'List A Wickets':[kWkts], 'List A BBI':[kBBI], 'List A BBM':[kBBM], 'List A Average(Bow)':[kAve], 'List A ER':[kEcon], 'List A SR(Bow)':[kSR], 'List A 4w':[k4w], 'List A 5w':[k5w], 'List A 10w':[k10w], 'T20s Matches(Bow)':[yMat], 'T20s Innings(Bow)':[yInns], 'T20s Balls':[yBalls], 'T20s Runs(Bow)':[yRuns], 'T20s Wickets':[yWkts], 'T20s BBI':[yBBI], 'T20s BBM':[yBBM], 'T20s Average(Bow)':[yAve], 'T20s ER':[yEcon], 'T20s SR(Bow)':[ySR], 'T20s 4w':[y4w], 'T20s 5w':[y5w], 'T20s 10w':[y10w]})

df.to_csv('master.csv', mode='a', header=False, index=False)

