from platform import system as _system_platform
from ctypes import Structure as _Structure
from ctypes import c_int as _c_int
from ctypes import c_float as _c_float
from ctypes import c_double as _c_double
from ctypes import c_uint as _c_uint
from ctypes import c_bool as _c_bool
from ctypes import c_longlong as _c_longlong

POSITION_VECTOR_SIZE           = 3
SCALE_VECTOR_SIZE              = 3
SHEAR_VECTOR_SIZE              = 3
NORMAL_VECTOR_SIZE             = 3
QUATERNION_VECTOR_SIZE         = 4
EULER_VECTOR_SIZE              = 3
UV_VECTOR_SIZE                 = 2
COLOR_VECTOR_SIZE              = 4
CV_VECTOR_SIZE                 = 4

PRIM_MIN_VERTEX_COUNT          = 1
PRIM_MAX_VERTEX_COUNT          = 16

INVALID_PARM_ID                = -1

ATTRIB_POSITION                = 'P'
ATTRIB_UV                      = 'uv'
ATTRIB_UV2                     = 'uv2'
ATTRIB_NORMAL                  = 'N'
ATTRIB_TANGENT                 = 'tangentu'
ATTRIB_TANGENT2                = 'tangentv'
ATTRIB_COLOR                   = 'Cd'
ATTRIB_NAME                    = 'name'
ATTRIB_INSTANCE                = 'instance'

UNGROUPED_GROUP_NAME           = '__ungrouped_group'

RAW_FORMAT_NAME                = 'HAPI_RAW'
PNG_FORMAT_NAME                = 'PNG'
JPEG_FORMAT_NAME               = 'JPEG'
BMP_FORMAT_NAME                = 'Bitmap'
TIFF_FORMAT_NAME               = 'TIFF'
TGA_FORMAT_NAME                = 'Targa'

DEFAULT_IMAGE_FORMAT_NAME      = PNG_FORMAT_NAME

GLOBAL_NODES_NODE_NAME         = 'GlobalNodes'

ENV_HIP                        = 'HIP'
ENV_JOB                        = 'JOB'
ENV_CLIENT_NAME                = 'HAPI_CLIENT_NAME'

CACHE_COP_COOK                 = 'COP Cook Cache'
CACHE_COP_FLIPBOOK             = 'COP Flipbook Cache'
CACHE_IMAGE                    = 'Image Cache'
CACHE_OBJ                      = 'Object Transform Cache'
CACHE_GL_TEXTURE               = 'OpenGL Texture Cache'
CACHE_GL_VERTEX                = 'OpenGL Vertex Cache'
CACHE_SOP                      = 'SOP Cache'
CACHE_VEX                      = 'VEX File Cache'

Bool = _c_bool

Int64 = _c_longlong

if _system_platform() == 'Windows':
    ProcessId = _c_uint
else:
    ProcessId = _c_int

SessionId = Int64

StringHandle = _c_int

AssetLibraryId = _c_int

NodeId = _c_int

ParmId = _c_int

PartId = _c_int

License = _c_int
(
    LICENSE_NONE,
    LICENSE_HOUDINI_ENGINE,
    LICENSE_HOUDINI,
    LICENSE_HOUDINI_FX,
    LICENSE_HOUDINI_ENGINE_INDIE,
    LICENSE_HOUDINI_INDIE,
    LICENSE_MAX
) = range(7)

StatusType = _c_int
(
    STATUS_CALL_RESULT,
    STATUS_COOK_RESULT,
    STATUS_COOK_STATE,
    STATUS_MAX
) = range(4)

StatusVerbosity = _c_int
STATUSVERBOSITY_0 = 0
STATUSVERBOSITY_1 = 1
STATUSVERBOSITY_2 = 2

STATUSVERBOSITY_ALL = STATUSVERBOSITY_2

STATUSVERBOSITY_ERRORS = STATUSVERBOSITY_0
STATUSVERBOSITY_WARNINGS = STATUSVERBOSITY_1
STATUSVERBOSITY_MESSAGES = STATUSVERBOSITY_2

