import ctypes

from .common import *
from .helpers import *

_hapi = ctypes.cdll.LoadLibrary('/opt/hfs/dsolib/libHAPIL.so')

CreateInProcessSession = _hapi.HAPI_CreateInProcessSession
CreateInProcessSession.restype = Result
CreateInProcessSession.argtypes = [ ctypes.POINTER(Session) ]

StartThriftSocketServer = _hapi.HAPI_StartThriftSocketServer
StartThriftSocketServer.restype = Result
StartThriftSocketServer.argtypes = [ ctypes.POINTER(ThriftServerOptions),
                                     ctypes.c_int,
                                     ctypes.POINTER(ProcessId) ]

CreateThriftSocketSession = _hapi.HAPI_CreateThriftSocketSession
CreateThriftSocketSession.restype = Result
CreateThriftSocketSession.argtypes = [ ctypes.POINTER(Session),
                                       ctypes.c_char_p,
                                       ctypes.c_int ]

StartThriftNamedPipeServer = _hapi.HAPI_StartThriftNamedPipeServer
StartThriftNamedPipeServer.restype = Result
StartThriftNamedPipeServer.argtypes = [ ctypes.POINTER(ThriftServerOptions),
                                        ctypes.c_char_p,
                                        ctypes.POINTER(ProcessId) ]

CreateThriftNamedPipeSession = _hapi.HAPI_CreateThriftNamedPipeSession
CreateThriftNamedPipeSession.restype = Result
CreateThriftNamedPipeSession.argtypes = [ ctypes.POINTER(Session),
                                          ctypes.c_char_p ]

BindCustomImplementation = _hapi.HAPI_BindCustomImplementation
BindCustomImplementation.restype = Result
BindCustomImplementation.argtypes = [ SessionType,
                                      ctypes.c_char_p ]

CreateCustomSession = _hapi.HAPI_CreateCustomSession
CreateCustomSession.restype = Result
CreateCustomSession.argtypes = [ SessionType,
                                 ctypes.c_void_p,
                                 ctypes.POINTER(Session) ]

IsSessionValid = _hapi.HAPI_IsSessionValid
IsSessionValid.restype = Result
IsSessionValid.argtypes = [ ctypes.POINTER(Session) ]

CloseSession = _hapi.HAPI_CloseSession
CloseSession.restype = Result
CloseSession.argtypes = [ ctypes.POINTER(Session) ]

IsInitialized = _hapi.HAPI_IsInitialized
IsInitialized.restype = Result
IsInitialized.argtypes = [ ctypes.POINTER(Session) ]


Initialize = _hapi.HAPI_Initialize
Initialize.restype = Result
Initialize.argtypes = [ ctypes.POINTER(Session),
                        ctypes.POINTER(CookOptions),
                        Bool,
                        ctypes.c_int,
                        ctypes.c_char_p,
                        ctypes.c_char_p,
                        ctypes.c_char_p,
                        ctypes.c_char_p,
                        ctypes.c_char_p ]

Cleanup = _hapi.HAPI_Cleanup
Cleanup.restype = Result
Cleanup.argtypes = [ctypes.POINTER(Session)]


GetEnvInt = _hapi.HAPI_GetEnvInt
GetEnvInt.restype = Result
GetEnvInt.argtypes = [ EnvIntType,
                       ctypes.POINTER(ctypes.c_int) ]

GetSessionEnvInt = _hapi.HAPI_GetSessionEnvInt
GetSessionEnvInt.restype = Result
GetSessionEnvInt.argtypes = [ ctypes.POINTER(Session),
                              SessionEnvIntType,
                              ctypes.POINTER(ctypes.c_int) ]

GetServerEnvInt = _hapi.HAPI_GetServerEnvInt
GetServerEnvInt.restype = Result
GetServerEnvInt.argtypes = [ ctypes.POINTER(Session),
                             ctypes.c_char_p,
                             ctypes.POINTER(ctypes.c_int) ]

GetServerEnvString = _hapi.HAPI_GetServerEnvString
GetServerEnvString.restype = Result
GetServerEnvString.argtypes = [ ctypes.POINTER(Session),
                                ctypes.c_char_p,
                                ctypes.POINTER(StringHandle) ]

SetServerEnvInt = _hapi.HAPI_SetServerEnvInt
SetServerEnvInt.restype = Result
SetServerEnvInt.argtypes = [ ctypes.POINTER(Session),
                             ctypes.c_char_p,
                             ctypes.c_int ]

SetServerEnvString = _hapi.HAPI_SetServerEnvString
SetServerEnvString.restype = Result
SetServerEnvString.argtypes = [ ctypes.POINTER(Session),
                                ctypes.c_char_p,
                                ctypes.c_char_p ]

GetStatus = _hapi.HAPI_GetStatus
GetStatus.restype = Result
GetStatus.argtypes = [ ctypes.POINTER(Session),
                       StatusType,
                       ctypes.POINTER(ctypes.c_int) ]

GetStatusStringBufLength = _hapi.HAPI_GetStatusStringBufLength
GetStatusStringBufLength.restype = Result
GetStatusStringBufLength.argtypes = [ ctypes.POINTER(Session),
                                      StatusType,
                                      StatusVerbosity,
                                      ctypes.POINTER(ctypes.c_int) ]

GetStatusString = _hapi.HAPI_GetStatusString
GetStatusString.restype = Result
GetStatusString.argtypes = [ ctypes.POINTER(Session),
                             StatusType,
                             ctypes.c_char_p,
                             ctypes.c_int ]

ComposeNodeCookResult = _hapi.HAPI_ComposeNodeCookResult
ComposeNodeCookResult.restype = Result
ComposeNodeCookResult.argtypes = [ ctypes.POINTER(Session),
                                   NodeId,
                                   StatusVerbosity,
                                   ctypes.POINTER(ctypes.c_int) ]

GetComposedNodeCookResult = _hapi.HAPI_GetComposedNodeCookResult
GetComposedNodeCookResult.restype = Result
GetComposedNodeCookResult.argtypes = [ ctypes.POINTER(Session),
                                       ctypes.c_char_p,
                                       ctypes.c_int ]

CheckForSpecificErrors = _hapi.HAPI_CheckForSpecificErrors
CheckForSpecificErrors.restype = Result
CheckForSpecificErrors.argtypes = [ ctypes.POINTER(Session),
                                    NodeId,
                                    ErrorCodeBits,
                                    ctypes.POINTER(ErrorCodeBits) ]

GetCookingTotalCount = _hapi.HAPI_GetCookingTotalCount
GetCookingTotalCount.restype = Result
GetCookingTotalCount.argtypes = [ ctypes.POINTER(Session),
                                  ctypes.POINTER(ctypes.c_int) ]

