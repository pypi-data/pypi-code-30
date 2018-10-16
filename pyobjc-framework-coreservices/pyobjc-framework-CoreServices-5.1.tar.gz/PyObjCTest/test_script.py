from PyObjCTools.TestSupport import *

import CoreServices

class TestScript (TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(not hasattr(CoreServices, name), "%r exposed in bindings"%(name,))

    def test_not_wrapped(self):
        self.assert_not_wrapped('smSystemScript')
        self.assert_not_wrapped('smCurrentScript')
        self.assert_not_wrapped('smAllScripts')
        self.assert_not_wrapped('smRoman')
        self.assert_not_wrapped('smJapanese')
        self.assert_not_wrapped('smTradChinese')
        self.assert_not_wrapped('smKorean')
        self.assert_not_wrapped('smArabic')
        self.assert_not_wrapped('smHebrew')
        self.assert_not_wrapped('smGreek')
        self.assert_not_wrapped('smCyrillic')
        self.assert_not_wrapped('smRSymbol')
        self.assert_not_wrapped('smDevanagari')
        self.assert_not_wrapped('smGurmukhi')
        self.assert_not_wrapped('smGujarati')
        self.assert_not_wrapped('smOriya')
        self.assert_not_wrapped('smBengali')
        self.assert_not_wrapped('smTamil')
        self.assert_not_wrapped('smTelugu')
        self.assert_not_wrapped('smKannada')
        self.assert_not_wrapped('smMalayalam')
        self.assert_not_wrapped('smSinhalese')
        self.assert_not_wrapped('smBurmese')
        self.assert_not_wrapped('smKhmer')
        self.assert_not_wrapped('smThai')
        self.assert_not_wrapped('smLao')
        self.assert_not_wrapped('smGeorgian')
        self.assert_not_wrapped('smArmenian')
        self.assert_not_wrapped('smSimpChinese')
        self.assert_not_wrapped('smTibetan')
        self.assert_not_wrapped('smMongolian')
        self.assert_not_wrapped('smEthiopic')
        self.assert_not_wrapped('smGeez')
        self.assert_not_wrapped('smCentralEuroRoman')
        self.assert_not_wrapped('smVietnamese')
        self.assert_not_wrapped('smExtArabic')
        self.assert_not_wrapped('smUninterp')
        self.assert_not_wrapped('smUnicodeScript')
        self.assert_not_wrapped('smChinese')
        self.assert_not_wrapped('smRussian')
        self.assert_not_wrapped('smLaotian')
        self.assert_not_wrapped('smAmharic')
        self.assert_not_wrapped('smSlavic')
        self.assert_not_wrapped('smEastEurRoman')
        self.assert_not_wrapped('smSindhi')
        self.assert_not_wrapped('smKlingon')
        self.assert_not_wrapped('langEnglish')
        self.assert_not_wrapped('langFrench')
        self.assert_not_wrapped('langGerman')
        self.assert_not_wrapped('langItalian')
        self.assert_not_wrapped('langDutch')
        self.assert_not_wrapped('langSwedish')
        self.assert_not_wrapped('langSpanish')
        self.assert_not_wrapped('langDanish')
        self.assert_not_wrapped('langPortuguese')
        self.assert_not_wrapped('langNorwegian')
        self.assert_not_wrapped('langHebrew')
        self.assert_not_wrapped('langJapanese')
        self.assert_not_wrapped('langArabic')
        self.assert_not_wrapped('langFinnish')
        self.assert_not_wrapped('langGreek')
        self.assert_not_wrapped('langIcelandic')
        self.assert_not_wrapped('langMaltese')
        self.assert_not_wrapped('langTurkish')
        self.assert_not_wrapped('langCroatian')
        self.assert_not_wrapped('langTradChinese')
        self.assert_not_wrapped('langUrdu')
        self.assert_not_wrapped('langHindi')
        self.assert_not_wrapped('langThai')
        self.assert_not_wrapped('langKorean')
        self.assert_not_wrapped('langLithuanian')
        self.assert_not_wrapped('langPolish')
        self.assert_not_wrapped('langHungarian')
        self.assert_not_wrapped('langEstonian')
        self.assert_not_wrapped('langLatvian')
        self.assert_not_wrapped('langSami')
        self.assert_not_wrapped('langFaroese')
        self.assert_not_wrapped('langFarsi')
        self.assert_not_wrapped('langPersian')
        self.assert_not_wrapped('langRussian')
        self.assert_not_wrapped('langSimpChinese')
        self.assert_not_wrapped('langFlemish')
        self.assert_not_wrapped('langIrishGaelic')
        self.assert_not_wrapped('langAlbanian')
        self.assert_not_wrapped('langRomanian')
        self.assert_not_wrapped('langCzech')
        self.assert_not_wrapped('langSlovak')
        self.assert_not_wrapped('langSlovenian')
        self.assert_not_wrapped('langYiddish')
        self.assert_not_wrapped('langSerbian')
        self.assert_not_wrapped('langMacedonian')
        self.assert_not_wrapped('langBulgarian')
        self.assert_not_wrapped('langUkrainian')
        self.assert_not_wrapped('langByelorussian')
        self.assert_not_wrapped('langBelorussian')
        self.assert_not_wrapped('langUzbek')
        self.assert_not_wrapped('langKazakh')
        self.assert_not_wrapped('langAzerbaijani')
        self.assert_not_wrapped('langAzerbaijanAr')
        self.assert_not_wrapped('langArmenian')
        self.assert_not_wrapped('langGeorgian')
        self.assert_not_wrapped('langMoldavian')
        self.assert_not_wrapped('langKirghiz')
        self.assert_not_wrapped('langTajiki')
        self.assert_not_wrapped('langTurkmen')
        self.assert_not_wrapped('langMongolian')
        self.assert_not_wrapped('langMongolianCyr')
        self.assert_not_wrapped('langPashto')
        self.assert_not_wrapped('langKurdish')
        self.assert_not_wrapped('langKashmiri')
        self.assert_not_wrapped('langSindhi')
        self.assert_not_wrapped('langTibetan')
        self.assert_not_wrapped('langNepali')
        self.assert_not_wrapped('langSanskrit')
        self.assert_not_wrapped('langMarathi')
        self.assert_not_wrapped('langBengali')
        self.assert_not_wrapped('langAssamese')
        self.assert_not_wrapped('langGujarati')
        self.assert_not_wrapped('langPunjabi')
        self.assert_not_wrapped('langOriya')
        self.assert_not_wrapped('langMalayalam')
        self.assert_not_wrapped('langKannada')
        self.assert_not_wrapped('langTamil')
        self.assert_not_wrapped('langTelugu')
        self.assert_not_wrapped('langSinhalese')
        self.assert_not_wrapped('langBurmese')
        self.assert_not_wrapped('langKhmer')
        self.assert_not_wrapped('langLao')
        self.assert_not_wrapped('langVietnamese')
        self.assert_not_wrapped('langIndonesian')
        self.assert_not_wrapped('langTagalog')
        self.assert_not_wrapped('langMalayRoman')
        self.assert_not_wrapped('langMalayArabic')
        self.assert_not_wrapped('langAmharic')
        self.assert_not_wrapped('langTigrinya')
        self.assert_not_wrapped('langOromo')
        self.assert_not_wrapped('langSomali')
        self.assert_not_wrapped('langSwahili')
        self.assert_not_wrapped('langKinyarwanda')
        self.assert_not_wrapped('langRuanda')
        self.assert_not_wrapped('langRundi')
        self.assert_not_wrapped('langNyanja')
        self.assert_not_wrapped('langChewa')
        self.assert_not_wrapped('langMalagasy')
        self.assert_not_wrapped('langEsperanto')
        self.assert_not_wrapped('langWelsh')
        self.assert_not_wrapped('langBasque')
        self.assert_not_wrapped('langCatalan')
        self.assert_not_wrapped('langLatin')
        self.assert_not_wrapped('langQuechua')
        self.assert_not_wrapped('langGuarani')
        self.assert_not_wrapped('langAymara')
        self.assert_not_wrapped('langTatar')
        self.assert_not_wrapped('langUighur')
        self.assert_not_wrapped('langDzongkha')
        self.assert_not_wrapped('langJavaneseRom')
        self.assert_not_wrapped('langSundaneseRom')
        self.assert_not_wrapped('langGalician')
        self.assert_not_wrapped('langAfrikaans')
        self.assert_not_wrapped('langBreton')
        self.assert_not_wrapped('langInuktitut')
        self.assert_not_wrapped('langScottishGaelic')
        self.assert_not_wrapped('langManxGaelic')
        self.assert_not_wrapped('langIrishGaelicScript')
        self.assert_not_wrapped('langTongan')
        self.assert_not_wrapped('langGreekAncient')
        self.assert_not_wrapped('langGreenlandic')
        self.assert_not_wrapped('langAzerbaijanRoman')
        self.assert_not_wrapped('langNynorsk')
        self.assert_not_wrapped('langUnspecified')
        self.assert_not_wrapped('langPortugese')
        self.assert_not_wrapped('langMalta')
        self.assert_not_wrapped('langYugoslavian')
        self.assert_not_wrapped('langChinese')
        self.assert_not_wrapped('langLettish')
        self.assert_not_wrapped('langLapponian')
        self.assert_not_wrapped('langLappish')
        self.assert_not_wrapped('langSaamisk')
        self.assert_not_wrapped('langFaeroese')
        self.assert_not_wrapped('langIrish')
        self.assert_not_wrapped('langGalla')
        self.assert_not_wrapped('langAfricaans')
        self.assert_not_wrapped('langGreekPoly')
        self.assert_not_wrapped('verUS')
        self.assert_not_wrapped('verFrance')
        self.assert_not_wrapped('verBritain')
        self.assert_not_wrapped('verGermany')
        self.assert_not_wrapped('verItaly')
        self.assert_not_wrapped('verNetherlands')
        self.assert_not_wrapped('verFlemish')
        self.assert_not_wrapped('verSweden')
        self.assert_not_wrapped('verSpain')
        self.assert_not_wrapped('verDenmark')
        self.assert_not_wrapped('verPortugal')
        self.assert_not_wrapped('verFrCanada')
        self.assert_not_wrapped('verNorway')
        self.assert_not_wrapped('verIsrael')
        self.assert_not_wrapped('verJapan')
        self.assert_not_wrapped('verAustralia')
        self.assert_not_wrapped('verArabic')
        self.assert_not_wrapped('verFinland')
        self.assert_not_wrapped('verFrSwiss')
        self.assert_not_wrapped('verGrSwiss')
        self.assert_not_wrapped('verGreece')
        self.assert_not_wrapped('verIceland')
        self.assert_not_wrapped('verMalta')
        self.assert_not_wrapped('verCyprus')
        self.assert_not_wrapped('verTurkey')
        self.assert_not_wrapped('verYugoCroatian')
        self.assert_not_wrapped('verNetherlandsComma')
        self.assert_not_wrapped('verFlemishPoint')
        self.assert_not_wrapped('verCanadaComma')
        self.assert_not_wrapped('verCanadaPoint')
        self.assert_not_wrapped('vervariantPortugal')
        self.assert_not_wrapped('vervariantNorway')
        self.assert_not_wrapped('vervariantDenmark')
        self.assert_not_wrapped('verIndiaHindi')
        self.assert_not_wrapped('verPakistanUrdu')
        self.assert_not_wrapped('verTurkishModified')
        self.assert_not_wrapped('verItalianSwiss')
        self.assert_not_wrapped('verInternational')
        self.assert_not_wrapped('verRomania')
        self.assert_not_wrapped('verGreekAncient')
        self.assert_not_wrapped('verLithuania')
        self.assert_not_wrapped('verPoland')
        self.assert_not_wrapped('verHungary')
        self.assert_not_wrapped('verEstonia')
        self.assert_not_wrapped('verLatvia')
        self.assert_not_wrapped('verSami')
        self.assert_not_wrapped('verFaroeIsl')
        self.assert_not_wrapped('verIran')
        self.assert_not_wrapped('verRussia')
        self.assert_not_wrapped('verIreland')
        self.assert_not_wrapped('verKorea')
        self.assert_not_wrapped('verChina')
        self.assert_not_wrapped('verTaiwan')
        self.assert_not_wrapped('verThailand')
        self.assert_not_wrapped('verScriptGeneric')
        self.assert_not_wrapped('verCzech')
        self.assert_not_wrapped('verSlovak')
        self.assert_not_wrapped('verEastAsiaGeneric')
        self.assert_not_wrapped('verMagyar')
        self.assert_not_wrapped('verBengali')
        self.assert_not_wrapped('verBelarus')
        self.assert_not_wrapped('verUkraine')
        self.assert_not_wrapped('verGreeceAlt')
        self.assert_not_wrapped('verSerbian')
        self.assert_not_wrapped('verSlovenian')
        self.assert_not_wrapped('verMacedonian')
        self.assert_not_wrapped('verCroatia')
        self.assert_not_wrapped('verGermanReformed')
        self.assert_not_wrapped('verBrazil')
        self.assert_not_wrapped('verBulgaria')
        self.assert_not_wrapped('verCatalonia')
        self.assert_not_wrapped('verMultilingual')
        self.assert_not_wrapped('verScottishGaelic')
        self.assert_not_wrapped('verManxGaelic')
        self.assert_not_wrapped('verBreton')
        self.assert_not_wrapped('verNunavut')
        self.assert_not_wrapped('verWelsh')
        self.assert_not_wrapped('                                    /*              80 is ID for KCHR resource - Canadian CSA*/')
        self.assert_not_wrapped('verIrishGaelicScript')
        self.assert_not_wrapped('verEngCanada')
        self.assert_not_wrapped('verBhutan')
        self.assert_not_wrapped('verArmenian')
        self.assert_not_wrapped('verGeorgian')
        self.assert_not_wrapped('verSpLatinAmerica')
        self.assert_not_wrapped('                                    /*              87 is ID for KCHR resource - Spanish ISO*/')
        self.assert_not_wrapped('verTonga')
        self.assert_not_wrapped('                                    /*              89 is ID for KCHR resource - Polish Modified*/')
        self.assert_not_wrapped('                                    /*              90 is ID for KCHR resource - Catalan ISO*/')
        self.assert_not_wrapped('verFrenchUniversal')
        self.assert_not_wrapped('verAustria')
        self.assert_not_wrapped('                                    /* Y          93 is unused alternate for verSpLatinAmerica*/')
        self.assert_not_wrapped('verGujarati')
        self.assert_not_wrapped('verPunjabi')
        self.assert_not_wrapped('verIndiaUrdu')
        self.assert_not_wrapped('verVietnam')
        self.assert_not_wrapped('verFrBelgium')
        self.assert_not_wrapped('verUzbek')
        self.assert_not_wrapped('verSingapore')
        self.assert_not_wrapped('verNynorsk')
        self.assert_not_wrapped('verAfrikaans')
        self.assert_not_wrapped('verEsperanto')
        self.assert_not_wrapped('verMarathi')
        self.assert_not_wrapped('verTibetan')
        self.assert_not_wrapped('verNepal')
        self.assert_not_wrapped('verGreenland')
        self.assert_not_wrapped('verIrelandEnglish')
        self.assert_not_wrapped('verFrBelgiumLux')
        self.assert_not_wrapped('verBelgiumLux')
        self.assert_not_wrapped('verArabia')
        self.assert_not_wrapped('verYugoslavia')
        self.assert_not_wrapped('verBelgiumLuxPoint')
        self.assert_not_wrapped('verIndia')
        self.assert_not_wrapped('verPakistan')
        self.assert_not_wrapped('verRumania')
        self.assert_not_wrapped('verGreecePoly')
        self.assert_not_wrapped('verLapland')
        self.assert_not_wrapped('verFaeroeIsl')
        self.assert_not_wrapped('verGenericFE')
        self.assert_not_wrapped('verFarEastGeneric')
        self.assert_not_wrapped('verByeloRussian')
        self.assert_not_wrapped('verUkrania')
        self.assert_not_wrapped('verAlternateGr')
        self.assert_not_wrapped('verSerbia')
        self.assert_not_wrapped('verSlovenia')
        self.assert_not_wrapped('verMacedonia')
        self.assert_not_wrapped('verBrittany')
        self.assert_not_wrapped('verWales')
        self.assert_not_wrapped('verArmenia')
        self.assert_not_wrapped('verGeorgia')
        self.assert_not_wrapped('verAustriaGerman')
        self.assert_not_wrapped('verTibet')
        self.assert_not_wrapped('minCountry')
        self.assert_not_wrapped('maxCountry')
        self.assert_not_wrapped('calGregorian')
        self.assert_not_wrapped('calArabicCivil')
        self.assert_not_wrapped('calArabicLunar')
        self.assert_not_wrapped('calJapanese')
        self.assert_not_wrapped('calJewish')
        self.assert_not_wrapped('calCoptic')
        self.assert_not_wrapped('calPersian')
        self.assert_not_wrapped('intWestern')
        self.assert_not_wrapped('intArabic')
        self.assert_not_wrapped('intRoman')
        self.assert_not_wrapped('intJapanese')
        self.assert_not_wrapped('intEuropean')
        self.assert_not_wrapped('intOutputMask')
        self.assert_not_wrapped('smSingleByte')
        self.assert_not_wrapped('smFirstByte')
        self.assert_not_wrapped('smLastByte')
        self.assert_not_wrapped('smMiddleByte')
        self.assert_not_wrapped('smcTypeMask')
        self.assert_not_wrapped('smcReserved')
        self.assert_not_wrapped('smcClassMask')
        self.assert_not_wrapped('smcOrientationMask')
        self.assert_not_wrapped('smcRightMask')
        self.assert_not_wrapped('smcUpperMask')
        self.assert_not_wrapped('smcDoubleMask')
        self.assert_not_wrapped('smCharPunct')
        self.assert_not_wrapped('smCharAscii')
        self.assert_not_wrapped('smCharEuro')
        self.assert_not_wrapped('smCharExtAscii')
        self.assert_not_wrapped('smCharKatakana')
        self.assert_not_wrapped('smCharHiragana')
        self.assert_not_wrapped('smCharIdeographic')
        self.assert_not_wrapped('smCharTwoByteGreek')
        self.assert_not_wrapped('smCharTwoByteRussian')
        self.assert_not_wrapped('smCharBidirect')
        self.assert_not_wrapped('smCharContextualLR')
        self.assert_not_wrapped('smCharNonContextualLR')
        self.assert_not_wrapped('smCharHangul')
        self.assert_not_wrapped('smCharJamo')
        self.assert_not_wrapped('smCharBopomofo')
        self.assert_not_wrapped('smCharGanaKana')
        self.assert_not_wrapped('smCharFISKana')
        self.assert_not_wrapped('smCharFISGana')
        self.assert_not_wrapped('smCharFISIdeo')
        self.assert_not_wrapped('smCharFISGreek')
        self.assert_not_wrapped('smCharFISRussian')
        self.assert_not_wrapped('                                    /* CharType classes for punctuation (smCharPunct) */')
        self.assert_not_wrapped('smPunctNormal')
        self.assert_not_wrapped('smPunctNumber')
        self.assert_not_wrapped('smPunctSymbol')
        self.assert_not_wrapped('smPunctBlank')
        self.assert_not_wrapped('smPunctRepeat')
        self.assert_not_wrapped('smPunctGraphic')
        self.assert_not_wrapped('                                    /* CharType Katakana and Hiragana classes for two-byte systems */')
        self.assert_not_wrapped('smKanaSmall')
        self.assert_not_wrapped('smKanaHardOK')
        self.assert_not_wrapped('smKanaSoftOK')
        self.assert_not_wrapped('                                    /* CharType Ideographic classes for two-byte systems */')
        self.assert_not_wrapped('smIdeographicLevel1')
        self.assert_not_wrapped('smIdeographicLevel2')
        self.assert_not_wrapped('smIdeographicUser')
        self.assert_not_wrapped('                                    /* old names for above, for backward compatibility */')
        self.assert_not_wrapped('smFISClassLvl1')
        self.assert_not_wrapped('smFISClassLvl2')
        self.assert_not_wrapped('smFISClassUser')
        self.assert_not_wrapped('                                    /* CharType Jamo classes for Korean systems */')
        self.assert_not_wrapped('smJamoJaeum')
        self.assert_not_wrapped('smJamoBogJaeum')
        self.assert_not_wrapped('smJamoMoeum')
        self.assert_not_wrapped('smJamoBogMoeum')
        self.assert_not_wrapped('smCharHorizontal')
        self.assert_not_wrapped('smCharVertical')
        self.assert_not_wrapped('                                    /* CharType directions */')
        self.assert_not_wrapped('smCharLeft')
        self.assert_not_wrapped('smCharRight')
        self.assert_not_wrapped('smCharLower')
        self.assert_not_wrapped('smCharUpper')
        self.assert_not_wrapped('smChar1byte')
        self.assert_not_wrapped('smChar2byte')
        self.assert_not_wrapped('smTransAscii')
        self.assert_not_wrapped('smTransNative')
        self.assert_not_wrapped('smTransCase')
        self.assert_not_wrapped('smTransSystem')
        self.assert_not_wrapped('                                    /* TransliterateText target types for two-byte scripts */')
        self.assert_not_wrapped('smTransAscii1')
        self.assert_not_wrapped('smTransAscii2')
        self.assert_not_wrapped('smTransKana1')
        self.assert_not_wrapped('smTransKana2')
        self.assert_not_wrapped('smTransGana2')
        self.assert_not_wrapped('smTransHangul2')
        self.assert_not_wrapped('smTransJamo2')
        self.assert_not_wrapped('smTransBopomofo2')
        self.assert_not_wrapped('                                    /* TransliterateText target modifiers */')
        self.assert_not_wrapped('smTransLower')
        self.assert_not_wrapped('smTransUpper')
        self.assert_not_wrapped('                                    /* TransliterateText resource format numbers */')
        self.assert_not_wrapped('smTransRuleBaseFormat')
        self.assert_not_wrapped('smTransHangulFormat')
        self.assert_not_wrapped('                                    /* TransliterateText property flags */')
        self.assert_not_wrapped('smTransPreDoubleByting')
        self.assert_not_wrapped('smTransPreLowerCasing')
        self.assert_not_wrapped('smMaskAll')
        self.assert_not_wrapped('                                    /* TransliterateText source masks */')
        self.assert_not_wrapped('smMaskAscii')
        self.assert_not_wrapped('smMaskNative')
        self.assert_not_wrapped('                                    /* TransliterateText source masks for two-byte scripts */')
        self.assert_not_wrapped('smMaskAscii1')
        self.assert_not_wrapped('smMaskAscii2')
        self.assert_not_wrapped('smMaskKana1')
        self.assert_not_wrapped('smMaskKana2')
        self.assert_not_wrapped('smMaskGana2')
        self.assert_not_wrapped('smMaskHangul2')
        self.assert_not_wrapped('smMaskJamo2')
        self.assert_not_wrapped('smMaskBopomofo2')
        self.assert_not_wrapped('                                    /* Special script code values for International Utilities */')
        self.assert_not_wrapped('iuSystemScript')
        self.assert_not_wrapped('iuCurrentScript')
        self.assert_not_wrapped('smKeyNextScript')
        self.assert_not_wrapped('smKeySysScript')
        self.assert_not_wrapped('smKeySwapScript')
        self.assert_not_wrapped('                                    /* New for System 7.0: */')
        self.assert_not_wrapped('smKeyNextKybd')
        self.assert_not_wrapped('smKeySwapKybd')
        self.assert_not_wrapped('smKeyDisableKybds')
        self.assert_not_wrapped('smKeyEnableKybds')
        self.assert_not_wrapped('smKeyToggleInline')
        self.assert_not_wrapped('smKeyToggleDirection')
        self.assert_not_wrapped('smKeyNextInputMethod')
        self.assert_not_wrapped('smKeySwapInputMethod')
        self.assert_not_wrapped('smKeyDisableKybdSwitch')
        self.assert_not_wrapped('smKeySetDirLeftRight')
        self.assert_not_wrapped('smKeySetDirRightLeft')
        self.assert_not_wrapped('smKeyRoman')
        self.assert_not_wrapped('smKeyForceKeyScriptBit')
        self.assert_not_wrapped('smKeyForceKeyScriptMask')
        self.assert_not_wrapped('romanSysFond')
        self.assert_not_wrapped('romanAppFond')
        self.assert_not_wrapped('romanFlags')
        self.assert_not_wrapped('                                    /* Script Manager font equates. */')
        self.assert_not_wrapped('smFondStart')
        self.assert_not_wrapped('smFondEnd')
        self.assert_not_wrapped('                                    /* Miscellaneous font equates. */')
        self.assert_not_wrapped('smUprHalfCharSet')
        self.assert_not_wrapped('diaeresisUprY')
        self.assert_not_wrapped('fraction')
        self.assert_not_wrapped('intlCurrency')
        self.assert_not_wrapped('leftSingGuillemet')
        self.assert_not_wrapped('rightSingGuillemet')
        self.assert_not_wrapped('fiLigature')
        self.assert_not_wrapped('flLigature')
        self.assert_not_wrapped('dblDagger')
        self.assert_not_wrapped('centeredDot')
        self.assert_not_wrapped('baseSingQuote')
        self.assert_not_wrapped('baseDblQuote')
        self.assert_not_wrapped('perThousand')
        self.assert_not_wrapped('circumflexUprA')
        self.assert_not_wrapped('circumflexUprE')
        self.assert_not_wrapped('acuteUprA')
        self.assert_not_wrapped('diaeresisUprE')
        self.assert_not_wrapped('graveUprE')
        self.assert_not_wrapped('acuteUprI')
        self.assert_not_wrapped('circumflexUprI')
        self.assert_not_wrapped('diaeresisUprI')
        self.assert_not_wrapped('graveUprI')
        self.assert_not_wrapped('acuteUprO')
        self.assert_not_wrapped('circumflexUprO')
        self.assert_not_wrapped('appleLogo')
        self.assert_not_wrapped('graveUprO')
        self.assert_not_wrapped('acuteUprU')
        self.assert_not_wrapped('circumflexUprU')
        self.assert_not_wrapped('graveUprU')
        self.assert_not_wrapped('dotlessLwrI')
        self.assert_not_wrapped('circumflex')
        self.assert_not_wrapped('tilde')
        self.assert_not_wrapped('macron')
        self.assert_not_wrapped('breveMark')
        self.assert_not_wrapped('overDot')
        self.assert_not_wrapped('ringMark')
        self.assert_not_wrapped('cedilla')
        self.assert_not_wrapped('doubleAcute')
        self.assert_not_wrapped('ogonek')
        self.assert_not_wrapped('hachek')
        self.assert_not_wrapped('tokenIntl')
        self.assert_not_wrapped('tokenEmpty')
        self.assert_not_wrapped('tokenUnknown')
        self.assert_not_wrapped('tokenWhite')
        self.assert_not_wrapped('tokenLeftLit')
        self.assert_not_wrapped('tokenRightLit')
        self.assert_not_wrapped('tokenAlpha')
        self.assert_not_wrapped('tokenNumeric')
        self.assert_not_wrapped('tokenNewLine')
        self.assert_not_wrapped('tokenLeftComment')
        self.assert_not_wrapped('tokenRightComment')
        self.assert_not_wrapped('tokenLiteral')
        self.assert_not_wrapped('tokenEscape')
        self.assert_not_wrapped('tokenAltNum')
        self.assert_not_wrapped('tokenRealNum')
        self.assert_not_wrapped('tokenAltReal')
        self.assert_not_wrapped('tokenReserve1')
        self.assert_not_wrapped('tokenReserve2')
        self.assert_not_wrapped('tokenLeftParen')
        self.assert_not_wrapped('tokenRightParen')
        self.assert_not_wrapped('tokenLeftBracket')
        self.assert_not_wrapped('tokenRightBracket')
        self.assert_not_wrapped('tokenLeftCurly')
        self.assert_not_wrapped('tokenRightCurly')
        self.assert_not_wrapped('tokenLeftEnclose')
        self.assert_not_wrapped('tokenRightEnclose')
        self.assert_not_wrapped('tokenPlus')
        self.assert_not_wrapped('tokenMinus')
        self.assert_not_wrapped('tokenAsterisk')
        self.assert_not_wrapped('tokenDivide')
        self.assert_not_wrapped('tokenPlusMinus')
        self.assert_not_wrapped('tokenSlash')
        self.assert_not_wrapped('tokenBackSlash')
        self.assert_not_wrapped('tokenLess')
        self.assert_not_wrapped('tokenGreat')
        self.assert_not_wrapped('tokenEqual')
        self.assert_not_wrapped('tokenLessEqual2')
        self.assert_not_wrapped('tokenLessEqual1')
        self.assert_not_wrapped('tokenGreatEqual2')
        self.assert_not_wrapped('tokenGreatEqual1')
        self.assert_not_wrapped('token2Equal')
        self.assert_not_wrapped('tokenColonEqual')
        self.assert_not_wrapped('tokenNotEqual')
        self.assert_not_wrapped('tokenLessGreat')
        self.assert_not_wrapped('tokenExclamEqual')
        self.assert_not_wrapped('tokenExclam')
        self.assert_not_wrapped('tokenTilde')
        self.assert_not_wrapped('tokenComma')
        self.assert_not_wrapped('tokenPeriod')
        self.assert_not_wrapped('tokenLeft2Quote')
        self.assert_not_wrapped('tokenRight2Quote')
        self.assert_not_wrapped('tokenLeft1Quote')
        self.assert_not_wrapped('tokenRight1Quote')
        self.assert_not_wrapped('token2Quote')
        self.assert_not_wrapped('token1Quote')
        self.assert_not_wrapped('tokenSemicolon')
        self.assert_not_wrapped('tokenPercent')
        self.assert_not_wrapped('tokenCaret')
        self.assert_not_wrapped('tokenUnderline')
        self.assert_not_wrapped('tokenAmpersand')
        self.assert_not_wrapped('tokenAtSign')
        self.assert_not_wrapped('tokenBar')
        self.assert_not_wrapped('tokenQuestion')
        self.assert_not_wrapped('tokenPi')
        self.assert_not_wrapped('tokenRoot')
        self.assert_not_wrapped('tokenSigma')
        self.assert_not_wrapped('tokenIntegral')
        self.assert_not_wrapped('tokenMicro')
        self.assert_not_wrapped('tokenCapPi')
        self.assert_not_wrapped('tokenInfinity')
        self.assert_not_wrapped('tokenColon')
        self.assert_not_wrapped('tokenHash')
        self.assert_not_wrapped('tokenDollar')
        self.assert_not_wrapped('tokenNoBreakSpace')
        self.assert_not_wrapped('tokenFraction')
        self.assert_not_wrapped('tokenIntlCurrency')
        self.assert_not_wrapped('tokenLeftSingGuillemet')
        self.assert_not_wrapped('tokenRightSingGuillemet')
        self.assert_not_wrapped('tokenPerThousand')
        self.assert_not_wrapped('tokenEllipsis')
        self.assert_not_wrapped('tokenCenterDot')
        self.assert_not_wrapped('tokenNil')
        self.assert_not_wrapped('delimPad')
        self.assert_not_wrapped('tokenTilda')
        self.assert_not_wrapped('tokenCarat')
        self.assert_not_wrapped('smWordSelectTable')
        self.assert_not_wrapped('smWordWrapTable')
        self.assert_not_wrapped('smNumberPartsTable')
        self.assert_not_wrapped('smUnTokenTable')
        self.assert_not_wrapped('smWhiteSpaceList')
        self.assert_not_wrapped('iuWordSelectTable')
        self.assert_not_wrapped('iuWordWrapTable')
        self.assert_not_wrapped('iuNumberPartsTable')
        self.assert_not_wrapped('iuUnTokenTable')
        self.assert_not_wrapped('iuWhiteSpaceList')
        self.assert_not_wrapped('tokenOK')
        self.assert_not_wrapped('tokenOverflow')
        self.assert_not_wrapped('stringOverflow')
        self.assert_not_wrapped('badDelim')
        self.assert_not_wrapped('badEnding')
        self.assert_not_wrapped('crash')
        self.assert_not_wrapped('TokenRec')
        self.assert_not_wrapped('TokenBlock')
        self.assert_not_wrapped('smNotInstalled')
        self.assert_not_wrapped('smBadVerb')
        self.assert_not_wrapped('smBadScript')
        self.assert_not_wrapped('smfShowIcon')
        self.assert_not_wrapped('smfDualCaret')
        self.assert_not_wrapped('smfNameTagEnab')
        self.assert_not_wrapped('smfUseAssocFontInfo')
        self.assert_not_wrapped('smfDisableKeyScriptSync')
        self.assert_not_wrapped('smfDisableKeyScriptSyncMask')
        self.assert_not_wrapped('smSysScript')
        self.assert_not_wrapped('smKeyScript')
        self.assert_not_wrapped('smKCHRCache')
        self.assert_not_wrapped('smRegionCode')
        self.assert_not_wrapped('smVersion')
        self.assert_not_wrapped('smMunged')
        self.assert_not_wrapped('smEnabled')
        self.assert_not_wrapped('smBidirect')
        self.assert_not_wrapped('smFontForce')
        self.assert_not_wrapped('smIntlForce')
        self.assert_not_wrapped('smForced')
        self.assert_not_wrapped('smDefault')
        self.assert_not_wrapped('smPrint')
        self.assert_not_wrapped('smLastScript')
        self.assert_not_wrapped('smSysRef')
        self.assert_not_wrapped('smKeyCache')
        self.assert_not_wrapped('smKeySwap')
        self.assert_not_wrapped('smGenFlags')
        self.assert_not_wrapped('smOverride')
        self.assert_not_wrapped('smCharPortion')
        self.assert_not_wrapped('smDoubleByte')
        self.assert_not_wrapped('smKeyDisableState')
        self.assert_not_wrapped('GetScriptManagerVariable')
        self.assert_not_wrapped('SetScriptManagerVariable')
        self.assert_not_wrapped('smRedrawChar')
        self.assert_not_wrapped('smRedrawWord')
        self.assert_not_wrapped('smRedrawLine')
        self.assert_not_wrapped('smsfIntellCP')
        self.assert_not_wrapped('smsfSingByte')
        self.assert_not_wrapped('smsfNatCase')
        self.assert_not_wrapped('smsfContext')
        self.assert_not_wrapped('smsfNoForceFont')
        self.assert_not_wrapped('smsfB0Digits')
        self.assert_not_wrapped('smsfAutoInit')
        self.assert_not_wrapped('smsfUnivExt')
        self.assert_not_wrapped('smsfSynchUnstyledTE')
        self.assert_not_wrapped('smsfForms')
        self.assert_not_wrapped('smsfLigatures')
        self.assert_not_wrapped('smsfReverse')
        self.assert_not_wrapped('smScriptVersion')
        self.assert_not_wrapped('smScriptMunged')
        self.assert_not_wrapped('smScriptEnabled')
        self.assert_not_wrapped('smScriptRight')
        self.assert_not_wrapped('smScriptJust')
        self.assert_not_wrapped('smScriptRedraw')
        self.assert_not_wrapped('smScriptSysFond')
        self.assert_not_wrapped('smScriptAppFond')
        self.assert_not_wrapped('smScriptBundle')
        self.assert_not_wrapped('smScriptNumber')
        self.assert_not_wrapped('smScriptDate')
        self.assert_not_wrapped('smScriptSort')
        self.assert_not_wrapped('smScriptFlags')
        self.assert_not_wrapped('smScriptToken')
        self.assert_not_wrapped('smScriptEncoding')
        self.assert_not_wrapped('smScriptLang')
        self.assert_not_wrapped('smScriptNumDate')
        self.assert_not_wrapped('smScriptKeys')
        self.assert_not_wrapped('smScriptIcon')
        self.assert_not_wrapped('smScriptPrint')
        self.assert_not_wrapped('smScriptTrap')
        self.assert_not_wrapped('smScriptCreator')
        self.assert_not_wrapped('smScriptFile')
        self.assert_not_wrapped('smScriptName')
        self.assert_not_wrapped('smScriptMonoFondSize')
        self.assert_not_wrapped('smScriptPrefFondSize')
        self.assert_not_wrapped('smScriptSmallFondSize')
        self.assert_not_wrapped('smScriptSysFondSize')
        self.assert_not_wrapped('smScriptAppFondSize')
        self.assert_not_wrapped('smScriptHelpFondSize')
        self.assert_not_wrapped('smScriptValidStyles')
        self.assert_not_wrapped('smScriptAliasStyle')
        self.assert_not_wrapped('smLayoutCache')
        self.assert_not_wrapped('smOldVerbSupport')
        self.assert_not_wrapped('smSetKashidas')
        self.assert_not_wrapped('smSetKashProp')
        self.assert_not_wrapped('smScriptSysBase')
        self.assert_not_wrapped('smScriptAppBase')
        self.assert_not_wrapped('smScriptFntBase')
        self.assert_not_wrapped('smScriptLigatures')
        self.assert_not_wrapped('smScriptNumbers')
        self.assert_not_wrapped('GetScriptVariable')
        self.assert_not_wrapped('SetScriptVariable')
        self.assert_not_wrapped('GetSysDirection')
        self.assert_not_wrapped('SetSysDirection')
        self.assert_not_wrapped('FontScript')
        self.assert_not_wrapped('IntlScript')
        self.assert_not_wrapped('FontToScript')
        self.assert_not_wrapped('CharacterByteType')
        self.assert_not_wrapped('CharacterType')
        self.assert_not_wrapped('TransliterateText')
        self.assert_not_wrapped('FillParseTable')
        self.assert_not_wrapped('GetIntlResource')
        self.assert_not_wrapped('ClearIntlResourceCache')
        self.assert_not_wrapped('GetIntlResourceTable')
        self.assert_not_wrapped('IntlTokenize')
        self.assert_not_wrapped('SetSysJust')
        self.assert_not_wrapped('GetSysJust')
        self.assert_not_wrapped('Font2Script')
        self.assert_not_wrapped('GetEnvirons')
        self.assert_not_wrapped('SetEnvirons')
        self.assert_not_wrapped('GetScript')
        self.assert_not_wrapped('SetScript')
        self.assert_not_wrapped('IUGetIntl')
        self.assert_not_wrapped('IUSetIntl')
        self.assert_not_wrapped('IUClearCache')
        self.assert_not_wrapped('IUGetItlTable')



if __name__ == "__main__":
    main()