Result = _c_int

RESULT_SUCCESS                                 = 0
RESULT_FAILURE                                 = 1
RESULT_ALREADY_INITIALIZED                     = 2
RESULT_NOT_INITIALIZED                         = 3
RESULT_CANT_LOADFILE                           = 4
RESULT_PARM_SET_FAILED                         = 5
RESULT_INVALID_ARGUMENT                        = 6
RESULT_CANT_LOAD_GEO                           = 7
RESULT_CANT_GENERATE_PRESET                    = 8
RESULT_CANT_LOAD_PRESET                        = 9
RESULT_ASSET_DEF_ALREADY_LOADED                = 10

RESULT_NO_LICENSE_FOUND                        = 110
RESULT_DISALLOWED_NC_LICENSE_FOUND             = 120
RESULT_DISALLOWED_NC_ASSET_WITH_C_LICENSE      = 130
RESULT_DISALLOWED_NC_ASSET_WITH_LC_LICENSE     = 140
RESULT_DISALLOWED_LC_ASSET_WITH_C_LICENSE      = 150
RESULT_DISALLOWED_HENGINEINDIE_W_3PARTY_PLUGIN = 160

RESULT_ASSET_INVALID                           = 200
RESULT_NODE_INVALID                            = 210

RESULT_USER_INTERRUPTED                        = 300

RESULT_INVALID_SESSION                         = 400

ErrorCode = _c_int
ERRORCODE_ASSET_DEF_NOT_FOUND                  = 1 << 0
ERRORCODE_PYTHON_NODE_ERROR                    = 1 << 1

ErrorCodeBits = _c_int

SessionType = _c_int
(
    SESSION_INPROCESS,
    SESSION_THRIFT,
    SESSION_CUSTOM1,
    SESSION_CUSTOM2,
    SESSION_CUSTOM3,
    SESSION_MAX
) = range(6)

State = _c_int
(
    STATE_READY,
    STATE_READY_WITH_FATAL_ERRORS,
    STATE_READY_WITH_COOK_ERRORS,
    STATE_STARTING_COOK,
    STATE_COOKING,
    STATE_STARTING_LOAD,
    STATE_LOADING,
    STATE_MAX,
) = range(8)
STATE_MAX_READY_STATE = STATE_READY_WITH_COOK_ERRORS

PackedPrimInstancingMode = _c_int
(
    PACKEDPRIM_INSTANCING_MODE_INVALID,
    PACKEDPRIM_INSTANCING_MODE_DISABLED,
    PACKEDPRIM_INSTANCING_MODE_HIERARCHY,
    PACKEDPRIM_INSTANCING_MODE_FLAT,
    PACKEDPRIM_INSTANCING_MODE_MAX
) = range(-1,4)

Permissions = _c_int
(
    PERMISSIONS_NON_APPLICABLE,
    PERMISSIONS_READ_WRITE,
    PERMISSIONS_READ_ONLY,
    PERMISSIONS_WRITE_ONLY,
    PERMISSIONS_MAX
) = range(5)

RampType = _c_int
(
    RAMPTYPE_INVALID,
    RAMPTYPE_FLOAT,
    RAMPTYPE_COLOR,
    RAMPTYPE_MAX,
) = range(-1, 3)

ParmType = _c_int
(
    PARMTYPE_INT,
    PARMTYPE_MULTIPARMLIST,
    PARMTYPE_TOGGLE,
    PARMTYPE_BUTTON,

    PARMTYPE_FLOAT,
    PARMTYPE_COLOR,

    PARMTYPE_STRING,
    PARMTYPE_PATH_FILE,
    PARMTYPE_PATH_FILE_GEO,
    PARMTYPE_PATH_FILE_IMAGE,

    PARMTYPE_NODE,

    PARMTYPE_FOLDERLIST,
    PARMTYPE_FOLDERLIST_RADIO,

    PARMTYPE_FOLDER,
    PARMTYPE_LABEL,
    PARMTYPE_SEPARATOR,

    PARMTYPE_MAX
) = range(17)

