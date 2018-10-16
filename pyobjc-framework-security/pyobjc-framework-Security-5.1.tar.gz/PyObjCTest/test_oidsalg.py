from PyObjCTools.TestSupport import *

import Security

class Testoidsalg (TestCase):

    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, 'CSSMOID_MD2'))
        self.assertFalse(hasattr(Security, 'CSSMOID_MD4'))
        self.assertFalse(hasattr(Security, 'CSSMOID_MD5'))
        self.assertFalse(hasattr(Security, 'CSSMOID_RSA'))
        self.assertFalse(hasattr(Security, 'CSSMOID_MD2WithRSA'))
        self.assertFalse(hasattr(Security, 'CSSMOID_MD4WithRSA'))
        self.assertFalse(hasattr(Security, 'CSSMOID_MD5WithRSA'))
        self.assertFalse(hasattr(Security, 'CSSMOID_SHA1WithRSA'))
        self.assertFalse(hasattr(Security, 'CSSMOID_SHA224WithRSA'))
        self.assertFalse(hasattr(Security, 'CSSMOID_SHA256WithRSA'))
        self.assertFalse(hasattr(Security, 'CSSMOID_SHA384WithRSA'))
        self.assertFalse(hasattr(Security, 'CSSMOID_SHA512WithRSA'))
        self.assertFalse(hasattr(Security, 'CSSMOID_SHA1WithRSA_OIW'))
        self.assertFalse(hasattr(Security, 'CSSMOID_RSAWithOAEP'))
        self.assertFalse(hasattr(Security, 'CSSMOID_OAEP_MGF1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_OAEP_ID_PSPECIFIED'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DES_CBC'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_DH_PUB_NUMBER'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_DH_STATIC'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_DH_ONE_FLOW'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_DH_EPHEM'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_DH_HYBRID1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_DH_HYBRID2'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_DH_HYBRID_ONEFLOW'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_MQV1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_MQV2'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_DH_STATIC_SHA1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_DH_ONE_FLOW_SHA1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_DH_EPHEM_SHA1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_DH_HYBRID1_SHA1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_DH_HYBRID2_SHA1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_MQV1_SHA1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ANSI_MQV2_SHA1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS3'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DH'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DSA  				// BSAFE only'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DSA_CMS  			// X509/CMS'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DSA_JDK  			// JDK 1.1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_SHA1WithDSA  		// BSAFE'))
        self.assertFalse(hasattr(Security, 'CSSMOID_SHA1WithDSA_CMS  	// X509/CMS'))
        self.assertFalse(hasattr(Security, 'CSSMOID_SHA1WithDSA_JDK  	// JDK 1.1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_SHA1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_SHA224'))
        self.assertFalse(hasattr(Security, 'CSSMOID_SHA256'))
        self.assertFalse(hasattr(Security, 'CSSMOID_SHA384'))
        self.assertFalse(hasattr(Security, 'CSSMOID_SHA512'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ecPublicKey'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ECDSA_WithSHA1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ECDSA_WithSHA224'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ECDSA_WithSHA256'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ECDSA_WithSHA384'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ECDSA_WithSHA512'))
        self.assertFalse(hasattr(Security, 'CSSMOID_ECDSA_WithSpecified'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_ISIGN'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_X509_BASIC'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_SSL'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_LOCAL_CERT_GEN'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_CSR_GEN'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_REVOCATION_CRL'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_REVOCATION_OCSP'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_SMIME'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_EAP'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_CODE_SIGN'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_SW_UPDATE_SIGNING'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_IP_SEC'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_ICHAT'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_RESOURCE_SIGN'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_PKINIT_CLIENT'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_PKINIT_SERVER'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_CODE_SIGNING'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_PACKAGE_SIGNING'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_MACAPPSTORE_RECEIPT'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_APPLEID_SHARING'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_TIMESTAMPING'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_REVOCATION'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_PASSBOOK_SIGNING'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_MOBILE_STORE'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_ESCROW_SERVICE'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_PROFILE_SIGNING'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_QA_PROFILE_SIGNING'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_TEST_MOBILE_STORE'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_PCS_ESCROW_SERVICE'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_TP_PROVISIONING_PROFILE_SIGNING'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_FEE'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_ASC'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_FEE_MD5'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_FEE_SHA1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_FEED'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_FEEDEXP'))
        self.assertFalse(hasattr(Security, 'CSSMOID_APPLE_ECDSA'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ_IDENTITY'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ_EMAIL_SIGN'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ_EMAIL_ENCRYPT'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ_ARCHIVE_LIST'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ_ARCHIVE_STORE'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ_ARCHIVE_FETCH'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ_ARCHIVE_REMOVE'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ_SHARED_SERVICES'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ_VALUE_USERNAME'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ_VALUE_PASSWORD'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ_VALUE_HOSTNAME'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ_VALUE_RENEW'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ_VALUE_ASYNC'))
        self.assertFalse(hasattr(Security, 'CSSMOID_DOTMAC_CERT_REQ_VALUE_IS_PENDING'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_DIGEST_ALG'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_ENCRYPT_ALG'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_HMAC_SHA1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_pbeWithMD2AndDES'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_pbeWithMD2AndRC2'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_pbeWithMD5AndDES'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_pbeWithMD5AndRC2'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_pbeWithSHA1AndDES'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_pbeWithSHA1AndRC2'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_PBKDF2'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_PBES2'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_PBMAC1'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_RC2_CBC'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_DES_EDE3_CBC'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS5_RC5_CBC'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS12_pbeWithSHAAnd128BitRC4'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS12_pbeWithSHAAnd40BitRC4'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS12_pbeWithSHAAnd3Key3DESCBC'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS12_pbeWithSHAAnd2Key3DESCBC'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS12_pbeWithSHAAnd128BitRC2CBC'))
        self.assertFalse(hasattr(Security, 'CSSMOID_PKCS12_pbewithSHAAnd40BitRC2CBC'))

if __name__ == "__main__":
    main()
