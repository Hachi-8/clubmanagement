from django.db.models.aggregates import Count, Sum
from django.shortcuts import render,redirect
from django.views import View
from .models import Conditions, MatchResultDetail, freeThrough, threeMen, MatchResult, Shooting
import datetime
from registration.models import UserDetail
from django.contrib.auth.models import User
import json
# Create your views here.
class Toppage_View(View): 
    def get(self, request, *args, **kwargs):  
        return render(request, 'club_management/top_page.html')

class Mypage_View(View):  
    def get(self, request, *args, **kwargs):
        myCondition = Conditions.objects.filter(name=request.user) 
        return render(request, 'club_management/my_page.html',{"myCondition":myCondition})

    def post(self, request, *args, **kwargs):
        if Conditions.objects.filter(name=request.user, date=datetime.date.today()).count()>0:
            date = datetime.date.today()
            bodyTemperature = request.POST.get("体温")
            cough = request.POST.get("咳")
            dyspnea = request.POST.get("息苦しさ")
            soreThroat = request.POST.get("喉の痛み")
            malaise = request.POST.get("倦怠感")
            abnormalTasteAndSmell = request.POST.get("味覚嗅覚異常")
            name = self.request.user
            other = request.POST.get("その他") 

            Conditions.objects.filter(name=request.user, date=datetime.date.today()).update(date=date,name=name,bodyTemperature=bodyTemperature, cough=cough, dyspnea=dyspnea, soreThroat=soreThroat, malaise=malaise, abnormalTasteAndSmell=abnormalTasteAndSmell,other=other)
            
            myCondition = Conditions.objects.filter(name=request.user)
            return render(request, 'club_management/my_page.html', {"myCondition":myCondition})

        else:
            date = datetime.date.today()
            bodyTemperature = request.POST.get("体温")
            cough = request.POST.get("咳")
            dyspnea = request.POST.get("息苦しさ")
            soreThroat = request.POST.get("喉の痛み")
            malaise = request.POST.get("倦怠感")
            abnormalTasteAndSmell = request.POST.get("味覚嗅覚異常")
            name = self.request.user
            other = request.POST.get("その他")

            condition = Conditions(date=date,name=name, bodyTemperature=bodyTemperature, cough=cough, dyspnea=dyspnea, soreThroat=soreThroat, malaise=malaise, abnormalTasteAndSmell=abnormalTasteAndSmell,other=other)
            condition.save()

            myCondition = Conditions.objects.filter(name=request.user)
            return render(request, 'club_management/my_page.html', {"myCondition":myCondition})

        

class Practice_View(View):  
    def get(self, request, *args, **kwargs): 
        d = datetime.date.today()
        fd = d.replace(day=1)
        twoWeeksAgo = d - datetime.timedelta(days=14)
        weekAgo = d - datetime.timedelta(days=7)

        players = UserDetail.objects.filter(position="プレイヤー")
        threeMenData = threeMen.objects.filter(date__range=[weekAgo,d])[::-1]
        freeThroughData = {}
        shootingData = {}

        for player in players:
            if freeThrough.objects.filter(date__range=[fd,d], name=player.name).count()>0:
                makeSum = freeThrough.objects.filter(date__range=[fd,d], name=player.name).aggregate(Sum("make"))["make__sum"]
                attemptSum = freeThrough.objects.filter(date__range=[fd,d], name=player.name).aggregate(Sum("attempt"))["attempt__sum"]
                probability = makeSum/attemptSum*100
                freeThroughData[player.name]=[makeSum,attemptSum, probability]
            else:
                freeThroughData[player.name]=[0,0,"データなし"]
            
            if Shooting.objects.filter(date__range=[twoWeeksAgo,d], name=player.name).count()>0:
                shootingMakeSum = Shooting.objects.filter(date__range=[twoWeeksAgo,d], name=player.name).aggregate(Sum("make"))["make__sum"]
                shootingAttemptSum = Shooting.objects.filter(date__range=[twoWeeksAgo,d], name=player.name).aggregate(Sum("attempt"))["attempt__sum"]
                rate = shootingMakeSum/shootingAttemptSum*100
                shootingData[player.name] = [shootingAttemptSum,shootingMakeSum,rate]
            else:
                shootingData[player.name] = [0,0,"データなし"]

        return render(request, 'club_management/practice_page.html', {"players":players, "threeMenData":threeMenData,"freeThroughData":freeThroughData, "shootingData":shootingData})
    
    

class PracticeForm_View(View):  
    def get(self, request, *args, **kwargs): 
        players = UserDetail.objects.filter(position="プレイヤー")
        return render(request, "club_management/practiceform_page.html", {"players":players})

    def post(self, request, *args, **kwargs):

        if "3men" in request.POST:
            attempt = request.POST.get("3men_attempt")
            make = request.POST.get("3men_make")
            accomplish = request.POST.get("達成")

            data = threeMen(date=datetime.date.today(), attempt=attempt, make=make, accomplish=accomplish)
            data.save()

        elif "freeThroughMake" in request.POST:

            players = UserDetail.objects.filter(position="プレイヤー")
            nums = request.POST.getlist("freeThroughMake")

            for (num, player) in zip(nums, players):
                user = User.objects.get(username=player.name)
                data = freeThrough(name=user, date=datetime.date.today(), attempt=2, make=int(num))
                data.save()
        elif "shooting" in request.POST:
            players = UserDetail.objects.filter(position="プレイヤー")
            for player in players:
                attemptName = str(player.name) + "_shootingAttempt"
                makeName = str(player.name) + "_shootingMake"
                
                attempt = request.POST.get(attemptName)
                make = request.POST.get(makeName)
                name = User.objects.get(username=player.name)

                data = Shooting(name=name, date=datetime.date.today(), attempt=attempt, make=make)
                data.save()

        else:
            pass

        return redirect("/club_management/practiceform_page/")
