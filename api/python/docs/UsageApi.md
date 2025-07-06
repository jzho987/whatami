# openapi_client.UsageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pc_usage**](UsageApi.md#get_pc_usage) | **GET** /usage/pc | 


# **get_pc_usage**
> IGetUsageResponseDTO get_pc_usage(start_time=start_time, end_time=end_time)

Get the usage information for software on the pc within a time range.

### Example


```python
import openapi_client
from openapi_client.models.i_get_usage_response_dto import IGetUsageResponseDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UsageApi(api_client)
    start_time = 56 # int | The start time of the usage data in unix epoch seconds. (optional)
    end_time = 56 # int | The end time of the usage data in unix epoch seconds. (optional)

    try:
        api_response = api_instance.get_pc_usage(start_time=start_time, end_time=end_time)
        print("The response of UsageApi->get_pc_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_pc_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| The start time of the usage data in unix epoch seconds. | [optional] 
 **end_time** | **int**| The end time of the usage data in unix epoch seconds. | [optional] 

### Return type

[**IGetUsageResponseDTO**](IGetUsageResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of values representing the daily usage. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

