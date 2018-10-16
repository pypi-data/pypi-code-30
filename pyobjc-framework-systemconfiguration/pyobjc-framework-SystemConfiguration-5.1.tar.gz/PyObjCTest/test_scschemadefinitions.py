from PyObjCTools.TestSupport import *
from SystemConfiguration import *

class TestSCSchemaDefinitions (TestCase):
    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kSCEntNetIPSec, unicode)
        self.assertIsInstance(kSCEntNetSMB, unicode)
        self.assertIsInstance(kSCPropNetIPSecLocalIdentifier, unicode)
        self.assertIsInstance(kSCPropNetIPSecLocalIdentifierType, unicode)
        self.assertIsInstance(kSCPropNetIPSecAuthenticationMethod, unicode)
        self.assertIsInstance(kSCPropNetIPSecSharedSecret, unicode)
        self.assertIsInstance(kSCPropNetIPSecSharedSecretEncryption, unicode)
        self.assertIsInstance(kSCPropNetIPSecLocalCertificate, unicode)
        self.assertIsInstance(kSCValNetIPSecAuthenticationMethodSharedSecret, unicode)
        self.assertIsInstance(kSCValNetIPSecAuthenticationMethodCertificate, unicode)
        self.assertIsInstance(kSCValNetIPSecSharedSecretEncryptionKeychain, unicode)
        self.assertIsInstance(kSCValNetIPSecLocalIdentifierTypeKeyID, unicode)
        self.assertIsInstance(kSCPropNetModemAccessPointName, unicode)
        self.assertIsInstance(kSCPropNetModemConnectionPersonality, unicode)
        self.assertIsInstance(kSCPropNetModemDeviceContextID, unicode)
        self.assertIsInstance(kSCPropNetModemDeviceModel, unicode)
        self.assertIsInstance(kSCPropNetModemDeviceVendor, unicode)
        self.assertIsInstance(kSCValNetPPPAuthPasswordEncryptionToken, unicode)
        self.assertIsInstance(kSCPropNetSMBNetBIOSName, unicode)
        self.assertIsInstance(kSCPropNetSMBNetBIOSNodeType, unicode)
        self.assertIsInstance(kSCPropNetSMBNetBIOSScope, unicode)
        self.assertIsInstance(kSCPropNetSMBWINSAddresses, unicode)
        self.assertIsInstance(kSCPropNetSMBWorkgroup, unicode)
        self.assertIsInstance(kSCValNetSMBNetBIOSNodeTypeBroadcast, unicode)
        self.assertIsInstance(kSCValNetSMBNetBIOSNodeTypePeer, unicode)
        self.assertIsInstance(kSCValNetSMBNetBIOSNodeTypeMixed, unicode)
        self.assertIsInstance(kSCValNetSMBNetBIOSNodeTypeHybrid, unicode)

    @min_os_level('10.6')
    def testConstants10_5_missing(self):
        self.assertIsInstance(kSCValNetIPSecAuthenticationMethodHybrid, unicode)

    def testConstants(self):
        self.assertIsInstance(kSCResvLink, unicode)
        self.assertIsInstance(kSCResvInactive, unicode)
        self.assertIsInstance(kSCPropInterfaceName, unicode)
        self.assertIsInstance(kSCPropMACAddress, unicode)
        self.assertIsInstance(kSCPropUserDefinedName, unicode)
        self.assertIsInstance(kSCPropVersion, unicode)
        self.assertIsInstance(kSCPrefCurrentSet, unicode)
        self.assertIsInstance(kSCPrefNetworkServices, unicode)
        self.assertIsInstance(kSCPrefSets, unicode)
        self.assertIsInstance(kSCPrefSystem, unicode)
        self.assertIsInstance(kSCCompNetwork, unicode)
        self.assertIsInstance(kSCCompService, unicode)
        self.assertIsInstance(kSCCompGlobal, unicode)
        self.assertIsInstance(kSCCompHostNames, unicode)
        self.assertIsInstance(kSCCompInterface, unicode)
        self.assertIsInstance(kSCCompSystem, unicode)
        self.assertIsInstance(kSCCompUsers, unicode)
        self.assertIsInstance(kSCCompAnyRegex, unicode)
        self.assertIsInstance(kSCEntNetAirPort, unicode)
        self.assertIsInstance(kSCEntNetAppleTalk, unicode)
        self.assertIsInstance(kSCEntNetDHCP, unicode)
        self.assertIsInstance(kSCEntNetDNS, unicode)
        self.assertIsInstance(kSCEntNetEthernet, unicode)
        self.assertIsInstance(kSCEntNetFireWire, unicode)
        self.assertIsInstance(kSCEntNetInterface, unicode)
        self.assertIsInstance(kSCEntNetIPv4, unicode)
        self.assertIsInstance(kSCEntNetIPv6, unicode)
        self.assertIsInstance(kSCEntNetL2TP, unicode)
        self.assertIsInstance(kSCEntNetLink, unicode)
        self.assertIsInstance(kSCEntNetModem, unicode)
        self.assertIsInstance(kSCEntNetNetInfo, unicode)
        self.assertIsInstance(kSCEntNetPPP, unicode)
        self.assertIsInstance(kSCEntNetPPPoE, unicode)
        self.assertIsInstance(kSCEntNetPPPSerial, unicode)
        self.assertIsInstance(kSCEntNetPPTP, unicode)
        self.assertIsInstance(kSCEntNetProxies, unicode)
        self.assertIsInstance(kSCEntNet6to4, unicode)
        self.assertIsInstance(kSCPropNetOverridePrimary, unicode)
        self.assertIsInstance(kSCPropNetServiceOrder, unicode)
        self.assertIsInstance(kSCPropNetPPPOverridePrimary, unicode)
        self.assertIsInstance(kSCPropNetInterfaces, unicode)
        self.assertIsInstance(kSCPropNetLocalHostName, unicode)
        self.assertIsInstance(kSCPropNetAirPortAllowNetCreation, unicode)
        self.assertIsInstance(kSCPropNetAirPortAuthPassword, unicode)
        self.assertIsInstance(kSCPropNetAirPortAuthPasswordEncryption, unicode)
        self.assertIsInstance(kSCPropNetAirPortJoinMode, unicode)
        self.assertIsInstance(kSCPropNetAirPortPowerEnabled, unicode)
        self.assertIsInstance(kSCPropNetAirPortPreferredNetwork, unicode)
        self.assertIsInstance(kSCPropNetAirPortSavePasswords, unicode)
        self.assertIsInstance(kSCValNetAirPortJoinModeAutomatic, unicode)
        self.assertIsInstance(kSCValNetAirPortJoinModePreferred, unicode)
        self.assertIsInstance(kSCValNetAirPortJoinModeRanked, unicode)
        self.assertIsInstance(kSCValNetAirPortJoinModeRecent, unicode)
        self.assertIsInstance(kSCValNetAirPortJoinModeStrongest, unicode)
        self.assertIsInstance(kSCValNetAirPortAuthPasswordEncryptionKeychain, unicode)
        self.assertIsInstance(kSCPropNetDNSDomainName, unicode)
        self.assertIsInstance(kSCPropNetDNSOptions, unicode)
        self.assertIsInstance(kSCPropNetDNSSearchDomains, unicode)
        self.assertIsInstance(kSCPropNetDNSSearchOrder, unicode)
        self.assertIsInstance(kSCPropNetDNSServerAddresses, unicode)
        self.assertIsInstance(kSCPropNetDNSServerPort, unicode)
        self.assertIsInstance(kSCPropNetDNSServerTimeout, unicode)
        self.assertIsInstance(kSCPropNetDNSSortList, unicode)
        self.assertIsInstance(kSCPropNetDNSSupplementalMatchDomains, unicode)
        self.assertIsInstance(kSCPropNetDNSSupplementalMatchOrders, unicode)
        self.assertIsInstance(kSCPropNetEthernetMediaSubType, unicode)
        self.assertIsInstance(kSCPropNetEthernetMediaOptions, unicode)
        self.assertIsInstance(kSCPropNetEthernetMTU, unicode)
        self.assertIsInstance(kSCPropNetInterfaceDeviceName, unicode)
        self.assertIsInstance(kSCPropNetInterfaceHardware, unicode)
        self.assertIsInstance(kSCPropNetInterfaceType, unicode)
        self.assertIsInstance(kSCPropNetInterfaceSubType, unicode)
        self.assertIsInstance(kSCPropNetInterfaceSupportsModemOnHold, unicode)
        self.assertIsInstance(kSCValNetInterfaceTypeEthernet, unicode)
        self.assertIsInstance(kSCValNetInterfaceTypeFireWire, unicode)
        self.assertIsInstance(kSCValNetInterfaceTypePPP, unicode)
        self.assertIsInstance(kSCValNetInterfaceType6to4, unicode)
        self.assertIsInstance(kSCValNetInterfaceSubTypePPPoE, unicode)
        self.assertIsInstance(kSCValNetInterfaceSubTypePPPSerial, unicode)
        self.assertIsInstance(kSCValNetInterfaceSubTypePPTP, unicode)
        self.assertIsInstance(kSCValNetInterfaceSubTypeL2TP, unicode)
        self.assertIsInstance(kSCPropNetIPv4Addresses, unicode)
        self.assertIsInstance(kSCPropNetIPv4ConfigMethod, unicode)
        self.assertIsInstance(kSCPropNetIPv4DHCPClientID, unicode)
        self.assertIsInstance(kSCPropNetIPv4Router, unicode)
        self.assertIsInstance(kSCPropNetIPv4SubnetMasks, unicode)
        self.assertIsInstance(kSCPropNetIPv4DestAddresses, unicode)
        self.assertIsInstance(kSCPropNetIPv4BroadcastAddresses, unicode)
        self.assertIsInstance(kSCValNetIPv4ConfigMethodBOOTP, unicode)
        self.assertIsInstance(kSCValNetIPv4ConfigMethodDHCP, unicode)
        self.assertIsInstance(kSCValNetIPv4ConfigMethodINFORM, unicode)
        self.assertIsInstance(kSCValNetIPv4ConfigMethodLinkLocal, unicode)
        self.assertIsInstance(kSCValNetIPv4ConfigMethodManual, unicode)
        self.assertIsInstance(kSCValNetIPv4ConfigMethodPPP, unicode)
        self.assertIsInstance(kSCPropNetIPv6Addresses, unicode)
        self.assertIsInstance(kSCPropNetIPv6ConfigMethod, unicode)
        self.assertIsInstance(kSCPropNetIPv6DestAddresses, unicode)
        self.assertIsInstance(kSCPropNetIPv6Flags, unicode)
        self.assertIsInstance(kSCPropNetIPv6PrefixLength, unicode)
        self.assertIsInstance(kSCPropNetIPv6Router, unicode)
        self.assertIsInstance(kSCValNetIPv6ConfigMethodAutomatic, unicode)
        self.assertIsInstance(kSCValNetIPv6ConfigMethodManual, unicode)
        self.assertIsInstance(kSCValNetIPv6ConfigMethodRouterAdvertisement, unicode)
        self.assertIsInstance(kSCValNetIPv6ConfigMethod6to4, unicode)
        self.assertIsInstance(kSCPropNet6to4Relay, unicode)
        self.assertIsInstance(kSCPropNetLinkActive, unicode)
        self.assertIsInstance(kSCPropNetLinkDetaching, unicode)
        self.assertIsInstance(kSCPropNetModemConnectionScript, unicode)
        self.assertIsInstance(kSCPropNetModemConnectSpeed, unicode)
        self.assertIsInstance(kSCPropNetModemDataCompression, unicode)
        self.assertIsInstance(kSCPropNetModemDialMode, unicode)
        self.assertIsInstance(kSCPropNetModemErrorCorrection, unicode)
        self.assertIsInstance(kSCPropNetModemHoldCallWaitingAudibleAlert, unicode)
        self.assertIsInstance(kSCPropNetModemHoldDisconnectOnAnswer, unicode)
        self.assertIsInstance(kSCPropNetModemHoldEnabled, unicode)
        self.assertIsInstance(kSCPropNetModemHoldReminder, unicode)
        self.assertIsInstance(kSCPropNetModemHoldReminderTime, unicode)
        self.assertIsInstance(kSCPropNetModemNote, unicode)
        self.assertIsInstance(kSCPropNetModemPulseDial, unicode)
        self.assertIsInstance(kSCPropNetModemSpeaker, unicode)
        self.assertIsInstance(kSCPropNetModemSpeed, unicode)
        self.assertIsInstance(kSCValNetModemDialModeIgnoreDialTone, unicode)
        self.assertIsInstance(kSCValNetModemDialModeManual, unicode)
        self.assertIsInstance(kSCValNetModemDialModeWaitForDialTone, unicode)
        self.assertIsInstance(kSCPropNetPPPACSPEnabled, unicode)
        self.assertIsInstance(kSCPropNetPPPConnectTime, unicode)
        self.assertIsInstance(kSCPropNetPPPDeviceLastCause, unicode)
        self.assertIsInstance(kSCPropNetPPPDialOnDemand, unicode)
        self.assertIsInstance(kSCPropNetPPPDisconnectOnFastUserSwitch, unicode)
        self.assertIsInstance(kSCPropNetPPPDisconnectOnIdle, unicode)
        self.assertIsInstance(kSCPropNetPPPDisconnectOnIdleTimer, unicode)
        self.assertIsInstance(kSCPropNetPPPDisconnectOnLogout, unicode)
        self.assertIsInstance(kSCPropNetPPPDisconnectOnSleep, unicode)
        self.assertIsInstance(kSCPropNetPPPDisconnectTime, unicode)
        self.assertIsInstance(kSCPropNetPPPIdleReminderTimer, unicode)
        self.assertIsInstance(kSCPropNetPPPIdleReminder, unicode)
        self.assertIsInstance(kSCPropNetPPPLastCause, unicode)
        self.assertIsInstance(kSCPropNetPPPLogfile, unicode)
        self.assertIsInstance(kSCPropNetPPPPlugins, unicode)
        self.assertIsInstance(kSCPropNetPPPRetryConnectTime, unicode)
        self.assertIsInstance(kSCPropNetPPPSessionTimer, unicode)
        self.assertIsInstance(kSCPropNetPPPStatus, unicode)
        self.assertIsInstance(kSCPropNetPPPUseSessionTimer, unicode)
        self.assertIsInstance(kSCPropNetPPPVerboseLogging, unicode)
        self.assertIsInstance(kSCPropNetPPPAuthEAPPlugins, unicode)
        self.assertIsInstance(kSCPropNetPPPAuthName, unicode)
        self.assertIsInstance(kSCPropNetPPPAuthPassword, unicode)
        self.assertIsInstance(kSCPropNetPPPAuthPasswordEncryption, unicode)
        self.assertIsInstance(kSCPropNetPPPAuthPrompt, unicode)
        self.assertIsInstance(kSCPropNetPPPAuthProtocol, unicode)
        self.assertIsInstance(kSCValNetPPPAuthPasswordEncryptionKeychain, unicode)
        self.assertIsInstance(kSCValNetPPPAuthPromptBefore, unicode)
        self.assertIsInstance(kSCValNetPPPAuthPromptAfter, unicode)
        self.assertIsInstance(kSCValNetPPPAuthProtocolCHAP, unicode)
        self.assertIsInstance(kSCValNetPPPAuthProtocolEAP, unicode)
        self.assertIsInstance(kSCValNetPPPAuthProtocolMSCHAP1, unicode)
        self.assertIsInstance(kSCValNetPPPAuthProtocolMSCHAP2, unicode)
        self.assertIsInstance(kSCValNetPPPAuthProtocolPAP, unicode)
        self.assertIsInstance(kSCPropNetPPPCommAlternateRemoteAddress, unicode)
        self.assertIsInstance(kSCPropNetPPPCommConnectDelay, unicode)
        self.assertIsInstance(kSCPropNetPPPCommDisplayTerminalWindow, unicode)
        self.assertIsInstance(kSCPropNetPPPCommRedialCount, unicode)
        self.assertIsInstance(kSCPropNetPPPCommRedialEnabled, unicode)
        self.assertIsInstance(kSCPropNetPPPCommRedialInterval, unicode)
        self.assertIsInstance(kSCPropNetPPPCommRemoteAddress, unicode)
        self.assertIsInstance(kSCPropNetPPPCommTerminalScript, unicode)
        self.assertIsInstance(kSCPropNetPPPCommUseTerminalScript, unicode)
        self.assertIsInstance(kSCPropNetPPPCCPEnabled, unicode)
        self.assertIsInstance(kSCPropNetPPPCCPMPPE40Enabled, unicode)
        self.assertIsInstance(kSCPropNetPPPCCPMPPE128Enabled, unicode)
        self.assertIsInstance(kSCPropNetPPPIPCPCompressionVJ, unicode)
        self.assertIsInstance(kSCPropNetPPPIPCPUsePeerDNS, unicode)
        self.assertIsInstance(kSCPropNetPPPLCPEchoEnabled, unicode)
        self.assertIsInstance(kSCPropNetPPPLCPEchoFailure, unicode)
        self.assertIsInstance(kSCPropNetPPPLCPEchoInterval, unicode)
        self.assertIsInstance(kSCPropNetPPPLCPCompressionACField, unicode)
        self.assertIsInstance(kSCPropNetPPPLCPCompressionPField, unicode)
        self.assertIsInstance(kSCPropNetPPPLCPMRU, unicode)
        self.assertIsInstance(kSCPropNetPPPLCPMTU, unicode)
        self.assertIsInstance(kSCPropNetPPPLCPReceiveACCM, unicode)
        self.assertIsInstance(kSCPropNetPPPLCPTransmitACCM, unicode)
        self.assertIsInstance(kSCPropNetL2TPIPSecSharedSecret, unicode)
        self.assertIsInstance(kSCPropNetL2TPIPSecSharedSecretEncryption, unicode)
        self.assertIsInstance(kSCPropNetL2TPTransport, unicode)
        self.assertIsInstance(kSCValNetL2TPIPSecSharedSecretEncryptionKeychain, unicode)
        self.assertIsInstance(kSCValNetL2TPTransportIP, unicode)
        self.assertIsInstance(kSCValNetL2TPTransportIPSec, unicode)
        self.assertIsInstance(kSCPropNetProxiesExceptionsList, unicode)
        self.assertIsInstance(kSCPropNetProxiesExcludeSimpleHostnames, unicode)
        self.assertIsInstance(kSCPropNetProxiesFTPEnable, unicode)
        self.assertIsInstance(kSCPropNetProxiesFTPPassive, unicode)
        self.assertIsInstance(kSCPropNetProxiesFTPPort, unicode)
        self.assertIsInstance(kSCPropNetProxiesFTPProxy, unicode)
        self.assertIsInstance(kSCPropNetProxiesGopherEnable, unicode)
        self.assertIsInstance(kSCPropNetProxiesGopherPort, unicode)
        self.assertIsInstance(kSCPropNetProxiesGopherProxy, unicode)
        self.assertIsInstance(kSCPropNetProxiesHTTPEnable, unicode)
        self.assertIsInstance(kSCPropNetProxiesHTTPPort, unicode)
        self.assertIsInstance(kSCPropNetProxiesHTTPProxy, unicode)
        self.assertIsInstance(kSCPropNetProxiesHTTPSEnable, unicode)
        self.assertIsInstance(kSCPropNetProxiesHTTPSPort, unicode)
        self.assertIsInstance(kSCPropNetProxiesHTTPSProxy, unicode)
        self.assertIsInstance(kSCPropNetProxiesRTSPEnable, unicode)
        self.assertIsInstance(kSCPropNetProxiesRTSPPort, unicode)
        self.assertIsInstance(kSCPropNetProxiesRTSPProxy, unicode)
        self.assertIsInstance(kSCPropNetProxiesSOCKSEnable, unicode)
        self.assertIsInstance(kSCPropNetProxiesSOCKSPort, unicode)
        self.assertIsInstance(kSCPropNetProxiesSOCKSProxy, unicode)
        self.assertIsInstance(kSCPropNetProxiesProxyAutoConfigEnable, unicode)
        self.assertIsInstance(kSCPropNetProxiesProxyAutoConfigURLString, unicode)
        self.assertIsInstance(kSCPropNetProxiesProxyAutoDiscoveryEnable, unicode)
        self.assertIsInstance(kSCEntUsersConsoleUser, unicode)
        self.assertIsInstance(kSCPropSystemComputerName, unicode)
        self.assertIsInstance(kSCPropSystemComputerNameEncoding, unicode)
        self.assertIsInstance(kSCDynamicStoreDomainFile, unicode)
        self.assertIsInstance(kSCDynamicStoreDomainPlugin, unicode)
        self.assertIsInstance(kSCDynamicStoreDomainSetup, unicode)
        self.assertIsInstance(kSCDynamicStoreDomainState, unicode)
        self.assertIsInstance(kSCDynamicStoreDomainPrefs, unicode)
        self.assertIsInstance(kSCDynamicStorePropSetupCurrentSet, unicode)
        self.assertIsInstance(kSCDynamicStorePropSetupLastUpdated, unicode)
        self.assertIsInstance(kSCDynamicStorePropNetInterfaces, unicode)
        self.assertIsInstance(kSCDynamicStorePropNetPrimaryInterface, unicode)
        self.assertIsInstance(kSCDynamicStorePropNetPrimaryService, unicode)
        self.assertIsInstance(kSCDynamicStorePropNetServiceIDs, unicode)
        self.assertIsInstance(kSCPropUsersConsoleUserName, unicode)
        self.assertIsInstance(kSCPropUsersConsoleUserUID, unicode)
        self.assertIsInstance(kSCPropUsersConsoleUserGID, unicode)

    @max_os_level('10.11')
    def testConstantsUpto10_12(self):
        self.assertIsInstance(kSCPropNetAppleTalkComputerName, unicode)
        self.assertIsInstance(kSCPropNetAppleTalkComputerNameEncoding, unicode)
        self.assertIsInstance(kSCPropNetAppleTalkConfigMethod, unicode)
        self.assertIsInstance(kSCPropNetAppleTalkDefaultZone, unicode)
        self.assertIsInstance(kSCPropNetAppleTalkNetworkID, unicode)
        self.assertIsInstance(kSCPropNetAppleTalkNetworkRange, unicode)
        self.assertIsInstance(kSCPropNetAppleTalkNodeID, unicode)
        self.assertIsInstance(kSCPropNetAppleTalkSeedNetworkRange, unicode)
        self.assertIsInstance(kSCPropNetAppleTalkSeedZones, unicode)
        self.assertIsInstance(kSCValNetAppleTalkConfigMethodNode, unicode)
        self.assertIsInstance(kSCValNetAppleTalkConfigMethodRouter, unicode)
        self.assertIsInstance(kSCValNetAppleTalkConfigMethodSeedRouter, unicode)
        self.assertIsInstance(kSCPropNetNetInfoBindingMethods, unicode)
        self.assertIsInstance(kSCPropNetNetInfoServerAddresses, unicode)
        self.assertIsInstance(kSCPropNetNetInfoServerTags, unicode)
        self.assertIsInstance(kSCPropNetNetInfoBroadcastServerTag, unicode)
        self.assertIsInstance(kSCValNetNetInfoBindingMethodsBroadcast, unicode)
        self.assertIsInstance(kSCValNetNetInfoBindingMethodsDHCP, unicode)
        self.assertIsInstance(kSCValNetNetInfoBindingMethodsManual, unicode)
        self.assertIsInstance(kSCValNetNetInfoDefaultServerTag, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kSCValNetInterfaceTypeIPSec, unicode)
        self.assertIsInstance(kSCPropNetIPSecConnectTime, unicode)
        self.assertIsInstance(kSCPropNetIPSecRemoteAddress, unicode)
        self.assertIsInstance(kSCPropNetIPSecStatus, unicode)
        self.assertIsInstance(kSCPropNetIPSecXAuthEnabled, unicode)
        self.assertIsInstance(kSCPropNetIPSecXAuthName, unicode)
        self.assertIsInstance(kSCPropNetIPSecXAuthPassword, unicode)
        self.assertIsInstance(kSCPropNetIPSecXAuthPasswordEncryption, unicode)
        self.assertIsInstance(kSCValNetIPSecXAuthPasswordEncryptionKeychain, unicode)
        self.assertIsInstance(kSCValNetIPSecXAuthPasswordEncryptionPrompt, unicode)
        self.assertIsInstance(kSCValNetIPv4ConfigMethodAutomatic, unicode)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(kSCValNetIPv6ConfigMethodLinkLocal, unicode)
        self.assertIsInstance(kSCPropNetProxiesProxyAutoConfigJavaScript, unicode)

if __name__ == "__main__":
    main()
