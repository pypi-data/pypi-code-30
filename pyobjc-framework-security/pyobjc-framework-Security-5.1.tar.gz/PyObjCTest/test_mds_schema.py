from PyObjCTools.TestSupport import *

import Security

class TestMDS (TestCase):

    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, 'MDS_OBJECT_DIRECTORY_NAME'))
        self.assertFalse(hasattr(Security, 'MDS_CDSA_DIRECTORY_NAME'))
        self.assertFalse(hasattr(Security, 'CSSM_DB_RELATIONID_MDS_START'))
        self.assertFalse(hasattr(Security, 'CSSM_DB_RELATIONID_MDS_END'))
        self.assertFalse(hasattr(Security, 'MDS_OBJECT_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSA_SCHEMA_START'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_CSSM_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_KRMM_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_EMM_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_COMMON_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_CSP_PRIMARY_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_CSP_CAPABILITY_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_CSP_ENCAPSULATED_PRODUCT_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_CSP_SC_INFO_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_DL_PRIMARY_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_DL_ENCAPSULATED_PRODUCT_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_CL_PRIMARY_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_CL_ENCAPSULATED_PRODUCT_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_TP_PRIMARY_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_TP_OIDS_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_TP_ENCAPSULATED_PRODUCT_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_EMM_PRIMARY_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_AC_PRIMARY_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_KR_PRIMARY_RECORDTYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_MDS_SCHEMA_RELATIONS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_MDS_SCHEMA_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_MDS_SCHEMA_INDEXES'))
        self.assertFalse(hasattr(Security, 'CSSM_DB_ATTRIBUTE_MDS_START'))
        self.assertFalse(hasattr(Security, 'CSSM_DB_ATTRIBUTE_MDS_END'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_MODULE_ID'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_MANIFEST'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_MODULE_NAME'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_PATH'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_CDSAVERSION'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_VENDOR'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_DESC'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_INTERFACE_GUID'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_POLICY_STMT'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_EMMSPECVERSION'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_EMM_VERSION'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_EMM_VENDOR'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_EMM_TYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_SSID'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_SERVICE_TYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_NATIVE_SERVICES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_DYNAMIC_FLAG'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_MULTITHREAD_FLAG'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_SERVICE_MASK'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_CSP_TYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_CSP_FLAGS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_CSP_CUSTOMFLAGS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_USEE_TAGS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_CONTEXT_TYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_ALG_TYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_GROUP_ID'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_ATTRIBUTE_TYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_ATTRIBUTE_VALUE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_PRODUCT_DESC'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_PRODUCT_VENDOR'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_PRODUCT_VERSION'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_PRODUCT_FLAGS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_PRODUCT_CUSTOMFLAGS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_STANDARD_DESC'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_STANDARD_VERSION'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_READER_DESC'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_READER_VENDOR'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_READER_VERSION'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_READER_FWVERSION'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_READER_FLAGS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_READER_CUSTOMFLAGS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_READER_SERIALNUMBER'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_SC_DESC'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_SC_VENDOR'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_SC_VERSION'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_SC_FWVERSION'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_SC_FLAGS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_SC_CUSTOMFLAGS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_SC_SERIALNUMBER'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_DL_TYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_QUERY_LIMITS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_CONJUNCTIVE_OPS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_RELATIONAL_OPS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_PROTOCOL'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_CERT_TYPEFORMAT'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_CRL_TYPEFORMAT'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_CERT_FIELDNAMES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_BUNDLE_TYPEFORMAT'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_CERT_CLASSNAME'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_ROOTCERT'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_ROOTCERT_TYPEFORMAT'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_VALUE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_REQCREDENTIALS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_SAMPLETYPES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_ACLSUBJECTTYPES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_AUTHTAGS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_USEETAG'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_RETRIEVALMODE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_OID'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_XLATIONTYPEFORMAT'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_DEFAULT_TEMPLATE_TYPE'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_TEMPLATE_FIELD_NAMES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSAATTR_AUTHORITY_REQUEST_TYPE'))
        self.assertFalse(hasattr(Security, 'MDS_OBJECT_NUM_RELATIONS'))
        self.assertFalse(hasattr(Security, 'MDS_OBJECT_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_NUM_RELATIONS'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_CSSM_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_EMM_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_COMMON_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_CSP_PRIMARY_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_CSP_CAPABILITY_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_CSP_ENCAPSULATED_PRODUCT_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_CSP_SC_INFO_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_DL_PRIMARY_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_DL_ENCAPSULATED_PRODUCT_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_CL_PRIMARY_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_CL_ENCAPSULATED_PRODUCT_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_TP_PRIMARY_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_TP_OIDS_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_TP_ENCAPSULATED_PRODUCT_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_EMM_PRIMARY_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_AC_PRIMARY_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_SCHEMA_RELATONS_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_SCHEMA_ATTRIBUTES_NUM_ATTRIBUTES'))
        self.assertFalse(hasattr(Security, 'MDS_CDSADIR_SCHEMA_INDEXES_NUM_ATTRIBUTES'))

if __name__ == "__main__":
    main()
