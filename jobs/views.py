from django.shortcuts import render, HttpResponse
from faker import Faker
import requests
from .models import Job
import os

# Create your views here.

def name(request):
    return render(request, 'jobs/name.html')
    
def result(request):
    name = request.POST.get('name')
    # DB에 이름이 있는지 확인
    job = Job.objects.filter(name=name)
    # 없으면, 새로 만들어주기(faker)
    if not job:
        job = Job()
        job.name = name
        faker = Faker('ko_kr')
        job.pastJob = faker.job()
        job.save()
    else:
        job = job[0]
    api_key = os.getenv('GIPHY_KEY')
    url = f'https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={job.pastJob}'
    res = requests.get(url).json()
    gif_url = res.get('data')[0].get('images').get('fixed_width').get('url')
    return render(request, 'jobs/result.html', {'job': job, 'gif_url': gif_url})