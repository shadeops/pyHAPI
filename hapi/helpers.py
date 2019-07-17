from __future__ import absolute_import

import ctypes

_hapi = ctypes.cdll.LoadLibrary('/opt/hfs/dsolib/libHAPIL.so')

from .common import *

# TIME ---------------------------------------------------------------------

TimelineOptions_Init = _hapi.HAPI_TimelineOptions_Init
TimelineOptions_Init.restype = None
TimelineOptions_Init.argtypes = [ctypes.POINTER(TimelineOptions)]

TimelineOptions_Create = _hapi.HAPI_TimelineOptions_Create
TimelineOptions_Create.restype = TimelineOptions
TimelineOptions_Create.argtypes = []


# # ASSETS -------------------------------------------------------------------
#
AssetInfo_Init = _hapi.HAPI_AssetInfo_Init
AssetInfo_Init.restype = None
AssetInfo_Init.argtypes = [ ctypes.POINTER(AssetInfo) ]

AssetInfo_Create = _hapi.HAPI_AssetInfo_Create
AssetInfo_Create.restype = AssetInfo
AssetInfo_Create.argtypes = []

CookOptions_Init = _hapi.HAPI_CookOptions_Init
CookOptions_Init.restype = None
CookOptions_Init.argtypes = [ctypes.POINTER(CookOptions)]

CookOptions_Create = _hapi.HAPI_CookOptions_Create
CookOptions_Create.restype = CookOptions
CookOptions_Create.argtypes = []

CookOptions_AreEqual = _hapi.HAPI_CookOptions_AreEqual
CookOptions_AreEqual.restype = Bool
CookOptions_AreEqual.argtypes = [ ctypes.POINTER(CookOptions),
                                  ctypes.POINTER(CookOptions) ]
# 
# # NODES --------------------------------------------------------------------
#
NodeInfo_Init = _hapi.HAPI_NodeInfo_Init
NodeInfo_Init.restype = None
NodeInfo_Init.argtypes = [ ctypes.POINTER(NodeInfo) ]

NodeInfo_Create = _hapi.HAPI_NodeInfo_Create
NodeInfo_Create.restype = NodeInfo
NodeInfo_Create.argtypes = []
# 
# # PARAMETERS ---------------------------------------------------------------
#
ParmInfo_Init = _hapi.HAPI_ParmInfo_Init
ParmInfo_Init.restype = None
ParmInfo_Init.argtypes = [ ctypes.POINTER(ParmInfo) ]

ParmInfo_Create = _hapi.HAPI_ParmInfo_Create
ParmInfo_Create.restype = ParmInfo
ParmInfo_Create.argtypes = []
#
# #/ Convenience function that checks on the value of the ::HAPI_ParmInfo::type
# #/ field to tell you the underlying data type.
# #/ @{
ParmInfo_Init = _hapi.HAPI_ParmInfo_Init
ParmInfo_Init.restype = None
ParmInfo_Init.argtypes = [ ctypes.POINTER(ParmInfo) ]

ParmInfo_IsFloat = _hapi.HAPI_ParmInfo_IsFloat
ParmInfo_IsFloat.restype = Bool
ParmInfo_IsFloat.argtypes = [ ctypes.POINTER(ParmInfo) ]

ParmInfo_IsString = _hapi.HAPI_ParmInfo_IsString
ParmInfo_IsString.restype = Bool
ParmInfo_IsString.argtypes = [ ctypes.POINTER(ParmInfo) ]

ParmInfo_IsPath = _hapi.HAPI_ParmInfo_IsPath
ParmInfo_IsPath.restype = Bool
ParmInfo_IsPath.argtypes = [ ctypes.POINTER(ParmInfo) ]

ParmInfo_IsNode = _hapi.HAPI_ParmInfo_IsNode
ParmInfo_IsNode.restype = Bool
ParmInfo_IsNode.argtypes = [ ctypes.POINTER(ParmInfo) ]
# #/ @}
# 
ParmInfo_IsNonValue = _hapi.HAPI_ParmInfo_IsNonValue
ParmInfo_IsNonValue.restype = Bool
ParmInfo_IsNonValue.argtypes = [ ctypes.POINTER(ParmInfo) ]
# 
# #/ Convenience function. If the parameter can be represented by this data
# #/ type, it returns ::HAPI_ParmInfo::size, and zero otherwise.
# #/ @{
ParmInfo_GetIntValueCount = _hapi.HAPI_ParmInfo_GetIntValueCount
ParmInfo_GetIntValueCount.restype = ctypes.c_int
ParmInfo_GetIntValueCount.argtypes = [ ctypes.POINTER(ParmInfo) ]