GetCookingCurrentCount = _hapi.HAPI_GetCookingCurrentCount
GetCookingCurrentCount.restype = Result
GetCookingCurrentCount.argtypes = [ ctypes.POINTER(Session),
                                    ctypes.POINTER(ctypes.c_int) ]

ConvertTransform = _hapi.HAPI_ConvertTransform
ConvertTransform.restype = Result
ConvertTransform.argtypes = [ ctypes.POINTER(Session),
                              ctypes.POINTER(TransformEuler),
                              RSTOrder,
                              XYZOrder,
                              ctypes.POINTER(TransformEuler) ]

ConvertMatrixToQuat = _hapi.HAPI_ConvertMatrixToQuat
ConvertMatrixToQuat.restype = Result
ConvertMatrixToQuat.argtypes = [ ctypes.POINTER(Session),
                                 ctypes.POINTER(ctypes.c_float),
                                 RSTOrder,
                                 ctypes.POINTER(Transform) ]

ConvertMatrixToEuler = _hapi.HAPI_ConvertMatrixToEuler
ConvertMatrixToEuler.restype = Result
ConvertMatrixToEuler.argtypes = [ ctypes.POINTER(Session),
                                  ctypes.POINTER(ctypes.c_float),
                                  RSTOrder,
                                  XYZOrder,
                                  ctypes.POINTER(TransformEuler) ]

ConvertTransformQuatToMatrix = _hapi.HAPI_ConvertTransformQuatToMatrix
ConvertTransformQuatToMatrix.restype = Result
ConvertTransformQuatToMatrix.argtypes = [ ctypes.POINTER(Session),
                                          ctypes.POINTER(Transform),
                                          ctypes.POINTER(ctypes.c_float) ]

ConvertTransformEulerToMatrix = _hapi.HAPI_ConvertTransformEulerToMatrix
ConvertTransformEulerToMatrix.restype = Result
ConvertTransformEulerToMatrix.argtypes = [ ctypes.POINTER(Session),
                                           ctypes.POINTER(TransformEuler),
                                           ctypes.POINTER(ctypes.c_float) ]

PythonThreadInterpreterLock = _hapi.HAPI_PythonThreadInterpreterLock
PythonThreadInterpreterLock.restype = Result
PythonThreadInterpreterLock.argtypes = [ ctypes.POINTER(Session),
                                         Bool ]


GetStringBufLength = _hapi.HAPI_GetStringBufLength
GetStringBufLength.restype = Result
GetStringBufLength.argtypes = [ ctypes.POINTER(Session),
                                StringHandle,
                                ctypes.POINTER(ctypes.c_int) ]

GetString = _hapi.HAPI_GetString
GetString.restype = Result
GetString.argtypes = [ ctypes.POINTER(Session),
                       StringHandle,
                       ctypes.c_char_p,
                       ctypes.c_int ]


GetTime = _hapi.HAPI_GetTime
GetTime.restype = Result
GetTime.argtypes = [ ctypes.POINTER(Session),
                     ctypes.POINTER(ctypes.c_float) ]

SetTime = _hapi.HAPI_SetTime
SetTime.restype = Result
SetTime.argtypes = [ ctypes.POINTER(Session),
                     ctypes.c_float ]

GetTimelineOptions = _hapi.HAPI_GetTimelineOptions
GetTimelineOptions.restype = Result
GetTimelineOptions.argtypes = [ ctypes.POINTER(Session),
                                ctypes.POINTER(TimelineOptions) ]

SetTimelineOptions = _hapi.HAPI_SetTimelineOptions
SetTimelineOptions.restype = Result
SetTimelineOptions.argtypes = [ ctypes.POINTER(Session),
                                ctypes.POINTER(TimelineOptions) ]

LoadAssetLibraryFromFile = _hapi.HAPI_LoadAssetLibraryFromFile
LoadAssetLibraryFromFile.restype = Result
LoadAssetLibraryFromFile.argtypes = [ ctypes.POINTER(Session),
                                      ctypes.c_char_p,
                                      Bool,
                                      ctypes.POINTER(AssetLibraryId) ]

LoadAssetLibraryFromMemory = _hapi.HAPI_LoadAssetLibraryFromMemory
LoadAssetLibraryFromMemory.restype = Result
LoadAssetLibraryFromMemory.argtypes = [ ctypes.POINTER(Session),
                                        ctypes.c_char_p,
                                        ctypes.c_int,
                                        Bool,
                                        ctypes.POINTER(AssetLibraryId) ]

GetAvailableAssetCount = _hapi.HAPI_GetAvailableAssetCount
GetAvailableAssetCount.restype = Result
GetAvailableAssetCount.argtypes = [ ctypes.POINTER(Session),
                                    AssetLibraryId,
                                    ctypes.POINTER(ctypes.c_int) ]

GetAvailableAssets = _hapi.HAPI_GetAvailableAssets
GetAvailableAssets.restype = Result
GetAvailableAssets.argtypes = [ ctypes.POINTER(Session),
                                AssetLibraryId,
                                ctypes.POINTER(StringHandle),
                                ctypes.c_int ]

GetAssetInfo = _hapi.HAPI_GetAssetInfo
GetAssetInfo.restype = Result
GetAssetInfo.argtypes = [ ctypes.POINTER(Session),
                          NodeId,
                          ctypes.POINTER(AssetInfo) ]

Interrupt = _hapi.HAPI_Interrupt
Interrupt.restype = Result
Interrupt.argtypes = [ ctypes.POINTER(Session) ]


LoadHIPFile = _hapi.HAPI_LoadHIPFile
LoadHIPFile.restype = Result
LoadHIPFile.argtypes = [ ctypes.POINTER(Session),
                         ctypes.c_char_p,
                         Bool ]

SaveHIPFile = _hapi.HAPI_SaveHIPFile
SaveHIPFile.restype = Result
SaveHIPFile.argtypes = [ ctypes.POINTER(Session),
                            ctypes.c_char_p,
                            Bool]


IsNodeValid = _hapi.HAPI_IsNodeValid
IsNodeValid.restype = Result
IsNodeValid.argtypes = [ ctypes.POINTER(Session),
                         NodeId,
                         ctypes.c_int,
                         ctypes.POINTER(Bool) ]

GetNodeInfo = _hapi.HAPI_GetNodeInfo
GetNodeInfo.restype = Result
GetNodeInfo.argtypes = [ ctypes.POINTER(Session),
                         NodeId,
                         ctypes.POINTER(NodeInfo) ]

GetNodePath = _hapi.HAPI_GetNodePath
GetNodePath.restype = Result
GetNodePath.argtypes = [ ctypes.POINTER(Session),
                         NodeId,
                         NodeId,
                         ctypes.POINTER(StringHandle) ]

