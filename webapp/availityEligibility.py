import requests

auth_token='89b08974d5f6b17ab3958578ce85058e'
headers = {"Authorization": "Bearer 89b08974d5f6b17ab3958578ce85058e",
           "content-type": "application/x-www-form-urlencoded",
           "accept": "application/json"}
data = {' payerId' : 'CMS',
        'providerLastName': 'Monis',
        'memberId': '9VW9W80JK14',
        'providerNpi': '1477114031',
         'asOfDate':'2024-06-27',
         'serviceType':'MH',
           'patientBirthDate':'07/05/1942',
            'patientLastName': 'LONG',
            'patientFirstName': 'Lynne',
            'patientGender': 'F',
            'requestedPatientSearchOption':'memberid'
             }

payload = "payerId=CMS&providerLastName=Monis&providerFirstName=Ann&providerNpi=1477114031&providerTaxId=832972411&providerState=FL&providerZipCode=33316&asOfDate=06/28/2024&serviceType=Mental Health-MH&memberId=9VW9W80JK14&patientLastName=Long&patientFirstName=Lynne&patientBirthDate=07/05/1942"

url = "https://api.availity.com/availity/development-partner/v1/coverages" 
 
response = requests.post(url, json=payload, headers=headers)

#response = requests.get(url)
print(response)
print(response.json())