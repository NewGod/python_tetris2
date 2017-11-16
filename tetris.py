import json
import numpy as np

W = 10
H = 20
N = 11

BShape = [
	[ [ 0,0,1,0,-1,0,-1,-1 ],[ 0,0,0,1,0,-1,1,-1 ],[ 0,0,-1,0,1,0,1,1 ],[ 0,0,0,-1,0,1,-1,1 ] ],
	[ [ 0,0,-1,0,1,0,1,-1 ],[ 0,0,0,-1,0,1,1,1 ],[ 0,0,1,0,-1,0,-1,1 ],[ 0,0,0,1,0,-1,-1,-1 ] ],
	[ [ 0,0,1,0,0,-1,-1,-1 ],[ 0,0,0,1,1,0,1,-1 ],[ 0,0,-1,0,0,1,1,1 ],[ 0,0,0,-1,-1,0,-1,1 ] ],
	[ [ 0,0,-1,0,0,-1,1,-1 ],[ 0,0,0,-1,1,0,1,1 ],[ 0,0,1,0,0,1,-1,1 ],[ 0,0,0,1,-1,0,-1,-1 ] ],
	[ [ 0,0,-1,0,0,1,1,0 ],[ 0,0,0,-1,-1,0,0,1 ],[ 0,0,1,0,0,-1,-1,0 ],[ 0,0,0,1,1,0,0,-1 ] ],
	[ [ 0,0,0,-1,0,1,0,2 ],[ 0,0,1,0,-1,0,-2,0 ],[ 0,0,0,1,0,-1,0,-2 ],[ 0,0,-1,0,1,0,2,0 ] ],
	[ [ 0,0,0,1,-1,0,-1,1 ],[ 0,0,-1,0,0,-1,-1,-1 ],[ 0,0,0,-1,1,-0,1,-1 ],[ 0,0,1,0,0,1,1,1 ] ]
]

rotateBlank = [
	[ [ 1,1,0,0 ],[ -1,1,0,0 ],[ -1,-1,0,0 ],[ 1,-1,0,0 ] ],
	[ [ -1,-1,0,0 ],[ 1,-1,0,0 ],[ 1,1,0,0 ],[ -1,1,0,0 ] ],
	[ [ 1,1,0,0 ],[ -1,1,0,0 ],[ -1,-1,0,0 ],[ 1,-1,0,0 ] ],
	[ [ -1,-1,0,0 ],[ 1,-1,0,0 ],[ 1,1,0,0 ],[ -1,1,0,0 ] ],
	[ [ -1,-1,-1,1,1,1,0,0 ],[ -1,-1,-1,1,1,-1,0,0 ],[ -1,-1,1,1,1,-1,0,0 ],[ -1,1,1,1,1,-1,0,0 ] ],
	[ [ 1,-1,-1,1,-2,1,-1,2,-2,2 ] ,[ 1,1,-1,-1,-2,-1,-1,-2,-2,-2 ] ,[ -1,1,1,-1,2,-1,1,-2,2,-2 ] ,[ -1,-1,1,1,2,1,1,2,2,2 ] ],
	[ [ 0,0 ],[ 0,0 ] ,[ 0,0 ] ,[ 0,0 ] ]
]

currBotColor = 0
enemyColor = 0
gridInfo = np.zeros((2,H+2,W+2)).astype("int32").tolist()
trans = np.zeros((2,6,W+2)).astype("int32").tolist()
transCount = [0]*2
maxHeight = [0]*2
elimTotal = [0]*2
elimCombo = [0]*2
elimBonus = [0,1,3,5,7]
typeCountForColor = [[0]*7,[0]*7]
 
xx = [0, 0, 1, -1];
yy = [1, -1, 0, 0];