ParmInfo_GetFloatValueCount = _hapi.HAPI_ParmInfo_GetFloatValueCount
ParmInfo_GetFloatValueCount.restype = ctypes.c_int
ParmInfo_GetFloatValueCount.argtypes = [ ctypes.POINTER(ParmInfo) ]

ParmInfo_GetStringValueCount = _hapi.HAPI_ParmInfo_GetStringValueCount
ParmInfo_GetStringValueCount.restype = ctypes.c_int
ParmInfo_GetStringValueCount.argtypes = [ ctypes.POINTER(ParmInfo) ]
# #/ @}
# 
ParmChoiceInfo_Init = _hapi.HAPI_ParmChoiceInfo_Init
ParmChoiceInfo_Init.restype = None
ParmChoiceInfo_Init.argtypes = [ ctypes.POINTER(ParmChoiceInfo) ]

ParmChoiceInfo_Create = _hapi.HAPI_ParmChoiceInfo_Create
ParmChoiceInfo_Create.restype = ParmChoiceInfo
ParmChoiceInfo_Create.argtypes = []
# 
# # HANDLES ------------------------------------------------------------------
# 
HandleInfo_Init = _hapi.HAPI_HandleInfo_Init
HandleInfo_Init.restype = None
HandleInfo_Init.argtypes = [ ctypes.POINTER(HandleInfo) ]

HandleInfo_Create = _hapi.HAPI_HandleInfo_Create
HandleInfo_Create.restype = HandleInfo
HandleInfo_Create.argtypes = []
# 
HandleBindingInfo_Init = _hapi.HAPI_HandleBindingInfo_Init
HandleBindingInfo_Init.restype = None
HandleBindingInfo_Init.argtypes = [ ctypes.POINTER(HandleBindingInfo) ]

HandleBindingInfo_Create = _hapi.HAPI_HandleBindingInfo_Create
HandleBindingInfo_Create.restype = HandleBindingInfo
HandleBindingInfo_Create.argtypes = []
# 
# # OBJECTS ------------------------------------------------------------------
# 
ObjectInfo_Init = _hapi.HAPI_ObjectInfo_Init
ObjectInfo_Init.restype = None
ObjectInfo_Init.argtypes = [ ctypes.POINTER(ObjectInfo) ]

ObjectInfo_Create = _hapi.HAPI_ObjectInfo_Create
ObjectInfo_Create.restype = ObjectInfo
ObjectInfo_Create.argtypes = []
# 
# # GEOMETRY -----------------------------------------------------------------
# 
GeoInfo_Init = _hapi.HAPI_GeoInfo_Init
GeoInfo_Init.restype = None
GeoInfo_Init.argtypes = [ ctypes.POINTER(GeoInfo) ]

GeoInfo_Create = _hapi.HAPI_GeoInfo_Create
GeoInfo_Create.restype = GeoInfo
GeoInfo_Create.argtypes = []

GeoInfo_GetGroupCountByType = _hapi.HAPI_GeoInfo_GetGroupCountByType
GeoInfo_GetGroupCountByType.restype = ctypes.c_int
GeoInfo_GetGroupCountByType.argtypes = [ ctypes.POINTER(GeoInfo),
                                         GroupType ]
#
PartInfo_Init = _hapi.HAPI_PartInfo_Init
PartInfo_Init.restype = None
PartInfo_Init.argtypes = [ ctypes.POINTER(PartInfo) ]

PartInfo_Create = _hapi.HAPI_PartInfo_Create
PartInfo_Create.restype = PartInfo
PartInfo_Create.argtypes = []

PartInfo_GetElementCountByAttributeOwner = _hapi.HAPI_PartInfo_GetElementCountByAttributeOwner
PartInfo_GetElementCountByAttributeOwner.restype = ctypes.c_int
PartInfo_GetElementCountByAttributeOwner.argtypes = [ ctypes.POINTER(PartInfo),
                                                      AttributeOwner ]

PartInfo_GetElementCountByGroupType = _hapi.HAPI_PartInfo_GetElementCountByGroupType
PartInfo_GetElementCountByGroupType.restype = ctypes.c_int
PartInfo_GetElementCountByGroupType.argtypes = [ ctypes.POINTER(PartInfo),
                                                 GroupType ]

