from django.shortcuts import render

# Create your views here.
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "6cf189b6f0msh079cda117e8a0e2p16b577jsn48c69fa034f7",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def HellloworldView(request):
    mylist = []
    noofresults = int(response['results'])

    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])

    if request.method == "POST":
        selectedCountry = request.POST['selectedCountry']
        noofresults = int(response['results'])
        for x in range(0, noofresults):
            if selectedCountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'selectedCountry': selectedCountry, 'mylist': mylist, 'new': new, 'active': active,
                   'critical': critical, 'recovered': recovered, 'deaths': deaths, 'total': total}
        return render(request, 'helloWorld.html', context)

    context = {'mylist': mylist}
    return render(request, 'helloWorld.html', context)