PARMTYPE_INT_START         = PARMTYPE_INT
PARMTYPE_INT_END           = PARMTYPE_BUTTON

PARMTYPE_FLOAT_START       = PARMTYPE_FLOAT
PARMTYPE_FLOAT_END         = PARMTYPE_COLOR

PARMTYPE_STRING_START      = PARMTYPE_STRING
PARMTYPE_STRING_END        = PARMTYPE_NODE

PARMTYPE_PATH_START        = PARMTYPE_PATH_FILE
PARMTYPE_PATH_END          = PARMTYPE_PATH_FILE_IMAGE

PARMTYPE_NODE_START        = PARMTYPE_NODE
PARMTYPE_NODE_END          = PARMTYPE_NODE

PARMTYPE_CONTAINER_START   = PARMTYPE_FOLDERLIST
PARMTYPE_CONTAINER_END     = PARMTYPE_FOLDERLIST_RADIO

PARMTYPE_NONVALUE_START    = PARMTYPE_FOLDER
PARMTYPE_NONVALUE_END      = PARMTYPE_SEPARATOR

ChoiceListType = _c_int
(
    CHOICELISTTYPE_NONE,
    CHOICELISTTYPE_NORMAL,
    CHOICELISTTYPE_MINI,
    CHOICELISTTYPE_REPLACE,
    CHOICELISTTYPE_TOGGLE
) = range(5)

PresetType = _c_int
(
    PRESETTYPE_INVALID,
    PRESETTYPE_BINARY,
    PRESETTYPE_IDX,
    PRESETTYPE_MAX
) = range(-1, 3)

NodeType = _c_int
NODETYPE_ANY       = -1
NODETYPE_NONE      = 0
NODETYPE_OBJ       = 1 << 0
NODETYPE_SOP       = 1 << 1
NODETYPE_POP       = 1 << 2
NODETYPE_CHOP      = 1 << 3
NODETYPE_ROP       = 1 << 4
NODETYPE_SHOP      = 1 << 5
NODETYPE_COP       = 1 << 6
NODETYPE_VOP       = 1 << 7
NODETYPE_DOP       = 1 << 8
NodeTypeBits = _c_int

NodeFlags = _c_int
NODEFLAGS_ANY          = -1
NODEFLAGS_NONE         = 0
NODEFLAGS_DISPLAY      = 1 << 0
NODEFLAGS_RENDER       = 1 << 1
NODEFLAGS_TEMPLATED    = 1 << 2
NODEFLAGS_LOCKED       = 1 << 3
NODEFLAGS_EDITABLE     = 1 << 4
NODEFLAGS_BYPASS       = 1 << 5
NODEFLAGS_NETWORK      = 1 << 6

NODEFLAGS_OBJ_GEOMETRY = 1 << 7
NODEFLAGS_OBJ_CAMERA   = 1 << 8
NODEFLAGS_OBJ_LIGHT    = 1 << 9
NODEFLAGS_OBJ_SUBNET   = 1 << 10

NODEFLAGS_SOP_CURVE    = 1 << 11
NodeFlagsBits = _c_int

GroupType = _c_int
(
    GROUPTYPE_INVALID,
    GROUPTYPE_POINT,
    GROUPTYPE_PRIM,
    GROUPTYPE_MAX
) = range(-1, 3)

AttributeOwner = _c_int
(
    ATTROWNER_INVALID,
    ATTROWNER_VERTEX,
    ATTROWNER_POINT,
    ATTROWNER_PRIM,
    ATTROWNER_DETAIL,
    ATTROWNER_MAX
) = range(-1, 5)

CurveType = _c_int
(
    CURVETYPE_INVALID,
    CURVETYPE_LINEAR,
    CURVETYPE_NURBS,
    CURVETYPE_BEZIER,
    CURVETYPE_MAX
) = range(-1, 4)