PartInfo_GetAttributeCountByOwner = _hapi.HAPI_PartInfo_GetAttributeCountByOwner
PartInfo_GetAttributeCountByOwner.restype = ctypes.c_int
PartInfo_GetAttributeCountByOwner.argtypes = [ ctypes.POINTER(PartInfo),
                                               AttributeOwner ]
#
AttributeInfo_Init = _hapi.HAPI_AttributeInfo_Init
AttributeInfo_Init.restype = None
AttributeInfo_Init.argtypes = [ ctypes.POINTER(AttributeInfo) ]

AttributeInfo_Create = _hapi.HAPI_AttributeInfo_Create
AttributeInfo_Create.restype = AttributeInfo
AttributeInfo_Create.argtypes = []
# 
# # MATERIALS ----------------------------------------------------------------
# 
MaterialInfo_Init = _hapi.HAPI_MaterialInfo_Init
MaterialInfo_Init.restype = None
MaterialInfo_Init.argtypes = [ ctypes.POINTER(MaterialInfo) ]

MaterialInfo_Create = _hapi.HAPI_MaterialInfo_Create
MaterialInfo_Create.restype = MaterialInfo
MaterialInfo_Create.argtypes = []
# 
ImageFileFormat_Init = _hapi.HAPI_ImageFileFormat_Init
ImageFileFormat_Init.restype = None
ImageFileFormat_Init.argtypes = [ ctypes.POINTER(ImageFileFormat) ]

ImageFileFormat_Create = _hapi.HAPI_ImageFileFormat_Create
ImageFileFormat_Create.restype = ImageFileFormat
ImageFileFormat_Create.argtypes = []
# 
ImageInfo_Init = _hapi.HAPI_ImageInfo_Init
ImageInfo_Init.restype = None
ImageInfo_Init.argtypes = [ ctypes.POINTER(ImageInfo) ]

ImageInfo_Create = _hapi.HAPI_ImageInfo_Create
ImageInfo_Create.restype = ImageInfo
ImageInfo_Create.argtypes = []
# 
# # ANIMATION ----------------------------------------------------------------
# 
Keyframe_Init = _hapi.HAPI_Keyframe_Init
Keyframe_Init.restype = None
Keyframe_Init.argtypes = [ ctypes.POINTER(Keyframe) ]

Keyframe_Create = _hapi.HAPI_Keyframe_Create
Keyframe_Create.restype = Keyframe
Keyframe_Create.argtypes = []
# 
# # VOLUMES ------------------------------------------------------------------
# 
VolumeInfo_Init = _hapi.HAPI_VolumeInfo_Init
VolumeInfo_Init.restype = None
VolumeInfo_Init.argtypes = [ ctypes.POINTER(VolumeInfo) ]

VolumeInfo_Create = _hapi.HAPI_VolumeInfo_Create
VolumeInfo_Create.restype = VolumeInfo
VolumeInfo_Create.argtypes = []
# 
VolumeTileInfo_Init = _hapi.HAPI_VolumeTileInfo_Init
VolumeTileInfo_Init.restype = None
VolumeTileInfo_Init.argtypes = [ ctypes.POINTER(VolumeTileInfo) ]

VolumeTileInfo_Create = _hapi.HAPI_VolumeTileInfo_Create
VolumeTileInfo_Create.restype = VolumeTileInfo
VolumeTileInfo_Create.argtypes = []
# 
# # CURVES -------------------------------------------------------------------
# 
CurveInfo_Init = _hapi.HAPI_CurveInfo_Init
CurveInfo_Init.restype = None
CurveInfo_Init.argtypes = [ ctypes.POINTER(CurveInfo) ]

CurveInfo_Create = _hapi.HAPI_CurveInfo_Create
CurveInfo_Create.restype = CurveInfo
CurveInfo_Create.argtypes = []
# 
# # TRANSFORMS ---------------------------------------------------------------
# 
Transform_Init = _hapi.HAPI_Transform_Init
Transform_Init.restype = None
Transform_Init.argtypes = [ ctypes.POINTER(Transform) ]

Transform_Create = _hapi.HAPI_Transform_Create
Transform_Create.restype = Transform
Transform_Create.argtypes = []
# 
TransformEuler_Init = _hapi.HAPI_TransformEuler_Init
TransformEuler_Init.restype = None
TransformEuler_Init.argtypes = [ ctypes.POINTER(TransformEuler) ]

TransformEuler_Create = _hapi.HAPI_TransformEuler_Create
TransformEuler_Create.restype = TransformEuler
TransformEuler_Create.argtypes = []
# 
