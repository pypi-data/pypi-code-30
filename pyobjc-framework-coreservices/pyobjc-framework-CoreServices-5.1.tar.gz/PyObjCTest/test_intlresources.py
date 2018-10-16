from PyObjCTools.TestSupport import *

import CoreServices

class TestIntlResources (TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(not hasattr(CoreServices, name), "%r exposed in bindings"%(name,))

    def test_not_wrapped(self):
        self.assert_not_wrapped('itlcShowIcon')
        self.assert_not_wrapped('itlcDualCaret')
        self.assert_not_wrapped('itlcSysDirection')
        self.assert_not_wrapped('itlcDisableKeyScriptSync')
        self.assert_not_wrapped('itlcDisableKeyScriptSyncMask')
        self.assert_not_wrapped('tokLeftQuote')
        self.assert_not_wrapped('tokRightQuote')
        self.assert_not_wrapped('tokLeadPlacer')
        self.assert_not_wrapped('tokLeader')
        self.assert_not_wrapped('tokNonLeader')
        self.assert_not_wrapped('tokZeroLead')
        self.assert_not_wrapped('tokPercent')
        self.assert_not_wrapped('tokPlusSign')
        self.assert_not_wrapped('tokMinusSign')
        self.assert_not_wrapped('tokThousands')
        self.assert_not_wrapped('tokReserved')
        self.assert_not_wrapped('tokSeparator')
        self.assert_not_wrapped('tokEscape')
        self.assert_not_wrapped('tokDecPoint')
        self.assert_not_wrapped('tokEPlus')
        self.assert_not_wrapped('tokEMinus')
        self.assert_not_wrapped('tokMaxSymbols')
        self.assert_not_wrapped('curNumberPartsVersion')
        self.assert_not_wrapped('currSymLead')
        self.assert_not_wrapped('currNegSym')
        self.assert_not_wrapped('currTrailingZ')
        self.assert_not_wrapped('currLeadingZ')
        self.assert_not_wrapped('mdy')
        self.assert_not_wrapped('dmy')
        self.assert_not_wrapped('ymd')
        self.assert_not_wrapped('myd')
        self.assert_not_wrapped('dym')
        self.assert_not_wrapped('ydm')
        self.assert_not_wrapped('timeCycle24')
        self.assert_not_wrapped('timeCycleZero')
        self.assert_not_wrapped('timeCycle12')
        self.assert_not_wrapped('zeroCycle')
        self.assert_not_wrapped('longDay')
        self.assert_not_wrapped('longWeek')
        self.assert_not_wrapped('longMonth')
        self.assert_not_wrapped('longYear')
        self.assert_not_wrapped('supDay')
        self.assert_not_wrapped('supWeek')
        self.assert_not_wrapped('supMonth')
        self.assert_not_wrapped('supYear')
        self.assert_not_wrapped('dayLdingZ')
        self.assert_not_wrapped('mntLdingZ')
        self.assert_not_wrapped('century')
        self.assert_not_wrapped('secLeadingZ')
        self.assert_not_wrapped('minLeadingZ')
        self.assert_not_wrapped('hrLeadingZ')
        self.assert_not_wrapped('OffPair')
        self.assert_not_wrapped('Intl0Rec')
        self.assert_not_wrapped('Intl1Rec')
        self.assert_not_wrapped('Itl1ExtRec')
        self.assert_not_wrapped('UntokenTable')
        self.assert_not_wrapped('WideChar')
        self.assert_not_wrapped('WideCharArr')
        self.assert_not_wrapped('NumberParts')
        self.assert_not_wrapped('Itl4Rec')
        self.assert_not_wrapped('NItl4Rec')
        self.assert_not_wrapped('TableDirectoryRecord')
        self.assert_not_wrapped('Itl5Record')
        self.assert_not_wrapped('RuleBasedTrslRecord')
        self.assert_not_wrapped('ItlcRecord')
        self.assert_not_wrapped('ItlbRecord')
        self.assert_not_wrapped('ItlbExtRecord')


if __name__ == "__main__":
    main()
