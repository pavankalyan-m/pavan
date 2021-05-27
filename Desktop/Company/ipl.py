import numpy
from numpy import random
mi=['Rohit Sharma(c)(bt)','Quinton de Kock(wk)(bt)','SuryaKumar Yadav(bt)','Ishan Kishan(bt)','Hardik Pandya(alr)','Kieron Pollard(alr)','Krunal Pandya(alr)','Bumrah(b)','Trent Boult(b)','Rahul Chahar(b)','James Pattinson(b)']
mi_bat={'Rohit Sharma(c)(bt)': 0, 'Quinton de Kock(wk)(bt)': 0, 'SuryaKumar Yadav(bt)': 0, 'Ishan Kishan(bt)': 0, 'Hardik Pandya(alr)': 0, 'Kieron Pollard(alr)': 0, 'Krunal Pandya(alr)': 0, 'Bumrah(b)': 0, 'Trent Boult(b)': 0, 'Rahul Chahar(b)': 0, 'James Pattinson(b)': 0}
mi_bowl={'Hardik Pandya(alr)': 0, 'Kieron Pollard(alr)': 0, 'Krunal Pandya(alr)': 0, 'Bumrah(b)': 0, 'Trent Boult(b)': 0, 'Rahul Chahar(b)': 0, 'James Pattinson(b)': 0}
list_mi_bowl=['Hardik Pandya(alr)','Kieron Pollard(alr)','Krunal Pandya(alr)','Bumrah(b)','Trent Boult(b)','Rahul Chahar(b)','James Pattinson(b)']
mi_bowl_w={'Hardik Pandya(alr)': 0, 'Kieron Pollard(alr)': 0, 'Krunal Pandya(alr)': 0, 'Bumrah(b)': 0, 'Trent Boult(b)': 0, 'Rahul Chahar(b)': 0, 'James Pattinson(b)': 0}
csk=['Watson(bt)', 'Duplesis(bt)', 'Rayudu(bt)', 'MS Dhoni(wk)(c)(bt)', 'Sam Curran(alr)', 'Ravindra Jadeja(alr)', 'Dwayne Bravo(alr)', 'Piyush Chawla(b)', 'Deepak Chahar(b)', 'Shardul Thakur(b)', 'Karn Sharma(b)']
csk_bat={'Watson(bt)': 0, 'Duplesis(bt)': 0, 'Rayudu(bt)': 0, 'MS Dhoni(wk)(c)(bt)': 0, 'Sam Curran(alr)': 0, 'Ravindra Jadeja(alr)': 0, 'Dwayne Bravo(alr)': 0, 'Piyush Chawla(b)': 0, 'Deepak Chahar(b)': 0, 'Shardul Thakur(b)': 0, 'Karn Sharma(b)': 0}
csk_bowl={'Sam Curran(alr)': 0, 'Ravindra Jadeja(alr)': 0, 'Dwayne Bravo(alr)': 0, 'Piyush Chawla(b)': 0, 'Deepak Chahar(b)': 0, 'Shardul Thakur(b)': 0, 'Karn Sharma(b)': 0}    
list_csk_bowl=['Sam Curran(alr)', 'Ravindra Jadeja(alr)', 'Dwayne Bravo(alr)', 'Piyush Chawla(b)', 'Deepak Chahar(b)', 'Shardul Thakur(b)', 'Karn Sharma(b)']
csk_bowl_w={'Sam Curran(alr)': 0, 'Ravindra Jadeja(alr)': 0, 'Dwayne Bravo(alr)': 0, 'Piyush Chawla(b)': 0, 'Deepak Chahar(b)': 0, 'Shardul Thakur(b)': 0, 'Karn Sharma(b)': 0}
l=0;n1=0;n2=0;y=0
def scorecard(r,w,ex,sixes,fours,dot,team,team_bat,team_bowl,team_bowl_w):
    print(team_bat)
    print("overs bowled=",team_bowl)
    print("wickets taken=",team_bowl_w)
    print("total=",r)
    print("dot balls=",dot)
    print("wickets=",w)
    print("Extras=",ex)
    print("No of Sixes=",sixes)
    print("No of fours=",fours)
