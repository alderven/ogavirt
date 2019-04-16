import json
import time
import pytest
import validators
import helpers


@pytest.allure.feature('Trivago')
@pytest.allure.story('Booking Availability')
@pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
@pytest.mark.parametrize('response', [helpers.booking(hotel_id) for hotel_id in range(1, 5)])
class TestBookingAvailability:

    def test01_check_that_response_code_is_200(self, response):
        with pytest.allure.step('Check, that response code is 200 OK'):
            assert response.status_code == 200

    def test02_check_that_response_contains_valid_json(self, response):
        with pytest.allure.step('Check, that response contains valid JSON'):
            assert type(response.json()) == dict

    def test03_check_api_version(self, response):
        with pytest.allure.step('Check, that responded API version, is identical to requested one'):
            assert json.loads(response.request.body)['api_version'] == response.json()['api_version']

    def test04_check_dates(self, response):
        with pytest.allure.step('Check, that responded date are identical to requested ones'):
            assert json.loads(response.request.body)['start_date'] == response.json()['start_date']
            assert json.loads(response.request.body)['end_date'] == response.json()['end_date']

    def test05_check_user_country(self, response):
        with pytest.allure.step('Check, that responded user country is identical to requested one'):
            assert json.loads(response.request.body)['user_country'] == response.json()['user_country']

    def test06_check_that_hotel_details_contains_a_name_of_type_string(self, response):
        with pytest.allure.step('Check, that hotel_details contains a name of type string'):
            assert type(response.json()['hotel_details']['name']) == str

    def test07_check_that_hotel_details_contains_an_address1_of_type_string(self, response):
        with pytest.allure.step('Check, that hotel_details contains an address1 of type string'):
            assert type(response.json()['hotel_details']['address1']) == str

    def test08_check_that_hotel_details_contains_a_city_of_type_string(self, response):
        with pytest.allure.step('Check, that hotel_details contains a city of type string'):
            assert type(response.json()['hotel_details']['city']) == str

    def test09_check_that_hotel_details_contains_a_valid_url(self, response):
        with pytest.allure.step('Check, that hotel_details contains a valid url'):
            assert validators.url(response.json()['hotel_details']['url'])

    def test10_check_that_room_types_array_contains_at_least_one_entry(self, response):
        with pytest.allure.step('Check, the room_types_array contains at least one entry, or more'):
            assert len(response.json()['room_types_array'])

    def test11_check_that_responded_room_has_a_name_and_its_data_format_is_type_string_with_at_least_3_letters(self, response):
        with pytest.allure.step('Check, that the responded room has a name and its data format is type string with at least 3 letters'):
            for room in response.json()['room_types_array']:
                assert type(room['name']) == str
                assert len(room['name']) > 2

    def test12_check_that_responded_room_has_a_final_price_at_booking_and_or_a_final_price_at_checkout(self, response):
        with pytest.allure.step('Check, that the responded room has a final_price_at_booking and/or a final_price_at_checkout'):
            for room in response.json()['room_types_array']:
                assert room['final_price_at_booking'] or room['final_price_at_checkout']

    def test13_check_that_currency_is_a_three_letter_code_of_type_string_and_fits_to_the_requested_one(self, response):
        with pytest.allure.step('Check, that currency is a three-letter code of type string and fits to the requested one'):
            for room in response.json()['room_types_array']:
                assert type(room['final_price_at_booking']['currency']) == str
                assert len(room['final_price_at_booking']['currency']) == 3
                assert room['final_price_at_booking']['currency'] == json.loads(response.request.body)['currency']

                assert type(room['final_price_at_checkout']['currency']) == str
                assert len(room['final_price_at_checkout']['currency']) == 3
                assert room['final_price_at_checkout']['currency'] == json.loads(response.request.body)['currency']

    def test14_check_that_amount_is_a_number_equal_or_greater_than_0(self, response):
        with pytest.allure.step('CCheck, that amount is a number equal or greater than 0'):
            for room in response.json()['room_types_array']:
                assert room['final_price_at_booking']['amount'] >= 0
                assert room['final_price_at_checkout']['amount'] >= 0

    def test15_check_that_the_start_date_is_before_the_end_date(self, response):
        with pytest.allure.step('Check, that the start_date is before the end_date'):
            assert time.strptime(response.json()['start_date'], '%Y-%m-%d') < time.strptime(response.json()['end_date'], '%Y-%m-%d')