GetManagerNodeId = _hapi.HAPI_GetManagerNodeId
GetManagerNodeId.restype = Result
GetManagerNodeId.argtypes = [ ctypes.POINTER(Session),
                              NodeType,
                              ctypes.POINTER(NodeId) ]

ComposeChildNodeList = _hapi.HAPI_ComposeChildNodeList
ComposeChildNodeList.restype = Result
ComposeChildNodeList.argtypes = [ ctypes.POINTER(Session),
                                     NodeId,
                                     NodeTypeBits,
                                     NodeFlagsBits,
                                     Bool,
                                    ctypes.POINTER(ctypes.c_int)]

GetComposedChildNodeList = _hapi.HAPI_GetComposedChildNodeList
GetComposedChildNodeList.restype = Result
GetComposedChildNodeList.argtypes = [ ctypes.POINTER(Session),
                                      NodeId,
                                      ctypes.POINTER(NodeId),
                                      ctypes.c_int ]

CreateNode = _hapi.HAPI_CreateNode
CreateNode.restype = Result
CreateNode.argtypes = [ ctypes.POINTER(Session),
                        NodeId,
                        ctypes.c_char_p,
                        ctypes.c_char_p,
                        Bool,
                        ctypes.POINTER(NodeId) ]

CreateInputNode = _hapi.HAPI_CreateInputNode
CreateInputNode.restype = Result
CreateInputNode.argtypes = [ ctypes.POINTER(Session),
                             ctypes.POINTER(NodeId),
                             ctypes.c_char_p ]

CookNode = _hapi.HAPI_CookNode
CookNode.restype = Result
CookNode.argtypes = [ ctypes.POINTER(Session),
                      NodeId,
                      ctypes.POINTER(CookOptions) ]

DeleteNode = _hapi.HAPI_DeleteNode
DeleteNode.restype = Result
DeleteNode.argtypes = [ ctypes.POINTER(Session),
                        NodeId ]

RenameNode = _hapi.HAPI_RenameNode
RenameNode.restype = Result
RenameNode.argtypes = [ ctypes.POINTER(Session),
                        NodeId,
                        ctypes.c_char_p ]

ConnectNodeInput = _hapi.HAPI_ConnectNodeInput
ConnectNodeInput.restype = Result
ConnectNodeInput.argtypes = [ ctypes.POINTER(Session),
                              NodeId,
                              ctypes.c_int,
                              NodeId ]

DisconnectNodeInput = _hapi.HAPI_DisconnectNodeInput
DisconnectNodeInput.restype = Result
DisconnectNodeInput.argtypes = [ ctypes.POINTER(Session),
                                 NodeId,
                                 ctypes.c_int ]

QueryNodeInput = _hapi.HAPI_QueryNodeInput
QueryNodeInput.restype = Result
QueryNodeInput.argtypes = [ ctypes.POINTER(Session),
                            NodeId,
                            ctypes.c_int,
                            ctypes.POINTER(NodeId) ]

GetNodeInputName = _hapi.HAPI_GetNodeInputName
GetNodeInputName.restype = Result
GetNodeInputName.argtypes = [ ctypes.POINTER(Session),
                              NodeId,
                              ctypes.c_int,
                              ctypes.POINTER(StringHandle) ]

GetParameters = _hapi.HAPI_GetParameters
GetParameters.restype = Result
GetParameters.argtypes = [ ctypes.POINTER(Session),
                           NodeId,
                           ctypes.POINTER(ParmInfo),
                           ctypes.c_int,
                           ctypes.c_int ]

GetParmInfo = _hapi.HAPI_GetParmInfo
GetParmInfo.restype = Result
GetParmInfo.argtypes = [ ctypes.POINTER(Session),
                         NodeId,
                         ParmId,
                         ctypes.POINTER(ParmInfo) ]

GetParmIdFromName = _hapi.HAPI_GetParmIdFromName
GetParmIdFromName.restype = Result
GetParmIdFromName.argtypes = [ ctypes.POINTER(Session),
                               NodeId,
                               ctypes.c_char_p,
                               ctypes.POINTER(ParmId) ]

GetParmInfoFromName = _hapi.HAPI_GetParmInfoFromName
GetParmInfoFromName.restype = Result
GetParmInfoFromName.argtypes = [ ctypes.POINTER(Session),
                                 NodeId,
                                 ctypes.c_char_p,
                                 ctypes.POINTER(ParmInfo) ]

GetParmTagName = _hapi.HAPI_GetParmTagName
GetParmTagName.restype = Result
GetParmTagName.argtypes = [ ctypes.POINTER(Session),
                            NodeId,
                            ParmId,
                            ctypes.c_int,
                            ctypes.POINTER(StringHandle) ]

GetParmTagValue = _hapi.HAPI_GetParmTagValue
GetParmTagValue.restype = Result
GetParmTagValue.argtypes = [ ctypes.POINTER(Session),
                             NodeId,
                             ParmId,
                             ctypes.c_char_p,
                             ctypes.POINTER(StringHandle) ]

ParmHasTag = _hapi.HAPI_ParmHasTag
ParmHasTag.restype = Result
ParmHasTag.argtypes = [ ctypes.POINTER(Session),
                        NodeId,
                        ParmId,
                        ctypes.c_char_p,
                        ctypes.POINTER(Bool) ]

GetParmWithTag = _hapi.HAPI_GetParmWithTag
GetParmWithTag.restype = Result
GetParmWithTag.argtypes = [ ctypes.POINTER(Session),
                            NodeId,
                            ctypes.c_char_p,
                            ctypes.POINTER(ParmId) ]

GetParmIntValue = _hapi.HAPI_GetParmIntValue
GetParmIntValue.restype = Result
GetParmIntValue.argtypes = [ ctypes.POINTER(Session),
                             NodeId,
                             ctypes.c_char_p,
                             ctypes.c_int,
                             ctypes.POINTER(ctypes.c_int) ]

GetParmIntValues = _hapi.HAPI_GetParmIntValues
GetParmIntValues.restype = Result
GetParmIntValues.argtypes = [ ctypes.POINTER(Session),
                              NodeId,
                              ctypes.POINTER(ctypes.c_int),
                              ctypes.c_int,
                              ctypes.c_int ]

GetParmFloatValue = _hapi.HAPI_GetParmFloatValue
GetParmFloatValue.restype = Result
GetParmFloatValue.argtypes = [ ctypes.POINTER(Session),
                               NodeId,
                               ctypes.c_char_p,
                               ctypes.c_int,
                               ctypes.POINTER(ctypes.c_float) ]

GetParmFloatValues = _hapi.HAPI_GetParmFloatValues
GetParmFloatValues.restype = Result
GetParmFloatValues.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                ctypes.POINTER(ctypes.c_float),
                                ctypes.c_int,
                                ctypes.c_int ]

