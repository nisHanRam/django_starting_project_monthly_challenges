from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

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
    "december": None,
}


def list_of_months(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


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
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month": month},
        )
    except:
        # Approach-1 - Manually returning a 404 page
        # We can't use render function here because it always returns a success response
        # Therefore, we need to import and use render_to_string function
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
    
        # Approach-2 - Raising the error class Http404
        # This automatically picks a file named "404.html" from templates folder at the root
        # In dev mode it shows error as debug is True & in production mode it renders 404.html
        raise Http404() 

