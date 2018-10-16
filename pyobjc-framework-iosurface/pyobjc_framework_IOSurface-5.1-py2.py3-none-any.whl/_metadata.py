# This file is generated by objective.metadata
#
# Last update: Tue Jun  5 23:25:02 2018

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$IOSurfacePropertyAllocSizeKey$IOSurfacePropertyKeyAllocSize$IOSurfacePropertyKeyBytesPerElement$IOSurfacePropertyKeyBytesPerRow$IOSurfacePropertyKeyCacheMode$IOSurfacePropertyKeyElementHeight$IOSurfacePropertyKeyElementWidth$IOSurfacePropertyKeyHeight$IOSurfacePropertyKeyOffset$IOSurfacePropertyKeyPixelFormat$IOSurfacePropertyKeyPixelSizeCastingAllowed$IOSurfacePropertyKeyPlaneBase$IOSurfacePropertyKeyPlaneBytesPerElement$IOSurfacePropertyKeyPlaneBytesPerRow$IOSurfacePropertyKeyPlaneElementHeight$IOSurfacePropertyKeyPlaneElementWidth$IOSurfacePropertyKeyPlaneHeight$IOSurfacePropertyKeyPlaneInfo$IOSurfacePropertyKeyPlaneOffset$IOSurfacePropertyKeyPlaneSize$IOSurfacePropertyKeyPlaneWidth$IOSurfacePropertyKeyWidth$kIOSurfaceAllocSize@^{__CFString=}$kIOSurfaceBytesPerElement@^{__CFString=}$kIOSurfaceBytesPerRow@^{__CFString=}$kIOSurfaceCacheMode@^{__CFString=}$kIOSurfaceElementHeight@^{__CFString=}$kIOSurfaceElementWidth@^{__CFString=}$kIOSurfaceHeight@^{__CFString=}$kIOSurfaceIsGlobal@^{__CFString=}$kIOSurfaceOffset@^{__CFString=}$kIOSurfacePixelFormat@^{__CFString=}$kIOSurfacePixelSizeCastingAllowed$kIOSurfacePlaneBase@^{__CFString=}$kIOSurfacePlaneBitsPerElement$kIOSurfacePlaneBytesPerElement@^{__CFString=}$kIOSurfacePlaneBytesPerRow@^{__CFString=}$kIOSurfacePlaneComponentBitDepths$kIOSurfacePlaneComponentBitOffsets$kIOSurfacePlaneComponentNames$kIOSurfacePlaneElementHeight@^{__CFString=}$kIOSurfacePlaneElementWidth@^{__CFString=}$kIOSurfacePlaneHeight@^{__CFString=}$kIOSurfacePlaneInfo@^{__CFString=}$kIOSurfacePlaneOffset@^{__CFString=}$kIOSurfacePlaneSize@^{__CFString=}$kIOSurfacePlaneWidth@^{__CFString=}$kIOSurfaceSubsampling$kIOSurfaceWidth@^{__CFString=}$'''
enums = '''$_IOSURFACE_API_H@1$_IOSURFACE_H@1$kIOSurfaceComponentNameAlpha@1$kIOSurfaceComponentNameBlue@4$kIOSurfaceComponentNameChromaBlue@7$kIOSurfaceComponentNameChromaRed@6$kIOSurfaceComponentNameGreen@3$kIOSurfaceComponentNameLuma@5$kIOSurfaceComponentNameRed@2$kIOSurfaceComponentNameUnknown@0$kIOSurfaceComponentRangeFullRange@1$kIOSurfaceComponentRangeUnknown@0$kIOSurfaceComponentRangeVideoRange@2$kIOSurfaceComponentRangeWideRange@3$kIOSurfaceComponentTypeFloat@3$kIOSurfaceComponentTypeSignedInteger@2$kIOSurfaceComponentTypeUnknown@0$kIOSurfaceComponentTypeUnsignedInteger@1$kIOSurfaceCopybackCache@3$kIOSurfaceCopybackInnerCache@5$kIOSurfaceDefaultCache@0$kIOSurfaceInhibitCache@1$kIOSurfaceLockAvoidSync@2$kIOSurfaceLockReadOnly@1$kIOSurfaceMapCacheShift@8$kIOSurfaceMapCopybackCache@768$kIOSurfaceMapCopybackInnerCache@1280$kIOSurfaceMapDefaultCache@0$kIOSurfaceMapInhibitCache@256$kIOSurfaceMapWriteCombineCache@1024$kIOSurfaceMapWriteThruCache@512$kIOSurfacePurgeableEmpty@2$kIOSurfacePurgeableKeepCurrent@3$kIOSurfacePurgeableNonVolatile@0$kIOSurfacePurgeableVolatile@1$kIOSurfaceSubsampling411@4$kIOSurfaceSubsampling420@3$kIOSurfaceSubsampling422@2$kIOSurfaceSubsamplingNone@1$kIOSurfaceSubsamplingUnknown@0$kIOSurfaceWriteCombineCache@4$kIOSurfaceWriteThruCache@2$'''
misc.update({})
functions={'IOSurfaceGetSeed': (b'I^{__IOSurface=}',), 'IOSurfaceGetRangeOfComponentOfPlane': (b'i^{__IOSurface=}II',), 'IOSurfaceLookupFromMachPort': (b'^{__IOSurface=}I', '', {'retval': {'already_cfretained': True}}), 'IOSurfaceGetBytesPerRow': (sel32or64(b'L^{__IOSurface=}', b'Q^{__IOSurface=}'),), 'IOSurfaceGetUseCount': (b'i^{__IOSurface=}',), 'IOSurfaceSetValue': (b'v^{__IOSurface=}^{__CFString=}@',), 'IOSurfaceGetPlaneCount': (sel32or64(b'L^{__IOSurface=}', b'Q^{__IOSurface=}'),), 'IOSurfaceLock': (b'i^{__IOSurface=}I^I', '', {'arguments': {2: {'type_modifier': 'N'}}}), 'IOSurfaceDecrementUseCount': (b'v^{__IOSurface=}',), 'IOSurfaceGetTypeOfComponentOfPlane': (b'i^{__IOSurface=}II',), 'IOSurfaceLookupFromXPCObject': (b'^{__IOSurface=}@', '', {'retval': {'already_cfretained': True}}), 'IOSurfaceGetElementHeight': (sel32or64(b'L^{__IOSurface=}', b'Q^{__IOSurface=}'),), 'IOSurfaceGetBaseAddressOfPlane': (sel32or64(b'^v^{__IOSurface=}L', b'^v^{__IOSurface=}Q'), '', {'retval': {'c_array_of_variable_length': True}}), 'IOSurfaceGetSubsampling': (b'i^{__IOSurface=}',), 'IOSurfaceLookup': (b'^{__IOSurface=}I', '', {'retval': {'already_cfretained': True}}), 'IOSurfaceGetPixelFormat': (sel32or64(b'L^{__IOSurface=}', b'I^{__IOSurface=}'),), 'IOSurfaceGetBitOffsetOfComponentOfPlane': (b'I^{__IOSurface=}II',), 'IOSurfaceCopyValue': (b'@^{__IOSurface=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'IOSurfaceIncrementUseCount': (b'v^{__IOSurface=}',), 'IOSurfaceGetElementWidthOfPlane': (sel32or64(b'L^{__IOSurface=}L', b'Q^{__IOSurface=}Q'),), 'IOSurfaceGetID': (b'I^{__IOSurface=}',), 'IOSurfaceSetValues': (b'v^{__IOSurface=}^{__CFDictionary=}',), 'IOSurfaceRemoveAllValues': (b'v^{__IOSurface=}',), 'IOSurfaceGetTypeID': (sel32or64(b'L', b'Q'),), 'IOSurfaceCreateXPCObject': (b'@^{__IOSurface=}', '', {'retval': {'already_cfretained': True}}), 'IOSurfaceGetAllocSize': (sel32or64(b'L^{__IOSurface=}', b'Q^{__IOSurface=}'),), 'IOSurfaceGetBitDepthOfComponentOfPlane': (b'I^{__IOSurface=}II',), 'IOSurfaceGetElementWidth': (sel32or64(b'L^{__IOSurface=}', b'Q^{__IOSurface=}'),), 'IOSurfaceGetBytesPerElementOfPlane': (sel32or64(b'L^{__IOSurface=}L', b'Q^{__IOSurface=}Q'),), 'IOSurfaceCreateMachPort': (b'I^{__IOSurface=}', '', {'retval': {'already_cfretained': True}}), 'IOSurfaceGetNumberOfComponentsOfPlane': (b'I^{__IOSurface=}I',), 'IOSurfaceGetWidth': (sel32or64(b'L^{__IOSurface=}', b'Q^{__IOSurface=}'),), 'IOSurfaceRemoveValue': (b'v^{__IOSurface=}^{__CFString=}',), 'IOSurfaceGetHeightOfPlane': (sel32or64(b'L^{__IOSurface=}L', b'Q^{__IOSurface=}Q'),), 'IOSurfaceGetHeight': (sel32or64(b'L^{__IOSurface=}', b'Q^{__IOSurface=}'),), 'IOSurfaceGetBaseAddress': (b'^v^{__IOSurface=}', '', {'retval': {'c_array_of_variable_length': True}}), 'IOSurfaceAlignProperty': (sel32or64(b'L^{__CFString=}L', b'Q^{__CFString=}Q'),), 'IOSurfaceGetBytesPerRowOfPlane': (sel32or64(b'L^{__IOSurface=}L', b'Q^{__IOSurface=}Q'),), 'IOSurfaceCreate': (b'^{__IOSurface=}^{__CFDictionary=}', '', {'retval': {'already_retained': True, 'already_cfretained': True}}), 'IOSurfaceGetElementHeightOfPlane': (sel32or64(b'L^{__IOSurface=}L', b'Q^{__IOSurface=}Q'),), 'IOSurfaceGetBytesPerElement': (sel32or64(b'L^{__IOSurface=}', b'Q^{__IOSurface=}'),), 'IOSurfaceGetPropertyAlignment': (sel32or64(b'L^{__CFString=}', b'Q^{__CFString=}'),), 'IOSurfaceGetNameOfComponentOfPlane': (b'i^{__IOSurface=}II',), 'IOSurfaceUnlock': (b'i^{__IOSurface=}I^I', '', {'arguments': {2: {'type_modifier': 'N'}}}), 'IOSurfaceGetPropertyMaximum': (sel32or64(b'L^{__CFString=}', b'Q^{__CFString=}'),), 'IOSurfaceGetWidthOfPlane': (sel32or64(b'L^{__IOSurface=}L', b'Q^{__IOSurface=}Q'),), 'IOSurfaceIsInUse': (b'Z^{__IOSurface=}',), 'IOSurfaceAllowsPixelSizeCasting': (b'Z^{__IOSurface=}',), 'IOSurfaceCopyAllValues': (b'^{__CFDictionary=}^{__IOSurface=}', '', {'retval': {'already_cfretained': True}})}
aliases = {'IOSFC_AVAILABLE_BUT_DEPRECATED': '__OSX_AVAILABLE_BUT_DEPRECATED', 'IOSFC_AVAILABLE_STARTING': '__OSX_AVAILABLE_STARTING', 'IOSFC_DEPRECATED': 'DEPRECATED_ATTRIBUTE'}
cftypes=[('IOSurfaceRef', b'^{__IOSurface=}', 'IOSurfaceGetTypeID', None)]
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'IOSurface', b'allowsPixelSizeCasting', {'retval': {'type': 'Z'}})
    r(b'IOSurface', b'baseAddressOfPlaneAtIndex:', {'retval': {'c_array_of_variable_length': True}})
    r(b'IOSurface', b'isInUse', {'retval': {'type': 'Z'}})
    r(b'IOSurface', b'lockWithOptions:seed:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'IOSurface', b'setPurgeable:oldState:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'IOSurface', b'unlockWithOptions:seed:', {'arguments': {3: {'type_modifier': b'o'}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