class Tetris:
    def __init__(self,t,color):
        self.BType = t
        self.shape = BShape[t]
        self.color = color 

    def set(self, x, y, o):
        self.BX = x 
        self.BY = y
        self.BO = o
        return self

    def isValid(self,x=-1,y=-1,o=-1):
        x = self.BX if x==-1 else x
        y = self.BY if y==-1 else y
        o = self.BO if o==-1 else o
        if o<0 or o>3 :
            return False

        for i in range(4):
            tmpX = x + self.shape[o][2*i]
            tmpY = y + self.shape[o][2*i+1];
            if tmpX < 1 or tmpX > W or tmpY < 1 or tmpY > H or gridInfo[self.color][tmpY][tmpX] != 0:
                return False
            
        return True

    def onGround(self):
        if self.isValid() and not self.isValid(-1,self.BY-1):
            return True
        return False
    
    def place(self,rec):
        PH = 100
        if rec == True : 
            ++RECID
            REC[RECID] = copy.deepcopy(gridInfo[self.color])
            REC2[RECID] = copy.deepcopy(val)
            #use deepcopy 
        if self.onGround() == False:
            return ;
        for i in range(4):
            tmpX = self.BX + self.shape[self.BO][2*i]
            tmpY = self.BY + self.shape[self.BO][2*i+1]
            PH = min(PH,tmpY)
            gridInfo[self.color][tmpY][tmpX] = 2

    def rotation(self, o):
        if o < 0 or o > 3 :
            return False
        if BO==o:
            return True
        fromO = BO
        while True:
            if isValid(-1,-1,fromO)!=False :
                return False
            if (fromO==o):
                break
            for i in range(5):
                blankX = self.BX + rotateBlank[self.BType][fromO][2*i]
                blankY = self.BY + rotateBlank[self.BType][fromO][2*i+1]
                if (blankX == self.BX and self.blankY == BY):
                    break
                if gridInfo[self.color][blankY][blankX] != 0:
                    return False
            fromO = (fromO + 1)%4
        return True

def init():
    for i in range(H+2):
        gridInfo[1][i][0]=gridInfo[0][i][0]=gridInfo[1][i][W+1]=gridInfo[0][i][W+1]=-2
    for i in range(W+2):
        gridInfo[1][0][i]=gridInfo[1][H+1][i]=gridInfo[0][0][i]=gridInfo[0][H+1][i]=-2
        

class Util:
    def checkDirectDropTo(color,BType,x,y,o):
        Def = BShape[BType][o]
        for Y in range(y,H+1):
            for i in range(4):
                _x = Def[i*2]+x
                _y = Def[i*2+1]+Y
                if _y > H :
                    continue
                if _y < 1 or _x < 1 or _x > W or gridInfo[color][_y][_x]:
                    return False
        return True

    def eliminate(color):
        transCount[color] = 0
        count = 0
        maxHeight[color] = H 
        hasBonus = 0
        firstFull = 1
        for i in range(1,H+1):
            emptyFlag = True
            fullFlag = True
            for j in range(1,W+1):
                if gridInfo[color][i][j] == 0 :
                    fullFlag = False
                else :
                    emptyFlag = False
            if fullFlag:
                if firstFull :
                    elimCombo[color] += 1
                    if elimCombo[color] >= 3:
                        for j in range(1,W+1):
                            trans[color][count][j] = 1 if gridInfo[color][i][j]==1 else 0
                        count+=1
                        hasBonus = 1
                firstFull = 0
                for j in range(1,W+1):
                    trans[color][count][j] = 1 if gridInfo[color][i][j]==1 else 0
                    gridInfo[color][i][j]=0
                count += 1
            else:
                if emptyFlag==True:
                    maxHeight[color] = i-1
                    break
                else :
                    for j in range(1,W+1):
                        gridInfo[color][i-count+hasBonus][j] = 1 if gridInfo[color][i][j] > 0 else gridInfo[color][i][j]
                        if count:
                            gridInfo[color][i][j] = 0
        if count == 0 :
            elimCombo[color] = 0
        maxHeight[color] -= count - hasBonus
        elimTotal[color] += elimBonus[count-hasBonus]
        transCount[color] = count

    def transfer():
        color1 = 0 
        color2 = 1
        if transCount[color1]==0 and transCount[color2] ==0 :
            return -1
        if transCount[color1]==0 or transCount[color2] == 0 :
            if transCount[color1]==0 and transCount[color2] > 0 :
                color1,color2 = color2,color1
            h2 = maxHeight[color2] + transCount[color1]
            maxHeight[color2] = h2
            if h2 > H :
                return color2
            for i in range(h2,transCount[color1],-1):
                for j in range(1,W+1):
                    gridInfo[color2][i][j] = gridInfo[color2][i-transCount[color1]][j]
            for i in range(transCount[color1],0,-1):
                for j in range(1,W+1):
                    gridInfo[color2][i][j] = trans[color1][i-1][j]
            return -1
        else : 
            h1 = maxHeight[color1]+transCount[color2]
            maxHeight[color1] = h1
            h2 = maxHeight[color2]+transCount[color1]
            maxHeight[color2] = h2
            if h1 > H :
                return color1
            if h2 > H :
                return color2
            
            for i in range(h2,transCount[color1],-1):
                for j in range(1,W+1):
                    gridInfo[color2][i][j] = gridInfo[color2][i-transCount[color1]][j]

            for i in range(transCount[color1],0,-1):
                for j in range(1,W+1):
                    gridInfo[color2][i][j] = trans[color1][i-1][j]

            for i in range(h1,transCount[color2],-1):
                for j in range(1,W+1):
                    gridInfo[color1][i][j] = gridInfo[color1][i-transCount[color2]][j]

            for i in range(transCount[color2],0,-1):
                for j in range(1,W+1):
                    gridInfo[color1][i][j] = trans[color2][i-1][j]

            return -1

    
    def printField():
        i2s = ['~~','~~','  ','[]','##']
        print("~~: 墙, []: 块, ##: 新块")
        for y in range(H+1,-1,-1):
            for x in range(0,W+2):
                print(i2s[gridInfo[0][y][x]+2],end='')
            for x in range(0,W+2):
                print(i2s[gridInfo[1][y][x]+2],end='')
            print()

