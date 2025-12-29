from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from functools import reduce
from django.template.loader import render_to_string

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


def list_of_months(request):
    months = list(monthly_challenges.keys())
    response_data = f"<ul>{reduce(
        lambda resp_str, month: resp_str + f"<li><a href={reverse("month-challenge", args=[month])}>{month.capitalize()}</a></li>", months, ""
    )}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month!</h1>")
    redirect_month = months[month - 1]
    # reverse() allows us to create paths by referring to the names of the existing paths/urls
    # This is important because we should not hardcode url paths
    redirect_path = reverse(
        "month-challenge", args=[redirect_month]
    )  # /challenges/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
