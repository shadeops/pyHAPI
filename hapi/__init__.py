from __future__ import absolute_import

import ctypes as _ctypes

from ._library import libHAPI as _hapi
from .version import *
from .common import *
from .helpers import *

CreateInProcessSession = _hapi.HAPI_CreateInProcessSession
CreateInProcessSession.restype = Result
CreateInProcessSession.argtypes = [ _ctypes.POINTER(Session) ]

StartThriftSocketServer = _hapi.HAPI_StartThriftSocketServer
StartThriftSocketServer.restype = Result
StartThriftSocketServer.argtypes = [ _ctypes.POINTER(ThriftServerOptions),
                                     _ctypes.c_int,
                                     _ctypes.POINTER(ProcessId) ]

CreateThriftSocketSession = _hapi.HAPI_CreateThriftSocketSession
CreateThriftSocketSession.restype = Result
CreateThriftSocketSession.argtypes = [ _ctypes.POINTER(Session),
                                       _ctypes.c_char_p,
                                       _ctypes.c_int ]

StartThriftNamedPipeServer = _hapi.HAPI_StartThriftNamedPipeServer
StartThriftNamedPipeServer.restype = Result
StartThriftNamedPipeServer.argtypes = [ _ctypes.POINTER(ThriftServerOptions),
                                        _ctypes.c_char_p,
                                        _ctypes.POINTER(ProcessId) ]

CreateThriftNamedPipeSession = _hapi.HAPI_CreateThriftNamedPipeSession
CreateThriftNamedPipeSession.restype = Result
CreateThriftNamedPipeSession.argtypes = [ _ctypes.POINTER(Session),
                                          _ctypes.c_char_p ]

BindCustomImplementation = _hapi.HAPI_BindCustomImplementation
BindCustomImplementation.restype = Result
BindCustomImplementation.argtypes = [ SessionType,
                                      _ctypes.c_char_p ]

CreateCustomSession = _hapi.HAPI_CreateCustomSession
CreateCustomSession.restype = Result
CreateCustomSession.argtypes = [ SessionType,
                                 _ctypes.c_void_p,
                                 _ctypes.POINTER(Session) ]

IsSessionValid = _hapi.HAPI_IsSessionValid
IsSessionValid.restype = Result
IsSessionValid.argtypes = [ _ctypes.POINTER(Session) ]

CloseSession = _hapi.HAPI_CloseSession
CloseSession.restype = Result
CloseSession.argtypes = [ _ctypes.POINTER(Session) ]

IsInitialized = _hapi.HAPI_IsInitialized
IsInitialized.restype = Result
IsInitialized.argtypes = [ _ctypes.POINTER(Session) ]


Initialize = _hapi.HAPI_Initialize
Initialize.restype = Result
Initialize.argtypes = [ _ctypes.POINTER(Session),
                        _ctypes.POINTER(CookOptions),
                        Bool,
                        _ctypes.c_int,
                        _ctypes.c_char_p,
                        _ctypes.c_char_p,
                        _ctypes.c_char_p,
                        _ctypes.c_char_p,
                        _ctypes.c_char_p ]

Cleanup = _hapi.HAPI_Cleanup
Cleanup.restype = Result
Cleanup.argtypes = [_ctypes.POINTER(Session)]


GetEnvInt = _hapi.HAPI_GetEnvInt
GetEnvInt.restype = Result
GetEnvInt.argtypes = [ EnvIntType,
                       _ctypes.POINTER(_ctypes.c_int) ]

GetSessionEnvInt = _hapi.HAPI_GetSessionEnvInt
GetSessionEnvInt.restype = Result
GetSessionEnvInt.argtypes = [ _ctypes.POINTER(Session),
                              SessionEnvIntType,
                              _ctypes.POINTER(_ctypes.c_int) ]

GetServerEnvInt = _hapi.HAPI_GetServerEnvInt
GetServerEnvInt.restype = Result
GetServerEnvInt.argtypes = [ _ctypes.POINTER(Session),
                             _ctypes.c_char_p,
                             _ctypes.POINTER(_ctypes.c_int) ]

GetServerEnvString = _hapi.HAPI_GetServerEnvString
GetServerEnvString.restype = Result
GetServerEnvString.argtypes = [ _ctypes.POINTER(Session),
                                _ctypes.c_char_p,
                                _ctypes.POINTER(StringHandle) ]

GetServerEnvVarCount = _hapi.HAPI_GetServerEnvVarCount
GetServerEnvVarCount.restype = Result
GetServerEnvVarCount.argtypes = [ _ctypes.POINTER(Session),
                               _ctypes.POINTER(_ctypes.c_int) ]

GetServerEnvVarList = _hapi.HAPI_GetServerEnvVarList
GetServerEnvVarList.restype = Result
GetServerEnvVarList.argtypes = [ _ctypes.POINTER(Session),
                                 _ctypes.POINTER(StringHandle),
                                 _ctypes.c_int,
                                 _ctypes.c_int ]

SetServerEnvInt = _hapi.HAPI_SetServerEnvInt
SetServerEnvInt.restype = Result
SetServerEnvInt.argtypes = [ _ctypes.POINTER(Session),
                             _ctypes.c_char_p,
                             _ctypes.c_int ]

SetServerEnvString = _hapi.HAPI_SetServerEnvString
SetServerEnvString.restype = Result
SetServerEnvString.argtypes = [ _ctypes.POINTER(Session),
                                _ctypes.c_char_p,
                                _ctypes.c_char_p ]

GetStatus = _hapi.HAPI_GetStatus
GetStatus.restype = Result
GetStatus.argtypes = [ _ctypes.POINTER(Session),
                       StatusType,
                       _ctypes.POINTER(_ctypes.c_int) ]

GetStatusStringBufLength = _hapi.HAPI_GetStatusStringBufLength
GetStatusStringBufLength.restype = Result
GetStatusStringBufLength.argtypes = [ _ctypes.POINTER(Session),
                                      StatusType,
                                      StatusVerbosity,
                                      _ctypes.POINTER(_ctypes.c_int) ]

GetStatusString = _hapi.HAPI_GetStatusString
GetStatusString.restype = Result
GetStatusString.argtypes = [ _ctypes.POINTER(Session),
                             StatusType,
                             _ctypes.c_char_p,
                             _ctypes.c_int ]

ComposeNodeCookResult = _hapi.HAPI_ComposeNodeCookResult
ComposeNodeCookResult.restype = Result
ComposeNodeCookResult.argtypes = [ _ctypes.POINTER(Session),
                                   NodeId,
                                   StatusVerbosity,
                                   _ctypes.POINTER(_ctypes.c_int) ]

GetComposedNodeCookResult = _hapi.HAPI_GetComposedNodeCookResult
GetComposedNodeCookResult.restype = Result
GetComposedNodeCookResult.argtypes = [ _ctypes.POINTER(Session),
                                       _ctypes.c_char_p,
                                       _ctypes.c_int ]

CheckForSpecificErrors = _hapi.HAPI_CheckForSpecificErrors
CheckForSpecificErrors.restype = Result
CheckForSpecificErrors.argtypes = [ _ctypes.POINTER(Session),
                                    NodeId,
                                    ErrorCodeBits,
                                    _ctypes.POINTER(ErrorCodeBits) ]

GetCookingTotalCount = _hapi.HAPI_GetCookingTotalCount
GetCookingTotalCount.restype = Result
GetCookingTotalCount.argtypes = [ _ctypes.POINTER(Session),
                                  _ctypes.POINTER(_ctypes.c_int) ]

GetCookingCurrentCount = _hapi.HAPI_GetCookingCurrentCount
GetCookingCurrentCount.restype = Result
GetCookingCurrentCount.argtypes = [ _ctypes.POINTER(Session),
                                    _ctypes.POINTER(_ctypes.c_int) ]

ConvertTransform = _hapi.HAPI_ConvertTransform
ConvertTransform.restype = Result
ConvertTransform.argtypes = [ _ctypes.POINTER(Session),
                              _ctypes.POINTER(TransformEuler),
                              RSTOrder,
                              XYZOrder,
                              _ctypes.POINTER(TransformEuler) ]

ConvertMatrixToQuat = _hapi.HAPI_ConvertMatrixToQuat
ConvertMatrixToQuat.restype = Result
ConvertMatrixToQuat.argtypes = [ _ctypes.POINTER(Session),
                                 _ctypes.POINTER(_ctypes.c_float),
                                 RSTOrder,
                                 _ctypes.POINTER(Transform) ]

ConvertMatrixToEuler = _hapi.HAPI_ConvertMatrixToEuler
ConvertMatrixToEuler.restype = Result
ConvertMatrixToEuler.argtypes = [ _ctypes.POINTER(Session),
                                  _ctypes.POINTER(_ctypes.c_float),
                                  RSTOrder,
                                  XYZOrder,
                                  _ctypes.POINTER(TransformEuler) ]