class Matchresult_View(View):  
    def get(self, request, *args, **kwargs):  
        matchResultData = MatchResult.objects.all()
        
        return render(request, 'club_management/matchresult_page.html',{"matchResultData":matchResultData}) #, "matchResultDetailData":matchResultDetailData})

class MatchResultDetail_View(View):
    def get(self, request, *args, **kwargs):

        return render(request, "club_management/matchresultdetail_page.html")

    def post(self, request, *args, **kwargs):
        op_team = request.POST.get("hidden_teamname")
        date = datetime.datetime.strptime(request.POST.get("hidden_date"), '%Y年%m月%d日')
        date = datetime.datetime.strftime(date, "%Y-%m-%d")
        data = MatchResult.objects.get(op_team=op_team, date=date)
        matchResultDetailData = MatchResultDetail.objects.filter(op_team=data, date=data)
        return render(request, "club_management/matchresultdetail_page.html", {"op_team":op_team, "date":date, "matchResultDetailData":matchResultDetailData,})

class MatchResultForm_View(View):
    def get(self, request, *args, **kwargs):
        players = UserDetail.objects.filter(position="プレイヤー")
        matchResultData = MatchResult.objects.all()
        return render(request, "club_management/matchresultform_page.html", {"players":players, "matchResultData":matchResultData})

    def post(self, request, *args, **kwargs):
        if "ICU_total" in request.POST:
            icu_total = request.POST.get("ICU_total")
            icu_1Q = request.POST.get("ICU_1Q")
            icu_2Q = request.POST.get("ICU_2Q")
            icu_3Q = request.POST.get("ICU_3Q")
            icu_4Q = request.POST.get("ICU_4Q")
            op_team = request.POST.get("OpponentTeam")
            op_total = request.POST.get("OpTotal")
            op_1Q = request.POST.get("Op1Q")
            op_2Q = request.POST.get("Op2Q")
            op_3Q = request.POST.get("Op3Q")
            op_4Q = request.POST.get("Op4Q")
            date = request.POST.get("matchDate")
            data = MatchResult(date=date, icu_total = icu_total, icu_1Q = icu_1Q, icu_2Q=icu_2Q, icu_3Q=icu_3Q, icu_4Q=icu_4Q, op_team=op_team, op_total=op_total, op_1Q=op_1Q, op_2Q=op_2Q, op_3Q=op_3Q, op_4Q=op_4Q)
            data.save()
        else:
            players = UserDetail.objects.filter(position="プレイヤー")
            individualPoints = request.POST.getlist("individualPoints")
            underGoalAttempts = request.POST.getlist("underGoalAttempt")
            underGoalIns = request.POST.getlist("underGoalIn")
            middleAttempts = request.POST.getlist("middleAttempt")
            middleIns = request.POST.getlist("middleIn")
            threePointAttempts = request.POST.getlist("threeAttempt")
            threePointIns = request.POST.getlist("threeIn")
            fauls = request.POST.getlist("faul")
            turnOvers = request.POST.getlist("turnOver")
  

            date = date = request.POST.get("matchDate")
            op_team = op_team = request.POST.get("opponentTeam")
            
            elm = MatchResult.objects.get(date=date, op_team=op_team)
            for i, player in enumerate(players, 0):
                name = player.name
                points = individualPoints[i]
                underGoalAttempt = underGoalAttempts[i]
                underGoalIn = underGoalIns[i]
                middleAttempt = middleAttempts[i]
                middleIn = middleIns[i]
                threePointAttempt = threePointAttempts[i]
                threePointIn = threePointIns[i]
                faul = fauls[i]
                turnOver = turnOvers[i]

                data = MatchResultDetail(name=name, date=elm, op_team=elm, points=points, underGoalAttempt=underGoalAttempt, underGoalIn=underGoalIn, middleAttempt=middleAttempt, middleIn=middleIn, threePointAttempt=threePointAttempt, threePointIn=threePointIn, faul=faul, turnOver=turnOver)
                data.save()

        return redirect("/club_management/matchresultform_page/")


class Group_View(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'club_management/group_page.html')

top_page = Toppage_View.as_view()
my_page = Mypage_View.as_view()
practice_page = Practice_View.as_view()
matchresult_page = Matchresult_View.as_view()
matchresultdetail_page = MatchResultDetail_View.as_view()
matchresultform_page = MatchResultForm_View.as_view()
practiceform_page = PracticeForm_View.as_view()
group_page = Group_View.as_view()