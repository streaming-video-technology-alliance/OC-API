# Changes in v2 (compared to v1.1)

## Changes in MI Objects

Modified property type from string to MI_SecretValue:
- MI.HeaderAuth, property header-value
- MI.AWSv4Auth, property secret-access-key

Changed property name:
- from "headers" to "header-transform" in MI.RequestTransform and MI_ResponseTransform

Modified property type MI.StageRules:
- Modified stage-metadata type from array of MI_StageMetadata to MI_StageMetadata

## Added properties in existing MI objects

Added properties in MI_SourceExtended:
- connection-control
- http-code-failover
- endpoint-detention

## Added MI objects

Objects related to protected secrets:
- MI_SecretStore
- MI_SecretStoreTypeVault
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

Objects related to NamedPrivateFeatures:
- MI.NamedPrivateFeatureType
- MI_NamedPrivateFeatureValue