ConvertTransformQuatToMatrix = _hapi.HAPI_ConvertTransformQuatToMatrix
ConvertTransformQuatToMatrix.restype = Result
ConvertTransformQuatToMatrix.argtypes = [ _ctypes.POINTER(Session),
                                          _ctypes.POINTER(Transform),
                                          _ctypes.POINTER(_ctypes.c_float) ]

ConvertTransformEulerToMatrix = _hapi.HAPI_ConvertTransformEulerToMatrix
ConvertTransformEulerToMatrix.restype = Result
ConvertTransformEulerToMatrix.argtypes = [ _ctypes.POINTER(Session),
                                           _ctypes.POINTER(TransformEuler),
                                           _ctypes.POINTER(_ctypes.c_float) ]

PythonThreadInterpreterLock = _hapi.HAPI_PythonThreadInterpreterLock
PythonThreadInterpreterLock.restype = Result
PythonThreadInterpreterLock.argtypes = [ _ctypes.POINTER(Session),
                                         Bool ]


GetStringBufLength = _hapi.HAPI_GetStringBufLength
GetStringBufLength.restype = Result
GetStringBufLength.argtypes = [ _ctypes.POINTER(Session),
                                StringHandle,
                                _ctypes.POINTER(_ctypes.c_int) ]

GetString = _hapi.HAPI_GetString
GetString.restype = Result
GetString.argtypes = [ _ctypes.POINTER(Session),
                       StringHandle,
                       _ctypes.c_char_p,
                       _ctypes.c_int ]

SetCustomString = _hapi.HAPI_SetCustomString
SetCustomString.restype = Result
SetCustomString.argtypes = [ _ctypes.POINTER(Session),
                             _ctypes.c_char_p,
                             _ctypes.POINTER(StringHandle) ]

RemoveCustomString = _hapi.HAPI_RemoveCustomString
RemoveCustomString.restype = Result
RemoveCustomString.argtypes = [ _ctypes.POINTER(Session),
                                _ctypes.POINTER(StringHandle) ]

GetStringBatchSize = _hapi.HAPI_GetStringBatchSize
GetStringBatchSize.restype = Result
GetStringBatchSize.argtypes = [ _ctypes.POINTER(Session),
                                _ctypes.POINTER(StringHandle),
                                _ctypes.c_int,
                                _ctypes.POINTER(_ctypes.c_int) ]

GetStringBatch = _hapi.HAPI_GetStringBatch
GetStringBatch.restype = Result
GetStringBatch.argtypes = [ _ctypes.POINTER(Session),
                            _ctypes.c_char_p,
                            _ctypes.c_int ]


GetTime = _hapi.HAPI_GetTime
GetTime.restype = Result
GetTime.argtypes = [ _ctypes.POINTER(Session),
                     _ctypes.POINTER(_ctypes.c_float) ]

SetTime = _hapi.HAPI_SetTime
SetTime.restype = Result
SetTime.argtypes = [ _ctypes.POINTER(Session),
                     _ctypes.c_float ]

GetTimelineOptions = _hapi.HAPI_GetTimelineOptions
GetTimelineOptions.restype = Result
GetTimelineOptions.argtypes = [ _ctypes.POINTER(Session),
                                _ctypes.POINTER(TimelineOptions) ]

SetTimelineOptions = _hapi.HAPI_SetTimelineOptions
SetTimelineOptions.restype = Result
SetTimelineOptions.argtypes = [ _ctypes.POINTER(Session),
                                _ctypes.POINTER(TimelineOptions) ]

LoadAssetLibraryFromFile = _hapi.HAPI_LoadAssetLibraryFromFile
LoadAssetLibraryFromFile.restype = Result
LoadAssetLibraryFromFile.argtypes = [ _ctypes.POINTER(Session),
                                      _ctypes.c_char_p,
                                      Bool,
                                      _ctypes.POINTER(AssetLibraryId) ]

LoadAssetLibraryFromMemory = _hapi.HAPI_LoadAssetLibraryFromMemory
LoadAssetLibraryFromMemory.restype = Result
LoadAssetLibraryFromMemory.argtypes = [ _ctypes.POINTER(Session),
                                        _ctypes.c_char_p,
                                        _ctypes.c_int,
                                        Bool,
                                        _ctypes.POINTER(AssetLibraryId) ]

GetAvailableAssetCount = _hapi.HAPI_GetAvailableAssetCount
GetAvailableAssetCount.restype = Result
GetAvailableAssetCount.argtypes = [ _ctypes.POINTER(Session),
                                    AssetLibraryId,
                                    _ctypes.POINTER(_ctypes.c_int) ]

GetAvailableAssets = _hapi.HAPI_GetAvailableAssets
GetAvailableAssets.restype = Result
GetAvailableAssets.argtypes = [ _ctypes.POINTER(Session),
                                AssetLibraryId,
                                _ctypes.POINTER(StringHandle),
                                _ctypes.c_int ]

GetAssetInfo = _hapi.HAPI_GetAssetInfo
GetAssetInfo.restype = Result
GetAssetInfo.argtypes = [ _ctypes.POINTER(Session),
                          NodeId,
                          _ctypes.POINTER(AssetInfo) ]

Interrupt = _hapi.HAPI_Interrupt
Interrupt.restype = Result
Interrupt.argtypes = [ _ctypes.POINTER(Session) ]


LoadHIPFile = _hapi.HAPI_LoadHIPFile
LoadHIPFile.restype = Result
LoadHIPFile.argtypes = [ _ctypes.POINTER(Session),
                         _ctypes.c_char_p,
                         Bool ]

SaveHIPFile = _hapi.HAPI_SaveHIPFile
SaveHIPFile.restype = Result
SaveHIPFile.argtypes = [ _ctypes.POINTER(Session),
                            _ctypes.c_char_p,
                            Bool]

IsNodeValid = _hapi.HAPI_IsNodeValid
IsNodeValid.restype = Result
IsNodeValid.argtypes = [ _ctypes.POINTER(Session),
                         NodeId,
                         _ctypes.c_int,
                         _ctypes.POINTER(Bool) ]

GetNodeInfo = _hapi.HAPI_GetNodeInfo
GetNodeInfo.restype = Result
GetNodeInfo.argtypes = [ _ctypes.POINTER(Session),
                         NodeId,
                         _ctypes.POINTER(NodeInfo) ]

GetNodePath = _hapi.HAPI_GetNodePath
GetNodePath.restype = Result
GetNodePath.argtypes = [ _ctypes.POINTER(Session),
                         NodeId,
                         NodeId,
                         _ctypes.POINTER(StringHandle) ]

GetManagerNodeId = _hapi.HAPI_GetManagerNodeId
GetManagerNodeId.restype = Result
GetManagerNodeId.argtypes = [ _ctypes.POINTER(Session),
                              NodeType,
                              _ctypes.POINTER(NodeId) ]

ComposeChildNodeList = _hapi.HAPI_ComposeChildNodeList
ComposeChildNodeList.restype = Result
ComposeChildNodeList.argtypes = [ _ctypes.POINTER(Session),
                                     NodeId,
                                     NodeTypeBits,
                                     NodeFlagsBits,
                                     Bool,
                                    _ctypes.POINTER(_ctypes.c_int)]

GetComposedChildNodeList = _hapi.HAPI_GetComposedChildNodeList
GetComposedChildNodeList.restype = Result
GetComposedChildNodeList.argtypes = [ _ctypes.POINTER(Session),
                                      NodeId,
                                      _ctypes.POINTER(NodeId),
                                      _ctypes.c_int ]

CreateNode = _hapi.HAPI_CreateNode
CreateNode.restype = Result
CreateNode.argtypes = [ _ctypes.POINTER(Session),
                        NodeId,
                        _ctypes.c_char_p,
                        _ctypes.c_char_p,
                        Bool,
                        _ctypes.POINTER(NodeId) ]

CreateInputNode = _hapi.HAPI_CreateInputNode
CreateInputNode.restype = Result
CreateInputNode.argtypes = [ _ctypes.POINTER(Session),
                             _ctypes.POINTER(NodeId),
                             _ctypes.c_char_p ]

CreateHeightfieldInputNode = _hapi.HAPI_CreateHeightfieldInputNode
CreateHeightfieldInputNode.restype = Result
CreateHeightfieldInputNode.argtypes = [ _ctypes.POINTER(Session),
                                        NodeId,
                                        _ctypes.c_char_p,
                                        _ctypes.c_int,
                                        _ctypes.c_int,
                                        _ctypes.c_float,
                                        _ctypes.POINTER(NodeId),
                                        _ctypes.POINTER(NodeId),
                                        _ctypes.POINTER(NodeId),
                                        _ctypes.POINTER(NodeId),
                                        ]