VolumeType = _c_int
(
    VOLUMETYPE_INVALID,
    VOLUMETYPE_HOUDINI,
    VOLUMETYPE_VDB,
    VOLUMETYPE_MAX
) = range(-1, 3)

StorageType = _c_int
(
    STORAGETYPE_INVALID,
    STORAGETYPE_INT,
    STORAGETYPE_INT64,
    STORAGETYPE_FLOAT,
    STORAGETYPE_FLOAT64,
    STORAGETYPE_STRING,
    STORAGETYPE_MAX
) = range(-1, 6)

AttributeTypeInfo = _c_int
(
    ATTRIBUTE_TYPE_INVALID,
    ATTRIBUTE_TYPE_NONE,
    ATTRIBUTE_TYPE_POINT,
    ATTRIBUTE_TYPE_HPOINT,
    ATTRIBUTE_TYPE_VECTOR,
    ATTRIBUTE_TYPE_NORMAL,
    ATTRIBUTE_TYPE_COLOR,
    ATTRIBUTE_TYPE_QUATERNION,
    ATTRIBUTE_TYPE_MATRIX3,
    ATTRIBUTE_TYPE_MATRIX,
    ATTRIBUTE_TYPE_ST,
    ATTRIBUTE_TYPE_HIDDEN,
    ATTRIBUTE_TYPE_BOX2,
    ATTRIBUTE_TYPE_BOX,
    ATTRIBUTE_TYPE_TEXTURE,
    ATTRIBUTE_TYPE_MAX
) = range(-1, 15)

GeoType = _c_int
(
    GEOTYPE_INVALID,
    GEOTYPE_DEFAULT,
    GEOTYPE_INTERMEDIATE,
    GEOTYPE_INPUT,
    GEOTYPE_CURVE,
    GEOTYPE_MAX
) = range(-1, 5)

PartType = _c_int
(
    PARTTYPE_INVALID,
    PARTTYPE_MESH,
    PARTTYPE_CURVE,
    PARTTYPE_VOLUME,
    PARTTYPE_INSTANCER,
    PARTTYPE_BOX,
    PARTTYPE_SPHERE,
    PARTTYPE_MAX
) = range(-1, 7)

InputType = _c_int
(
    INPUT_INVALID,
    INPUT_TRANSFORM,
    INPUT_GEOMETRY,
    INPUT_MAX
) = range(-1, 3)

CurveOrders = _c_int
CURVE_ORDER_VARYING =   0
CURVE_ORDER_INVALID =   1
CURVE_ORDER_LINEAR =    2
CURVE_ORDER_QUADRATIC = 3
CURVE_ORDER_CUBIC =     4

TransformComponent = _c_int
(
    TRANSFORM_TX,
    TRANSFORM_TY,
    TRANSFORM_TZ,
    TRANSFORM_RX,
    TRANSFORM_RY,
    TRANSFORM_RZ,
    TRANSFORM_QX,
    TRANSFORM_QY,
    TRANSFORM_QZ,
    TRANSFORM_QW,
    TRANSFORM_SX,
    TRANSFORM_SY,
    TRANSFORM_SZ
) = range(13)

RSTOrder = _c_int
(
    TRS,
    TSR,
    RTS,
    RST,
    STR,
    SRT
) = range(6)
RSTORDER_DEFAULT = SRT

XYZOrder = _c_int
(
    XYZ,
    XZY,
    YXZ,
    YZX,
    ZXY,
    ZYX
) = range(6)
XYZORDER_DEFAULT = XYZ

ImageDataFormat = _c_int
(
    IMAGE_DATA_UNKNOWN,
    IMAGE_DATA_INT8,
    IMAGE_DATA_INT16,
    IMAGE_DATA_INT32,
    IMAGE_DATA_FLOAT16,
    IMAGE_DATA_FLOAT32,
    IMAGE_DATA_MAX,
) = range(-1,6)
IMAGE_DATA_DEFAULT = IMAGE_DATA_INT8

