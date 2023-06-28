import requests
from django.shortcuts import render

def predict_car_price(request):
    if request.method == 'POST':
        mileage = float(request.POST['mileage'])
        age = float(request.POST['age'])

        # Make a request to the ML model API
        api_url = 'http://<api_endpoint>/api/predict'  # Replace <api_endpoint> with the actual endpoint
        payload = {'mileage': mileage, 'age': age}
        response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            prediction = response.json()['prediction']
            return render(request, 'index.html', {'prediction': prediction})

    return render(request, 'index.html')