CreateHeightfieldInputVolumeNode = _hapi.HAPI_CreateHeightfieldInputVolumeNode
CreateHeightfieldInputVolumeNode.restype = Result
CreateHeightfieldInputVolumeNode.argtypes = [ _ctypes.POINTER(Session),
                                              NodeId,
                                              _ctypes.POINTER(NodeId),
                                              _ctypes.c_char_p,
                                              _ctypes.c_int,
                                              _ctypes.c_int,
                                              _ctypes.c_float,
                                        ]

CookNode = _hapi.HAPI_CookNode
CookNode.restype = Result
CookNode.argtypes = [ _ctypes.POINTER(Session),
                      NodeId,
                      _ctypes.POINTER(CookOptions) ]

DeleteNode = _hapi.HAPI_DeleteNode
DeleteNode.restype = Result
DeleteNode.argtypes = [ _ctypes.POINTER(Session),
                        NodeId ]

RenameNode = _hapi.HAPI_RenameNode
RenameNode.restype = Result
RenameNode.argtypes = [ _ctypes.POINTER(Session),
                        NodeId,
                        _ctypes.c_char_p ]

ConnectNodeInput = _hapi.HAPI_ConnectNodeInput
ConnectNodeInput.restype = Result
ConnectNodeInput.argtypes = [ _ctypes.POINTER(Session),
                              NodeId,
                              _ctypes.c_int,
                              NodeId,
                              _ctypes.c_int,
                            ]

DisconnectNodeInput = _hapi.HAPI_DisconnectNodeInput
DisconnectNodeInput.restype = Result
DisconnectNodeInput.argtypes = [ _ctypes.POINTER(Session),
                                 NodeId,
                                 _ctypes.c_int ]

QueryNodeInput = _hapi.HAPI_QueryNodeInput
QueryNodeInput.restype = Result
QueryNodeInput.argtypes = [ _ctypes.POINTER(Session),
                            NodeId,
                            _ctypes.c_int,
                            _ctypes.POINTER(NodeId) ]

GetNodeInputName = _hapi.HAPI_GetNodeInputName
GetNodeInputName.restype = Result
GetNodeInputName.argtypes = [ _ctypes.POINTER(Session),
                              NodeId,
                              _ctypes.c_int,
                              _ctypes.POINTER(StringHandle) ]

DisconnectNodeOutputsAt = _hapi.HAPI_DisconnectNodeOutputsAt
DisconnectNodeOutputsAt.restype = Result
DisconnectNodeOutputsAt.argtypes = [ _ctypes.POINTER(Session),
                                     NodeId,
                                     _ctypes.c_int ]

QueryNodeOutputConnectedCount = _hapi.HAPI_QueryNodeOutputConnectedCount
QueryNodeOutputConnectedCount.restype = Result
QueryNodeOutputConnectedCount.argtypes = [ _ctypes.POINTER(Session),
                                           NodeId,
                                           _ctypes.c_int,
                                           Bool,
                                           Bool,
                                           _ctypes.POINTER(_ctypes.c_int) ]

QueryNodeOutputConnectedNodes = _hapi.HAPI_QueryNodeOutputConnectedNodes
QueryNodeOutputConnectedNodes.restype = Result
QueryNodeOutputConnectedNodes.argtypes = [ _ctypes.POINTER(Session),
                                           NodeId,
                                           _ctypes.c_int,
                                           Bool,
                                           Bool,
                                           _ctypes.POINTER(NodeId),
                                           _ctypes.c_int,
                                           _ctypes.c_int, ]

GetNodeOutputName = _hapi.HAPI_GetNodeOutputName
GetNodeOutputName.restype = Result
GetNodeOutputName.argtypes = [ _ctypes.POINTER(Session),
                               NodeId,
                               _ctypes.c_int,
                               _ctypes.POINTER(StringHandle) ]

GetParameters = _hapi.HAPI_GetParameters
GetParameters.restype = Result
GetParameters.argtypes = [ _ctypes.POINTER(Session),
                           NodeId,
                           _ctypes.POINTER(ParmInfo),
                           _ctypes.c_int,
                           _ctypes.c_int ]

GetParmInfo = _hapi.HAPI_GetParmInfo
GetParmInfo.restype = Result
GetParmInfo.argtypes = [ _ctypes.POINTER(Session),
                         NodeId,
                         ParmId,
                         _ctypes.POINTER(ParmInfo) ]

GetParmIdFromName = _hapi.HAPI_GetParmIdFromName
GetParmIdFromName.restype = Result
GetParmIdFromName.argtypes = [ _ctypes.POINTER(Session),
                               NodeId,
                               _ctypes.c_char_p,
                               _ctypes.POINTER(ParmId) ]

GetParmInfoFromName = _hapi.HAPI_GetParmInfoFromName
GetParmInfoFromName.restype = Result
GetParmInfoFromName.argtypes = [ _ctypes.POINTER(Session),
                                 NodeId,
                                 _ctypes.c_char_p,
                                 _ctypes.POINTER(ParmInfo) ]

GetParmTagName = _hapi.HAPI_GetParmTagName
GetParmTagName.restype = Result
GetParmTagName.argtypes = [ _ctypes.POINTER(Session),
                            NodeId,
                            ParmId,
                            _ctypes.c_int,
                            _ctypes.POINTER(StringHandle) ]

GetParmTagValue = _hapi.HAPI_GetParmTagValue
GetParmTagValue.restype = Result
GetParmTagValue.argtypes = [ _ctypes.POINTER(Session),
                             NodeId,
                             ParmId,
                             _ctypes.c_char_p,
                             _ctypes.POINTER(StringHandle) ]

ParmHasTag = _hapi.HAPI_ParmHasTag
ParmHasTag.restype = Result
ParmHasTag.argtypes = [ _ctypes.POINTER(Session),
                        NodeId,
                        ParmId,
                        _ctypes.c_char_p,
                        _ctypes.POINTER(Bool) ]

ParmHasExpression = _hapi.HAPI_ParmHasExpression
ParmHasExpression.restype = Result
ParmHasExpression.argtypes = [ _ctypes.POINTER(Session),
                               NodeId,
                               _ctypes.c_char_p,
                               _ctypes.c_int,
                               _ctypes.POINTER(Bool) ]

GetParmWithTag = _hapi.HAPI_GetParmWithTag
GetParmWithTag.restype = Result
GetParmWithTag.argtypes = [ _ctypes.POINTER(Session),
                            NodeId,
                            _ctypes.c_char_p,
                            _ctypes.POINTER(ParmId) ]

GetParmExpression = _hapi.HAPI_GetParmExpression
GetParmExpression.restype = Result
GetParmExpression.argtypes = [ _ctypes.POINTER(Session),
                               NodeId,
                               _ctypes.c_char_p,
                               _ctypes.c_int,
                               _ctypes.POINTER(StringHandle) ]

RevertParmToDefault = _hapi.HAPI_RevertParmToDefault
RevertParmToDefault.restype = Result
RevertParmToDefault.argtypes = [ _ctypes.POINTER(Session),
                                 NodeId,
                                 _ctypes.c_char_p,
                                 _ctypes.c_int ]

RevertParmToDefaults = _hapi.HAPI_RevertParmToDefaults
RevertParmToDefaults.restype = Result
RevertParmToDefaults.argtypes = [ _ctypes.POINTER(Session),
                                  NodeId,
                                  _ctypes.c_char_p ]

SetParmExpression = _hapi.HAPI_SetParmExpression
SetParmExpression.restype = Result
SetParmExpression.argtypes = [ _ctypes.POINTER(Session),
                               NodeId,
                               _ctypes.c_char_p,
                               ParmId,
                               _ctypes.c_int ]

RemoveParmExpression = _hapi.HAPI_RemoveParmExpression
RemoveParmExpression.restype = Result
RemoveParmExpression.argtypes = [ _ctypes.POINTER(Session),
                                  NodeId,
                                  ParmId,
                                  _ctypes.c_int ]

GetParmIntValue = _hapi.HAPI_GetParmIntValue
GetParmIntValue.restype = Result
GetParmIntValue.argtypes = [ _ctypes.POINTER(Session),
                             NodeId,
                             _ctypes.c_char_p,
                             _ctypes.c_int,
                             _ctypes.POINTER(_ctypes.c_int) ]

GetParmIntValues = _hapi.HAPI_GetParmIntValues
GetParmIntValues.restype = Result
GetParmIntValues.argtypes = [ _ctypes.POINTER(Session),
                              NodeId,
                              _ctypes.POINTER(_ctypes.c_int),
                              _ctypes.c_int,
                              _ctypes.c_int ]

