from django.shortcuts import render


#Wn0jsnoMcqB/YDTD1KcbNg==rP0A5RMNFd9SJjh8
def home(request):
    import requests
    import json

    if request.method=='POST':
        query=request.POST['query']
        api_url='https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query,headers={'X-Api-Key': 'API KEY'}) #Write your API key in place of API key

        try:
            api=json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api="Error found"
            print(e)
        return render(request,'home.html',{'api':api})
    else:
        return render(request,'home.html',{'query':'Enter a valid query'})
        
