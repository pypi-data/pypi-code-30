# This file is generated by objective.metadata
#
# Last update: Fri May 25 17:45:37 2012

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
constants = '''$XGActionMonitorResultsOutputFilesKey$XGActionMonitorResultsOutputStreamsKey$XGConnectionKeyIsClosed$XGConnectionKeyIsOpened$XGConnectionKeyState$XGControllerWillDeallocNotification$XGFileStandardErrorPath$XGFileStandardOutputPath$XGJobSpecificationARTConditionsKey$XGJobSpecificationARTDataKey$XGJobSpecificationARTEqualKey$XGJobSpecificationARTMaximumKey$XGJobSpecificationARTMinimumKey$XGJobSpecificationARTSpecificationsKey$XGJobSpecificationApplicationIdentifierKey$XGJobSpecificationArgumentTypeKey$XGJobSpecificationArgumentsKey$XGJobSpecificationCommandKey$XGJobSpecificationDependsOnJobsKey$XGJobSpecificationDependsOnTasksKey$XGJobSpecificationEnvironmentKey$XGJobSpecificationFileDataKey$XGJobSpecificationGridIdentifierKey$XGJobSpecificationInputFileMapKey$XGJobSpecificationInputFilesKey$XGJobSpecificationInputStreamKey$XGJobSpecificationIsExecutableKey$XGJobSpecificationNameKey$XGJobSpecificationNotificationEmailKey$XGJobSpecificationPathIdentifierKey$XGJobSpecificationSchedulerHintsKey$XGJobSpecificationSchedulerParametersKey$XGJobSpecificationSubmissionIdentifierKey$XGJobSpecificationTaskPrototypeIdentifierKey$XGJobSpecificationTaskPrototypesKey$XGJobSpecificationTaskSpecificationsKey$XGJobSpecificationTypeKey$XGJobSpecificationTypeTaskListValue$'''
enums = '''$XGActionMonitorOutcomeFailure@2$XGActionMonitorOutcomeNone@0$XGActionMonitorOutcomeSuccess@1$XGAuthenticatorStateAuthenticated@2$XGAuthenticatorStateAuthenticating@1$XGAuthenticatorStateFailed@3$XGAuthenticatorStateUnauthenticated@0$XGConnectionStateClosed@0$XGConnectionStateClosing@3$XGConnectionStateOpen@2$XGConnectionStateOpening@1$XGFileTypeNone@0$XGFileTypeRegular@1$XGFileTypeStream@2$XGResourceActionDelete@5$XGResourceActionGetOutputFiles@10$XGResourceActionGetOutputStreams@9$XGResourceActionGetSpecification@11$XGResourceActionMakeDefault@7$XGResourceActionNone@0$XGResourceActionRename@6$XGResourceActionRestart@2$XGResourceActionResume@4$XGResourceActionStop@1$XGResourceActionSubmitJob@8$XGResourceActionSuspend@3$XGResourceStateAvailable@4$XGResourceStateCanceled@12$XGResourceStateConnecting@2$XGResourceStateFailed@13$XGResourceStateFinished@14$XGResourceStateOffline@1$XGResourceStatePending@6$XGResourceStateRunning@9$XGResourceStateStagingIn@8$XGResourceStateStagingOut@11$XGResourceStateStarting@7$XGResourceStateSuspended@10$XGResourceStateUnavailable@3$XGResourceStateUninitialized@0$XGResourceStateWorking@5$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'XGActionMonitor', b'actionDidFail', {'retval': {'type': 'Z'}})
    r(b'XGActionMonitor', b'actionDidSucceed', {'retval': {'type': 'Z'}})
    r(b'XGConnection', b'isClosed', {'retval': {'type': 'Z'}})
    r(b'XGConnection', b'isOpened', {'retval': {'type': 'Z'}})
    r(b'XGFileDownload', b'setDestination:allowOverwrite:', {'arguments': {3: {'type': 'Z'}}})
    r(b'XGGrid', b'isDefault', {'retval': {'type': 'Z'}})
    r(b'XGResource', b'isUpdated', {'retval': {'type': 'Z'}})
    r(b'XGResource', b'isUpdating', {'retval': {'type': 'Z'}})
finally:
    objc._updatingMetadata(False)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'authenticatorDidAuthenticate:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'authenticatorDidNotAuthenticate:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'connectionDidClose:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'connectionDidNotOpen:withError:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'connectionDidOpen:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'fileDownload:decideDestinationWithSuggestedPath:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'fileDownload:didCreateDestination:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'fileDownload:didFailWithError:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'fileDownload:didReceiveAttributes:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'fileDownload:didReceiveData:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'fileDownloadDidBegin:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'fileDownloadDidFinish:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
finally:
    objc._updatingMetadata(False)
protocols={'XGAuthenticatorDelegate': objc.informal_protocol('XGAuthenticatorDelegate', [objc.selector(None, b'authenticatorDidNotAuthenticate:', b'v@:@', isRequired=False), objc.selector(None, b'authenticatorDidAuthenticate:', b'v@:@', isRequired=False)]), 'XGFileDownloadDelegate': objc.informal_protocol('XGFileDownloadDelegate', [objc.selector(None, b'fileDownload:decideDestinationWithSuggestedPath:', b'v@:@@', isRequired=False), objc.selector(None, b'fileDownload:didReceiveAttributes:', b'v@:@@', isRequired=False), objc.selector(None, b'fileDownloadDidFinish:', b'v@:@', isRequired=False), objc.selector(None, b'fileDownload:didFailWithError:', b'v@:@@', isRequired=False), objc.selector(None, b'fileDownload:didReceiveData:', b'v@:@@', isRequired=False), objc.selector(None, b'fileDownloadDidBegin:', b'v@:@', isRequired=False), objc.selector(None, b'fileDownload:didCreateDestination:', b'v@:@@', isRequired=False)]), 'XGConnectionDelegate': objc.informal_protocol('XGConnectionDelegate', [objc.selector(None, b'connectionDidOpen:', b'v@:@', isRequired=False), objc.selector(None, b'connectionDidClose:', b'v@:@', isRequired=False), objc.selector(None, b'connectionDidNotOpen:withError:', b'v@:@@', isRequired=False)])}
expressions = {}

# END OF FILE