GetParmFloatValue = _hapi.HAPI_GetParmFloatValue
GetParmFloatValue.restype = Result
GetParmFloatValue.argtypes = [ _ctypes.POINTER(Session),
                               NodeId,
                               _ctypes.c_char_p,
                               _ctypes.c_int,
                               _ctypes.POINTER(_ctypes.c_float) ]

GetParmFloatValues = _hapi.HAPI_GetParmFloatValues
GetParmFloatValues.restype = Result
GetParmFloatValues.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                _ctypes.POINTER(_ctypes.c_float),
                                _ctypes.c_int,
                                _ctypes.c_int ]

GetParmStringValue = _hapi.HAPI_GetParmStringValue
GetParmStringValue.restype = Result
GetParmStringValue.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                _ctypes.c_char_p,
                                _ctypes.c_int,
                                Bool,
                                _ctypes.POINTER(StringHandle) ]

GetParmStringValues = _hapi.HAPI_GetParmStringValues
GetParmStringValues.restype = Result
GetParmStringValues.argtypes = [ _ctypes.POINTER(Session),
                                 NodeId,
                                 Bool,
                                 _ctypes.POINTER(StringHandle),
                                 _ctypes.c_int,
                                 _ctypes.c_int ]

GetParmNodeValue = _hapi.HAPI_GetParmNodeValue
GetParmNodeValue.restype = Result
GetParmNodeValue.argtypes = [ _ctypes.POINTER(Session),
                              NodeId,
                              _ctypes.c_char_p,
                              _ctypes.POINTER(NodeId) ]

GetParmFile = _hapi.HAPI_GetParmFile
GetParmFile.restype = Result
GetParmFile.argtypes = [ _ctypes.POINTER(Session),
                         NodeId,
                         _ctypes.c_char_p,
                         _ctypes.c_char_p,
                         _ctypes.c_char_p ]

GetParmChoiceLists = _hapi.HAPI_GetParmChoiceLists
GetParmChoiceLists.restype = Result
GetParmChoiceLists.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                _ctypes.POINTER(ParmChoiceInfo),
                                _ctypes.c_int,
                                _ctypes.c_int ]

SetParmIntValue = _hapi.HAPI_SetParmIntValue
SetParmIntValue.restype = Result
SetParmIntValue.argtypes = [ _ctypes.POINTER(Session),
                             NodeId,
                             _ctypes.c_char_p,
                             _ctypes.c_int,
                             _ctypes.c_int ]

SetParmIntValues = _hapi.HAPI_SetParmIntValues
SetParmIntValues.restype = Result
SetParmIntValues.argtypes = [ _ctypes.POINTER(Session),
                              NodeId,
                              _ctypes.POINTER(_ctypes.c_int),
                              _ctypes.c_int,
                              _ctypes.c_int ]

SetParmFloatValue = _hapi.HAPI_SetParmFloatValue
SetParmFloatValue.restype = Result
SetParmFloatValue.argtypes = [ _ctypes.POINTER(Session),
                               NodeId,
                               _ctypes.c_char_p,
                               _ctypes.c_int,
                               _ctypes.c_float ]

SetParmFloatValues = _hapi.HAPI_SetParmFloatValues
SetParmFloatValues.restype = Result
SetParmFloatValues.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                _ctypes.POINTER(_ctypes.c_float),
                                _ctypes.c_int,
                                _ctypes.c_int ]

SetParmStringValue = _hapi.HAPI_SetParmStringValue
SetParmStringValue.restype = Result
SetParmStringValue.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                _ctypes.c_char_p,
                                ParmId,
                                _ctypes.c_int ]

SetParmNodeValue = _hapi.HAPI_SetParmNodeValue
SetParmNodeValue.restype = Result
SetParmNodeValue.argtypes = [ _ctypes.POINTER(Session),
                              NodeId,
                              _ctypes.c_char_p,
                              NodeId ]

InsertMultiparmInstance = _hapi.HAPI_InsertMultiparmInstance
InsertMultiparmInstance.restype = Result
InsertMultiparmInstance.argtypes = [ _ctypes.POINTER(Session),
                                     NodeId,
                                     ParmId,
                                     _ctypes.c_int ]

RemoveMultiparmInstance = _hapi.HAPI_RemoveMultiparmInstance
RemoveMultiparmInstance.restype = Result
RemoveMultiparmInstance.argtypes = [ _ctypes.POINTER(Session),
                                     NodeId,
                                     ParmId,
                                     _ctypes.c_int ]


GetHandleInfo = _hapi.HAPI_GetHandleInfo
GetHandleInfo.restype = Result
GetHandleInfo.argtypes = [ _ctypes.POINTER(Session),
                           NodeId,
                           _ctypes.POINTER(HandleInfo),
                           _ctypes.c_int,
                           _ctypes.c_int ]

GetHandleBindingInfo = _hapi.HAPI_GetHandleBindingInfo
GetHandleBindingInfo.restype = Result
GetHandleBindingInfo.argtypes = [ _ctypes.POINTER(Session),
                                  NodeId,
                                  _ctypes.c_int,
                                  _ctypes.POINTER(HandleBindingInfo),
                                  _ctypes.c_int,
                                  _ctypes.c_int ]

GetPresetBufLength = _hapi.HAPI_GetPresetBufLength
GetPresetBufLength.restype = Result
GetPresetBufLength.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                PresetType,
                                _ctypes.c_char_p,
                                _ctypes.POINTER(_ctypes.c_int) ]

GetPreset = _hapi.HAPI_GetPreset
GetPreset.restype = Result
GetPreset.argtypes = [ _ctypes.POINTER(Session),
                       NodeId,
                       _ctypes.c_char_p,
                       _ctypes.c_int ]

SetPreset = _hapi.HAPI_SetPreset
SetPreset.restype = Result
SetPreset.argtypes = [ _ctypes.POINTER(Session),
                       NodeId,
                       PresetType,
                       _ctypes.c_char_p,
                       _ctypes.c_char_p,
                       _ctypes.c_int ]

GetObjectInfo = _hapi.HAPI_GetObjectInfo
GetObjectInfo.restype = Result
GetObjectInfo.argtypes = [ _ctypes.POINTER(Session),
                           NodeId,
                           _ctypes.POINTER(ObjectInfo) ]

GetObjectTransform = _hapi.HAPI_GetObjectTransform
GetObjectTransform.restype = Result
GetObjectTransform.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                NodeId,
                                RSTOrder,
                                _ctypes.POINTER(Transform) ]

ComposeObjectList = _hapi.HAPI_ComposeObjectList
ComposeObjectList.restype = Result
ComposeObjectList.argtypes = [ _ctypes.POINTER(Session),
                               NodeId,
                               _ctypes.c_char_p,
                               _ctypes.POINTER(_ctypes.c_int) ]

GetComposedObjectList = _hapi.HAPI_GetComposedObjectList
GetComposedObjectList.restype = Result
GetComposedObjectList.argtypes = [ _ctypes.POINTER(Session),
                                   NodeId,
                                   _ctypes.POINTER(ObjectInfo),
                                   _ctypes.c_int,
                                   _ctypes.c_int ]

GetComposedObjectTransforms = _hapi.HAPI_GetComposedObjectTransforms
GetComposedObjectTransforms.restype = Result
GetComposedObjectTransforms.argtypes = [ _ctypes.POINTER(Session),
                                         NodeId,
                                         RSTOrder,
                                         _ctypes.POINTER(Transform),
                                         _ctypes.c_int,
                                         _ctypes.c_int ]

GetInstancedObjectIds = _hapi.HAPI_GetInstancedObjectIds
GetInstancedObjectIds.restype = Result
GetInstancedObjectIds.argtypes = [ _ctypes.POINTER(Session),
                                   NodeId,
                                   _ctypes.POINTER(NodeId),
                                   _ctypes.c_int,
                                   _ctypes.c_int ]

GetInstanceTransforms = _hapi.HAPI_GetInstanceTransforms
GetInstanceTransforms.restype = Result
GetInstanceTransforms.argtypes = [ _ctypes.POINTER(Session),
                                   NodeId,
                                   RSTOrder,
                                   _ctypes.POINTER(Transform),
                                   _ctypes.c_int,
                                   _ctypes.c_int ]

GetInstanceTransformsOnPart = _hapi.HAPI_GetInstanceTransformsOnPart
GetInstanceTransformsOnPart.restype = Result
GetInstanceTransformsOnPart.argtypes = [ _ctypes.POINTER(Session),
                                         NodeId,
                                         PartId,
                                         RSTOrder,
                                         _ctypes.POINTER(Transform),
                                         _ctypes.c_int,
                                         _ctypes.c_int ]

SetObjectTransform = _hapi.HAPI_SetObjectTransform
SetObjectTransform.restype = Result
SetObjectTransform.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                _ctypes.POINTER(TransformEuler)]


