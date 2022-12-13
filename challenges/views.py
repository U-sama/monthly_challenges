from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month!!",
    "february": "Walks for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes!!",
    "april": "the month before my birthday",
    "may": "my birthday month",
    "june": "the month after my birthday",
    "july": "study deep learning",
    "august": "just random txt",
    "september": "three more months and finish the millitary",
    "october": "one more month and finish millitary",
    "november": "the last month of millitary",
    "december": None
}

# Create your views here.


def challenge_home(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months" : months
    })



def monthly_challenge_num(request, month):
    months = list(monthly_challenges.keys())

    if month > 12:
        return HttpResponseNotFound("Invalid Number!!")
    redirect_month = months[month-1]
    # /challenge/"month_name"
    redicrected_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redicrected_path)


def monthly_challenge(request, month):
    try:
        challenge_txt = monthly_challenges[month]
        """ response_data = render_to_string("challenges/challenge.html") #old way of sending responces e can just use render
        return HttpResponse(response_data) """
        return render(request, "challenges/challenge.html", {
            "text": challenge_txt,
            "month_name": month,
        })
    except:
        raise Http404()