class ipl:
    def __init__(self,team_bowl):
        self.team_bowl=team_bowl
        self.l=l
    def bowl(self,n):
      k=random.choice(n)
      if(self.team_bowl[k]>=4):
        return self.bowl(n)
      else:
        self.team_bowl[k]=self.team_bowl[k]+1
      return k
    def kalyan(self,y,score,team,list_bowl,team_bowl_w,team_bat):
      self.y=y
      self.score=score
      team=list(team)
      list_bowl=list(list_bowl)
      team_bowl_w=dict(team_bowl_w)
      a=team[0];b=team[1];temp="";dot=0;sixes=0;fours=0;w=0;r=0;ex=0
      for i in range(1,21):
          if(w==10):
              break
          if(self.y==2):
            break
          n=6
          z=self.bowl(list_bowl)
          print("----------------",i,z,"----------------")
          while(n!=0 and w<10):
              if(y==1 and r>score):
                return r,w,ex,sixes,fours,dot,team,team_bat,self.team_bowl,team_bowl_w
              k=random.randint(0,9)
              if(k==0):
                  w+=1
                  print("wicket")
                  team.remove(a)
                  if(w<9):
                      a=team[1]
                  else:
                      a=team[0]
                  team_bowl_w[z]+=1
              elif(k>=1 and k<=6):
                  team_bat[a]+=k
                  if(k%2!=0):
                      temp=b
                      b=a
                      a=temp
                  if(k==4):
                      fours+=1
                  elif(k==6):
                      sixes+=1
                  print(k)
                  r+=k
              elif(k==7):
                  print("wide")
                  r+=1
                  n+=1
                  ex+=1
              elif(k==8):
                  print("no ball",end=" ")
                  n+=2
              elif(k==9):
                  dot+=1
                  print("dot ball")
              n-=1
          temp=b
          b=a
          a=temp
      return r,w,ex,sixes,fours,dot,team,team_bat,self.team_bowl,team_bowl_w
team,innings=random.choice(['Rohit Sharma','MS Dhoni']),random.choice(['bat','bowl'])
print(team,innings)
print("------------------------------------1st Innings--------------------------")
if((team=="Rohit Sharma" and innings=="bowl") or (team=="MS Dhoni" and innings=="bat")):
    object1=ipl(mi_bowl)
    r,w,ex,sixes,fours,dot,team,team_bat,team_bowl,team_bowl_w=object1.kalyan(y,n2,tuple(csk),tuple(list_mi_bowl),mi_bowl_w,csk_bat)
    scorecard(r,w,ex,sixes,fours,dot,team,team_bat,team_bowl,team_bowl_w)
    n1=r
    l=1
    y+=1
else:
    object1=ipl(csk_bowl)
    r,w,ex,sixes,fours,dot,team,team_bat,team_bowl,team_bowl_w=object1.kalyan(y,n1,tuple(mi),tuple(list_csk_bowl),csk_bowl_w,mi_bat)
    scorecard(r,w,ex,sixes,fours,dot,team,team_bat,team_bowl,team_bowl_w)
    n2=r
    l=2
    y+=1
print("------------------------------------2nd Innings--------------------------")
if(l==1):
    object2=ipl(csk_bowl)
    r,w,ex,sixes,fours,dot,team,team_bat,team_bowl,team_bowl_w=object2.kalyan(y,n1,tuple(mi),tuple(list_csk_bowl),csk_bowl_w,mi_bat)
    scorecard(r,w,ex,sixes,fours,dot,team,team_bat,team_bowl,team_bowl_w)
    n2=r
elif(l==2):
    object2=ipl(mi_bowl)
    r,w,ex,sixes,fours,dot,team,team_bat,team_bowl,team_bowl_w=object2.kalyan(y,n2,tuple(csk),tuple(list_mi_bowl),mi_bowl_w,csk_bat)
    scorecard(r,w,ex,sixes,fours,dot,team,team_bat,team_bowl,team_bowl_w)
    n1=r
if(n1<n2):
    print("Mumbai Indians Won the Match")
else:
    print("Chennai Super Kings Won the Match")
