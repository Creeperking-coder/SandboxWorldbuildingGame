import pygame
import random

pygame.init()

windowwidth = 800
windowheight = 800

win = pygame.display.set_mode((windowwidth, windowheight))
black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
dull_red = (150,50,50)
green = (0,255,0)
blue = (0,0,255)
grey = (129,126,130)

#teams
redT = []
greenT = []
nutralT = []

class Duckisite:
    ducks = []
    swarmducks = []
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.xgoal = random.randint(1,800)
        self.ygoal = random.randint(1,800)
        self.speed = 0.01
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("Duckisite.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        Duckisite.ducks.append(self)
        Duckisite.swarmducks.append(self)
    def tick(self, win):

        self.goal = pygame.math.Vector2(self.xgoal,self.ygoal)
        self.pos = pygame.math.Vector2(self.x,self.y)
        self.x,self.y = pygame.math.Vector2.lerp(self.pos,self.goal,self.speed)

        if random.randint(0,10) == 10:
            self.xgoal = random.randint(1, 800)
            self.ygoal = random.randint(1, 800)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)

class DuckisiteBlue:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.xgoal = random.randint(1,800)
        self.ygoal = random.randint(1,800)
        self.speed = 0.1
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("DuckisiteBlue.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        Duckisite.ducks.append(self)
    def tick(self, win):

        self.goal = pygame.math.Vector2(self.xgoal,self.ygoal)
        self.pos = pygame.math.Vector2(self.x,self.y)
        self.x,self.y = pygame.math.Vector2.lerp(self.pos,self.goal,self.speed)

        if random.randint(0,5) == 5:
            self.xgoal = random.randint(1, 800)
            self.ygoal = random.randint(1, 800)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)

class DuckisiteAbomination:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 45
        self.height = 45
        self.xgoal = random.randint(1,800)
        self.ygoal = random.randint(1,800)
        self.speed = 0.003
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("DuckisiteAbomination.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        Duckisite.ducks.append(self)
    def tick(self, win):

        self.goal = pygame.math.Vector2(self.xgoal,self.ygoal)
        self.pos = pygame.math.Vector2(self.x,self.y)
        self.x,self.y = pygame.math.Vector2.lerp(self.pos,self.goal,self.speed)

        if random.randint(0,10) == 10:
            self.xgoal = random.randint(1, 800)
            self.ygoal = random.randint(1, 800)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)

class DuckisiteHeavy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.xgoal = random.randint(1,800)
        self.ygoal = random.randint(1,800)
        self.speed = 0.004
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("Duckisite.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        Duckisite.ducks.append(self)
    def tick(self, win):

        self.goal = pygame.math.Vector2(self.xgoal,self.ygoal)
        self.pos = pygame.math.Vector2(self.x,self.y)
        self.x,self.y = pygame.math.Vector2.lerp(self.pos,self.goal,self.speed)

        if random.randint(0,20) == 10:
            self.xgoal = random.randint(1, 800)
            self.ygoal = random.randint(1, 800)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)

class DuckisiteRoom:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.upgrading = None
        self.time = 0
        self.length = 500
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.begin = False
        self.img = pygame.image.load("DuckisiteRoom.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        Duckisite.ducks.append(self)
    def tick(self, win):

        if self.upgrading == None:
            if random.randint(0,100) == 100:
                if len(Duckisite.swarmducks) != 0:
                    self.upgrading = random.choice(Duckisite.swarmducks)
        else:
            self.upgrading.xgoal = self.x
            self.upgrading.ygoal = self.y
            if self.rect.colliderect(self.upgrading.rect)==True:
                self.begin = True
        if self.begin == True:
            self.upgrading.x = self.x
            self.upgrading.y = self.y
            self.time += 1
            if self.time >= self.length:
                self.time = 0
                self.begin = False
                Duckisite.ducks.remove(self.upgrading)
                Duckisite.swarmducks.remove(self.upgrading)
                self.upgrading = None


        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)

class DuckisiteLauncher:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.time = 0
        self.length = 3000
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("DuckisiteLauncher.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        Duckisite.ducks.append(self)
    def tick(self, win):

        self.time +=1
        if self.time >= self.length:
            self.time = 0
            d = DuckisitePod(random.randint(0,800),random.randint(0,800))


        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)


