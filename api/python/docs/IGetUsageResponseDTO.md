# IGetUsageResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_list** | [**IUsageItemDTO**](IUsageItemDTO.md) |  | 

## Example

```python
from openapi_client.models.i_get_usage_response_dto import IGetUsageResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IGetUsageResponseDTO from a JSON string
i_get_usage_response_dto_instance = IGetUsageResponseDTO.from_json(json)
# print the JSON string representation of the object
print(IGetUsageResponseDTO.to_json())

# convert the object into a dict
i_get_usage_response_dto_dict = i_get_usage_response_dto_instance.to_dict()
# create an instance of IGetUsageResponseDTO from a dict
i_get_usage_response_dto_from_dict = IGetUsageResponseDTO.from_dict(i_get_usage_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