GetParmStringValue = _hapi.HAPI_GetParmStringValue
GetParmStringValue.restype = Result
GetParmStringValue.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                ctypes.c_char_p,
                                ctypes.c_int,
                                Bool,
                                ctypes.POINTER(StringHandle) ]

GetParmStringValues = _hapi.HAPI_GetParmStringValues
GetParmStringValues.restype = Result
GetParmStringValues.argtypes = [ ctypes.POINTER(Session),
                                 NodeId,
                                 Bool,
                                 ctypes.POINTER(StringHandle),
                                 ctypes.c_int,
                                 ctypes.c_int ]

GetParmNodeValue = _hapi.HAPI_GetParmNodeValue
GetParmNodeValue.restype = Result
GetParmNodeValue.argtypes = [ ctypes.POINTER(Session),
                              NodeId,
                              ctypes.c_char_p,
                              ctypes.POINTER(NodeId) ]

GetParmFile = _hapi.HAPI_GetParmFile
GetParmFile.restype = Result
GetParmFile.argtypes = [ ctypes.POINTER(Session),
                         NodeId,
                         ctypes.c_char_p,
                         ctypes.c_char_p,
                         ctypes.c_char_p ]

GetParmChoiceLists = _hapi.HAPI_GetParmChoiceLists
GetParmChoiceLists.restype = Result
GetParmChoiceLists.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                ctypes.POINTER(ParmChoiceInfo),
                                ctypes.c_int,
                                ctypes.c_int ]

SetParmIntValue = _hapi.HAPI_SetParmIntValue
SetParmIntValue.restype = Result
SetParmIntValue.argtypes = [ ctypes.POINTER(Session),
                             NodeId,
                             ctypes.c_char_p,
                             ctypes.c_int,
                             ctypes.c_int ]

SetParmIntValues = _hapi.HAPI_SetParmIntValues
SetParmIntValues.restype = Result
SetParmIntValues.argtypes = [ ctypes.POINTER(Session),
                              NodeId,
                              ctypes.POINTER(ctypes.c_int),
                              ctypes.c_int,
                              ctypes.c_int ]

SetParmFloatValue = _hapi.HAPI_SetParmFloatValue
SetParmFloatValue.restype = Result
SetParmFloatValue.argtypes = [ ctypes.POINTER(Session),
                               NodeId,
                               ctypes.c_char_p,
                               ctypes.c_int,
                               ctypes.c_float ]

SetParmFloatValues = _hapi.HAPI_SetParmFloatValues
SetParmFloatValues.restype = Result
SetParmFloatValues.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                ctypes.POINTER(ctypes.c_float),
                                ctypes.c_int,
                                ctypes.c_int ]

SetParmStringValue = _hapi.HAPI_SetParmStringValue
SetParmStringValue.restype = Result
SetParmStringValue.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                ctypes.c_char_p,
                                ParmId,
                                ctypes.c_int ]

SetParmNodeValue = _hapi.HAPI_SetParmNodeValue
SetParmNodeValue.restype = Result
SetParmNodeValue.argtypes = [ ctypes.POINTER(Session),
                              NodeId,
                              ctypes.c_char_p,
                              NodeId ]

InsertMultiparmInstance = _hapi.HAPI_InsertMultiparmInstance
InsertMultiparmInstance.restype = Result
InsertMultiparmInstance.argtypes = [ ctypes.POINTER(Session),
                                     NodeId,
                                     ParmId,
                                     ctypes.c_int ]

RemoveMultiparmInstance = _hapi.HAPI_RemoveMultiparmInstance
RemoveMultiparmInstance.restype = Result
RemoveMultiparmInstance.argtypes = [ ctypes.POINTER(Session),
                                     NodeId,
                                     ParmId,
                                     ctypes.c_int ]


GetHandleInfo = _hapi.HAPI_GetHandleInfo
GetHandleInfo.restype = Result
GetHandleInfo.argtypes = [ ctypes.POINTER(Session),
                           NodeId,
                           ctypes.POINTER(HandleInfo),
                           ctypes.c_int,
                           ctypes.c_int ]

GetHandleBindingInfo = _hapi.HAPI_GetHandleBindingInfo
GetHandleBindingInfo.restype = Result
GetHandleBindingInfo.argtypes = [ ctypes.POINTER(Session),
                                  NodeId,
                                  ctypes.c_int,
                                  ctypes.POINTER(HandleBindingInfo),
                                  ctypes.c_int,
                                  ctypes.c_int ]

GetPresetBufLength = _hapi.HAPI_GetPresetBufLength
GetPresetBufLength.restype = Result
GetPresetBufLength.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                PresetType,
                                ctypes.c_char_p,
                                ctypes.POINTER(ctypes.c_int) ]

GetPreset = _hapi.HAPI_GetPreset
GetPreset.restype = Result
GetPreset.argtypes = [ ctypes.POINTER(Session),
                       NodeId,
                       ctypes.c_char_p,
                       ctypes.c_int ]

SetPreset = _hapi.HAPI_SetPreset
SetPreset.restype = Result
SetPreset.argtypes = [ ctypes.POINTER(Session),
                       NodeId,
                       PresetType,
                       ctypes.c_char_p,
                       ctypes.c_char_p,
                       ctypes.c_int ]

GetObjectInfo = _hapi.HAPI_GetObjectInfo
GetObjectInfo.restype = Result
GetObjectInfo.argtypes = [ ctypes.POINTER(Session),
                           NodeId,
                           ctypes.POINTER(ObjectInfo) ]

GetObjectTransform = _hapi.HAPI_GetObjectTransform
GetObjectTransform.restype = Result
GetObjectTransform.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                NodeId,
                                RSTOrder,
                                ctypes.POINTER(Transform) ]

ComposeObjectList = _hapi.HAPI_ComposeObjectList
ComposeObjectList.restype = Result
ComposeObjectList.argtypes = [ ctypes.POINTER(Session),
                               NodeId,
                               ctypes.c_char_p,
                               ctypes.POINTER(ctypes.c_int) ]

GetComposedObjectList = _hapi.HAPI_GetComposedObjectList
GetComposedObjectList.restype = Result
GetComposedObjectList.argtypes = [ ctypes.POINTER(Session),
                                   NodeId,
                                   ctypes.POINTER(ObjectInfo),
                                   ctypes.c_int,
                                   ctypes.c_int ]

GetComposedObjectTransforms = _hapi.HAPI_GetComposedObjectTransforms
GetComposedObjectTransforms.restype = Result
GetComposedObjectTransforms.argtypes = [ ctypes.POINTER(Session),
                                         NodeId,
                                         RSTOrder,
                                         ctypes.POINTER(Transform),
                                         ctypes.c_int,
                                         ctypes.c_int ]

