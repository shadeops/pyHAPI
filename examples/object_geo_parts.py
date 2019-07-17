from __future__ import print_function

import sys
from ctypes import byref, c_int, c_float, create_string_buffer

import hapi

class HAPIException(Exception):
    pass

def get_last_error():
    buf_len = c_int()
    hapi.GetStatusStringBufLength(None,
                                  hapi.STATUS_CALL_RESULT,
                                  hapi.STATUSVERBOSITY_ERRORS,
                                  byref(buf_len))
    buf = create_string_buffer(buf_len.value)
    hapi.GetStatusString(None, hapi.STATUS_CALL_RESULT, buf, buf_len)
    result = str(buf.value)
    return result

def get_last_cook_error():
    buf_len = c_int()
    hapi.GetStatusStringBufLength(None,
                                  hapi.STATUS_COOK_RESULT,
                                  hapi.STATUSVERBOSITY_ERRORS,
                                  byref(buf_len))
    buf = create_string_buffer(buf_len.value)
    hapi.GetStatusString(None, hapi.STATUS_COOK_RESULT, buf, buf_len)
    result = str(buf.value)
    return result

def get_string(string_handle):
    if string_handle == None:
        return ''
    buf_len = c_int()
    hapi.GetStringBufLength(None,
                            string_handle,
                            byref(buf_len))
    buf = create_string_buffer(buf_len.value)
    hapi.GetString(None, string_handle, buf, buf_len)
    result = str(buf.value)
    return result

def ensure_success(result):
    if isinstance(result, c_int):
        result = result.value
    if result != hapi.RESULT_SUCCESS:
        raise HAPIException('Failure: %s' % get_last_error())

def ensure_cook_success(result):
    if isinstance(result, c_int):
        result = result.value
    if result != hapi.RESULT_SUCCESS:
        raise HAPIException('Cook Failure: %s' % get_last_cook_error())

def process_float_attrib(session, asset_info, geo_node, part_id, owner, name):
    attrib_info = hapi.AttributeInfo()
    ensure_success(hapi.GetAttributeInfo(byref(session),
                                         geo_node,
                                         part_id,
                                         name,
                                         owner,
                                         byref(attrib_info)))
    attrib_data = (c_float * (attrib_info.count * attrib_info.tupleSize))()
    ensure_success(hapi.GetAttributeFloatData(byref(session),
                                              geo_node,
                                              part_id,
                                              name,
                                              byref(attrib_info),
                                              -1,
                                              attrib_data,
                                              0,
                                              attrib_info.count))
    for elm_idx in range(attrib_info.count):
        for tuple_idx in range(attrib_info.tupleSize):
            print(attrib_data[elm_idx * attrib_info.tupleSize + tuple_idx], end='')
        print()
    return

def process_geo_parts(session, asset_info, object_node, geo_node, part_id):
    print('Object %s, Geo %s, Part %s' % (object_node, geo_node, part_id))

    part_info = hapi.PartInfo()
    ensure_success(hapi.GetPartInfo(byref(session),
                                    geo_node,
                                    part_id,
                                    byref(part_info)))
    attrib_names_sh = (hapi.StringHandle * part_info.attributeCounts[hapi.ATTROWNER_POINT])()
    ensure_success(hapi.GetAttributeNames(byref(session),
                                          geo_node,
                                          part_info.id,
                                          hapi.ATTROWNER_POINT,
                                          attrib_names_sh,
                                          part_info.attributeCounts[hapi.ATTROWNER_POINT]))
    for i in range(part_info.attributeCounts[hapi.ATTROWNER_POINT]):
        print('\t', attrib_names_sh[i])

    print('Point Positions: ')

    process_float_attrib(session,
                         asset_info,
                         geo_node,
                         part_id,
                         hapi.ATTROWNER_POINT,
                         'P')

    print('Number of Faces: %i' % part_info.faceCount)

    if part_info.type != hapi.PARTTYPE_CURVE:
        face_counts = (c_int * part_info.faceCount)()
        ensure_success(hapi.GetFaceCounts(byref(session),
                                          geo_node,
                                          part_id,
                                          face_counts,
                                          0,
                                          part_info.faceCount))
        print(','.join([str(i) for i in face_counts]))

        vertex_list = (c_int * part_info.vertexCount)()
        ensure_success(hapi.GetVertexList(byref(session),
                                          geo_node,
                                          part_id,
                                          vertex_list,
                                          0,
                                          part_info.vertexCount))
        print('Vertex Indices into Points array:')
        current_idx = 0
        for i in range(part_info.faceCount):
            for j in range(face_counts[i]):
                print('Vertex : %i, belong to face: %i, index: %i of points array' % (
                    current_idx, i, vertex_list[current_idx]))
                current_idx += 1