GetDisplayGeoInfo = _hapi.HAPI_GetDisplayGeoInfo
GetDisplayGeoInfo.restype = Result
GetDisplayGeoInfo.argtypes = [ _ctypes.POINTER(Session),
                               NodeId,
                               _ctypes.POINTER(GeoInfo)]

GetGeoInfo = _hapi.HAPI_GetGeoInfo
GetGeoInfo.restype = Result
GetGeoInfo.argtypes = [ _ctypes.POINTER(Session),
                        NodeId,
                        _ctypes.POINTER(GeoInfo)]

GetPartInfo = _hapi.HAPI_GetPartInfo
GetPartInfo.restype = Result
GetPartInfo.argtypes = [ _ctypes.POINTER(Session),
                         NodeId,
                         PartId,
                         _ctypes.POINTER(PartInfo) ]

GetFaceCounts = _hapi.HAPI_GetFaceCounts
GetFaceCounts.restype = Result
GetFaceCounts.argtypes = [ _ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           _ctypes.POINTER(_ctypes.c_int),
                           _ctypes.c_int,
                           _ctypes.c_int ]

GetVertexList = _hapi.HAPI_GetVertexList
GetVertexList.restype = Result
GetVertexList.argtypes = [ _ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           _ctypes.POINTER(_ctypes.c_int),
                           _ctypes.c_int,
                           _ctypes.c_int ]

GetAttributeInfo = _hapi.HAPI_GetAttributeInfo
GetAttributeInfo.restype = Result
GetAttributeInfo.argtypes = [ _ctypes.POINTER(Session),
                              NodeId,
                              PartId,
                              _ctypes.c_char_p,
                              AttributeOwner,
                              _ctypes.POINTER(AttributeInfo) ]

GetAttributeNames = _hapi.HAPI_GetAttributeNames
GetAttributeNames.restype = Result
GetAttributeNames.argtypes = [ _ctypes.POINTER(Session),
                               NodeId,
                               PartId,
                               AttributeOwner,
                               _ctypes.POINTER(StringHandle),
                               _ctypes.c_int ]

GetAttributeIntData = _hapi.HAPI_GetAttributeIntData
GetAttributeIntData.restype = Result
GetAttributeIntData.argtypes = [ _ctypes.POINTER(Session),
                                 NodeId,
                                 PartId,
                                 _ctypes.c_char_p,
                                 _ctypes.POINTER(AttributeInfo),
                                 _ctypes.c_int,
                                 _ctypes.POINTER(_ctypes.c_int),
                                 _ctypes.c_int,
                                 _ctypes.c_int ]

GetAttributeInt64Data = _hapi.HAPI_GetAttributeInt64Data
GetAttributeInt64Data.restype = Result
GetAttributeInt64Data.argtypes = [ _ctypes.POINTER(Session),
                                   NodeId,
                                   PartId,
                                   _ctypes.c_char_p,
                                   _ctypes.POINTER(AttributeInfo),
                                   _ctypes.c_int,
                                   _ctypes.POINTER(Int64),
                                   _ctypes.c_int,
                                   _ctypes.c_int ]

GetAttributeFloatData = _hapi.HAPI_GetAttributeFloatData
GetAttributeFloatData.restype = Result
GetAttributeFloatData.argtypes = [ _ctypes.POINTER(Session),
                                   NodeId,
                                   PartId,
                                   _ctypes.c_char_p,
                                   _ctypes.POINTER(AttributeInfo),
                                   _ctypes.c_int,
                                   _ctypes.POINTER(_ctypes.c_float),
                                   _ctypes.c_int,
                                   _ctypes.c_int ]

GetAttributeFloat64Data = _hapi.HAPI_GetAttributeFloat64Data
GetAttributeFloat64Data.restype = Result
GetAttributeFloat64Data.argtypes = [ _ctypes.POINTER(Session),
                                     NodeId,
                                     PartId,
                                     _ctypes.c_char_p,
                                     _ctypes.POINTER(AttributeInfo),
                                     _ctypes.c_int,
                                     _ctypes.POINTER(_ctypes.c_double),
                                     _ctypes.c_int,
                                     _ctypes.c_int ]

GetAttributeStringData = _hapi.HAPI_GetAttributeStringData
GetAttributeStringData.restype = Result
GetAttributeStringData.argtypes = [ _ctypes.POINTER(Session),
                                    NodeId,
                                    PartId,
                                    _ctypes.c_char_p,
                                    _ctypes.POINTER(AttributeInfo),
                                    _ctypes.POINTER(StringHandle),
                                    _ctypes.c_int,
                                    _ctypes.c_int ]

GetGroupNames = _hapi.HAPI_GetGroupNames
GetGroupNames.restype = Result
GetGroupNames.argtypes = [ _ctypes.POINTER(Session),
                           NodeId,
                           GroupType,
                           _ctypes.POINTER(StringHandle),
                           _ctypes.c_int ]

GetGroupMembership = _hapi.HAPI_GetGroupMembership
GetGroupMembership.restype = Result
GetGroupMembership.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                PartId,
                                GroupType,
                                _ctypes.c_char_p,
                                _ctypes.POINTER(Bool),
                                _ctypes.POINTER(_ctypes.c_int),
                                _ctypes.c_int,
                                _ctypes.c_int ]

GetGroupCountOnPackedInstancePart = _hapi.HAPI_GetGroupCountOnPackedInstancePart
GetGroupCountOnPackedInstancePart.restype = Result
GetGroupCountOnPackedInstancePart.argtypes = [ _ctypes.POINTER(Session),
                                               NodeId,
                                               PartId,
                                               _ctypes.POINTER(_ctypes.c_int),
                                               _ctypes.POINTER(_ctypes.c_int) ]

GetGroupNamesOnPackedInstancePart = _hapi.HAPI_GetGroupNamesOnPackedInstancePart
GetGroupNamesOnPackedInstancePart.restype = Result
GetGroupNamesOnPackedInstancePart.argtypes = [ _ctypes.POINTER(Session),
                                               NodeId,
                                               PartId,
                                               GroupType,
                                               _ctypes.POINTER(StringHandle),
                                               _ctypes.c_int ]

GetGroupMembershipOnPackedInstancePart = _hapi.HAPI_GetGroupMembershipOnPackedInstancePart
GetGroupMembershipOnPackedInstancePart.restype = Result
GetGroupMembershipOnPackedInstancePart.argtypes = [ _ctypes.POINTER(Session),
                                                    NodeId,
                                                    PartId,
                                                    GroupType,
                                                    _ctypes.c_char_p,
                                                    _ctypes.POINTER(Bool),
                                                    _ctypes.POINTER(_ctypes.c_int),
                                                    _ctypes.c_int,
                                                    _ctypes.c_int ]

GetInstancedPartIds = _hapi.HAPI_GetInstancedPartIds
GetInstancedPartIds.restype = Result
GetInstancedPartIds.argtypes = [ _ctypes.POINTER(Session),
                                 NodeId,
                                 PartId,
                                 _ctypes.POINTER(PartId),
                                 _ctypes.c_int,
                                 _ctypes.c_int ]

GetInstancerPartTransforms = _hapi.HAPI_GetInstancerPartTransforms
GetInstancerPartTransforms.restype = Result
GetInstancerPartTransforms.argtypes = [ _ctypes.POINTER(Session),
                                        NodeId,
                                        PartId,
                                        RSTOrder,
                                        _ctypes.POINTER(Transform),
                                        _ctypes.c_int,
                                        _ctypes.c_int ]


SetPartInfo = _hapi.HAPI_SetPartInfo
SetPartInfo.restype = Result
SetPartInfo.argtypes = [ _ctypes.POINTER(Session),
                         NodeId,
                         PartId,
                         _ctypes.POINTER(PartInfo) ]

SetFaceCounts = _hapi.HAPI_SetFaceCounts
SetFaceCounts.restype = Result
SetFaceCounts.argtypes = [ _ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           _ctypes.POINTER(_ctypes.c_int),
                           _ctypes.c_int,
                           _ctypes.c_int ]

SetVertexList = _hapi.HAPI_SetVertexList
SetVertexList.restype = Result
SetVertexList.argtypes = [ _ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           _ctypes.POINTER(_ctypes.c_int),
                           _ctypes.c_int,
                           _ctypes.c_int ]

AddAttribute = _hapi.HAPI_AddAttribute
AddAttribute.restype = Result
AddAttribute.argtypes = [ _ctypes.POINTER(Session),
                          NodeId,
                          PartId,
                          _ctypes.c_char_p,
                          _ctypes.POINTER(AttributeInfo)]

DeleteAttribute = _hapi.HAPI_DeleteAttribute
DeleteAttribute.restype = Result
DeleteAttribute.argtypes = [ _ctypes.POINTER(Session),
                             NodeId,
                             PartId,
                             _ctypes.c_char_p,
                             _ctypes.POINTER(AttributeInfo)]