GetInstancedObjectIds = _hapi.HAPI_GetInstancedObjectIds
GetInstancedObjectIds.restype = Result
GetInstancedObjectIds.argtypes = [ ctypes.POINTER(Session),
                                   NodeId,
                                   ctypes.POINTER(NodeId),
                                   ctypes.c_int,
                                   ctypes.c_int ]

GetInstanceTransforms = _hapi.HAPI_GetInstanceTransforms
GetInstanceTransforms.restype = Result
GetInstanceTransforms.argtypes = [ ctypes.POINTER(Session),
                                   NodeId,
                                   RSTOrder,
                                   ctypes.POINTER(Transform),
                                   ctypes.c_int,
                                   ctypes.c_int ]

SetObjectTransform = _hapi.HAPI_SetObjectTransform
SetObjectTransform.restype = Result
SetObjectTransform.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                ctypes.POINTER(TransformEuler)]


GetDisplayGeoInfo = _hapi.HAPI_GetDisplayGeoInfo
GetDisplayGeoInfo.restype = Result
GetDisplayGeoInfo.argtypes = [ ctypes.POINTER(Session),
                               NodeId,
                               ctypes.POINTER(GeoInfo)]

GetGeoInfo = _hapi.HAPI_GetGeoInfo
GetGeoInfo.restype = Result
GetGeoInfo.argtypes = [ ctypes.POINTER(Session),
                        NodeId,
                        ctypes.POINTER(GeoInfo)]

GetPartInfo = _hapi.HAPI_GetPartInfo
GetPartInfo.restype = Result
GetPartInfo.argtypes = [ ctypes.POINTER(Session),
                         NodeId,
                         PartId,
                         ctypes.POINTER(PartInfo) ]

GetFaceCounts = _hapi.HAPI_GetFaceCounts
GetFaceCounts.restype = Result
GetFaceCounts.argtypes = [ ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           ctypes.POINTER(ctypes.c_int),
                           ctypes.c_int,
                           ctypes.c_int ]

GetVertexList = _hapi.HAPI_GetVertexList
GetVertexList.restype = Result
GetVertexList.argtypes = [ ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           ctypes.POINTER(ctypes.c_int),
                           ctypes.c_int,
                           ctypes.c_int ]

GetAttributeInfo = _hapi.HAPI_GetAttributeInfo
GetAttributeInfo.restype = Result
GetAttributeInfo.argtypes = [ ctypes.POINTER(Session),
                              NodeId,
                              PartId,
                              ctypes.c_char_p,
                              AttributeOwner,
                              ctypes.POINTER(AttributeInfo) ]

GetAttributeNames = _hapi.HAPI_GetAttributeNames
GetAttributeNames.restype = Result
GetAttributeNames.argtypes = [ ctypes.POINTER(Session),
                               NodeId,
                               PartId,
                               AttributeOwner,
                               ctypes.POINTER(StringHandle),
                               ctypes.c_int ]

GetAttributeIntData = _hapi.HAPI_GetAttributeIntData
GetAttributeIntData.restype = Result
GetAttributeIntData.argtypes = [ ctypes.POINTER(Session),
                                 NodeId,
                                 PartId,
                                 ctypes.c_char_p,
                                 ctypes.POINTER(AttributeInfo),
                                 ctypes.c_int,
                                 ctypes.POINTER(ctypes.c_int),
                                 ctypes.c_int,
                                 ctypes.c_int ]

GetAttributeInt64Data = _hapi.HAPI_GetAttributeInt64Data
GetAttributeInt64Data.restype = Result
GetAttributeInt64Data.argtypes = [ ctypes.POINTER(Session),
                                   NodeId,
                                   PartId,
                                   ctypes.c_char_p,
                                   ctypes.POINTER(AttributeInfo),
                                   ctypes.c_int,
                                   ctypes.POINTER(Int64),
                                   ctypes.c_int,
                                   ctypes.c_int ]

GetAttributeFloatData = _hapi.HAPI_GetAttributeFloatData
GetAttributeFloatData.restype = Result
GetAttributeFloatData.argtypes = [ ctypes.POINTER(Session),
                                   NodeId,
                                   PartId,
                                   ctypes.c_char_p,
                                   ctypes.POINTER(AttributeInfo),
                                   ctypes.c_int,
                                   ctypes.POINTER(ctypes.c_float),
                                   ctypes.c_int,
                                   ctypes.c_int ]

GetAttributeFloat64Data = _hapi.HAPI_GetAttributeFloat64Data
GetAttributeFloat64Data.restype = Result
GetAttributeFloat64Data.argtypes = [ ctypes.POINTER(Session),
                                     NodeId,
                                     PartId,
                                     ctypes.c_char_p,
                                     ctypes.POINTER(AttributeInfo),
                                     ctypes.c_int,
                                     ctypes.POINTER(ctypes.c_double),
                                     ctypes.c_int,
                                     ctypes.c_int ]

GetAttributeStringData = _hapi.HAPI_GetAttributeStringData
GetAttributeStringData.restype = Result
GetAttributeStringData.argtypes = [ ctypes.POINTER(Session),
                                    NodeId,
                                    PartId,
                                    ctypes.c_char_p,
                                    ctypes.POINTER(AttributeInfo),
                                    ctypes.POINTER(StringHandle),
                                    ctypes.c_int, 
                                    ctypes.c_int ]

GetGroupNames = _hapi.HAPI_GetGroupNames
GetGroupNames.restype = Result
GetGroupNames.argtypes = [ ctypes.POINTER(Session),
                           NodeId,
                           GroupType,
                           ctypes.POINTER(StringHandle),
                           ctypes.c_int ]

GetGroupMembership = _hapi.HAPI_GetGroupMembership
GetGroupMembership.restype = Result
GetGroupMembership.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                PartId,
                                GroupType,
                                ctypes.c_char_p,
                                ctypes.POINTER(Bool),
                                ctypes.POINTER(ctypes.c_int),
                                ctypes.c_int,
                                ctypes.c_int ]

GetInstancedPartIds = _hapi.HAPI_GetInstancedPartIds
GetInstancedPartIds.restype = Result
GetInstancedPartIds.argtypes = [ ctypes.POINTER(Session),
                                 NodeId,
                                 PartId,
                                 ctypes.POINTER(PartId),
                                 ctypes.c_int,
                                 ctypes.c_int ]

GetInstancerPartTransforms = _hapi.HAPI_GetInstancerPartTransforms
GetInstancerPartTransforms.restype = Result
GetInstancerPartTransforms.argtypes = [ ctypes.POINTER(Session),
                                        NodeId,
                                        PartId,
                                        RSTOrder,
                                        ctypes.POINTER(Transform),
                                        ctypes.c_int,
                                        ctypes.c_int ]