class DuckisiteTower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("DuckisiteTower.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        Duckisite.ducks.append(self)

    def tick(self, win):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)

class DuckisiteBuilder:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.xgoal = random.randint(1,800)
        self.ygoal = random.randint(1,800)
        self.speed = 0.01
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("DuckisiteBuilder.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.time = 0
        self.summonsickness = 250
        Duckisite.ducks.append(self)
    def tick(self, win):

        self.goal = pygame.math.Vector2(self.xgoal,self.ygoal)
        self.pos = pygame.math.Vector2(self.x,self.y)
        self.x,self.y = pygame.math.Vector2.lerp(self.pos,self.goal,self.speed)

        if random.randint(0,10) == 10:
            self.xgoal = random.randint(1, 800)
            self.ygoal = random.randint(1, 800)

        self.time += 1
        if self.time >= self.summonsickness:
            if random.randint(0,10) == 10:
                Duckisite.ducks.remove(self)
                self.build = random.randint(0,2)
                if self.build == 0:
                    r = DuckisiteRoom(self.x,self.y)
                elif self.build == 1:
                    r = DuckisiteTower(self.x, self.y)
                elif self.build == 2:
                    r = DuckisiteLauncher(self.x, self.y)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)

class DuckisiteEgg:
    def __init__(self,x,y,ducktype):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.incubationTime = random.randint(500,1000)
        self.time = 0
        self.cargo = ducktype
        self.width = 20
        self.height = 20
        if self.cargo == 1:
            self.width = 25
            self.height = 25
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("DuckisiteEgg.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        Duckisite.ducks.append(self)
    def tick(self, win):

        self.time += 1
        if self.time >= self.incubationTime:
            if self.cargo == 0:
                d = Duckisite(self.x,self.y)
            elif self.cargo == 1:
                h = DuckisiteHeavy(self.x,self.y)
            elif self.cargo == 2:
                b = DuckisiteBuilder(self.x,self.y)
            Duckisite.ducks.remove(self)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)

class DuckisitePod:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("DuckisiteEgg.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        Duckisite.ducks.append(self)
    def tick(self, win):

        if random.randint(0,100) == 0:
            Duckisite.ducks.remove(self)
            d = Duckisite(self.x,self.y)
            d = Duckisite(self.x, self.y)
            d = Duckisite(self.x, self.y)
            d = Duckisite(self.x, self.y)
            d = DuckisiteHeavy(self.x, self.y)
            d = DuckisiteHeavy(self.x, self.y)
            d = DuckisiteBuilder(self.x, self.y)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)

class MotherDuckisite:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.xgoal = random.randint(1,800)
        self.ygoal = random.randint(1,800)
        self.speed = 0.002
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("Duckisite.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.time = 0
        self.laytime = 100
        Duckisite.ducks.append(self)
    def tick(self, win):

        self.goal = pygame.math.Vector2(self.xgoal,self.ygoal)
        self.pos = pygame.math.Vector2(self.x,self.y)
        self.x,self.y = pygame.math.Vector2.lerp(self.pos,self.goal,self.speed)

        if random.randint(0,20) == 10:
            self.xgoal = random.randint(1, 800)
            self.ygoal = random.randint(1, 800)

        self.time += 1
        if self.time >= self.laytime:
            self.time = 0
            if random.randint(0,5) != 0:
                e = DuckisiteEgg(self.x,self.y,0)
            else:
                e = DuckisiteEgg(self.x,self.y,random.randint(0,2))


        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)

class GreenMortar:
    morts = []
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 45
        self.height = 60
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("GreenMortar.png")
        self.targetx = 400
        self.targety = 400
        self.target = False
        self.reloadtime = 100
        self.reload = 0
        self.fire = False
        self.spread = 20
        self.payloadsize = 50
        self.payloadamount = 1
        self.payloadlinger = 5
        self.payloadtime = 0
        self.loads = []
        GreenMortar.morts.append(self)
        greenT.append(self)
    def tick(self, win):

        if self.target == True:
            self.reload += 1
            if self.reload >= self.reloadtime and self.fire != True:
                self.fire = True
                self.loads = []
                self.payloadtime = 0
                for i in range(self.payloadamount):
                    self.loads.append((self.targetx+random.randint(-self.spread,self.spread),self.targety+random.randint(-self.spread,self.spread)))
            pygame.draw.circle(win,dull_red,(self.targetx,self.targety),self.spread)
            if self.fire == True:
                for i in self.loads:
                    pygame.draw.circle(win,red,i,self.payloadsize)
                self.payloadtime += 1
                if self.payloadtime >= self.payloadlinger:
                    self.fire = False
                    self.payloadtime = 0
                    self.loads = []
                    self.target = False
                    self.reload = 0


        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)