# 解析读入的JSON
if __name__=="__main__":


    init()
    turnID = int(input())
    BType,currBotColor = list(map(int,input().split()))

    enemyColor = 1 - currBotColor
    nextTypeForColor = [BType,BType]
    typeCountForColor[0][BType] = typeCountForColor[1][BType] = 1
    #add(0, BType, 1)
    #add(1, BType, 1)
    for i in range(1,turnID):
        currTypeForColor = nextTypeForColor[:]
        BType,x,y,o = list(map(int,input().split()))
        myB = Tetris(currTypeForColor[currBotColor],currBotColor)
        myB.set(x,y,o).place(0)
        #add(enemyColor, BType, 1)
        typeCountForColor[enemyColor][BType]+=1
        nextTypeForColor[enemyColor] = BType;
        
        BType,x,y,o = list(map(int,input().split()))
        enemyB = Tetris(currTypeForColor[enemyColor],enemyColor)
        enemyB.set(x,y,o).place(0)
        #add(currBotColor, BType, 1)
        typeCountForColor[currBotColor][BType]+=1
        nextTypeForColor[currBotColor] = BType;
        Util.eliminate(0)
        Util.eliminate(1)
        Util.transfer()

        #if __debug__ : 
        #    Util.printField()



# TODO: 作出决策并输出
    block = Tetris(nextTypeForColor[currBotColor],currBotColor);
    for y in range(1,H+1):
        for x in range(1,W+1):
            for o in range(4):
                if block.set(x,y,o).isValid() and Util.checkDirectDropTo(currBotColor,block.BType,x,y,o):
                    def detemined():
                        maxCount = max(typeCountForColor[enemyColor])
                        minCount = min(typeCountForColor[enemyColor])

                        if maxCount - minCount == 2:
                            for i in range(7):
                                if typeCountForColor[enemyColor][i]!=maxCount:
                                    return i
                        else :
                            return np.random.randint(7)
                    finalX = x
                    finalY = y
                    finalO = o
                    blockForEnemy = detemined()

                    my_action = { "x": finalX, "y": finalY,"o": finalO,"block": blockForEnemy }
                    print(blockForEnemy,finalX,finalY,finalO)

                    exit(0)
