# This file is generated by objective.metadata
#
# Last update: Mon Oct 24 13:37:21 2016

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
misc.update({'LSItemInfoRecord': objc.createStructType('LSItemInfoRecord', sel32or64(b'{LSItemInfoRecord=LLL^{__CFString=}^{__CFString=}L}', b'{LSItemInfoRecord=III^{__CFString=}}'), sel32or64(['flags', 'filetype', 'creator', 'extension', 'iconFileName', 'kindID'], ['flags', 'filetype', 'creator', 'extension']), None, 2), 'LSLaunchFSRefSpec': objc.createStructType('LSLaunchFSRefSpec', sel32or64(b'{LSLaunchFSRefSpec=^{FSRef=[80C]}L^{FSRef=[80C]}^{AEDesc=L^^{OpaqueAEDataStorageType=}}L^v}', b'{LSLaunchFSRefSpec=^{FSRef=[80C]}Q^{FSRef=[80C]}^{AEDesc=I^^{OpaqueAEDataStorageType=}}I^v}'), ['appRef', 'numDocs', 'itemRefs', 'passThruParams', 'launchFlags', 'asyncRefCon'], None, 2), 'LSApplicationParameters': objc.createStructType('LSApplicationParameters', sel32or64(b'{LSApplicationParameters=lL^{FSRef=[80C]}^v^{__CFDictionary=}^{__CFArray=}^{AEDesc=L^^{OpaqueAEDataStorageType=}}}', b'{LSApplicationParameters=qI^{FSRef=[80C]}^v^{__CFDictionary=}^{__CFArray=}^{AEDesc=I^^{OpaqueAEDataStorageType=}}}'), ['version', 'flags', 'application', 'asyncLaunchRefCon', 'environment', 'argv', 'initialEvent']), 'LSLaunchURLSpec': objc.createStructType('LSLaunchURLSpec', sel32or64(b'{LSLaunchURLSpec=^{__CFURL=}^{__CFArray=}^{AEDesc=L^^{OpaqueAEDataStorageType=}}L^v}', b'{LSLaunchURLSpec=^{__CFURL=}^{__CFArray=}^{AEDesc=I^^{OpaqueAEDataStorageType=}}I^v}'), ['appURL', 'itemURLs', 'passThruParams', 'launchFlags', 'asyncRefCon'], None, 2)})
constants = '''$kLSItemContentType@^{__CFString=}$kLSItemDisplayKind@^{__CFString=}$kLSItemDisplayName@^{__CFString=}$kLSItemExtension@^{__CFString=}$kLSItemExtensionIsHidden@^{__CFString=}$kLSItemFileCreator@^{__CFString=}$kLSItemFileType@^{__CFString=}$kLSItemIsInvisible@^{__CFString=}$kLSItemQuarantineProperties@^{__CFString=}$kLSItemRoleHandlerDisplayName@^{__CFString=}$kLSQuarantineAgentBundleIdentifierKey@^{__CFString=}$kLSQuarantineAgentNameKey@^{__CFString=}$kLSQuarantineDataURLKey@^{__CFString=}$kLSQuarantineOriginURLKey@^{__CFString=}$kLSQuarantineTimeStampKey@^{__CFString=}$kLSQuarantineTypeCalendarEventAttachment@^{__CFString=}$kLSQuarantineTypeEmailAttachment@^{__CFString=}$kLSQuarantineTypeInstantMessageAttachment@^{__CFString=}$kLSQuarantineTypeKey@^{__CFString=}$kLSQuarantineTypeOtherAttachment@^{__CFString=}$kLSQuarantineTypeOtherDownload@^{__CFString=}$kLSQuarantineTypeWebDownload@^{__CFString=}$kLSSharedFileListFavoriteItems@^{__CFString=}$kLSSharedFileListFavoriteVolumes@^{__CFString=}$kLSSharedFileListGlobalLoginItems@^{__CFString=}$kLSSharedFileListItemBeforeFirst@==^{OpaqueLSSharedFileListItemRef=}$kLSSharedFileListItemHidden@^{__CFString=}$kLSSharedFileListItemLast@==^{OpaqueLSSharedFileListItemRef=}$kLSSharedFileListLoginItemHidden@^{__CFString=}$kLSSharedFileListRecentApplicationItems@^{__CFString=}$kLSSharedFileListRecentDocumentItems@^{__CFString=}$kLSSharedFileListRecentItemsMaxAmount@^{__CFString=}$kLSSharedFileListRecentServerItems@^{__CFString=}$kLSSharedFileListSessionLoginItems@^{__CFString=}$kLSSharedFileListVolumesComputerVisible@^{__CFString=}$kLSSharedFileListVolumesIDiskVisible@^{__CFString=}$kLSSharedFileListVolumesNetworkVisible@^{__CFString=}$kUTExportedTypeDeclarationsKey@^{__CFString=}$kUTImportedTypeDeclarationsKey@^{__CFString=}$kUTTagClassFilenameExtension@^{__CFString=}$kUTTagClassMIMEType@^{__CFString=}$kUTTagClassNSPboardType@^{__CFString=}$kUTTagClassOSType@^{__CFString=}$kUTType3DContent@^{__CFString=}$kUTTypeAVIMovie@^{__CFString=}$kUTTypeAliasFile@^{__CFString=}$kUTTypeAliasRecord@^{__CFString=}$kUTTypeAppleICNS@^{__CFString=}$kUTTypeAppleProtectedMPEG4Audio@^{__CFString=}$kUTTypeAppleProtectedMPEG4Video@^{__CFString=}$kUTTypeAppleScript@^{__CFString=}$kUTTypeApplication@^{__CFString=}$kUTTypeApplicationBundle@^{__CFString=}$kUTTypeApplicationFile@^{__CFString=}$kUTTypeArchive@^{__CFString=}$kUTTypeAssemblyLanguageSource@^{__CFString=}$kUTTypeAudio@^{__CFString=}$kUTTypeAudioInterchangeFileFormat@^{__CFString=}$kUTTypeAudiovisualContent@^{__CFString=}$kUTTypeBMP@^{__CFString=}$kUTTypeBinaryPropertyList@^{__CFString=}$kUTTypeBookmark@^{__CFString=}$kUTTypeBundle@^{__CFString=}$kUTTypeBzip2Archive@^{__CFString=}$kUTTypeCHeader@^{__CFString=}$kUTTypeCPlusPlusHeader@^{__CFString=}$kUTTypeCPlusPlusSource@^{__CFString=}$kUTTypeCSource@^{__CFString=}$kUTTypeCalendarEvent@^{__CFString=}$kUTTypeCommaSeparatedText@^{__CFString=}$kUTTypeCompositeContent@^{__CFString=}$kUTTypeConformsToKey@^{__CFString=}$kUTTypeContact@^{__CFString=}$kUTTypeContent@^{__CFString=}$kUTTypeData@^{__CFString=}$kUTTypeDatabase@^{__CFString=}$kUTTypeDelimitedText@^{__CFString=}$kUTTypeDescriptionKey@^{__CFString=}$kUTTypeDirectory@^{__CFString=}$kUTTypeDiskImage@^{__CFString=}$kUTTypeElectronicPublication@^{__CFString=}$kUTTypeEmailMessage@^{__CFString=}$kUTTypeExecutable@^{__CFString=}$kUTTypeFileURL@^{__CFString=}$kUTTypeFlatRTFD@^{__CFString=}$kUTTypeFolder@^{__CFString=}$kUTTypeFont@^{__CFString=}$kUTTypeFramework@^{__CFString=}$kUTTypeGIF@^{__CFString=}$kUTTypeGNUZipArchive@^{__CFString=}$kUTTypeHTML@^{__CFString=}$kUTTypeICO@^{__CFString=}$kUTTypeIconFileKey@^{__CFString=}$kUTTypeIdentifierKey@^{__CFString=}$kUTTypeImage@^{__CFString=}$kUTTypeInkText@^{__CFString=}$kUTTypeInternetLocation@^{__CFString=}$kUTTypeItem@^{__CFString=}$kUTTypeJPEG@^{__CFString=}$kUTTypeJPEG2000@^{__CFString=}$kUTTypeJSON@^{__CFString=}$kUTTypeJavaArchive@^{__CFString=}$kUTTypeJavaClass@^{__CFString=}$kUTTypeJavaScript@^{__CFString=}$kUTTypeJavaSource@^{__CFString=}$kUTTypeLog@^{__CFString=}$kUTTypeM3UPlaylist@^{__CFString=}$kUTTypeMIDIAudio@^{__CFString=}$kUTTypeMP3@^{__CFString=}$kUTTypeMPEG@^{__CFString=}$kUTTypeMPEG2TransportStream@^{__CFString=}$kUTTypeMPEG2Video@^{__CFString=}$kUTTypeMPEG4@^{__CFString=}$kUTTypeMPEG4Audio@^{__CFString=}$kUTTypeMessage@^{__CFString=}$kUTTypeMountPoint@^{__CFString=}$kUTTypeMovie@^{__CFString=}$kUTTypeOSAScript@^{__CFString=}$kUTTypeOSAScriptBundle@^{__CFString=}$kUTTypeObjectiveCPlusPlusSource@^{__CFString=}$kUTTypeObjectiveCSource@^{__CFString=}$kUTTypePDF@^{__CFString=}$kUTTypePHPScript@^{__CFString=}$kUTTypePICT@^{__CFString=}$kUTTypePKCS12@^{__CFString=}$kUTTypePNG@^{__CFString=}$kUTTypePackage@^{__CFString=}$kUTTypePerlScript@^{__CFString=}$kUTTypePlainText@^{__CFString=}$kUTTypePlaylist@^{__CFString=}$kUTTypePluginBundle@^{__CFString=}$kUTTypePresentation@^{__CFString=}$kUTTypePropertyList@^{__CFString=}$kUTTypePythonScript@^{__CFString=}$kUTTypeQuickLookGenerator@^{__CFString=}$kUTTypeQuickTimeImage@^{__CFString=}$kUTTypeQuickTimeMovie@^{__CFString=}$kUTTypeRTF@^{__CFString=}$kUTTypeRTFD@^{__CFString=}$kUTTypeRawImage@^{__CFString=}$kUTTypeReferenceURLKey@^{__CFString=}$kUTTypeResolvable@^{__CFString=}$kUTTypeRubyScript@^{__CFString=}$kUTTypeScalableVectorGraphics@^{__CFString=}$kUTTypeScript@^{__CFString=}$kUTTypeShellScript@^{__CFString=}$kUTTypeSourceCode@^{__CFString=}$kUTTypeSpotlightImporter@^{__CFString=}$kUTTypeSpreadsheet@^{__CFString=}$kUTTypeSwiftSource$kUTTypeSymLink@^{__CFString=}$kUTTypeSystemPreferencesPane@^{__CFString=}$kUTTypeTIFF@^{__CFString=}$kUTTypeTXNTextAndMultimediaData@^{__CFString=}$kUTTypeTabSeparatedText@^{__CFString=}$kUTTypeTagSpecificationKey@^{__CFString=}$kUTTypeText@^{__CFString=}$kUTTypeToDoItem@^{__CFString=}$kUTTypeURL@^{__CFString=}$kUTTypeURLBookmarkData@^{__CFString=}$kUTTypeUTF16ExternalPlainText@^{__CFString=}$kUTTypeUTF16PlainText@^{__CFString=}$kUTTypeUTF8PlainText@^{__CFString=}$kUTTypeUTF8TabSeparatedText@^{__CFString=}$kUTTypeUnixExecutable@^{__CFString=}$kUTTypeVCard@^{__CFString=}$kUTTypeVersionKey@^{__CFString=}$kUTTypeVideo@^{__CFString=}$kUTTypeVolume@^{__CFString=}$kUTTypeWaveformAudio@^{__CFString=}$kUTTypeWebArchive@^{__CFString=}$kUTTypeWindowsExecutable@^{__CFString=}$kUTTypeX509Certificate@^{__CFString=}$kUTTypeXML@^{__CFString=}$kUTTypeXMLPropertyList@^{__CFString=}$kUTTypeXPCService@^{__CFString=}$kUTTypeZipArchive@^{__CFString=}$'''
enums = '''$appleMenuFolderIconResource@-3982$controlPanelFolderIconResource@-3976$desktopIconResource@-3992$dropFolderIconResource@-3979$extensionsFolderIconResource@-3973$floppyIconResource@-3998$fontsFolderIconResource@-3968$fullTrashIconResource@-3984$genericApplicationIconResource@-3996$genericCDROMIconResource@-3987$genericDeskAccessoryIconResource@-3991$genericDocumentIconResource@-4000$genericEditionFileIconResource@-3989$genericExtensionIconResource@-16415$genericFileServerIconResource@-3972$genericFolderIconResource@-3999$genericHardDiskIconResource@-3995$genericMoverObjectIconResource@-3969$genericPreferencesIconResource@-3971$genericQueryDocumentIconResource@-16506$genericRAMDiskIconResource@-3988$genericStationeryIconResource@-3985$genericSuitcaseIconResource@-3970$kAFPServerIcon@1634103411$kAlertCautionBadgeIcon@1667392615$kAlertCautionIcon@1667331444$kAlertNoteIcon@1852798053$kAlertStopIcon@1937010544$kAliasBadgeIcon@1633838183$kAppearanceFolderIcon@1634758770$kAppleExtrasFolderIcon@1634040004$kAppleLogoIcon@1667330156$kAppleMenuFolderIcon@1634561653$kAppleMenuFolderIconResource@-3982$kAppleMenuIcon@1935765612$kAppleScriptBadgeIcon@1935897200$kAppleTalkIcon@1635019883$kAppleTalkZoneIcon@1635023470$kApplicationSupportFolderIcon@1634956656$kApplicationsFolderIcon@1634758771$kAssistantsFolderIcon@1634956484$kBackwardArrowIcon@1650553455$kBurningIcon@1651864174$kClipboardIcon@1129072976$kClippingPictureTypeIcon@1668051056$kClippingSoundTypeIcon@1668051059$kClippingTextTypeIcon@1668051060$kClippingUnknownTypeIcon@1668051061$kColorSyncFolderIcon@1886547814$kComputerIcon@1919905652$kConnectToIcon@1668178804$kContextualMenuItemsFolderIcon@1668116085$kControlPanelDisabledFolderIcon@1668575812$kControlPanelFolderIcon@1668575852$kControlPanelFolderIconResource@-3976$kControlStripModulesFolderIcon@1935963844$kDeleteAliasIcon@1684106345$kDesktopIcon@1684370283$kDesktopIconResource@-3992$kDocumentsFolderIcon@1685021555$kDropFolderIcon@1684172664$kDropFolderIconResource@-3979$kEjectMediaIcon@1701471587$kExtensionsDisabledFolderIcon@1702392900$kExtensionsFolderIcon@1702392942$kExtensionsFolderIconResource@-3973$kFTPServerIcon@1718906995$kFavoriteItemsIcon@1717663346$kFavoritesFolderIcon@1717663347$kFinderIcon@1179534418$kFloppyIconResource@-3998$kFontSuitcaseIcon@1179011404$kFontsFolderIcon@1718578804$kFontsFolderIconResource@-3968$kForwardArrowIcon@1717662319$kFullTrashIcon@1718907496$kFullTrashIconResource@-3984$kGenericApplicationIcon@1095782476$kGenericApplicationIconResource@-3996$kGenericCDROMIcon@1667523698$kGenericCDROMIconResource@-3987$kGenericComponentIcon@1953001063$kGenericControlPanelIcon@1095782467$kGenericControlStripModuleIcon@1935959414$kGenericDeskAccessoryIcon@1095782468$kGenericDeskAccessoryIconResource@-3991$kGenericDocumentIcon@1685021557$kGenericDocumentIconResource@-4000$kGenericEditionFileIcon@1701082214$kGenericEditionFileIconResource@-3989$kGenericExtensionIcon@1229867348$kGenericExtensionIconResource@-16415$kGenericFileServerIcon@1936881266$kGenericFileServerIconResource@-3972$kGenericFloppyIcon@1718382713$kGenericFolderIcon@1718379634$kGenericFolderIconResource@-3999$kGenericFontIcon@1717987692$kGenericFontScalerIcon@1935895666$kGenericHardDiskIcon@1751413611$kGenericHardDiskIconResource@-3995$kGenericIDiskIcon@1768190827$kGenericMoverObjectIcon@1836021362$kGenericMoverObjectIconResource@-3969$kGenericNetworkIcon@1735288180$kGenericPCCardIcon@1885564259$kGenericPreferencesIcon@1886545254$kGenericPreferencesIconResource@-3971$kGenericQueryDocumentIcon@1902473849$kGenericQueryDocumentIconResource@-16506$kGenericRAMDiskIcon@1918987620$kGenericRAMDiskIconResource@-3988$kGenericRemovableMediaIcon@1919774582$kGenericSharedLibaryIcon@1936223330$kGenericStationeryIcon@1935961955$kGenericStationeryIconResource@-3985$kGenericSuitcaseIcon@1937074548$kGenericSuitcaseIconResource@-3970$kGenericURLIcon@1735750252$kGenericWORMIcon@2003792493$kGenericWindowIcon@1735879022$kGridIcon@1735551332$kGroupIcon@1735554416$kGuestUserIcon@1735750514$kHTTPServerIcon@1752461427$kHelpFolderIcon@-999789456$kHelpIcon@1751477360$kHelpIconResource@-20271$kIPFileServerIcon@1769173622$kIconServicesCatalogInfoMask@531550$kIconServicesNoBadgeFlag@1$kIconServicesNormalUsageFlag@0$kIconServicesUpdateIfNeededFlag@2$kInternationResourcesIcon@1768319340$kInternationalResourcesIcon@1768319340$kInternetFolderIcon@1768846532$kInternetLocationAppleShareIcon@1768710502$kInternetLocationAppleTalkZoneIcon@1768710516$kInternetLocationFTPIcon@1768711796$kInternetLocationFileIcon@1768711785$kInternetLocationGenericIcon@1768712037$kInternetLocationHTTPIcon@1768712308$kInternetLocationMailIcon@1768713569$kInternetLocationNSLNeighborhoodIcon@1768713843$kInternetLocationNewsIcon@1768713847$kInternetPlugInFolderIcon@-999398028$kInternetSearchSitesFolderIcon@1769173862$kKeepArrangedIcon@1634889319$kKeyboardLayoutIcon@1801873772$kLSAcceptAllowLoginUI@2$kLSAcceptDefault@1$kLSAppDoesNotClaimTypeErr@-10820$kLSAppDoesNotSupportSchemeWarning@-10821$kLSAppInTrashErr@-10660$kLSApplicationNotFoundErr@-10814$kLSAttributeNotFoundErr@-10662$kLSAttributeNotSettableErr@-10663$kLSCannotSetInfoErr@-10823$kLSDataErr@-10817$kLSDataTooOldErr@-10816$kLSDataUnavailableErr@-10813$kLSExecutableIncorrectFormat@-10661$kLSHandlerOptionsDefault@0$kLSHandlerOptionsIgnoreCreator@1$kLSIncompatibleApplicationVersionErr@-10664$kLSIncompatibleSystemVersionErr@-10825$kLSInitializeDefaults@1$kLSItemInfoAppIsScriptable@2048$kLSItemInfoAppPrefersClassic@1024$kLSItemInfoAppPrefersNative@512$kLSItemInfoExtensionIsHidden@1048576$kLSItemInfoIsAliasFile@16$kLSItemInfoIsApplication@4$kLSItemInfoIsClassicApp@256$kLSItemInfoIsContainer@8$kLSItemInfoIsInvisible@64$kLSItemInfoIsNativeApp@128$kLSItemInfoIsPackage@2$kLSItemInfoIsPlainFile@1$kLSItemInfoIsSymlink@32$kLSItemInfoIsVolume@4096$kLSLaunchAndDisplayErrors@64$kLSLaunchAndHide@1048576$kLSLaunchAndHideOthers@2097152$kLSLaunchAndPrint@2$kLSLaunchAsync@65536$kLSLaunchDefaults@1$kLSLaunchDontAddToRecents@256$kLSLaunchDontSwitch@512$kLSLaunchHasUntrustedContents@4194304$kLSLaunchInClassic@262144$kLSLaunchInProgressErr@-10818$kLSLaunchInhibitBGOnly@128$kLSLaunchNewInstance@524288$kLSLaunchNoParams@2048$kLSLaunchReserved2@4$kLSLaunchReserved3@8$kLSLaunchReserved4@16$kLSLaunchReserved5@32$kLSLaunchStartClassic@131072$kLSMinCatInfoBitmap@6154$kLSMultipleSessionsNotSupportedErr@-10829$kLSNoClassicEnvironmentErr@-10828$kLSNoExecutableErr@-10827$kLSNoLaunchPermissionErr@-10826$kLSNoRegistrationInfoErr@-10824$kLSNoRosettaEnvironmentErr@-10665$kLSNotAnApplicationErr@-10811$kLSNotInitializedErr@-10812$kLSNotRegisteredErr@-10819$kLSRequestAllFlags@16$kLSRequestAllInfo@4294967295$kLSRequestAppTypeFlags@8$kLSRequestBasicFlagsOnly@4$kLSRequestExtension@1$kLSRequestExtensionFlagsOnly@64$kLSRequestIconAndKind@32$kLSRequestTypeCreator@2$kLSRolesAll@4294967295$kLSRolesEditor@4$kLSRolesNone@1$kLSRolesShell@8$kLSRolesViewer@2$kLSServerCommunicationErr@-10822$kLSSharedFileListDoNotMountVolumes@2$kLSSharedFileListNoUserInteraction@1$kLSUnknownCreator@0$kLSUnknownErr@-10810$kLSUnknownKindID@0$kLSUnknownType@0$kLSUnknownTypeErr@-10815$kLocalesFolderIcon@-999526557$kLockedBadgeIcon@1818387559$kLockedIcon@1819239275$kMacOSReadMeFolderIcon@1836020420$kMountedBadgeIcon@1835164775$kMountedFolderIcon@1835955300$kMountedFolderIconResource@-3977$kNoFilesIcon@1852205420$kNoFolderIcon@1852206180$kNoWriteIcon@1853321844$kOpenFolderIcon@1868983396$kOpenFolderIconResource@-3997$kOwnedFolderIcon@1870098020$kOwnedFolderIconResource@-3980$kOwnerIcon@1937077106$kPreferencesFolderIcon@1886545604$kPreferencesFolderIconResource@-3974$kPrintMonitorFolderIcon@1886547572$kPrintMonitorFolderIconResource@-3975$kPrinterDescriptionFolderIcon@1886413926$kPrinterDriverFolderIcon@-999263644$kPrivateFolderIcon@1886549606$kPrivateFolderIconResource@-3994$kProtectedApplicationFolderIcon@1885433968$kProtectedSystemFolderIcon@1886615923$kPublicFolderIcon@1886741094$kQuestionMarkIcon@1903519091$kRecentApplicationsFolderIcon@1918988400$kRecentDocumentsFolderIcon@1919184739$kRecentItemsIcon@1919118964$kRecentServersFolderIcon@1920168566$kRightContainerArrowIcon@1919115634$kScriptingAdditionsFolderIcon@-999070862$kScriptsFolderIcon@1935897284$kSharedBadgeIcon@1935828071$kSharedFolderIcon@1936221804$kSharedFolderIconResource@-3978$kSharedLibrariesFolderIcon@-999528094$kSharingPrivsNotApplicableIcon@1936223841$kSharingPrivsReadOnlyIcon@1936224879$kSharingPrivsReadWriteIcon@1936224887$kSharingPrivsUnknownIcon@1936225643$kSharingPrivsWritableIcon@2003986804$kShortcutIcon@1936224884$kShutdownItemsDisabledFolderIcon@1936221252$kShutdownItemsFolderIcon@1936221286$kSortAscendingIcon@1634954852$kSortDescendingIcon@1685286500$kSoundFileIcon@1936091500$kSpeakableItemsFolder@1936747369$kStartupFolderIconResource@-3981$kStartupItemsDisabledFolderIcon@1937011268$kStartupItemsFolderIcon@1937011316$kSystemExtensionDisabledFolderIcon@1835098948$kSystemFolderIcon@1835098995$kSystemFolderIconResource@-3983$kSystemIconsCreator@1835098995$kSystemSuitcaseIcon@2054388083$kTextEncodingsFolderIcon@-999004808$kToolbarAdvancedIcon@1952604534$kToolbarApplicationsFolderIcon@1950445683$kToolbarCustomizeIcon@1952675187$kToolbarDeleteIcon@1952736620$kToolbarDesktopFolderIcon@1950643051$kToolbarDocumentsFolderIcon@1950642019$kToolbarDownloadsFolderIcon@1950644078$kToolbarFavoritesIcon@1952866678$kToolbarHomeIcon@1953001325$kToolbarInfoIcon@1952606574$kToolbarLabelsIcon@1952607330$kToolbarLibraryFolderIcon@1951164770$kToolbarMovieFolderIcon@1951231862$kToolbarMusicFolderIcon@1951233395$kToolbarPicturesFolderIcon@1951426915$kToolbarPublicFolderIcon@1951429986$kToolbarSitesFolderIcon@1951626355$kToolbarUtilitiesFolderIcon@1951757420$kTrashIcon@1953657704$kTrashIconResource@-3993$kTrueTypeFlatFontIcon@1936092788$kTrueTypeFontIcon@1952868716$kTrueTypeMultiFlatFontIcon@1953784678$kUnknownFSObjectIcon@1970169459$kUnlockedIcon@1970037611$kUserFolderIcon@1969646692$kUserIDiskIcon@1969517419$kUserIcon@1970496882$kUsersFolderIcon@1970500292$kUtilitiesFolderIcon@1970563524$kVoicesFolderIcon@1719037795$kWorkgroupFolderIcon@2003201124$mountedFolderIconResource@-3977$openFolderIconResource@-3997$ownedFolderIconResource@-3980$preferencesFolderIconResource@-3974$printMonitorFolderIconResource@-3975$privateFolderIconResource@-3994$sharedFolderIconResource@-3978$startupFolderIconResource@-3981$systemFolderIconResource@-3983$trashIconResource@-3993$'''
misc.update({})
functions={'LSSharedFileListItemCopyDisplayName': (b'^{__CFString=}^{OpaqueLSSharedFileListItemRef=}', '', {'retval': {'already_cfretained': True}}), '_LSCopyAllApplicationURLs': (b'v^@', '', {'arguments': {0: {'already_retained': True, 'type_modifier': 'o'}}}), 'LSCopyItemInfoForRef': (sel32or64(b'l^{FSRef=[80C]}L^{LSItemInfoRecord=LLL^{__CFString=}^{__CFString=}L}', b'i^{FSRef=[80C]}I^{LSItemInfoRecord=III^{__CFString=}}'), '', {'retval': {'already_cfretained': True}, 'arguments': {0: {'type_modifier': 'n'}, 2: {'type_modifier': 'o'}}}), 'GetIconRefFromTypeInfo': (sel32or64(b'sLL^{__CFString=}^{__CFString=}L^^{OpaqueIconRef=}', b'sII^{__CFString=}^{__CFString=}I^^{OpaqueIconRef=}'), '', {'arguments': {5: {'type_modifier': 'o'}}}), 'ReadIconFromFSRef': (sel32or64(b'l^{FSRef=[80C]}^^^{IconFamilyResource=Ll[1{IconFamilyElement=Ll[1C]}]}', b'i^{FSRef=[80C]}^^^{IconFamilyResource=Ii[1{IconFamilyElement=Ii[1C]}]}'), '', {'arguments': {0: {'type_modifier': 'n'}}}), 'LSSharedFileListRemoveAllItems': (sel32or64(b'l^{OpaqueLSSharedFileListRef=}', b'i^{OpaqueLSSharedFileListRef=}'),), 'LSCopyItemAttribute': (sel32or64(b'l^{FSRef=[80C]}L^{__CFString=}^@', b'i^{FSRef=[80C]}I^{__CFString=}^@'), '', {'retval': {'already_cfretained': True}, 'arguments': {0: {'type_modifier': 'n'}, 3: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'LSSharedFileListItemMove': (sel32or64(b'l^{OpaqueLSSharedFileListRef=}^{OpaqueLSSharedFileListItemRef=}^{OpaqueLSSharedFileListItemRef=}', b'i^{OpaqueLSSharedFileListRef=}^{OpaqueLSSharedFileListItemRef=}^{OpaqueLSSharedFileListItemRef=}'),), 'LSSetDefaultRoleHandlerForContentType': (sel32or64(b'l^{__CFString=}L^{__CFString=}', b'i^{__CFString=}I^{__CFString=}'),), 'LSSetHandlerOptionsForContentType': (sel32or64(b'l^{__CFString=}L', b'i^{__CFString=}I'),), 'LSSharedFileListGetTypeID': (sel32or64(b'L', b'Q'),), 'LSInit': (sel32or64(b'lL', b'iI'),), 'LSCopyDefaultHandlerForURLScheme': (b'^{__CFString=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'LSCopyAllRoleHandlersForContentType': (sel32or64(b'^{__CFArray=}^{__CFString=}L', b'^{__CFArray=}^{__CFString=}I'), '', {'retval': {'already_cfretained': True}}), 'IsDataAvailableInIconRef': (sel32or64(b'ZL^{OpaqueIconRef=}', b'ZI^{OpaqueIconRef=}'),), 'IsValidIconRef': (b'Z^{OpaqueIconRef=}',), 'LSCanRefAcceptItem': (sel32or64(b'l^{FSRef=[80C]}^{FSRef=[80C]}LL^Z', b'i^{FSRef=[80C]}^{FSRef=[80C]}II^Z'), '', {'arguments': {0: {'type_modifier': 'n'}, 1: {'type_modifier': 'n'}, 4: {'type_modifier': 'o'}}}), 'LSCopyKindStringForTypeInfo': (sel32or64(b'lLL^{__CFString=}^^{__CFString=}', b'iII^{__CFString=}^^{__CFString=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {3: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'UTTypeCopyPreferredTagWithClass': (b'^{__CFString=}^{__CFString=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'FlushIconRefs': (b'sLL',), 'LSSetExtensionHiddenForURL': (sel32or64(b'l^{__CFURL=}Z', b'i^{__CFURL=}Z'),), 'LSOpenFSRef': (sel32or64(b'l^{FSRef=[80C]}^{FSRef=[80C]}', b'i^{FSRef=[80C]}^{FSRef=[80C]}'), '', {'arguments': {0: {'type_modifier': 'n'}, 1: {'type_modifier': 'o'}}}), 'LSSharedFileListInsertItemFSRef': (b'^{OpaqueLSSharedFileListItemRef=}^{OpaqueLSSharedFileListRef=}^{OpaqueLSSharedFileListItemRef=}^{__CFString=}^{OpaqueIconRef=}^{FSRef=[80C]}^{__CFDictionary=}^{__CFArray=}', '', {'arguments': {4: {'type_modifier': 'n'}}}), 'RegisterIconRefFromIconFile': (b'sLL^{FSSpec=sl[64C]}^^{OpaqueIconRef=}', '', {'arguments': {3: {'type_modifier': 'o'}}}), 'LSCopyItemAttributes': (sel32or64(b'l^{FSRef=[80C]}L^{__CFArray=}^^{__CFDictionary=}', b'i^{FSRef=[80C]}I^{__CFArray=}^^{__CFDictionary=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {0: {'type_modifier': 'n'}, 3: {'type_modifier': 'o'}}}), 'LSSharedFileListItemSetProperty': (sel32or64(b'l^{OpaqueLSSharedFileListItemRef=}^{__CFString=}@', b'i^{OpaqueLSSharedFileListItemRef=}^{__CFString=}@'),), 'UTTypeCreateAllIdentifiersForTag': (b'^{__CFArray=}^{__CFString=}^{__CFString=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'UTTypeCopyDeclaringBundleURL': (b'^{__CFURL=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'LSGetHandlerOptionsForContentType': (sel32or64(b'L^{__CFString=}', b'I^{__CFString=}'),), 'LSTerm': (sel32or64(b'l', b'i'),), 'LSSharedFileListItemCopyProperty': (b'@^{OpaqueLSSharedFileListItemRef=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'UpdateIconRef': (b's^{OpaqueIconRef=}',), 'LSGetApplicationForInfo': (sel32or64(b'lLL^{__CFString=}L^{FSRef=[80C]}^^{__CFURL=}', b'iII^{__CFString=}I^{FSRef=[80C]}^^{__CFURL=}'), '', {'arguments': {4: {'type_modifier': 'o'}, 5: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'LSSharedFileListItemGetTypeID': (sel32or64(b'L', b'Q'),), 'GetIconRefFromComponent': (sel32or64(b'l^{ComponentRecord=[1l]}^^{OpaqueIconRef=}', b'i^{ComponentRecord=[1q]}^^{OpaqueIconRef=}'), '', {'arguments': {1: {'type_modifier': 'o'}}}), 'UTTypeCopyDeclaration': (b'^{__CFDictionary=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'LSSharedFileListSetProperty': (sel32or64(b'l^{OpaqueLSSharedFileListRef=}^{__CFString=}@', b'i^{OpaqueLSSharedFileListRef=}^{__CFString=}@'),), 'LSSharedFileListItemCopyResolvedURL': (sel32or64(b'^{__CFURL=}^{OpaqueLSSharedFileListItemRef=}L^^{__CFError=}', b'^{__CFURL=}^{OpaqueLSSharedFileListItemRef=}I^^{__CFError=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {2: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'LSSharedFileListRemoveObserver': (b'v^{OpaqueLSSharedFileListRef=}^{__CFRunLoop=}^{__CFString=}^?^v', '', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^{OpaqueLSSharedFileListRef=}'}, 1: {'type': b'^v'}}}}}}), 'RegisterIconRefFromFSRef': (sel32or64(b'lLL^{FSRef=[80C]}^^{OpaqueIconRef=}', b'iII^{FSRef=[80C]}^^{OpaqueIconRef=}'), '', {'arguments': {2: {'type_modifier': 'n'}}}), 'LSCopyApplicationForMIMEType': (sel32or64(b'l^{__CFString=}L^^{__CFURL=}', b'i^{__CFString=}I^^{__CFURL=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {2: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'ReleaseIconRef': (b's^{OpaqueIconRef=}',), 'UTTypeCreatePreferredIdentifierForTag': (b'^{__CFString=}^{__CFString=}^{__CFString=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'LSSharedFileListItemResolve': (sel32or64(b'l^{OpaqueLSSharedFileListItemRef=}L^^{__CFURL=}^{FSRef=[80C]}', b'i^{OpaqueLSSharedFileListItemRef=}I^^{__CFURL=}^{FSRef=[80C]}'), '', {'arguments': {2: {'already_cfretained': True, 'type_modifier': 'o'}, 3: {'type_modifier': 'o'}}}), 'GetIconRefFromIconFamilyPtr': (sel32or64(b'l^{IconFamilyResource=Ll[1{IconFamilyElement=Ll[1C]}]}l^^{OpaqueIconRef=}', b'i^{IconFamilyResource=Ii[1{IconFamilyElement=Ii[1C]}]}q^^{OpaqueIconRef=}'), '', {'arguments': {0: {'type_modifier': 'n'}, 2: {'type_modifier': 'o'}}}), 'LSSharedFileListCreate': (b'^{OpaqueLSSharedFileListRef=}^{__CFAllocator=}^{__CFString=}@', '', {'retval': {'already_cfretained': True}}), 'WriteIconFile': (b's^^{IconFamilyResource=Ll[1{IconFamilyElement=Ll[1C]}]}^{FSSpec=sl[64C]}',), 'OverrideIconRef': (b's^{OpaqueIconRef=}^{OpaqueIconRef=}',), 'LSSharedFileListCopyProperty': (b'@^{OpaqueLSSharedFileListRef=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'IsIconRefComposite': (b's^{OpaqueIconRef=}^^{OpaqueIconRef=}^^{OpaqueIconRef=}', '', {'arguments': {1: {'type_modifier': 'o'}, 2: {'type_modifier': 'o'}}}), 'LSCanURLAcceptURL': (sel32or64(b'l^{__CFURL=}^{__CFURL=}LL^Z', b'i^{__CFURL=}^{__CFURL=}II^Z'), '', {'arguments': {4: {'type_modifier': 'o'}}}), 'GetIconRefFromFile': (b's^{FSSpec=sl[64C]}^^{OpaqueIconRef=}^s', '', {'arguments': {2: {'type_modifier': 'o'}}}), 'RemoveIconRefOverride': (b's^{OpaqueIconRef=}',), 'LSSharedFileListSetAuthorization': (sel32or64(b'l^{OpaqueLSSharedFileListRef=}^{AuthorizationOpaqueRef=}', b'i^{OpaqueLSSharedFileListRef=}^{AuthorizationOpaqueRef=}'),), 'LSOpenItemsWithRole': (sel32or64(b'l^{FSRef=[80C]}lL^{AEKeyDesc=L{AEDesc=L^^{OpaqueAEDataStorageType=}}}^{LSApplicationParameters=lL^{FSRef=[80C]}^v^{__CFDictionary=}^{__CFArray=}^{AEDesc=L^^{OpaqueAEDataStorageType=}}}^{ProcessSerialNumber=LL}l', b'i^{FSRef=[80C]}qI^{AEKeyDesc=I{AEDesc=I^^{OpaqueAEDataStorageType=}}}^{LSApplicationParameters=qI^{FSRef=[80C]}^v^{__CFDictionary=}^{__CFArray=}^{AEDesc=I^^{OpaqueAEDataStorageType=}}}^{ProcessSerialNumber=II}q'), '', {'arguments': {0: {'c_array_length_in_arg': 1, 'type_modifier': 'n'}, 3: {'type_modifier': 'n'}, 4: {'type_modifier': 'n'}, 5: {'c_array_length_in_arg': 6, 'type_modifier': 'o'}}}), 'RegisterIconRefFromResource': (b'sLL^{FSSpec=sl[64C]}s^^{OpaqueIconRef=}',), 'LSSharedFileListGetSeedValue': (sel32or64(b'L^{OpaqueLSSharedFileListRef=}', b'I^{OpaqueLSSharedFileListRef=}'),), 'LSOpenApplication': (sel32or64(b'l^{LSApplicationParameters=lL^{FSRef=[80C]}^v^{__CFDictionary=}^{__CFArray=}^{AEDesc=L^^{OpaqueAEDataStorageType=}}}^{ProcessSerialNumber=LL}', b'i^{LSApplicationParameters=qI^{FSRef=[80C]}^v^{__CFDictionary=}^{__CFArray=}^{AEDesc=I^^{OpaqueAEDataStorageType=}}}^{ProcessSerialNumber=II}'), '', {'arguments': {0: {'type_modifier': 'n'}, 1: {'type_modifier': 'o'}}}), 'LSGetApplicationForItem': (sel32or64(b'l^{FSRef=[80C]}L^{FSRef=[80C]}^^{__CFURL=}', b'i^{FSRef=[80C]}I^{FSRef=[80C]}^^{__CFURL=}'), '', {'arguments': {0: {'type_modifier': 'n'}, 2: {'type_modifier': 'o'}, 3: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'LSSetDefaultHandlerForURLScheme': (sel32or64(b'l^{__CFString=}^{__CFString=}', b'i^{__CFString=}^{__CFString=}'),), 'GetIconRef': (sel32or64(b'ssLL^^{OpaqueIconRef=}', b'ssII^^{OpaqueIconRef=}'), '', {'arguments': {3: {'type_modifier': 'o'}}}), 'LSRegisterURL': (sel32or64(b'l^{__CFURL=}Z', b'i^{__CFURL=}Z'),), 'GetIconRefOwners': (b's^{OpaqueIconRef=}^S', '', {'arguments': {1: {'type_modifier': 'o'}}}), 'LSCopyAllHandlersForURLScheme': (b'^{__CFArray=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'LSCopyDefaultApplicationURLForContentType': (sel32or64(b'^{__CFURL=}^{__CFString=}L^^{__CFError=}', b'^{__CFURL=}^{__CFString=}I^^{__CFError=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {2: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'UTTypeIsDynamic': (b'Z^{__CFString=}',), 'AcquireIconRef': (b's^{OpaqueIconRef=}',), 'ReadIconFile': (b's^{FSSpec=sl[64C]}^^^{IconFamilyResource=Ll[1{IconFamilyElement=Ll[1C]}]}',), 'LSSharedFileListItemCopyIconRef': (b'^{OpaqueIconRef=}^{OpaqueLSSharedFileListItemRef=}', '', {'retval': {'already_cfretained': True}}), 'UTGetOSTypeFromString': (sel32or64(b'L^{__CFString=}', b'I^{__CFString=}'),), 'LSGetApplicationForURL': (sel32or64(b'l^{__CFURL=}L^{FSRef=[80C]}^^{__CFURL=}', b'i^{__CFURL=}I^{FSRef=[80C]}^^{__CFURL=}'), '', {'arguments': {2: {'type_modifier': 'o'}, 3: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'LSSharedFileListInsertItemURL': (b'^{OpaqueLSSharedFileListItemRef=}^{OpaqueLSSharedFileListRef=}^{OpaqueLSSharedFileListItemRef=}^{__CFString=}^{OpaqueIconRef=}^{__CFURL=}^{__CFDictionary=}^{__CFArray=}', '', {'retval': {'already_cfretained': True}}), 'LSOpenURLsWithRole': (sel32or64(b'l^{__CFArray=}L^{AEKeyDesc=L{AEDesc=L^^{OpaqueAEDataStorageType=}}}^{LSApplicationParameters=lL^{FSRef=[80C]}^v^{__CFDictionary=}^{__CFArray=}^{AEDesc=L^^{OpaqueAEDataStorageType=}}}^{ProcessSerialNumber=LL}l', b'i^{__CFArray=}I^{AEKeyDesc=I{AEDesc=I^^{OpaqueAEDataStorageType=}}}^{LSApplicationParameters=qI^{FSRef=[80C]}^v^{__CFDictionary=}^{__CFArray=}^{AEDesc=I^^{OpaqueAEDataStorageType=}}}^{ProcessSerialNumber=II}q'), '', {'arguments': {2: {'type_modifier': 'n'}, 3: {'type_modifier': 'n'}, 4: {'c_array_length_in_arg': 5, 'type_modifier': 'o'}}}), 'LSCopyDefaultRoleHandlerForContentType': (sel32or64(b'^{__CFString=}^{__CFString=}L', b'^{__CFString=}^{__CFString=}I'), '', {'retval': {'already_cfretained': True}}), 'UnregisterIconRef': (sel32or64(b'sLL', b'sII'),), 'LSOpenFromURLSpec': (sel32or64(b'l^{LSLaunchURLSpec=^{__CFURL=}^{__CFArray=}^{AEDesc=L^^{OpaqueAEDataStorageType=}}L^v}^^{__CFURL=}', b'i^{LSLaunchURLSpec=^{__CFURL=}^{__CFArray=}^{AEDesc=I^^{OpaqueAEDataStorageType=}}I^v}^^{__CFURL=}'), '', {'arguments': {0: {'type_modifier': 'n'}, 1: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'UTTypeConformsTo': (b'Z^{__CFString=}^{__CFString=}',), 'SetCustomIconsEnabled': (b'ssZ',), 'LSRegisterFSRef': (sel32or64(b'l^{FSRef=[80C]}Z', b'i^{FSRef=[80C]}Z'), '', {'arguments': {0: {'type_modifier': 'n'}}}), 'LSSetItemAttribute': (sel32or64(b'l^{FSRef=[80C]}L^{__CFString=}@', b'i^{FSRef=[80C]}I^{__CFString=}@'), '', {'arguments': {0: {'type_modifier': 'n'}}}), 'UTCreateStringForOSType': (sel32or64(b'^{__CFString=}L', b'^{__CFString=}I'), '', {'retval': {'already_cfretained': True}}), 'LSCopyKindStringForRef': (sel32or64(b'l^{FSRef=[80C]}^^{__CFString=}', b'i^{FSRef=[80C]}^^{__CFString=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {0: {'type_modifier': 'n'}, 1: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'LSCopyDisplayNameForRef': (sel32or64(b'l^{FSRef=[80C]}^^{__CFString=}', b'i^{FSRef=[80C]}^^{__CFString=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {0: {'type_modifier': 'n'}, 1: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'CompositeIconRef': (b's^{OpaqueIconRef=}^{OpaqueIconRef=}^^{OpaqueIconRef=}', '', {'arguments': {2: {'type_modifier': 'o'}}}), 'UTTypeEqual': (b'Z^{__CFString=}^{__CFString=}',), 'UTTypeCopyAllTagsWithClass': (b'^{__CFArray=}^{__CFString=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'LSCopyKindStringForMIMEType': (sel32or64(b'l^{__CFString=}^^{__CFString=}', b'i^{__CFString=}^^{__CFString=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'RegisterIconRefFromIconFamily': (sel32or64(b'sLL^^{IconFamilyResource=Ll[1{IconFamilyElement=Ll[1C]}]}^^{OpaqueIconRef=}', b'sII^^{IconFamilyResource=Ii[1{IconFamilyElement=Ii[1C]}]}^^{OpaqueIconRef=}'),), 'UTTypeIsDeclared': (b'Z^{__CFString=}',), 'LSCopyDisplayNameForURL': (sel32or64(b'l^{__CFURL=}^^{__CFString=}', b'i^{__CFURL=}^^{__CFString=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'GetIconRefFromFolder': (sel32or64(b'ssllcc^^{OpaqueIconRef=}', b'ssiicc^^{OpaqueIconRef=}'), '', {'arguments': {5: {'type_modifier': 'o'}}}), 'LSSetExtensionHiddenForRef': (sel32or64(b'l^{FSRef=[80C]}Z', b'i^{FSRef=[80C]}Z'), '', {'arguments': {0: {'type_modifier': 'n'}}}), 'OverrideIconRefFromResource': (b's^{OpaqueIconRef=}^{FSSpec=sl[64C]}s',), 'LSGetExtensionInfo': (sel32or64(b'lL^T^L', b'iQ^T^Q'), '', {'arguments': {1: {'c_array_length_in_arg': 0, 'type_modifier': 'n'}, 2: {'type_modifier': 'o'}}}), 'LSCopyDefaultApplicationURLForURL': (sel32or64(b'^{__CFURL=}^{__CFURL=}L^^{__CFError=}', b'^{__CFURL=}^{__CFURL=}I^^{__CFError=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {2: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'GetIconRefFromFileInfo': (sel32or64(b'l^{FSRef=[80C]}L^TL^{FSCatalogInfo=SsLLCCCC{UTCDateTime=SLS}{UTCDateTime=SLS}{UTCDateTime=SLS}{UTCDateTime=SLS}{UTCDateTime=SLS}[4L][16C][16C]QQQQLL}L^^{OpaqueIconRef=}^s', b'i^{FSRef=[80C]}Q^TI^{FSCatalogInfo=SsIICCCC{UTCDateTime=SIS}{UTCDateTime=SIS}{UTCDateTime=SIS}{UTCDateTime=SIS}{UTCDateTime=SIS}{FSPermissionInfo=IICCS^{__FSFileSecurity=}}[16C][16C]QQQQII}I^^{OpaqueIconRef=}^s'), '', {'arguments': {0: {'type_modifier': 'n'}, 2: {'c_array_length_in_arg': 1, 'type_modifier': 'n'}, 4: {'null_accepted': True, 'type_modifier': 'n'}, 6: {'type_modifier': 'o'}, 7: {'type_modifier': 'o'}}}), 'UTTypeCopyDescription': (b'^{__CFString=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'LSCopyApplicationURLsForBundleIdentifier': (b'^{__CFArray=}^{__CFString=}^^{__CFError=}', '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'null_accepted': True, 'already_cfretained': True, 'type_modifier': 'o'}}}), 'FlushIconRefsByVolume': (b'ss',), 'GetCustomIconsEnabled': (b'ss^Z', '', {'arguments': {1: {'type_modifier': 'o'}}}), 'LSCopyItemInfoForURL': (sel32or64(b'l^{__CFURL=}L^{LSItemInfoRecord=LLL^{__CFString=}^{__CFString=}L}', b'i^{__CFURL=}I^{LSItemInfoRecord=III^{__CFString=}}'), '', {'retval': {'already_cfretained': True}, 'arguments': {2: {'type_modifier': 'o'}}}), 'LSFindApplicationForInfo': (sel32or64(b'lL^{__CFString=}^{__CFString=}^{FSRef=[80C]}^^{__CFURL=}', b'iI^{__CFString=}^{__CFString=}^{FSRef=[80C]}^^{__CFURL=}'), '', {'arguments': {3: {'type_modifier': 'o'}, 4: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'LSOpenFromRefSpec': (sel32or64(b'l^{LSLaunchFSRefSpec=^{FSRef=[80C]}L^{FSRef=[80C]}^{AEDesc=L^^{OpaqueAEDataStorageType=}}L^v}^{FSRef=[80C]}', b'i^{LSLaunchFSRefSpec=^{FSRef=[80C]}Q^{FSRef=[80C]}^{AEDesc=I^^{OpaqueAEDataStorageType=}}I^v}^{FSRef=[80C]}'), '', {'arguments': {0: {'type_modifier': 'n'}, 1: {'type_modifier': 'o'}}}), 'LSSharedFileListItemRemove': (sel32or64(b'l^{OpaqueLSSharedFileListRef=}^{OpaqueLSSharedFileListItemRef=}', b'i^{OpaqueLSSharedFileListRef=}^{OpaqueLSSharedFileListItemRef=}'),), 'LSCopyKindStringForURL': (sel32or64(b'l^{__CFURL=}^^{__CFString=}', b'i^{__CFURL=}^^{__CFString=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'LSCopyApplicationURLsForURL': (sel32or64(b'^{__CFArray=}^{__CFURL=}L', b'^{__CFArray=}^{__CFURL=}I'), '', {'retval': {'already_cfretained': True}}), 'LSOpenCFURLRef': (sel32or64(b'l^{__CFURL=}^^{__CFURL=}', b'i^{__CFURL=}^^{__CFURL=}'), '', {'arguments': {1: {'already_cfretained': True, 'type_modifier': 'o'}}}), 'LSSharedFileListCopySnapshot': (sel32or64(b'^{__CFArray=}^{OpaqueLSSharedFileListRef=}^L', b'^{__CFArray=}^{OpaqueLSSharedFileListRef=}^I'), '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'type_modifier': 'o'}}}), 'LSSharedFileListAddObserver': (b'v^{OpaqueLSSharedFileListRef=}^{__CFRunLoop=}^{__CFString=}^?^v', '', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^{OpaqueLSSharedFileListRef=}'}, 1: {'type': b'^v'}}}, 'callable_retained': True}}}), 'LSSharedFileListItemGetID': (sel32or64(b'L^{OpaqueLSSharedFileListItemRef=}', b'I^{OpaqueLSSharedFileListItemRef=}'),)}
aliases = {'mountedFolderIconResource': 'kMountedFolderIconResource', 'genericFolderIconResource': 'kGenericFolderIconResource', 'genericApplicationIconResource': 'kGenericApplicationIconResource', 'genericFileServerIconResource': 'kGenericFileServerIconResource', 'printMonitorFolderIconResource': 'kPrintMonitorFolderIconResource', 'sharedFolderIconResource': 'kSharedFolderIconResource', 'openFolderIconResource': 'kOpenFolderIconResource', 'controlPanelFolderIconResource': 'kControlPanelFolderIconResource', 'desktopIconResource': 'kDesktopIconResource', 'floppyIconResource': 'kFloppyIconResource', 'genericSuitcaseIconResource': 'kGenericSuitcaseIconResource', 'fontsFolderIconResource': 'kFontsFolderIconResource', 'kLSInvalidExtensionIndex': 'ULONG_MAX', 'genericEditionFileIconResource': 'kGenericEditionFileIconResource', 'genericQueryDocumentIconResource': 'kGenericQueryDocumentIconResource', 'genericMoverObjectIconResource': 'kGenericMoverObjectIconResource', 'extensionsFolderIconResource': 'kExtensionsFolderIconResource', 'genericRAMDiskIconResource': 'kGenericRAMDiskIconResource', 'dropFolderIconResource': 'kDropFolderIconResource', 'genericHardDiskIconResource': 'kGenericHardDiskIconResource', 'genericDocumentIconResource': 'kGenericDocumentIconResource', 'appleMenuFolderIconResource': 'kAppleMenuFolderIconResource', 'systemFolderIconResource': 'kSystemFolderIconResource', 'genericDeskAccessoryIconResource': 'kGenericDeskAccessoryIconResource', 'privateFolderIconResource': 'kPrivateFolderIconResource', 'preferencesFolderIconResource': 'kPreferencesFolderIconResource', 'fullTrashIconResource': 'kFullTrashIconResource', 'trashIconResource': 'kTrashIconResource', 'genericPreferencesIconResource': 'kGenericPreferencesIconResource', 'genericStationeryIconResource': 'kGenericStationeryIconResource', 'genericExtensionIconResource': 'kGenericExtensionIconResource', 'ownedFolderIconResource': 'kOwnedFolderIconResource', 'startupFolderIconResource': 'kStartupFolderIconResource', 'genericCDROMIconResource': 'kGenericCDROMIconResource', 'kInternationResourcesIcon': 'kInternationalResourcesIcon'}
cftypes=[('LSSharedFileListItemRef', b'^{OpaqueLSSharedFileListItemRef=}', 'LSSharedFileListItemGetTypeID', None), ('LSSharedFileListRef', b'^{OpaqueLSSharedFileListRef=}', 'LSSharedFileListGetTypeID', None)]
misc.update({'IconRef': objc.createOpaquePointerType('IconRef', b'^{OpaqueIconRef=}')})
expressions = {}

# END OF FILE
