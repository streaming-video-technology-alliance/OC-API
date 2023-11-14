# Changes in v2 (compared to v1.1)

## Changes in MI Objects

Modified property type from string to MI_SecretValue:
- MI.HeaderAuth, property header-value
- MI.AWSv4Auth, property secret-access-key

Default values for MI.CachePolicy properties external and internal: as-is

Changed property name:
- MI.StaleContentCachePolicy: failed-refresh-ttl to failed-revalidation-delta-seconds

Modified description/type of property failover-errors in MI.SourceExtended:
- failover-errors: HTTP error codes now supporting more generic string including 4xx and 5xx

## Added properties in existing MI objects

Added properties in MI_SourceExtended:
- connection-control
- http-code-failover
- endpoint-detention

Added properties in MI_CrossoriginPolicy:
- no-origin-response-headers
- apply-to-all-methods

Added properties in MI_SourceMetadataExtended:
- source-detention

Added properties in MI_CrossOriginPolicy:
- max-age
- preflight-only (removed apply-to-all-methods)

## Added MI objects

Object related to processing stages:
- MI_ClientRequestStage
- MI_OriginRequestStage
- MI_OriginResponseStage
- MI_ClientResponseStage
- MI_MatchGroup

Object related to processing delivery metadata:
- MI_MediaServiceDescription

Objects related to protected secrets:
- MI_SecretStore
- MI_SecretStoreTypeVault
- MI_SecretStoreTypeHashiCorpVault
- MI_SecretValue
- MI_SecretCertificate

Objects related to edge control:
- MI_ClientConnectionControl

Objects related to source access control:
- MI_EndpointDetention
- MI_EndpointDetentionTrigger
- MI_EndpointRepeatingFailures
- MI_HTTPErrorCodeTrigger
- MI_SourceDetention
- MI_DetentionFullBehavior
- MI_DetentionResetBehavior
- MI_SourceConnectionControl
- MI_SourceByteReadTimeoutActions
- MI_SourceTimeoutActions
- MI_SourceConnectionRetries
- MI_HTTPCodeFailover
- MI_HTTPCodeReforwards

Objects related to MEL:
- MI_SetVariable

Objects related to client access control:
- MI_CertificateMetadata
- MI_EncryptionLevelMetadata
- MI_CertificateCredentialsMetadata
- MI_LocationACLExtended
- MI_LocationRuleExtended
- MI_TimeWindowAclExtended
- MI_TimeWindowRuleExtended
- MI_ClientAuthMetadata
- MI_CATAuth
- MI_CATTokenLocator
- MI_CATTokenConfiguration
- MI_CATTokenVerificationAction
- MI_CATTokenDefinedResponse
- MI_CATIF
- MI_CATTokenObject

Objects related to NamedPrivateFeatures:
- MI.NamedPrivateFeatureType
- MI_NamedPrivateFeatureValue

## Deprecated objects
- MI.RequestedCapacityLimits
- MI.RequestedCapacityLimit