SetAttributeIntData = _hapi.HAPI_SetAttributeIntData
SetAttributeIntData.restype = Result
SetAttributeIntData.argtypes = [ _ctypes.POINTER(Session),
                                 NodeId,
                                 PartId,
                                 _ctypes.c_char_p,
                                 _ctypes.POINTER(AttributeInfo),
                                 _ctypes.POINTER(_ctypes.c_int),
                                 _ctypes.c_int,
                                 _ctypes.c_int ]

SetAttributeInt64Data = _hapi.HAPI_SetAttributeInt64Data
SetAttributeInt64Data.restype = Result
SetAttributeInt64Data.argtypes = [ _ctypes.POINTER(Session),
                                   NodeId,
                                   PartId,
                                   _ctypes.c_char_p,
                                   _ctypes.POINTER(AttributeInfo),
                                   _ctypes.POINTER(Int64),
                                   _ctypes.c_int,
                                   _ctypes.c_int ]

SetAttributeFloatData = _hapi.HAPI_SetAttributeFloatData
SetAttributeFloatData.restype = Result
SetAttributeFloatData.argtypes = [ _ctypes.POINTER(Session),
                                   NodeId,
                                   PartId,
                                   _ctypes.c_char_p,
                                   _ctypes.POINTER(AttributeInfo),
                                   _ctypes.POINTER(_ctypes.c_float),
                                   _ctypes.c_int,
                                   _ctypes.c_int ]

SetAttributeFloat64Data = _hapi.HAPI_SetAttributeFloat64Data
SetAttributeFloat64Data.restype = Result
SetAttributeFloat64Data.argtypes = [ _ctypes.POINTER(Session),
                                     NodeId,
                                     PartId,
                                     _ctypes.c_char_p,
                                     _ctypes.POINTER(AttributeInfo),
                                     _ctypes.POINTER(_ctypes.c_double),
                                     _ctypes.c_int,
                                     _ctypes.c_int ]

SetAttributeStringData = _hapi.HAPI_SetAttributeStringData
SetAttributeStringData.restype = Result
SetAttributeStringData.argtypes = [ _ctypes.POINTER(Session),
                                    NodeId,
                                    PartId,
                                    _ctypes.c_char_p,
                                    _ctypes.POINTER(AttributeInfo),
                                    _ctypes.POINTER(_ctypes.c_char_p),
                                    _ctypes.c_int,
                                    _ctypes.c_int ]

AddGroup = _hapi.HAPI_AddGroup
AddGroup.restype = Result
AddGroup.argtypes = [ _ctypes.POINTER(Session),
                      NodeId,
                      PartId,
                      GroupType,
                      _ctypes.c_char_p ]

DeleteGroup = _hapi.HAPI_DeleteGroup
DeleteGroup.restype = Result
DeleteGroup.argtypes = [ _ctypes.POINTER(Session),
                         NodeId,
                         PartId,
                         GroupType,
                         _ctypes.c_char_p ]

SetGroupMembership = _hapi.HAPI_SetGroupMembership
SetGroupMembership.restype = Result
SetGroupMembership.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                PartId,
                                GroupType,
                                _ctypes.c_char_p,
                                _ctypes.POINTER(_ctypes.c_int),
                                _ctypes.c_int,
                                _ctypes.c_int ]

CommitGeo = _hapi.HAPI_CommitGeo
CommitGeo.restype = Result
CommitGeo.argtypes = [ _ctypes.POINTER(Session),
                       NodeId ]

RevertGeo = _hapi.HAPI_RevertGeo
RevertGeo.restype = Result
RevertGeo.argtypes = [ _ctypes.POINTER(Session),
                       NodeId ]

GetMaterialNodeIdsOnFaces = _hapi.HAPI_GetMaterialNodeIdsOnFaces
GetMaterialNodeIdsOnFaces.restype = Result
GetMaterialNodeIdsOnFaces.argtypes = [ _ctypes.POINTER(Session),
                                       NodeId,
                                       PartId,
                                       _ctypes.POINTER(Bool),
                                       _ctypes.POINTER(NodeId),
                                       _ctypes.c_int,
                                       _ctypes.c_int ]

GetMaterialInfo = _hapi.HAPI_GetMaterialInfo
GetMaterialInfo.restype = Result
GetMaterialInfo.argtypes = [ _ctypes.POINTER(Session),
                             NodeId,
                             _ctypes.POINTER(MaterialInfo) ]

RenderCOPToImage = _hapi.HAPI_RenderCOPToImage
RenderCOPToImage.restype = Result
RenderCOPToImage.argtypes = [ _ctypes.POINTER(Session),
                              NodeId ]

RenderTextureToImage = _hapi.HAPI_RenderTextureToImage
RenderTextureToImage.restype = Result
RenderTextureToImage.argtypes = [ _ctypes.POINTER(Session),
                                  NodeId,
                                  ParmId ]

GetImageInfo = _hapi.HAPI_GetImageInfo
GetImageInfo.restype = Result
GetImageInfo.argtypes = [ _ctypes.POINTER(Session),
                          NodeId,
                          _ctypes.POINTER(ImageInfo) ]

SetImageInfo = _hapi.HAPI_SetImageInfo
SetImageInfo.restype = Result
SetImageInfo.argtypes = [ _ctypes.POINTER(Session),
                          NodeId,
                          _ctypes.POINTER(ImageInfo) ]

GetImagePlaneCount = _hapi.HAPI_GetImagePlaneCount
GetImagePlaneCount.restype = Result
GetImagePlaneCount.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                _ctypes.POINTER(_ctypes.c_int) ]

GetImagePlanes = _hapi.HAPI_GetImagePlanes
GetImagePlanes.restype = Result
GetImagePlanes.argtypes = [ _ctypes.POINTER(Session),
                            NodeId,
                            _ctypes.POINTER(StringHandle),
                            _ctypes.c_int ]

ExtractImageToFile = _hapi.HAPI_ExtractImageToFile
ExtractImageToFile.restype = Result
ExtractImageToFile.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                _ctypes.c_char_p,
                                _ctypes.c_char_p,
                                _ctypes.c_char_p,
                                _ctypes.c_char_p,
                                _ctypes.POINTER(_ctypes.c_int) ]

ExtractImageToMemory = _hapi.HAPI_ExtractImageToMemory
ExtractImageToMemory.restype = Result
ExtractImageToMemory.argtypes = [ _ctypes.POINTER(Session),
                                  NodeId,
                                  _ctypes.c_char_p,
                                  _ctypes.c_char_p,
                                  _ctypes.POINTER(_ctypes.c_int) ]

GetImageMemoryBuffer = _hapi.HAPI_GetImageMemoryBuffer
GetImageMemoryBuffer.restype = Result
GetImageMemoryBuffer.argtypes = [ _ctypes.POINTER(Session),
                                  NodeId,
                                  _ctypes.c_char_p,
                                  _ctypes.c_int ]

GetSupportedImageFileFormatCount = _hapi.HAPI_GetSupportedImageFileFormatCount
GetSupportedImageFileFormatCount.restype = Result
GetSupportedImageFileFormatCount.argtypes = [ _ctypes.POINTER(Session),
                                              _ctypes.POINTER(_ctypes.c_int) ]

GetSupportedImageFileFormats = _hapi.HAPI_GetSupportedImageFileFormats
GetSupportedImageFileFormats.restype = Result
GetSupportedImageFileFormats.argtypes = [ _ctypes.POINTER(Session),
                                          _ctypes.POINTER(ImageFileFormat),
                                          _ctypes.c_int ]

SetAnimCurve = _hapi.HAPI_SetAnimCurve
SetAnimCurve.restype = Result
SetAnimCurve.argtypes = [ _ctypes.POINTER(Session),
                          NodeId,
                          ParmId,
                          _ctypes.c_int,
                          _ctypes.POINTER(Keyframe),
                          _ctypes.c_int ]

SetTransformAnimCurve = _hapi.HAPI_SetTransformAnimCurve
SetTransformAnimCurve.restype = Result
SetTransformAnimCurve.argtypes = [ _ctypes.POINTER(Session),
                                   NodeId,
                                   TransformComponent,
                                   _ctypes.POINTER(Keyframe),
                                   _ctypes.c_int ]

ResetSimulation = _hapi.HAPI_ResetSimulation
ResetSimulation.restype = Result
ResetSimulation.argtypes = [ _ctypes.POINTER(Session),
                             NodeId ]

GetVolumeInfo = _hapi.HAPI_GetVolumeInfo
GetVolumeInfo.restype = Result
GetVolumeInfo.argtypes = [ _ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           _ctypes.POINTER(VolumeInfo) ]

GetFirstVolumeTile = _hapi.HAPI_GetFirstVolumeTile
GetFirstVolumeTile.restype = Result
GetFirstVolumeTile.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                PartId,
                                _ctypes.POINTER(VolumeTileInfo) ]