ImagePacking = _c_int
(
    IMAGE_PACKING_UNKNOWN,
    IMAGE_PACKING_SINGLE,
    IMAGE_PACKING_DUAL,
    IMAGE_PACKING_RGB,
    IMAGE_PACKING_BGR,
    IMAGE_PACKING_RGBA,
    IMAGE_PACKING_ABGR,
    IMAGE_PACKING_MAX
) = range(-1, 7)
IMAGE_PACKING_DEFAULT3 = IMAGE_PACKING_RGB
IMAGE_PACKING_DEFAULT4 = IMAGE_PACKING_RGBA

EnvIntType = _c_int

ENVINT_INVALID = _c_int(-1)

ENVINT_VERSION_HOUDINI_MAJOR = 100
ENVINT_VERSION_HOUDINI_MINOR = 110
ENVINT_VERSION_HOUDINI_BUILD = 120
ENVINT_VERSION_HOUDINI_PATCH = 130

ENVINT_VERSION_HOUDINI_ENGINE_MAJOR = 200
ENVINT_VERSION_HOUDINI_ENGINE_MINOR = 210

ENVINT_VERSION_HOUDINI_ENGINE_API = 220

ENVINT_MAX = ENVINT_VERSION_HOUDINI_ENGINE_API+1

SessionEnvIntType = _c_int

SESSIONENVINT_INVALID = -1

SESSIONENVINT_LICENSE = 100

SESSIONENVINT_MAX = SESSIONENVINT_LICENSE+1

CacheProperty = _c_int
(
    CACHEPROP_CURRENT,

    CACHEPROP_HAS_MIN,
    CACHEPROP_MIN,
    CACHEPROP_HAS_MAX,
    CACHEPROP_MAX,
    CACHEPROP_CULL_LEVEL,
) = range(6)

# Main API Structs

# GENERICS -----------------------------------------------------------------

class Transform(_Structure):
    _fields_ = [('position', _c_float * POSITION_VECTOR_SIZE),
                ('rotationQuaternion', _c_float * QUATERNION_VECTOR_SIZE),
                ('scale', _c_float * SCALE_VECTOR_SIZE),
                ('shear', _c_float * SHEAR_VECTOR_SIZE),

                ('rstOrder', RSTOrder)]

class TransformEuler(_Structure):
    _fields_ = [('position', _c_float * POSITION_VECTOR_SIZE),
                ('rotationEuler', _c_float * EULER_VECTOR_SIZE),
                ('scale', _c_float * SCALE_VECTOR_SIZE),
                ('shear', _c_float * SHEAR_VECTOR_SIZE),

                ('rotationOrder', XYZOrder),
                ('rstOrder', RSTOrder)]

# SESSIONS -----------------------------------------------------------------

class Session(_Structure):
    _fields_= [('type', SessionType),
               ('id', SessionId)]

class ThriftServerOptions(_Structure):
    _fields_ = [('autoClose', Bool),
                ('timeoutMs', _c_float)]

# TIME ---------------------------------------------------------------------

class TimelineOptions(_Structure):
    _fields_= [('fps',_c_float),
               ('startTime',_c_float),
               ('endTime',_c_float)]


# ASSETS -------------------------------------------------------------------

class AssetInfo(_Structure):
    _fields_ = [
                ('nodeId', NodeId),
                ('objectNodeId', NodeId),
                ('hasEverCooked', Bool),
                ('nameSH', StringHandle),
                ('labelSH', StringHandle),
                ('filePathSH', StringHandle),
                ('versionSH', StringHandle),
                ('fullOpNameSH', StringHandle),
                ('helpTextSH', StringHandle),
                ('objectCount', _c_int),
                ('handleCount', _c_int),
                ('transformInputCount', _c_int),
                ('geoInputCount', _c_int),
                ('haveObjectsChanged', _c_int),
                ('haveMaterialsChanged', Bool)
                ]