SetPartInfo = _hapi.HAPI_SetPartInfo
SetPartInfo.restype = Result
SetPartInfo.argtypes = [ ctypes.POINTER(Session),
                         NodeId,
                         PartId,
                         ctypes.POINTER(PartInfo) ]

SetFaceCounts = _hapi.HAPI_SetFaceCounts
SetFaceCounts.restype = Result
SetFaceCounts.argtypes = [ ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           ctypes.POINTER(ctypes.c_int),
                           ctypes.c_int,
                           ctypes.c_int ]

SetVertexList = _hapi.HAPI_SetVertexList
SetVertexList.restype = Result
SetVertexList.argtypes = [ ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           ctypes.POINTER(ctypes.c_int),
                           ctypes.c_int,
                           ctypes.c_int ]

AddAttribute = _hapi.HAPI_AddAttribute
AddAttribute.restype = Result
AddAttribute.argtypes = [ ctypes.POINTER(Session),
                          NodeId,
                          PartId,
                          ctypes.c_char_p,
                          ctypes.POINTER(AttributeInfo)]

SetAttributeIntData = _hapi.HAPI_SetAttributeIntData
SetAttributeIntData.restype = Result
SetAttributeIntData.argtypes = [ ctypes.POINTER(Session),
                                 NodeId,
                                 PartId,
                                 ctypes.c_char_p,
                                 ctypes.POINTER(AttributeInfo),
                                 ctypes.POINTER(ctypes.c_int),
                                 ctypes.c_int,
                                 ctypes.c_int ]

SetAttributeInt64Data = _hapi.HAPI_SetAttributeInt64Data
SetAttributeInt64Data.restype = Result
SetAttributeInt64Data.argtypes = [ ctypes.POINTER(Session),
                                   NodeId,
                                   PartId,
                                   ctypes.c_char_p,
                                   ctypes.POINTER(AttributeInfo),
                                   ctypes.POINTER(Int64),
                                   ctypes.c_int,
                                   ctypes.c_int ]

SetAttributeFloatData = _hapi.HAPI_SetAttributeFloatData
SetAttributeFloatData.restype = Result
SetAttributeFloatData.argtypes = [ ctypes.POINTER(Session),
                                   NodeId,
                                   PartId,
                                   ctypes.c_char_p,
                                   ctypes.POINTER(AttributeInfo),
                                   ctypes.POINTER(ctypes.c_float),
                                   ctypes.c_int,
                                   ctypes.c_int ]

SetAttributeFloat64Data = _hapi.HAPI_SetAttributeFloat64Data
SetAttributeFloat64Data.restype = Result
SetAttributeFloat64Data.argtypes = [ ctypes.POINTER(Session),
                                     NodeId,
                                     PartId,
                                     ctypes.c_char_p,
                                     ctypes.POINTER(AttributeInfo),
                                     ctypes.POINTER(ctypes.c_double),
                                     ctypes.c_int,
                                     ctypes.c_int ]

SetAttributeStringData = _hapi.HAPI_SetAttributeStringData
SetAttributeStringData.restype = Result
SetAttributeStringData.argtypes = [ ctypes.POINTER(Session),
                                    NodeId,
                                    PartId,
                                    ctypes.c_char_p,
                                    ctypes.POINTER(AttributeInfo),
                                    ctypes.POINTER(ctypes.c_char_p),
                                    ctypes.c_int,
                                    ctypes.c_int ]

AddGroup = _hapi.HAPI_AddGroup
AddGroup.restype = Result
AddGroup.argtypes = [ ctypes.POINTER(Session),
                      NodeId,
                      PartId,
                      GroupType,
                      ctypes.c_char_p ]

SetGroupMembership = _hapi.HAPI_SetGroupMembership
SetGroupMembership.restype = Result
SetGroupMembership.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                PartId,
                                GroupType,
                                ctypes.c_char_p,
                                ctypes.POINTER(ctypes.c_int),
                                ctypes.c_int,
                                ctypes.c_int ]

CommitGeo = _hapi.HAPI_CommitGeo
CommitGeo.restype = Result
CommitGeo.argtypes = [ ctypes.POINTER(Session),
                       NodeId ]

RevertGeo = _hapi.HAPI_RevertGeo
RevertGeo.restype = Result
RevertGeo.argtypes = [ ctypes.POINTER(Session),
                       NodeId ]

GetMaterialNodeIdsOnFaces = _hapi.HAPI_GetMaterialNodeIdsOnFaces
GetMaterialNodeIdsOnFaces.restype = Result
GetMaterialNodeIdsOnFaces.argtypes = [ ctypes.POINTER(Session),
                                       NodeId,
                                       PartId,
                                       ctypes.POINTER(Bool),
                                       ctypes.POINTER(NodeId),
                                       ctypes.c_int,
                                       ctypes.c_int ]

GetMaterialInfo = _hapi.HAPI_GetMaterialInfo
GetMaterialInfo.restype = Result
GetMaterialInfo.argtypes = [ ctypes.POINTER(Session),
                             NodeId,
                             ctypes.POINTER(MaterialInfo) ]

RenderCOPToImage = _hapi.HAPI_RenderCOPToImage
RenderCOPToImage.restype = Result
RenderCOPToImage.argtypes = [ ctypes.POINTER(Session),
                              NodeId ]

RenderTextureToImage = _hapi.HAPI_RenderTextureToImage
RenderTextureToImage.restype = Result
RenderTextureToImage.argtypes = [ ctypes.POINTER(Session),
                                  NodeId,
                                  ParmId ]

GetImageInfo = _hapi.HAPI_GetImageInfo
GetImageInfo.restype = Result
GetImageInfo.argtypes = [ ctypes.POINTER(Session),
                          NodeId,
                          ctypes.POINTER(ImageInfo) ]

SetImageInfo = _hapi.HAPI_SetImageInfo
SetImageInfo.restype = Result
SetImageInfo.argtypes = [ ctypes.POINTER(Session),
                          NodeId,
                          ctypes.POINTER(ImageInfo) ]

GetImagePlaneCount = _hapi.HAPI_GetImagePlaneCount
GetImagePlaneCount.restype = Result
GetImagePlaneCount.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                ctypes.POINTER(ctypes.c_int) ]

GetImagePlanes = _hapi.HAPI_GetImagePlanes
GetImagePlanes.restype = Result
GetImagePlanes.argtypes = [ ctypes.POINTER(Session),
                            NodeId,
                            ctypes.POINTER(StringHandle),
                            ctypes.c_int ]

ExtractImageToFile = _hapi.HAPI_ExtractImageToFile
ExtractImageToFile.restype = Result
ExtractImageToFile.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                ctypes.c_char_p,
                                ctypes.c_char_p,
                                ctypes.c_char_p,
                                ctypes.c_char_p,
                                ctypes.POINTER(ctypes.c_int) ]

