# \UsageAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetPCUsage**](UsageAPI.md#GetPCUsage) | **Get** /usage/pc | 



## GetPCUsage

> IGetUsageResponseDTO GetPCUsage(ctx).StartTime(startTime).EndTime(endTime).Execute()





### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/GIT_USER_ID/GIT_REPO_ID"
)

func main() {
	startTime := int32(56) // int32 | The start time of the usage data in unix epoch seconds. (optional)
	endTime := int32(56) // int32 | The end time of the usage data in unix epoch seconds. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UsageAPI.GetPCUsage(context.Background()).StartTime(startTime).EndTime(endTime).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UsageAPI.GetPCUsage``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetPCUsage`: IGetUsageResponseDTO
	fmt.Fprintf(os.Stdout, "Response from `UsageAPI.GetPCUsage`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetPCUsageRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startTime** | **int32** | The start time of the usage data in unix epoch seconds. | 
 **endTime** | **int32** | The end time of the usage data in unix epoch seconds. | 

### Return type

[**IGetUsageResponseDTO**](IGetUsageResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

