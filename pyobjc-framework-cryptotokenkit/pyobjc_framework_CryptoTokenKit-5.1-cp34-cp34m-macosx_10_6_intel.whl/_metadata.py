# This file is generated by objective.metadata
#
# Last update: Sun Jun 11 11:15:38 2017

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
constants = '''$TKErrorDomain$'''
enums = '''$TKErrorAuthenticationFailed@-5$TKErrorCodeAuthenticationFailed@-5$TKErrorCodeAuthenticationNeeded@-9$TKErrorCodeBadParameter@-8$TKErrorCodeCanceledByUser@-4$TKErrorCodeCommunicationError@-2$TKErrorCodeCorruptedData@-3$TKErrorCodeNotImplemented@-1$TKErrorCodeObjectNotFound@-6$TKErrorCodeTokenNotFound@-7$TKErrorObjectNotFound@-6$TKErrorTokenNotFound@-7$TKSmartCardNoSlot@0$TKSmartCardPINCharsetAlphanumeric@1$TKSmartCardPINCharsetNumeric@0$TKSmartCardPINCharsetUpperAlphanumeric@2$TKSmartCardPINCompletionKey@2$TKSmartCardPINCompletionMaxLength@1$TKSmartCardPINCompletionTimeout@4$TKSmartCardPINConfirmationCurrent@2$TKSmartCardPINConfirmationNew@1$TKSmartCardPINConfirmationNone@0$TKSmartCardPINEncodingASCII@1$TKSmartCardPINEncodingBCD@2$TKSmartCardPINEncodingBinary@0$TKSmartCardPINJustificationLeft@0$TKSmartCardPINJustificationRight@1$TKSmartCardProtocolAny@65535$TKSmartCardProtocolNone@0$TKSmartCardProtocolT0@1$TKSmartCardProtocolT1@2$TKSmartCardProtocolT15@32768$TKSmartCardSlotEmpty@1$TKSmartCardSlotMuteCard@3$TKSmartCardSlotProbing@2$TKSmartCardSlotStateEmpty@1$TKSmartCardSlotStateMissing@0$TKSmartCardSlotStateMuteCard@3$TKSmartCardSlotStateProbing@2$TKSmartCardSlotStateValidCard@4$TKSmartCardSlotValidCard@4$TKTokenOperationDecryptData@3$TKTokenOperationNone@0$TKTokenOperationPerformKeyExchange@4$TKTokenOperationReadData@1$TKTokenOperationSignData@2$'''
misc.update({})
aliases = {'TKSmartCardNoSlot': 'TKSmartCardSlotStateMissing', 'TKSmartCardSlotMuteCard': 'TKSmartCardSlotStateMuteCard', 'TKSmartCardSlotEmpty': 'TKSmartCardSlotStateEmpty', 'TKSmartCardSlotValidCard': 'TKSmartCardSlotStateValidCard', 'TKSmartCardSlotProbing': 'TKSmartCardSlotStateProbing'}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'token:createSessionWithError:', {'arguments': {3: {'type': 'o^@'}}})
    r(b'NSObject', b'tokenDriver:createTokenForSmartCard:AID:error:', {'arguments': {5: {'type': 'o^@'}}})
    r(b'NSObject', b'tokenSession:beginAuthForOperation:constraint:error:', {'arguments': {5: {'type': 'o^@'}}})
    r(b'NSObject', b'tokenSession:decryptData:usingKey:algorithm:error:', {'arguments': {6: {'type': 'o^@'}}})
    r(b'NSObject', b'tokenSession:performKeyExchangeWithPublicKey:usingKey:algorithm:parameters:error:', {'arguments': {7: {'type': 'o^@'}}})
    r(b'NSObject', b'tokenSession:signData:usingKey:algorithm:error:', {'arguments': {6: {'type': 'o^@'}}})
    r(b'NSObject', b'tokenSession:supportsOperation:usingKey:algorithm:', {'retval': {'type': 'Z'}})
    r(b'TKSmartCard', b'beginSessionWithReply:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'Z'}, 2: {'type': b'@'}}}}}})
    r(b'TKSmartCard', b'inSessionWithError:executeBlock:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type_modifier': b'o'}, 3: {'callable': {'retval': {'type': b'Z'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'o^@'}}}}}})
    r(b'TKSmartCard', b'sendIns:p1:p2:data:le:reply:', {'arguments': {7: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'S'}, 3: {'type': b'@'}}}}}})
    r(b'TKSmartCard', b'sendIns:p1:p2:data:le:sw:error:', {'arguments': {7: {'type_modifier': b'o'}, 8: {'type_modifier': b'o'}}})
    r(b'TKSmartCard', b'sensitive', {'retval': {'type': b'Z'}})
    r(b'TKSmartCard', b'setSensitive:', {'arguments': {2: {'type': b'Z'}}})
    r(b'TKSmartCard', b'setUseExtendedLength:', {'arguments': {2: {'type': b'Z'}}})
    r(b'TKSmartCard', b'transmitRequest:reply:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'TKSmartCard', b'useExtendedLength', {'retval': {'type': b'Z'}})
    r(b'TKSmartCard', b'valid', {'retval': {'type': b'Z'}})
    r(b'TKSmartCardATR', b'initWithSource:', {'arguments': {2: {'callable': {'retval': {'type': b'i'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'TKSmartCardSlotManager', b'getSlotWithName:reply:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'TKSmartCardUserInteraction', b'cancel', {'retval': {'type': 'Z'}})
    r(b'TKSmartCardUserInteraction', b'runWithReply:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'Z'}, 2: {'type': b'@'}}}}}})
    r(b'TKSmartCardUserInteractionForConfirmation', b'result', {'retval': {'type': 'Z'}})
    r(b'TKSmartCardUserInteractionForConfirmation', b'setResult:', {'arguments': {2: {'type': 'Z'}}})
    r(b'TKTokenAuthOperation', b'finishWithError:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r(b'TKTokenKeyAlgorithm', b'isAlgorithm:', {'retval': {'type': 'Z'}})
    r(b'TKTokenKeyAlgorithm', b'supportsAlgorithm:', {'retval': {'type': 'Z'}})
    r(b'TKTokenKeychainContents', b'certificateForObjectID:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'TKTokenKeychainContents', b'keyForObjectID:error:', {'arguments': {3: {'type_modifier': b'o'}}})
    r(b'TKTokenKeychainKey', b'canDecrypt', {'retval': {'type': 'Z'}})
    r(b'TKTokenKeychainKey', b'canPerformKeyExchange', {'retval': {'type': 'Z'}})
    r(b'TKTokenKeychainKey', b'canSign', {'retval': {'type': 'Z'}})
    r(b'TKTokenKeychainKey', b'isSuitableForLogin', {'retval': {'type': 'Z'}})
    r(b'TKTokenKeychainKey', b'setCanDecrypt:', {'arguments': {2: {'type': 'Z'}}})
    r(b'TKTokenKeychainKey', b'setCanPerformKeyExchange:', {'arguments': {2: {'type': 'Z'}}})
    r(b'TKTokenKeychainKey', b'setCanSign:', {'arguments': {2: {'type': 'Z'}}})
    r(b'TKTokenKeychainKey', b'setSuitableForLogin:', {'arguments': {2: {'type': 'Z'}}})
    r(b'TKTokenWatcher', b'addRemovalHandler:forTokenID:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'TKTokenWatcher', b'initWithInsertionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'TKTokenWatcher', b'setInsertionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