def print_complete_node_info(session, node_id, asset_info):
    object_count = c_int()
    ensure_success(hapi.ComposeObjectList(byref(session),
                                          node_id,
                                          None,
                                          byref(object_count)))
    print(object_count.value)
    object_infos = (hapi.ObjectInfo * object_count.value)()
    ensure_success(hapi.GetComposedObjectList(byref(session),
                                              node_id,
                                              object_infos,
                                              0,
                                              object_count))
    for object_info in object_infos:
        geo_info = hapi.GeoInfo()
        ensure_success(hapi.GetDisplayGeoInfo(byref(session),
                                              object_info.nodeId,
                                              byref(geo_info)))
        for i in range(geo_info.partCount):
            process_geo_parts(session,
                              asset_info,
                              object_info.nodeId,
                              geo_info.nodeId,
                              i)

def main():

    hda_file = 'examples/TestShapes.hda'
    if len(sys.argv) == 2:
        hda_file = sys.argv[1]

    cook_options = hapi.CookOptions_Create()
    session = hapi.Session()
    hapi.CreateInProcessSession(byref(session))

    ensure_success(hapi.Initialize(byref(session),
                                   byref(cook_options),
                                   True,
                                   -1,
                                   None,
                                   None,
                                   None,
                                   None,
                                   None))
    asset_lib_id = c_int()
    ensure_success(hapi.LoadAssetLibraryFromFile(byref(session),
                                                 hda_file,
                                                 True,
                                                 byref(asset_lib_id)))

    asset_count = c_int()
    ensure_success(hapi.GetAvailableAssetCount(byref(session),
                                               asset_lib_id,
                                               byref(asset_count)))

    if (asset_count.value > 1):
        print('Should only be 1 asset')
        sys.exit(1)

    asset_sh = hapi.StringHandle()
    ensure_success(hapi.GetAvailableAssets(byref(session),
                                           asset_lib_id,
                                           byref(asset_sh),
                                           asset_count))
    asset_name = get_string(asset_sh)

    node_id = hapi.NodeId()
    ensure_success(hapi.CreateNode(byref(session),
                                   -1,
                                   asset_name,
                                   'TestObject',
                                   False,
                                   byref(node_id)))

    ensure_success(hapi.CookNode(byref(session),
                                 node_id,
                                 byref(cook_options)))

    cook_status = c_int()
    while True:
        cook_result = hapi.GetStatus(byref(session),
                                     hapi.STATUS_COOK_STATE,
                                     byref(cook_status))
        if not ( cook_status.value > hapi.STATE_MAX_READY_STATE and
             cook_result == hapi.RESULT_SUCCESS):
            break
    ensure_success(cook_result)
    ensure_cook_success(cook_status)

    asset_info = hapi.AssetInfo()
    ensure_success(hapi.GetAssetInfo(byref(session),
                                     node_id,
                                     byref(asset_info)))
    print_complete_node_info(session,
                             node_id,
                             asset_info)

    hapi.Cleanup(byref(session))


if __name__ == '__main__':
    main()