class CookOptions(_Structure):
    _fields_ = [
                ('splitGeosByGroup', Bool),
                ('maxVerticesPerPrimitive', _c_int),
                ('refineCurveToLinear', Bool),
                ('curveRefineLOD', _c_float),
                ('clearErrorsAndWarnings', Bool),
                ('cookTemplatedGeos', Bool),
                ('splitPointsByVertexAttributes', Bool),
                ('packedPrimInstancingMode', PackedPrimInstancingMode),
                ('handleBoxPartTypes', Bool),
                ('handleSpherePartTypes', Bool),
                ('extraFlags', _c_int)
                ]

# NODES --------------------------------------------------------------------

class NodeInfo(_Structure):
    _fields_ = [('id', NodeId),
                ('parentId', NodeId),
                ('nameSH', StringHandle),
                ('type', NodeType),
                ('isValid', Bool),
                ('totalCookCount', _c_int),
                ('uniqueHoudiniNodeId', _c_int),
                ('internalNodePathSH', StringHandle),
                ('parmCount', _c_int),
                ('parmIntValueCount', _c_int),
                ('parmFloatValueCount', _c_int),
                ('parmStringValueCount', _c_int),
                ('parmChoiceCount', _c_int),
                ('childNodeCount', _c_int),
                ('inputCount', _c_int),
                ('createdPostAssetLoad', Bool)
                ]


# PARAMETERS ---------------------------------------------------------------

class ParmInfo(_Structure):
    _fields_ = [
                ('id', ParmId),
                ('parentId', ParmId),
                ('childIndex', _c_int),
                ('type', ParmType),
                ('typeInfoSH', StringHandle),
                ('permissions', Permissions),
                ('tagCount', _c_int),
                ('size', _c_int),
                ('choiceListType', ChoiceListType),
                ('choiceCount', _c_int),
                ('nameSH', StringHandle),
                ('labelSH', StringHandle),
                ('templateNameSH', StringHandle),
                ('helpSH', StringHandle),
                ('hasMin', Bool),
                ('hasMax', Bool),
                ('hasUIMin', Bool),
                ('hasUIMax', Bool),
                ('min', _c_float),
                ('max', _c_float),
                ('UIMin', _c_float),
                ('UIMax', _c_float),
                ('invisible', Bool),
                ('disabled', Bool),
                ('spare', Bool),
                ('joinNext', Bool),
                ('labelNone', Bool),
                ('intValuesIndex', _c_int),
                ('floatValuesIndex', _c_int),
                ('stringValuesIndex', _c_int),
                ('choiceIndex', _c_int),
                ('inputNodeType', NodeType),
                ('inputNodeFlag', NodeFlags),
                ('isChildOfMultiParm', Bool),
                ('instanceNum', _c_int),
                ('instanceLength', _c_int),
                ('instanceCount', _c_int),
                ('instanceStartOffset', _c_int),
                ('rampType', RampType)
               ]

class ParmChoiceInfo(_Structure):
    _fields_ = [
                ('parentParmId', ParmId),
                ('labelSH', StringHandle),
                ('valueSH', StringHandle)
                ]

# HANDLES ------------------------------------------------------------------

class HandleInfo(_Structure):
    _fields_ = [
                ('nameSH', StringHandle),
                ('typeNameSH', StringHandle),
                ('bindingsCount', _c_int)
               ]

class HandleBindingInfo(_Structure):
    _fields_ = [
                ('handleParmNameSH', StringHandle),
                ('assetParmNameSH', StringHandle),
                ('assetParmId', ParmId)
               ]

# OBJECTS ------------------------------------------------------------------

class ObjectInfo(_Structure):
    _fields_ = [
                ('nameSH', StringHandle),
                ('objectInstancePathSH', StringHandle),
                ('hasTransformChanged', Bool),
                ('haveGeosChanged', Bool),
                ('isVisible', Bool),
                ('isInstancer', Bool),
                ('isInstanced', Bool),
                ('geoCount', _c_int),
                ('nodeId', NodeId),
                ('objectToInstanceId', NodeId)
               ]

# GEOMETRY -----------------------------------------------------------------

