from django.shortcuts import render
from django.http import JsonResponse
import datetime


def home(request):
    slack_name=request.GET.get("slack_name")
    track=request.GET.get("track")
    day=datetime.datetime.now().strftime("%A")
    utc_date=datetime.datetime.utcnow()
    github_file=''
    github_repo=''
    response={
        "slack_name":slack_name,
        "track":track,
        "day":day,
        "current_utc":utc_date,
        "github_file":github_file,
        "githun_repo":github_repo,
        "status_code":200
    }
    return JsonResponse(data=response)

