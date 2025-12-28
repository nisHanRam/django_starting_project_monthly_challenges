from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for entire month",
    "february": "Walk for 30 minutes everyday",
    "march": "Learn for 20 minutes everyday",
    "april": "Dance for 10 minutes everyday",
    "may": "Draw for 60 minutes everyday",
    "june": "Code for 30 minutes everyday",
    "july": "Sleep for 8 hours at least everyday",
    "august": "Exercise for 30 minutes everyday",
    "september": "Do social service once a week",
    "october": "Do yoga for 60 minutes everyday",
    "november": "Eat one seasonal fruit daily",
    "december": "Meditate for 30 minutes everyday",
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    # reverse() allows us to create paths by referring to the names of the existing paths/urls
    # This is important because we should not hardcode url paths
    redirect_path = reverse(
        "month-challenge", args=[redirect_month]
    )  # /challenges/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        return HttpResponse(monthly_challenges[month])
    except:
        return HttpResponseNotFound("This month is not supported!")