class GreenSpotter:
    spots = []
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 32
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("GreenSpotter.png")
        self.img = pygame.transform.scale(self.img, (30, 48))
        self.sightrange = 200
        self.speed = 0.5
        self.xvel = 0
        self.yvel = 0
        self.change = 0
        GreenSpotter.spots.append(self)
        greenT.append(self)
    def tick(self, win):

        self.change += 1
        if self.change >= 10:
            self.change = 0
            self.xvel = random.randint(-1, 1)
            self.yvel = random.randint(-1, 1)

        self.x += self.xvel * self.speed
        self.y += self.yvel * self.speed

        for r in redT:
            if ((r.x-self.x) + (r.y-self.y))<= self.sightrange:
                for m in GreenMortar.morts:
                    if m.target != True:
                        m.target = True
                        m.targetx = r.x
                        m.targety = r.y

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)

class RedMortar:
    morts = []
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 45
        self.height = 60
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("RedMortar.png")
        self.targetx = 400
        self.targety = 400
        self.target = False
        self.reloadtime = 100
        self.reload = 0
        self.fire = False
        self.spread = 20
        self.payloadsize = 50
        self.payloadamount = 1
        self.payloadlinger = 5
        self.payloadtime = 0
        self.loads = []
        RedMortar.morts.append(self)
        redT.append(self)
    def tick(self, win):

        if self.target == True:
            self.reload += 1
            if self.reload >= self.reloadtime and self.fire != True:
                self.fire = True
                self.loads = []
                self.payloadtime = 0
                for i in range(self.payloadamount):
                    self.loads.append((self.targetx+random.randint(-self.spread,self.spread),self.targety+random.randint(-self.spread,self.spread)))
            pygame.draw.circle(win,dull_red,(self.targetx,self.targety),self.spread)
            if self.fire == True:
                for i in self.loads:
                    pygame.draw.circle(win,red,i,self.payloadsize)
                    self.loadrect = pygame.Rect(i[0]-self.payloadsize,i[1]-self.payloadsize,self.payloadsize*2,self.payloadsize*2)
                    for i in greenT:
                        if self.loadrect.colliderect(i.rect) == True:
                            greenT.remove(i)

                self.payloadtime += 1
                if self.payloadtime >= self.payloadlinger:
                    self.fire = False
                    self.payloadtime = 0
                    self.loads = []
                    self.target = False
                    self.reload = 0

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)

class RedSpotter:
    spots = []
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 32
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = pygame.image.load("RedSpotter.png")
        self.img = pygame.transform.scale(self.img, (30, 48))
        self.sightrange = 200
        self.speed = 0.5
        self.xvel = 0
        self.yvel = 0
        self.change = 0
        RedSpotter.spots.append(self)
        redT.append(self)
    def tick(self, win):

        self.change += 1
        if self.change >= 10:
            self.change = 0
            self.xvel = random.randint(-1,1)
            self.yvel = random.randint(-1,1)

        self.x += self.xvel * self.speed
        self.y += self.yvel * self.speed

        for r in greenT:
            if ((r.x-self.x) + (r.y-self.y))<= self.sightrange:
                for m in RedMortar.morts:
                    if m.target != True:
                        m.target = True
                        m.targetx = r.x
                        m.targety = r.y

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.img, self.rect)


# d = GreenMortar(200,200)
# s = GreenSpotter(400,400)
#
# r = RedMortar(200,700)
# l = RedSpotter(500,500)

m = MotherDuckisite(400,400)

run = True
while run == True:

    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    win.fill(grey)

    for g in greenT:
        g.tick(win)
    for r in redT:
        r.tick(win)
    for d in Duckisite.ducks:
        d.tick(win)

    pygame.display.update()












