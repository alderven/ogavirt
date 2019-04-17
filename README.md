# ogavirt
API automation tests for "ogavirt" project

### Technical stack:
Programming language: [Python](https://www.python.org/)

Test framework: [pytest](https://docs.pytest.org/en/latest/)

Test report framework: [Yandex Allure](http://allure.qatools.ru/)


### API Test Case Steps:

№   | Test Script                                                             | Steps                                                        | Run Result                                                                                                       
-- | ------------------------------------------------------------------------| ------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------
1  | [test_API.py](https://github.com/alderven/ngti/blob/master/test_API.py) | Call "all" API method and check that it returns 200 response code       | [Passed](https://rawcdn.githack.com/alderven/ngti/1e8a53d4bd78708119970efb53cb418ee835eeee/allure-report/index.html#suites/7983043a6903f0897d9ea32d712c9b31/8016455467409c9f/)
2  | [test_API.py](https://github.com/alderven/ngti/blob/master/test_API.py) | Call "vehicles" API method and check that it returns 200 response code  | [Passed](https://rawcdn.githack.com/alderven/ngti/1e8a53d4bd78708119970efb53cb418ee835eeee/allure-report/index.html#suites/7983043a6903f0897d9ea32d712c9b31/8016455467409c9f/)
3  | [test_API.py](https://github.com/alderven/ngti/blob/master/test_API.py) | Call "starships" API method and check that it returns 200 response code | [Passed](https://rawcdn.githack.com/alderven/ngti/1e8a53d4bd78708119970efb53cb418ee835eeee/allure-report/index.html#suites/7983043a6903f0897d9ea32d712c9b31/8016455467409c9f/)
4  | [test_API.py](https://github.com/alderven/ngti/blob/master/test_API.py) | Check, that "all" and "vehicles" responses contains same vehicles       | [Passed](https://rawcdn.githack.com/alderven/ngti/1e8a53d4bd78708119970efb53cb418ee835eeee/allure-report/index.html#suites/7983043a6903f0897d9ea32d712c9b31/8016455467409c9f/)
5  | [test_API.py](https://github.com/alderven/ngti/blob/master/test_API.py) | Check, that "all" and "starships" responses contains same starships     | [Passed](https://rawcdn.githack.com/alderven/ngti/1e8a53d4bd78708119970efb53cb418ee835eeee/allure-report/index.html#suites/7983043a6903f0897d9ea32d712c9b31/8016455467409c9f/)  

### UI Test Case:

№   | Test Script                                                             | Steps                                                        | Run Result                                                                                                       
-- | ------------------------------------------------------------------------| ------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------
1  | [test_UI.py](https://github.com/alderven/ngti/blob/master/test_UI.py) | Open web page       | [Passed](https://rawcdn.githack.com/alderven/ngti/1e8a53d4bd78708119970efb53cb418ee835eeee/allure-report/index.html#suites/d557be277f93322ae44b8632f35030b4/d1bbf711a41d9f6e/)
2  | [test_UI.py](https://github.com/alderven/ngti/blob/master/test_UI.py) | Check that page contains both "vehicle" and "starship" classes  | [Passed](https://rawcdn.githack.com/alderven/ngti/1e8a53d4bd78708119970efb53cb418ee835eeee/allure-report/index.html#suites/d557be277f93322ae44b8632f35030b4/d1bbf711a41d9f6e/)
3  | [test_UI.py](https://github.com/alderven/ngti/blob/master/test_UI.py) | Search for "Sullustan" vehicle (it should be found) | [Passed](https://rawcdn.githack.com/alderven/ngti/1e8a53d4bd78708119970efb53cb418ee835eeee/allure-report/index.html#suites/d557be277f93322ae44b8632f35030b4/d1bbf711a41d9f6e/)
4  | [test_UI.py](https://github.com/alderven/ngti/blob/master/test_UI.py) | Switch to "Starships"       | [Passed](https://rawcdn.githack.com/alderven/ngti/1e8a53d4bd78708119970efb53cb418ee835eeee/allure-report/index.html#suites/d557be277f93322ae44b8632f35030b4/d1bbf711a41d9f6e/)
5  | [test_UI.py](https://github.com/alderven/ngti/blob/master/test_UI.py) | Search for "Wookiee" (it should be found)     | [Passed](https://rawcdn.githack.com/alderven/ngti/1e8a53d4bd78708119970efb53cb418ee835eeee/allure-report/index.html#suites/d557be277f93322ae44b8632f35030b4/d1bbf711a41d9f6e/)  
6  | [test_UI.py](https://github.com/alderven/ngti/blob/master/test_UI.py) | Switch to "Vehicles"       | [Passed](https://rawcdn.githack.com/alderven/ngti/1e8a53d4bd78708119970efb53cb418ee835eeee/allure-report/index.html#suites/d557be277f93322ae44b8632f35030b4/d1bbf711a41d9f6e/)
7  | [test_UI.py](https://github.com/alderven/ngti/blob/master/test_UI.py) | Search for "Zabrak" (it should be found)     | [Passed](https://rawcdn.githack.com/alderven/ngti/1e8a53d4bd78708119970efb53cb418ee835eeee/allure-report/index.html#suites/d557be277f93322ae44b8632f35030b4/d1bbf711a41d9f6e/) 

### How to install
1. Download and unzip [this project](https://github.com/alderven/ogavirt/archive/master.zip)
1. Install [Python 3.6 or higher](https://www.python.org/downloads/)
1. Install following Python libs:
   * [pytest](https://docs.pytest.org/en/latest/)
   * [allure-pytest](https://pypi.python.org/pypi/allure-pytest)
1. Install [Allure Framework](https://docs.qameta.io/allure/latest/)


### How to run tests
Execute following command from the the test folder:
```
python -m pytest --alluredir /full/path/to/report/folder
```

### How to generate Allure report
Execute following command:
```
allure serve /full/path/to/report/folder
```
See [doc](https://docs.qameta.io/allure/#_report_generation) for more details
