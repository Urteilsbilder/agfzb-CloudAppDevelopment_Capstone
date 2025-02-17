import requests
import json
# import related models here
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        if 'features' not in kwargs:
            response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
        else:
            params = dict()
            params["text"] = kwargs["text"]
            params["version"] = kwargs["version"]
            params["features"] = kwargs["features"]
            params["return_analyzed_text"] = kwargs["return_analyzed_text"]
            response = requests.get(url, params=params, headers={'Content-Type': 'application/json'}, 
                        auth=HTTPBasicAuth('apikey', "gjT6JluHqCjWnUc64L-jHCb_AB1Of152W0cha9FANiKc"))
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
def post_request(url, json_payload, **kwargs):
     print(kwargs)
     print("POST to {} ".format(url))
     try:
        response = requests.post(url, params=kwargs, json=json_payload)
     except:
         # If any error occurs
        print("Network exception occurred")
     status_code = response.status_code
     print("With status {} ".format(status_code))
     json_data = json.loads(response.text)
     return json_data

# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # For each dealer object
        for dealer in json_result:
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer["address"], city=dealer["city"], full_name=dealer["full_name"],
                                   id=dealer["id"], lat=dealer["lat"], long=dealer["long"],
                                   short_name=dealer["short_name"],
                                   st=dealer["st"], zip=dealer["zip"])
            results.append(dealer_obj)

    return results

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list
def get_dealer_reviews_from_cf(url, dealerId):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url, dealer=dealerId)
    if json_result:
        # For each dealer object
        for dealer in json_result:
            # Create a DealerReview object with values in `doc` object
            dealer_obj = DealerReview(dealership=dealer["dealership"], name=dealer["name"], purchase=dealer["purchase"],
                                   review=dealer["review"], purchase_date=dealer["purchase_date"], car_make=dealer["car_make"],
                                   car_model=dealer["car_model"],
                                   car_year=dealer["car_year"],  sentiment=analyze_review_sentiments(dealer["review"]), id=dealer["id"])
            results.append(dealer_obj)
    
    return results


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
def analyze_review_sentiments(text, **kwargs):
  results = get_request("https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/499e2f9d-dc23-4cb5-aa3d-c179e82ab061/v1/analyze", 
                text=text, version="2019-07-12", features="emotion", return_analyzed_text=True)
  emotion = results["emotion"]["document"]["emotion"]
  print('positive' if emotion["joy"] > emotion["sadness"] else 'negative')
  return 'positive' if emotion["joy"] > emotion["sadness"] else 'negative' 