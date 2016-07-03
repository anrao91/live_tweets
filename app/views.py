from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
import json
import requests as django_requests
from django.template.context_processors import csrf

from app.models import Tweet

context = {}
tweets = {}

def home(request):
    populate_context(request)
    return render_to_response('index.html', context)
    '''if request.user.is_authenticated():
        return render_to_response('index.html', context)
    else:
        return HttpResponseRedirect('/admin/')'''


def get_tweets(request):
    populate_context(request)
    if request.POST:
        hashtag = request.POST.get('hashtag')
        if hashtag:
            tweets = fetch_tweets_from_hashtag(hashtag)
        return HttpResponse(json.dumps(tweets), content_type="application/json")
    else:
        return HttpResponse(json.dumps(dict({"error": "send post request"})), content_type="application/json")


def populate_context(request):
    context.clear()
    context.update(csrf(request))
    if request.user.is_authenticated():
        context['user'] = request.user
    else:
        context.pop('user', None)
    context['authenticated'] = request.user.is_authenticated
    context['debug'] = settings.DEBUG
    return context


def fetch_tweets_from_hashtag(search_string):
    resp_dict = {}
    # This is the Twitter authentication per application basis generated
    # by encoding consumer key and secret of a twitter account
    headers = {'Authorization':'Bearer AAAAAAAAAAAAAAAAAAAAANCXvwAAAAAAu0UB%2FW4UTIaNpyhlvz1T9a8ezA8%3DgZQF8ztuITZI4KIUqBZJjwIwUD2eOwKd4lWYohgNpaFcROYsP4'}
    url = "https://api.twitter.com/1.1/search/tweets.json?q=" + search_string
    response = django_requests.get(url, headers=headers)
    response_data = json.loads(response.text)
    if response_data and response_data.get("statuses"):
        Tweet.objects.all().delete()
        for i in range(len(response_data.get("statuses"))):
            resp_dict[i] = {'text' : response_data.get("statuses")[i].get("text"),
                            'id': response_data.get("statuses")[i].get("id_str"),
                            'dp': response_data.get('statuses')[i].get('user').get('profile_image_url'),
                            'created_time': response_data.get('statuses')[i].get('created_at'),
                            }
            try:
                Tweet.objects.create(hashtag=search_string, text=resp_dict[i])
            except Exception, e:
                raise e
    return resp_dict


# ## Login Authentication view.
# def auth_view(request):
#     populate_context(request)
#     login_form = LoginForm(request.POST or None)
#     if request.POST and login_form.is_valid():
#         if request.is_ajax:
#             user = login_form.login(request)
#             if user is not None:
#                 login(request, user)
#                 # msmeuser = MsmeUser.objects.filter(customuser_ptr_id = user.id)[0]
#                 # if msmeuser :
#                 #     return HttpResponseRedirect('/business/')
#                 # else:
#                 return HttpResponse(request.POST.get('next','/'))
#         else :
#             return HttpResponseForbidden()
#     context['login_form'] = login_form
#     return HttpResponse("Fail")
