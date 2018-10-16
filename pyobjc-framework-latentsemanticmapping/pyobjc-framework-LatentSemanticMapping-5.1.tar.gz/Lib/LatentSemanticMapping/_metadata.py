# This file is generated by objective.metadata
#
# Last update: Fri Sep 21 15:42:58 2012

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
constants = '''$$'''
enums = '''$kLSMClusterAgglomerative@4$kLSMClusterCategories@0$kLSMClusterKMeans@0$kLSMClusterTokens@2$kLSMClusterWords@1$kLSMMapBadCluster@-6644$kLSMMapBadPath@-6643$kLSMMapDiscardCounts@1$kLSMMapHashText@256$kLSMMapLoadMutable@2$kLSMMapNoSuchCategory@-6641$kLSMMapOutOfState@-6640$kLSMMapOverflow@-6645$kLSMMapPairs@1$kLSMMapTriplets@2$kLSMMapWriteError@-6642$kLSMResultBestWords@1$kLSMTextApplySpamHeuristics@4$kLSMTextPreserveAcronyms@2$kLSMTextPreserveCase@1$'''
misc.update({'kLSMAlgorithmDense': b'LSMAlgorithmDense'.decode("utf-8"), 'kLSMPrecisionFloat': b'LSMPrecisionFloat'.decode("utf-8"), 'kLSMSweepCutoffKey': b'LSMSweepCutoff'.decode("utf-8"), 'kLSMAlgorithmSparse': b'LSMAlgorithmSparse'.decode("utf-8"), 'kLSMDimensionKey': b'LSMDimension'.decode("utf-8"), 'kLSMAlgorithmKey': b'LSMAlgorithm'.decode("utf-8"), 'kLSMPrecisionKey': b'LSMPrecision'.decode("utf-8"), 'kLSMPrecisionDouble': b'LSMPrecisionDouble'.decode("utf-8"), 'kLSMSweepAgeKey': b'LSMSweepAge'.decode("utf-8"), 'kLSMIterationsKey': b'LSMIterations'.decode("utf-8")})
functions={'LSMMapGetCategoryCount': (sel32or64(b'l^{__LSMMap=}', b'q^{__LSMMap=}'),), 'LSMMapAddTextWithWeight': (sel32or64(b'l^{__LSMMap=}^{__LSMText=}If', b'i^{__LSMMap=}^{__LSMText=}If'),), 'LSMTextAddToken': (sel32or64(b'l^{__LSMText=}^{__CFData=}', b'i^{__LSMText=}^{__CFData=}'),), 'LSMMapSetStopWords': (sel32or64(b'l^{__LSMMap=}^{__LSMText=}', b'i^{__LSMMap=}^{__LSMText=}'),), 'LSMTextGetTypeID': (sel32or64(b'L', b'Q'),), 'LSMMapStartTraining': (sel32or64(b'l^{__LSMMap=}', b'i^{__LSMMap=}'),), 'LSMMapCompile': (sel32or64(b'l^{__LSMMap=}', b'i^{__LSMMap=}'),), 'LSMMapWriteToStream': (sel32or64(b'l^{__LSMMap=}^{__LSMText=}^{__CFWriteStream=}L', b'i^{__LSMMap=}^{__LSMText=}^{__CFWriteStream=}Q'),), 'LSMResultCopyWordCluster': (sel32or64(b'^{__CFArray=}^{__LSMResult=}l', b'^{__CFArray=}^{__LSMResult=}q'), '', {'retval': {'already_cfretained': True}}), 'LSMResultGetCount': (sel32or64(b'l^{__LSMResult=}', b'q^{__LSMResult=}'),), 'LSMResultGetCategory': (sel32or64(b'I^{__LSMResult=}l', b'I^{__LSMResult=}q'),), 'LSMMapCreate': (sel32or64(b'^{__LSMMap=}^{__CFAllocator=}L', b'^{__LSMMap=}^{__CFAllocator=}Q'), '', {'retval': {'already_cfretained': True}}), 'LSMResultGetTypeID': (sel32or64(b'L', b'Q'),), 'LSMResultCreate': (sel32or64(b'^{__LSMResult=}^{__CFAllocator=}^{__LSMMap=}^{__LSMText=}lL', b'^{__LSMResult=}^{__CFAllocator=}^{__LSMMap=}^{__LSMText=}qQ'), '', {'retval': {'already_cfretained': True}}), 'LSMResultCopyWord': (sel32or64(b'^{__CFString=}^{__LSMResult=}l', b'^{__CFString=}^{__LSMResult=}q'), '', {'retval': {'already_cfretained': True}}), 'LSMMapCreateClusters': (sel32or64(b'^{__CFArray=}^{__CFAllocator=}^{__LSMMap=}^{__CFArray=}lL', b'^{__CFArray=}^{__CFAllocator=}^{__LSMMap=}^{__CFArray=}qQ'), '', {'retval': {'already_cfretained': True}}), 'LSMMapApplyClusters': (sel32or64(b'l^{__LSMMap=}^{__CFArray=}', b'i^{__LSMMap=}^{__CFArray=}'),), 'LSMTextAddWords': (sel32or64(b'l^{__LSMText=}^{__CFString=}^{__CFLocale=}L', b'i^{__LSMText=}^{__CFString=}^{__CFLocale=}Q'),), 'LSMResultCopyTokenCluster': (sel32or64(b'^{__CFArray=}^{__LSMResult=}l', b'^{__CFArray=}^{__LSMResult=}q'), '', {'retval': {'already_cfretained': True}}), 'LSMMapAddText': (sel32or64(b'l^{__LSMMap=}^{__LSMText=}I', b'i^{__LSMMap=}^{__LSMText=}I'),), 'LSMTextCreate': (b'^{__LSMText=}^{__CFAllocator=}^{__LSMMap=}', '', {'retval': {'already_cfretained': True}}), 'LSMMapWriteToURL': (sel32or64(b'l^{__LSMMap=}^{__CFURL=}L', b'i^{__LSMMap=}^{__CFURL=}Q'),), 'LSMResultGetScore': (sel32or64(b'f^{__LSMResult=}l', b'f^{__LSMResult=}q'),), 'LSMMapCreateFromURL': (sel32or64(b'^{__LSMMap=}^{__CFAllocator=}^{__CFURL=}L', b'^{__LSMMap=}^{__CFAllocator=}^{__CFURL=}Q'), '', {'retval': {'already_cfretained': True}}), 'LSMMapSetProperties': (b'v^{__LSMMap=}^{__CFDictionary=}',), 'LSMResultCopyToken': (sel32or64(b'^{__CFData=}^{__LSMResult=}l', b'^{__CFData=}^{__LSMResult=}q'), '', {'retval': {'already_cfretained': True}}), 'LSMMapGetProperties': (b'^{__CFDictionary=}^{__LSMMap=}',), 'LSMMapAddCategory': (b'I^{__LSMMap=}',), 'LSMTextAddWord': (sel32or64(b'l^{__LSMText=}^{__CFString=}', b'i^{__LSMText=}^{__CFString=}'),), 'LSMMapGetTypeID': (sel32or64(b'L', b'Q'),)}
cftypes=[('LSMMapRef', b'^{__LSMMap=}', 'LSMMapGetTypeID', None), ('LSMResultRef', b'^{__LSMResult=}', 'LSMResultGetTypeID', None), ('LSMTextRef', b'^{__LSMText=}', 'LSMTextGetTypeID', None)]
expressions = {}

# END OF FILE