ExtractImageToMemory = _hapi.HAPI_ExtractImageToMemory
ExtractImageToMemory.restype = Result
ExtractImageToMemory.argtypes = [ ctypes.POINTER(Session),
                                  NodeId,
                                  ctypes.c_char_p,
                                  ctypes.c_char_p,
                                  ctypes.POINTER(ctypes.c_int) ]

GetImageMemoryBuffer = _hapi.HAPI_GetImageMemoryBuffer
GetImageMemoryBuffer.restype = Result
GetImageMemoryBuffer.argtypes = [ ctypes.POINTER(Session),
                                  NodeId,
                                  ctypes.c_char_p,
                                  ctypes.c_int ]

GetSupportedImageFileFormatCount = _hapi.HAPI_GetSupportedImageFileFormatCount
GetSupportedImageFileFormatCount.restype = Result
GetSupportedImageFileFormatCount.argtypes = [ ctypes.POINTER(Session),
                                              ctypes.POINTER(ctypes.c_int) ]

GetSupportedImageFileFormats = _hapi.HAPI_GetSupportedImageFileFormats
GetSupportedImageFileFormats.restype = Result
GetSupportedImageFileFormats.argtypes = [ ctypes.POINTER(Session),
                                          ctypes.POINTER(ImageFileFormat),
                                          ctypes.c_int ]

SetAnimCurve = _hapi.HAPI_SetAnimCurve
SetAnimCurve.restype = Result
SetAnimCurve.argtypes = [ ctypes.POINTER(Session),
                          NodeId,
                          ParmId,
                          ctypes.c_int,
                          ctypes.POINTER(Keyframe),
                          ctypes.c_int ]

SetTransformAnimCurve = _hapi.HAPI_SetTransformAnimCurve
SetTransformAnimCurve.restype = Result
SetTransformAnimCurve.argtypes = [ ctypes.POINTER(Session),
                                   NodeId,
                                   TransformComponent,
                                   ctypes.POINTER(Keyframe),
                                   ctypes.c_int ]

ResetSimulation = _hapi.HAPI_ResetSimulation
ResetSimulation.restype = Result
ResetSimulation.argtypes = [ ctypes.POINTER(Session),
                             NodeId ]

GetVolumeInfo = _hapi.HAPI_GetVolumeInfo
GetVolumeInfo.restype = Result
GetVolumeInfo.argtypes = [ ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           ctypes.POINTER(VolumeInfo) ]

GetFirstVolumeTile = _hapi.HAPI_GetFirstVolumeTile
GetFirstVolumeTile.restype = Result
GetFirstVolumeTile.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                PartId,
                                ctypes.POINTER(VolumeTileInfo) ]

GetNextVolumeTile = _hapi.HAPI_GetNextVolumeTile
GetNextVolumeTile.restype = Result
GetNextVolumeTile.argtypes = [ ctypes.POINTER(Session),
                               NodeId,
                               PartId,
                               ctypes.POINTER(VolumeTileInfo) ]

GetVolumeVoxelFloatData = _hapi.HAPI_GetVolumeVoxelFloatData
GetVolumeVoxelFloatData.restype = Result
GetVolumeVoxelFloatData.argtypes = [ ctypes.POINTER(Session),
                                     NodeId,
                                     PartId,
                                     ctypes.c_int,
                                     ctypes.c_int,
                                     ctypes.c_int,
                                     ctypes.POINTER(ctypes.c_float),
                                     ctypes.c_int ]

GetVolumeTileFloatData = _hapi.HAPI_GetVolumeTileFloatData
GetVolumeTileFloatData.restype = Result
GetVolumeTileFloatData.argtypes = [ ctypes.POINTER(Session),
                                    NodeId,
                                    PartId,
                                    ctypes.c_float,
                                    ctypes.POINTER(VolumeTileInfo),
                                    ctypes.POINTER(ctypes.c_float),
                                    ctypes.c_int ]

GetVolumeVoxelIntData = _hapi.HAPI_GetVolumeVoxelIntData
GetVolumeVoxelIntData.restype = Result
GetVolumeVoxelIntData.argtypes = [ ctypes.POINTER(Session),
                                   NodeId,
                                   PartId,
                                   ctypes.c_int,
                                   ctypes.c_int,
                                   ctypes.c_int,
                                   ctypes.POINTER(ctypes.c_int),
                                   ctypes.c_int ]

GetVolumeTileIntData = _hapi.HAPI_GetVolumeTileIntData
GetVolumeTileIntData.restype = Result
GetVolumeTileIntData.argtypes = [ ctypes.POINTER(Session),
                                  NodeId,
                                  PartId,
                                  ctypes.c_int,
                                  ctypes.POINTER(VolumeTileInfo),
                                  ctypes.POINTER(ctypes.c_int),
                                  ctypes.c_int ]

GetHeightFieldData = _hapi.HAPI_GetHeightFieldData
GetHeightFieldData.restype = Result
GetHeightFieldData.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                PartId,
                                ctypes.POINTER(ctypes.c_float),
                                ctypes.c_int,
                                ctypes.c_int]

SetVolumeInfo = _hapi.HAPI_SetVolumeInfo
SetVolumeInfo.restype = Result
SetVolumeInfo.argtypes = [ ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           ctypes.POINTER(VolumeInfo) ]

SetVolumeTileFloatData = _hapi.HAPI_SetVolumeTileFloatData
SetVolumeTileFloatData.restype = Result
SetVolumeTileFloatData.argtypes = [ ctypes.POINTER(Session),
                                    NodeId,
                                    PartId,
                                    ctypes.POINTER(VolumeTileInfo),
                                    ctypes.POINTER(ctypes.c_float),
                                    ctypes.c_int ]

SetVolumeTileIntData = _hapi.HAPI_SetVolumeTileIntData
SetVolumeTileIntData.restype = Result
SetVolumeTileIntData.argtypes = [ ctypes.POINTER(Session),
                                  NodeId,
                                  PartId,
                                  ctypes.POINTER(VolumeTileInfo),
                                  ctypes.POINTER(ctypes.c_int),
                                  ctypes.c_int ]

SetVolumeVoxelFloatData = _hapi.HAPI_SetVolumeVoxelFloatData
SetVolumeVoxelFloatData.restype = Result
SetVolumeVoxelFloatData.argtypes = [ ctypes.POINTER(Session),
                                     NodeId,
                                     PartId,
                                     ctypes.c_int,
                                     ctypes.c_int,
                                     ctypes.c_int,
                                     ctypes.POINTER(ctypes.c_float),
                                     ctypes.c_int ]

SetVolumeVoxelIntData = _hapi.HAPI_SetVolumeVoxelIntData
SetVolumeVoxelIntData.restype = Result
SetVolumeVoxelIntData.argtypes = [ ctypes.POINTER(Session),
                                   NodeId,
                                   PartId,
                                   ctypes.c_int,
                                   ctypes.c_int,
                                   ctypes.c_int,
                                   ctypes.POINTER(ctypes.c_int),
                                   ctypes.c_int ]

