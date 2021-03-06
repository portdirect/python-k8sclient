# V1PersistentVolumeClaim

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/release-1.4/docs/devel/api-conventions.md#types-kinds | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/release-1.4/docs/devel/api-conventions.md#resources | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. More info: http://releases.k8s.io/release-1.4/docs/devel/api-conventions.md#metadata | [optional] 
**spec** | [**V1PersistentVolumeClaimSpec**](V1PersistentVolumeClaimSpec.md) | Spec defines the desired characteristics of a volume requested by a pod author. More info: http://releases.k8s.io/release-1.4/docs/user-guide/persistent-volumes.md#persistentvolumeclaims | [optional] 
**status** | [**V1PersistentVolumeClaimStatus**](V1PersistentVolumeClaimStatus.md) | Status represents the current information/status of a persistent volume claim. Read-only. More info: http://releases.k8s.io/release-1.4/docs/user-guide/persistent-volumes.md#persistentvolumeclaims | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