GetNextVolumeTile = _hapi.HAPI_GetNextVolumeTile
GetNextVolumeTile.restype = Result
GetNextVolumeTile.argtypes = [ _ctypes.POINTER(Session),
                               NodeId,
                               PartId,
                               _ctypes.POINTER(VolumeTileInfo) ]

GetVolumeVoxelFloatData = _hapi.HAPI_GetVolumeVoxelFloatData
GetVolumeVoxelFloatData.restype = Result
GetVolumeVoxelFloatData.argtypes = [ _ctypes.POINTER(Session),
                                     NodeId,
                                     PartId,
                                     _ctypes.c_int,
                                     _ctypes.c_int,
                                     _ctypes.c_int,
                                     _ctypes.POINTER(_ctypes.c_float),
                                     _ctypes.c_int ]

GetVolumeTileFloatData = _hapi.HAPI_GetVolumeTileFloatData
GetVolumeTileFloatData.restype = Result
GetVolumeTileFloatData.argtypes = [ _ctypes.POINTER(Session),
                                    NodeId,
                                    PartId,
                                    _ctypes.c_float,
                                    _ctypes.POINTER(VolumeTileInfo),
                                    _ctypes.POINTER(_ctypes.c_float),
                                    _ctypes.c_int ]

GetVolumeVoxelIntData = _hapi.HAPI_GetVolumeVoxelIntData
GetVolumeVoxelIntData.restype = Result
GetVolumeVoxelIntData.argtypes = [ _ctypes.POINTER(Session),
                                   NodeId,
                                   PartId,
                                   _ctypes.c_int,
                                   _ctypes.c_int,
                                   _ctypes.c_int,
                                   _ctypes.POINTER(_ctypes.c_int),
                                   _ctypes.c_int ]

GetVolumeTileIntData = _hapi.HAPI_GetVolumeTileIntData
GetVolumeTileIntData.restype = Result
GetVolumeTileIntData.argtypes = [ _ctypes.POINTER(Session),
                                  NodeId,
                                  PartId,
                                  _ctypes.c_int,
                                  _ctypes.POINTER(VolumeTileInfo),
                                  _ctypes.POINTER(_ctypes.c_int),
                                  _ctypes.c_int ]

GetHeightFieldData = _hapi.HAPI_GetHeightFieldData
GetHeightFieldData.restype = Result
GetHeightFieldData.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                PartId,
                                _ctypes.POINTER(_ctypes.c_float),
                                _ctypes.c_int,
                                _ctypes.c_int]

SetVolumeInfo = _hapi.HAPI_SetVolumeInfo
SetVolumeInfo.restype = Result
SetVolumeInfo.argtypes = [ _ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           _ctypes.POINTER(VolumeInfo) ]

SetVolumeTileFloatData = _hapi.HAPI_SetVolumeTileFloatData
SetVolumeTileFloatData.restype = Result
SetVolumeTileFloatData.argtypes = [ _ctypes.POINTER(Session),
                                    NodeId,
                                    PartId,
                                    _ctypes.POINTER(VolumeTileInfo),
                                    _ctypes.POINTER(_ctypes.c_float),
                                    _ctypes.c_int ]

SetVolumeTileIntData = _hapi.HAPI_SetVolumeTileIntData
SetVolumeTileIntData.restype = Result
SetVolumeTileIntData.argtypes = [ _ctypes.POINTER(Session),
                                  NodeId,
                                  PartId,
                                  _ctypes.POINTER(VolumeTileInfo),
                                  _ctypes.POINTER(_ctypes.c_int),
                                  _ctypes.c_int ]

SetVolumeVoxelFloatData = _hapi.HAPI_SetVolumeVoxelFloatData
SetVolumeVoxelFloatData.restype = Result
SetVolumeVoxelFloatData.argtypes = [ _ctypes.POINTER(Session),
                                     NodeId,
                                     PartId,
                                     _ctypes.c_int,
                                     _ctypes.c_int,
                                     _ctypes.c_int,
                                     _ctypes.POINTER(_ctypes.c_float),
                                     _ctypes.c_int ]

SetVolumeVoxelIntData = _hapi.HAPI_SetVolumeVoxelIntData
SetVolumeVoxelIntData.restype = Result
SetVolumeVoxelIntData.argtypes = [ _ctypes.POINTER(Session),
                                   NodeId,
                                   PartId,
                                   _ctypes.c_int,
                                   _ctypes.c_int,
                                   _ctypes.c_int,
                                   _ctypes.POINTER(_ctypes.c_int),
                                   _ctypes.c_int ]

GetVolumeBounds = _hapi.HAPI_GetVolumeBounds
GetVolumeBounds.restype = Result
GetVolumeBounds.argtypes = [ _ctypes.POINTER(Session),
                             NodeId,
                             PartId,
                             _ctypes.POINTER(_ctypes.c_float),
                             _ctypes.POINTER(_ctypes.c_float),
                             _ctypes.POINTER(_ctypes.c_float),
                             _ctypes.POINTER(_ctypes.c_float),
                             _ctypes.POINTER(_ctypes.c_float),
                             _ctypes.POINTER(_ctypes.c_float),
                             _ctypes.POINTER(_ctypes.c_float),
                             _ctypes.POINTER(_ctypes.c_float),
                             _ctypes.POINTER(_ctypes.c_float) ]

SetHeightFieldData = _hapi.HAPI_SetHeightFieldData
SetHeightFieldData.restype = Result
SetHeightFieldData.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                PartId,
                                _ctypes.POINTER(_ctypes.c_float),
                                _ctypes.c_int,
                                _ctypes.c_int,
                                _ctypes.c_char_p ]

GetCurveInfo = _hapi.HAPI_GetCurveInfo
GetCurveInfo.restype = Result
GetCurveInfo.argtypes = [ _ctypes.POINTER(Session),
                          NodeId,
                          PartId,
                          _ctypes.POINTER(CurveInfo) ]

GetCurveCounts = _hapi.HAPI_GetCurveCounts
GetCurveCounts.restype = Result
GetCurveCounts.argtypes = [ _ctypes.POINTER(Session),
                            NodeId,
                            PartId,
                            _ctypes.POINTER(_ctypes.c_int),
                            _ctypes.c_int,
                            _ctypes.c_int ]

GetCurveOrders = _hapi.HAPI_GetCurveOrders
GetCurveOrders.restype = Result
GetCurveOrders.argtypes = [ _ctypes.POINTER(Session),
                            NodeId,
                            PartId,
                            _ctypes.POINTER(_ctypes.c_int),
                            _ctypes.c_int,
                            _ctypes.c_int ]

GetCurveKnots = _hapi.HAPI_GetCurveKnots
GetCurveKnots.restype = Result
GetCurveKnots.argtypes = [ _ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           _ctypes.POINTER(_ctypes.c_float),
                           _ctypes.c_int,
                           _ctypes.c_int ]

SetCurveInfo = _hapi.HAPI_SetCurveInfo
SetCurveInfo.restype = Result
SetCurveInfo.argtypes = [ _ctypes.POINTER(Session),
                          NodeId,
                          PartId,
                          _ctypes.POINTER(CurveInfo) ]

SetCurveCounts = _hapi.HAPI_SetCurveCounts
SetCurveCounts.restype = Result
SetCurveCounts.argtypes = [ _ctypes.POINTER(Session),
                            NodeId,
                            PartId,
                            _ctypes.POINTER(_ctypes.c_int),
                            _ctypes.c_int,
                            _ctypes.c_int ]

SetCurveOrders = _hapi.HAPI_SetCurveOrders
SetCurveOrders.restype = Result
SetCurveOrders.argtypes = [ _ctypes.POINTER(Session),
                            NodeId,
                            PartId,
                            _ctypes.POINTER(_ctypes.c_int),
                            _ctypes.c_int,
                            _ctypes.c_int ]

SetCurveKnots = _hapi.HAPI_SetCurveKnots
SetCurveKnots.restype = Result
SetCurveKnots.argtypes = [ _ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           _ctypes.POINTER(_ctypes.c_float),
                           _ctypes.c_int,
                           _ctypes.c_int ]

GetBoxInfo = _hapi.HAPI_GetBoxInfo
GetBoxInfo.restype = Result
GetBoxInfo.argtypes = [ _ctypes.POINTER(Session),
                        NodeId,
                        PartId,
                        _ctypes.POINTER(BoxInfo) ]

GetSphereInfo = _hapi.HAPI_GetSphereInfo
GetSphereInfo.restype = Result
GetSphereInfo.argtypes = [ _ctypes.POINTER(Session),
                           NodeId,
                           PartId,
                           _ctypes.POINTER(SphereInfo) ]


