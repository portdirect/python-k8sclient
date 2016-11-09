# V1NodeStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **object** | Capacity represents the total resources of a node. More info: http://releases.k8s.io/release-1.4/docs/user-guide/persistent-volumes.md#capacity for more details. | [optional] 
**allocatable** | **object** | Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity. | [optional] 
**phase** | **str** | NodePhase is the recently observed lifecycle phase of the node. More info: http://releases.k8s.io/release-1.4/docs/admin/node.md#node-phase The field is never populated, and now is deprecated. | [optional] 
**conditions** | [**list[V1NodeCondition]**](V1NodeCondition.md) | Conditions is an array of current observed node conditions. More info: http://releases.k8s.io/release-1.4/docs/admin/node.md#node-condition | [optional] 
**addresses** | [**list[V1NodeAddress]**](V1NodeAddress.md) | List of addresses reachable to the node. Queried from cloud provider, if available. More info: http://releases.k8s.io/release-1.4/docs/admin/node.md#node-addresses | [optional] 
**daemon_endpoints** | [**V1NodeDaemonEndpoints**](V1NodeDaemonEndpoints.md) | Endpoints of daemons running on the Node. | [optional] 
**node_info** | [**V1NodeSystemInfo**](V1NodeSystemInfo.md) | Set of ids/uuids to uniquely identify the node. More info: http://releases.k8s.io/release-1.4/docs/admin/node.md#node-info | [optional] 
**images** | [**list[V1ContainerImage]**](V1ContainerImage.md) | List of container images on this node | [optional] 
**volumes_in_use** | [**list[V1UniqueVolumeName]**](V1UniqueVolumeName.md) | List of attachable volumes in use (mounted) by the node. | [optional] 
**volumes_attached** | [**list[V1AttachedVolume]**](V1AttachedVolume.md) | List of volumes that are attached to the node. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


