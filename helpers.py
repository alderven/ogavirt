import requests
import warnings

warnings.filterwarnings('ignore')


def booking(hotel_id):
    return requests.post('https://tbec-mock-advertiser-qa.dus.tcs.trivago.cloud/api/v1/booking_availability',
                         json={'api_version': 1,
                               'hotel': {'item_id': hotel_id, 'partner_reference': 'abc123'},
                               'start_date': '2019-10-21',
                               'end_date': '2019-10-23',
                               'party': [{'adults': 2, 'children': [1]}],
                               'lang': 'en_US',
                               'currency': 'USD',
                               'user_country': 'US'},
                         auth=('qa', 'case_study'),
                         verify=False)