GetActiveCacheCount = _hapi.HAPI_GetActiveCacheCount
GetActiveCacheCount.restype = Result
GetActiveCacheCount.argtypes = [ _ctypes.POINTER(Session),
                                 _ctypes.POINTER(_ctypes.c_int) ]

GetActiveCacheNames = _hapi.HAPI_GetActiveCacheNames
GetActiveCacheNames.restype = Result
GetActiveCacheNames.argtypes = [ _ctypes.POINTER(Session),
                                 _ctypes.POINTER(StringHandle),
                                 _ctypes.c_int ]

GetCacheProperty = _hapi.HAPI_GetCacheProperty
GetCacheProperty.restype = Result
GetCacheProperty.argtypes = [ _ctypes.POINTER(Session),
                              _ctypes.c_char_p,
                              CacheProperty,
                              _ctypes.POINTER(_ctypes.c_int) ]

SetCacheProperty = _hapi.HAPI_SetCacheProperty
SetCacheProperty.restype = Result
SetCacheProperty.argtypes = [ _ctypes.POINTER(Session),
                              _ctypes.c_char_p,
                              CacheProperty,
                              _ctypes.c_int ]

SaveGeoToFile = _hapi.HAPI_SaveGeoToFile
SaveGeoToFile.restype = Result
SaveGeoToFile.argtypes = [ _ctypes.POINTER(Session),
                           NodeId,
                           _ctypes.c_char_p ]

LoadGeoFromFile = _hapi.HAPI_LoadGeoFromFile
LoadGeoFromFile.restype = Result
LoadGeoFromFile.argtypes = [ _ctypes.POINTER(Session),
                             NodeId,
                             _ctypes.c_char_p ]

GetGeoSize = _hapi.HAPI_GetGeoSize
GetGeoSize.restype = Result
GetGeoSize.argtypes = [ _ctypes.POINTER(Session),
                        NodeId,
                        _ctypes.c_char_p,
                        _ctypes.POINTER(_ctypes.c_int) ]

SaveGeoToMemory = _hapi.HAPI_SaveGeoToMemory
SaveGeoToMemory.restype = Result
SaveGeoToMemory.argtypes = [ _ctypes.POINTER(Session),
                             NodeId,
                             _ctypes.c_char_p,
                             _ctypes.c_int ]

LoadGeoFromMemory = _hapi.HAPI_LoadGeoFromMemory
LoadGeoFromMemory.restype = Result
LoadGeoFromMemory.argtypes = [ _ctypes.POINTER(Session),
                               NodeId,
                               _ctypes.c_char_p,
                               _ctypes.c_char_p,
                               _ctypes.c_int ]

GetPDGGraphContexts = _hapi.HAPI_GetPDGGraphContexts
GetPDGGraphContexts.restype = Result
GetPDGGraphContexts.argtypes = [ _ctypes.POINTER(Session),
                                 _ctypes.POINTER(_ctypes.c_int),
                                 _ctypes.POINTER(StringHandle),
                                 _ctypes.POINTER(PDG_GraphContextId),
                                 _ctypes.c_int ]

CookPDG = _hapi.HAPI_CookPDG
CookPDG.restype = Result
CookPDG.argtypes = [ _ctypes.POINTER(Session),
                     NodeId,
                     _ctypes.c_int,
                     _ctypes.c_int ]

GetPDGEvents = _hapi.HAPI_GetPDGEvents
GetPDGEvents.restype = Result
GetPDGEvents.argtypes = [ _ctypes.POINTER(Session),
                          _ctypes.POINTER(PDG_GraphContextId),
                          _ctypes.POINTER(PDG_EventInfo),
                          _ctypes.c_int,
                          _ctypes.POINTER(_ctypes.c_int),
                          _ctypes.POINTER(_ctypes.c_int) ]

GetPDGState = _hapi.HAPI_GetPDGState
GetPDGState.restype = Result
GetPDGState.argtypes = [ _ctypes.POINTER(Session),
                         PDG_GraphContextId,
                         _ctypes.POINTER(_ctypes.c_int) ]

CreateWorkitem = _hapi.HAPI_CreateWorkitem
CreateWorkitem.restype = Result
CreateWorkitem.argtypes = [ _ctypes.POINTER(Session),
                            NodeId,
                            _ctypes.POINTER(PDG_WorkitemId),
                            _ctypes.c_char_p,
                            _ctypes.c_int ]

GetWorkitemInfo = _hapi.HAPI_GetWorkitemInfo
GetWorkitemInfo.restype = Result
GetWorkitemInfo.argtypes = [ _ctypes.POINTER(Session),
                             PDG_GraphContextId,
                             PDG_WorkitemId,
                             _ctypes.POINTER(PDG_EventInfo) ]

SetWorkitemIntData = _hapi.HAPI_SetWorkitemIntData
SetWorkitemIntData.restype = Result
SetWorkitemIntData.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                PDG_WorkitemId,
                                _ctypes.c_char_p,
                                _ctypes.POINTER(_ctypes.c_int),
                                _ctypes.c_int ]

SetWorkitemFloatData = _hapi.HAPI_SetWorkitemFloatData
SetWorkitemFloatData.restype = Result
SetWorkitemFloatData.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                PDG_WorkitemId,
                                _ctypes.c_char_p,
                                _ctypes.POINTER(_ctypes.c_float),
                                _ctypes.c_int ]

SetWorkitemStringData = _hapi.HAPI_SetWorkitemStringData
SetWorkitemStringData.restype = Result
SetWorkitemStringData.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                PDG_WorkitemId,
                                _ctypes.c_char_p,
                                _ctypes.c_int,
                                _ctypes.c_char_p ]

GetNumWorkitems = _hapi.HAPI_GetNumWorkitems
GetNumWorkitems.restype = Result
GetNumWorkitems.argtypes = [ _ctypes.POINTER(Session),
                             NodeId,
                             _ctypes.POINTER(_ctypes.c_int) ]

GetWorkitems = _hapi.HAPI_GetWorkitems
GetWorkitems.restype = Result
GetWorkitems.argtypes = [ _ctypes.POINTER(Session),
                          NodeId,
                          _ctypes.POINTER(_ctypes.c_int),
                          _ctypes.c_int ]

GetWorkitemDataLength = _hapi.HAPI_GetWorkitemDataLength
GetWorkitemDataLength.restype = Result
GetWorkitemDataLength.argtypes = [ _ctypes.POINTER(Session),
                                   NodeId,
                                   PDG_WorkitemId,
                                   _ctypes.c_char_p,
                                   _ctypes.POINTER(_ctypes.c_int) ]

GetWorkitemIntData = _hapi.HAPI_GetWorkitemIntData
GetWorkitemIntData.restype = Result
GetWorkitemIntData.argtypes = [ _ctypes.POINTER(Session),
                                NodeId,
                                PDG_WorkitemId,
                                _ctypes.c_char_p,
                                _ctypes.POINTER(_ctypes.c_int),
                                _ctypes.c_int ]

GetWorkitemFloatData = _hapi.HAPI_GetWorkitemFloatData
GetWorkitemFloatData.restype = Result
GetWorkitemFloatData.argtypes = [ _ctypes.POINTER(Session),
                                  NodeId,
                                  PDG_WorkitemId,
                                  _ctypes.c_char_p,
                                  _ctypes.POINTER(_ctypes.c_float),
                                  _ctypes.c_int ]

GetWorkitemStringData = _hapi.HAPI_GetWorkitemStringData
GetWorkitemStringData.restype = Result
GetWorkitemStringData.argtypes = [ _ctypes.POINTER(Session),
                                   NodeId,
                                   PDG_WorkitemId,
                                   _ctypes.c_char_p,
                                   _ctypes.POINTER(StringHandle),
                                   _ctypes.c_int ]

GetWorkitemResultInfo = _hapi.HAPI_GetWorkitemResultInfo
GetWorkitemResultInfo.restype = Result
GetWorkitemResultInfo.argtypes = [ _ctypes.POINTER(Session),
                                   NodeId,
                                   PDG_WorkitemId,
                                   _ctypes.POINTER(PDG_WorkitemResultInfo),
                                   _ctypes.c_int ]

DirtyPDGNode = _hapi.HAPI_DirtyPDGNode
DirtyPDGNode.restype = Result
DirtyPDGNode.argtypes = [ _ctypes.POINTER(Session),
                          NodeId,
                          _ctypes.c_int ]

PausePDGCook = _hapi.HAPI_PausePDGCook
PausePDGCook.restype = Result
PausePDGCook.argtypes = [ _ctypes.POINTER(Session),
                          PDG_GraphContextId ]

CancelPDGCook = _hapi.HAPI_CancelPDGCook
CancelPDGCook.restype = Result
CancelPDGCook.argtypes = [ _ctypes.POINTER(Session),
                          PDG_GraphContextId ]