GetVolumeBounds = _hapi.HAPI_GetVolumeBounds
GetVolumeBounds.restype = Result
GetVolumeBounds.argtypes = [ ctypes.POINTER(Session),
                             NodeId,
                             PartId,
                             ctypes.POINTER(ctypes.c_float),
                             ctypes.POINTER(ctypes.c_float),
                             ctypes.POINTER(ctypes.c_float),
                             ctypes.POINTER(ctypes.c_float),
                             ctypes.POINTER(ctypes.c_float),
                             ctypes.POINTER(ctypes.c_float),
                             ctypes.POINTER(ctypes.c_float),
                             ctypes.POINTER(ctypes.c_float),
                             ctypes.POINTER(ctypes.c_float) ]

SetHeightFieldData = _hapi.HAPI_SetHeightFieldData
SetHeightFieldData.restype = Result
SetHeightFieldData.argtypes = [ ctypes.POINTER(Session),
                                NodeId,
                                PartId,
                                ctypes.POINTER(ctypes.c_float),
                                ctypes.c_int,
                                ctypes.c_int,
                                ctypes.c_char_p ]

GetCurveInfo = _hapi.HAPI_GetCurveInfo
GetCurveInfo.restype = Result
GetCurveInfo.argtypes = [ ctypes.POINTER(Session),
                          NodeId,
                          PartId,
                          ctypes.POINTER(CurveInfo) ]

GetCurveCounts = _hapi.HAPI_GetCurveCounts
GetCurveCounts.restype = Result
GetCurveCounts.argtypes = [ ctypes.POINTER(Session),
                            NodeId,
                            PartId,
                            ctypes.POINTER(ctypes.c_int),
                            ctypes.c_int,
                            ctypes.c_int ]

GetCurveOrders = _hapi.HAPI_GetCurveOrders
GetCurveOrders.restype = Result
GetCurveOrders.argtypes = [ ctypes.POINTER(Session),
                            NodeId,
                            PartId,
                            ctypes.POINTER(ctypes.c_int),
                            ctypes.c_int,
                            ctypes.c_int ]

GetCurveKnots = _hapi.HAPI_GetCurveKnots
GetCurveKnots.restype = Result
GetCurveKnots.argtypes = [ ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           ctypes.POINTER(ctypes.c_float),
                           ctypes.c_int,
                           ctypes.c_int ]

SetCurveInfo = _hapi.HAPI_SetCurveInfo
SetCurveInfo.restype = Result
SetCurveInfo.argtypes = [ ctypes.POINTER(Session),
                          NodeId,
                          PartId,
                          ctypes.POINTER(CurveInfo) ]

SetCurveCounts = _hapi.HAPI_SetCurveCounts
SetCurveCounts.restype = Result
SetCurveCounts.argtypes = [ ctypes.POINTER(Session),
                            NodeId,
                            PartId,
                            ctypes.POINTER(ctypes.c_int),
                            ctypes.c_int,
                            ctypes.c_int ]

SetCurveOrders = _hapi.HAPI_SetCurveOrders
SetCurveOrders.restype = Result
SetCurveOrders.argtypes = [ ctypes.POINTER(Session),
                            NodeId,
                            PartId,
                            ctypes.POINTER(ctypes.c_int),
                            ctypes.c_int,
                            ctypes.c_int ]

SetCurveKnots = _hapi.HAPI_SetCurveKnots
SetCurveKnots.restype = Result
SetCurveKnots.argtypes = [ ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           ctypes.POINTER(ctypes.c_float),
                           ctypes.c_int,
                           ctypes.c_int ]

GetBoxInfo = _hapi.HAPI_GetBoxInfo
GetBoxInfo.restype = Result
GetBoxInfo.argtypes = [ ctypes.POINTER(Session),
                        NodeId,
                        PartId,
                        ctypes.POINTER(BoxInfo) ]

GetSphereInfo = _hapi.HAPI_GetSphereInfo
GetSphereInfo.restype = Result
GetSphereInfo.argtypes = [ ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           ctypes.POINTER(SphereInfo) ]


GetActiveCacheCount = _hapi.HAPI_GetActiveCacheCount
GetActiveCacheCount.restype = Result
GetActiveCacheCount.argtypes = [ ctypes.POINTER(Session),
                                 ctypes.POINTER(ctypes.c_int) ]

GetActiveCacheNames = _hapi.HAPI_GetActiveCacheNames
GetActiveCacheNames.restype = Result
GetActiveCacheNames.argtypes = [ ctypes.POINTER(Session),
                                 ctypes.POINTER(StringHandle),
                                 ctypes.c_int ]

GetCacheProperty = _hapi.HAPI_GetCacheProperty
GetCacheProperty.restype = Result
GetCacheProperty.argtypes = [ ctypes.POINTER(Session),
                              ctypes.c_char_p,
                              CacheProperty,
                              ctypes.POINTER(ctypes.c_int) ]

SetCacheProperty = _hapi.HAPI_SetCacheProperty
SetCacheProperty.restype = Result
SetCacheProperty.argtypes = [ ctypes.POINTER(Session),
                              ctypes.c_char_p,
                              CacheProperty,
                              ctypes.c_int ]

SaveGeoToFile = _hapi.HAPI_SaveGeoToFile
SaveGeoToFile.restype = Result
SaveGeoToFile.argtypes = [ ctypes.POINTER(Session),
                           NodeId,
                           ctypes.c_char_p ]

LoadGeoFromFile = _hapi.HAPI_LoadGeoFromFile
LoadGeoFromFile.restype = Result
LoadGeoFromFile.argtypes = [ ctypes.POINTER(Session),
                             NodeId,
                             ctypes.c_char_p ]

GetGeoSize = _hapi.HAPI_GetGeoSize
GetGeoSize.restype = Result
GetGeoSize.argtypes = [ ctypes.POINTER(Session),
                        NodeId,
                        ctypes.c_char_p,
                        ctypes.POINTER(ctypes.c_int) ]

SaveGeoToMemory = _hapi.HAPI_SaveGeoToMemory
SaveGeoToMemory.restype = Result
SaveGeoToMemory.argtypes = [ ctypes.POINTER(Session),
                             NodeId,
                             ctypes.c_char_p,
                             ctypes.c_int ]

LoadGeoFromMemory = _hapi.HAPI_LoadGeoFromMemory
LoadGeoFromMemory.restype = Result
LoadGeoFromMemory.argtypes = [ ctypes.POINTER(Session),
                               NodeId,
                               ctypes.c_char_p,
                               ctypes.c_char_p,
                               ctypes.c_int ]
