# IUsageItemDTO

A datapoint to describe the usage of a particular item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**start_time** | **int** |  | [optional] 
**end_time** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.i_usage_item_dto import IUsageItemDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IUsageItemDTO from a JSON string
i_usage_item_dto_instance = IUsageItemDTO.from_json(json)
# print the JSON string representation of the object
print(IUsageItemDTO.to_json())

# convert the object into a dict
i_usage_item_dto_dict = i_usage_item_dto_instance.to_dict()
# create an instance of IUsageItemDTO from a dict
i_usage_item_dto_from_dict = IUsageItemDTO.from_dict(i_usage_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