class GeoInfo(_Structure):
    _fields_ = [
                ('type', GeoType),
                ('nameSH', StringHandle),
                ('nodeId', NodeId),
                ('isEditable', Bool),
                ('isTemplated', Bool),
                ('isDisplayGeo', Bool),
                ('hasGeoChanged', Bool),
                ('hasMaterialChanged', Bool),
                ('pointGroupCount', _c_int),
                ('primitiveGroupCount', _c_int),
                ('partCount', _c_int),
               ]

class PartInfo(_Structure):
    _fields_ = [
                ('id', PartId),
                ('nameSH', StringHandle),
                ('type', PartType),
                ('faceCount', _c_int),
                ('vertexCount', _c_int),
                ('pointCount', _c_int),
                ('attributeCounts', _c_int * ATTROWNER_MAX),
                ('isInstanced', Bool),
                ('instancedPartCount', _c_int),
                ('instanceCount', _c_int)
               ]

class AttributeInfo(_Structure):
    _fields_ = [
                ('exists', Bool),
                ('owner', AttributeOwner),
                ('storage', StorageType),
                ('originalOwner', AttributeOwner),
                ('count', _c_int),
                ('tupleSize', _c_int),
                ('typeInfo', AttributeTypeInfo)
                ]

# MATERIALS ----------------------------------------------------------------

class MaterialInfo(_Structure):
    _fields_ = [
                ('nodeId', NodeId),
                ('exists', Bool),
                ('hasChanged', Bool)
               ]

class ImageFileFormat(_Structure):
    _fields_ = [
                ('nameSH', StringHandle),
                ('descriptionSH', StringHandle),
                ('defaultExtensionSH', StringHandle)
                ]

class ImageInfo(_Structure):
    _fields_ = [
                ('imageFileFormatNameSH', StringHandle),
                ('xRes', _c_int),
                ('yRes', _c_int),
                ('dataFormat', ImageDataFormat),
                ('interleaved', Bool),
                ('packing', ImagePacking),
                ('gamma', _c_double)
               ]

# ANIMATION ----------------------------------------------------------------

class Keyframe(_Structure):
    _fields_ = [
                ('time', _c_float),
                ('value', _c_float),
                ('inTangent', _c_float),
                ('outtangent', _c_float)
                ]

# VOLUMES ------------------------------------------------------------------

class VolumeInfo(_Structure):
    _fields_ = [
                ('nameSH', StringHandle),
                ('type', VolumeType),
                ('xLength', _c_int),
                ('yLength', _c_int),
                ('zLength', _c_int),
                ('minX', _c_int),
                ('minY', _c_int),
                ('minZ', _c_int),
                ('tupleSize', _c_int),
                ('storage', StorageType),
                ('tileSize', _c_int),
                ('transform', Transform),
                ('hasTaper', Bool),
                ('xTaper', _c_float),
                ('yTaper', _c_float)
               ]

class VolumeTileInfo(_Structure):
    _fields_ = [
                ('minX', _c_int),
                ('minY', _c_int),
                ('minZ', _c_int),
                ('isValid', Bool)
                ]

# CURVES -------------------------------------------------------------------

class CurveInfo(_Structure):
    _fields_ = [
                ('curveType', CurveType),
                ('curveCount', _c_int),
                ('vertexCount', _c_int),
                ('knotCount', _c_int),
                ('isPeriodic', Bool),
                ('isRational', Bool),
                ('order', _c_int),
                ('hasKnots', Bool)
               ]

# BASIC PRIMITIVES ---------------------------------------------------------

class BoxInfo(_Structure):
    _fields_ = [
                ('center', _c_float * POSITION_VECTOR_SIZE),
                ('size', _c_float * SCALE_VECTOR_SIZE),
                ('rotation', _c_float * EULER_VECTOR_SIZE)
               ]

class SphereInfo(_Structure):
    _fields_ = [
                ('center', _c_float * POSITION_VECTOR_SIZE),
                ('radius', _c_float)
               ]

