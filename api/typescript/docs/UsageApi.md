# UsageApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getPCUsage**](#getpcusage) | **GET** /usage/pc | |

# **getPCUsage**
> IGetUsageResponseDTO getPCUsage()

Get the usage information for software on the pc within a time range.

### Example

```typescript
import {
    UsageApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new UsageApi(configuration);

let startTime: number; //The start time of the usage data in unix epoch seconds. (optional) (default to undefined)
let endTime: number; //The end time of the usage data in unix epoch seconds. (optional) (default to undefined)

const { status, data } = await apiInstance.getPCUsage(
    startTime,
    endTime
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **startTime** | [**number**] | The start time of the usage data in unix epoch seconds. | (optional) defaults to undefined|
| **endTime** | [**number**] | The end time of the usage data in unix epoch seconds. | (optional) defaults to undefined|


### Return type

**IGetUsageResponseDTO**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | An array of values representing the daily usage. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

