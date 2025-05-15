# OC-API
OpenAPI descriptions of the SVA Open Caching interface based on CDNI modeling ([RFC8006], [RFC8007], [RFC8008], [RFC8804]) and SVTA specifications. It is recommended to read first the Open Caching Architecture document (SVTA2051) for a better understanding of the Open Caching eco-system.
The list of files is listed here with for each the corresponding SVTA specification number when appropriate.
- README.md: this file
- SVTA_OC_openAPI_BOI.yaml (SVTA2060): the Bootstrap API allowing the uCDN to get the available versions and corresponding API/URLs for each interface. 
- SVTA_OC_openAPI_FCI.yaml (SVTA2045): the Footprint And Capabilities Interface allowing the dCDN to expose its CDN capabilities and footprint to any uCDN
- SVTA_OC_openAPI_COI.yaml (SVTA2028-SVTA2030, SVTA2040-SVTA2042): The COnfiguration Interface allowing the uCDN to provision streaming delegation to a dCDN.
    - SVTA_OC_openAPI_COI_2a.yaml (SVTA2031): the Metadata Expression Language (MEL)
    - SVTA_OC_openAPI_COI_2b.yaml (SVTA2032): Processing Stages Metadata
    - SVTA_OC_openAPI_COI_2c.yaml (SVTA2033): Cache Control Metadata
    - SVTA_OC_openAPI_COI_2d.yaml (SVTA2034): Source Access Control Metadata 
    - SVTA_OC_openAPI_COI_2e.yaml (SVTA2035): Client Access Control Metadata
    - SVTA_OC_openAPI_COI_2f.yaml (SVTA2036): Edge Control Metadata
    - SVTA_OC_openAPI_COI_2g.yaml (SVTA2037): Delivery Metadata
    - SVTA_OC_openAPI_COI_2h.yaml (SVTA2038): Private Features Metadata
    - SVTA_OC_openAPI_COI_2i.yaml (SVTA2039): Protected Secrets Metadata
- SVTA_OC_openAPI_LOI.yaml (SVTA2050): the Logging Interface exposed by the dCDN baed on [RFC7937]
- SVTA_OC_openAPI_RRI.yaml (SVTA2048): The Request Routing Interface allowing the streaming delegation through the recursive mode of operations.

This is an ongoing work.
# Format
The files are JSON objects, yaml formated according to the OpenAPI specification (http://spec.openapis.org/oas/v3.0.3)
# Viewing/editing
The files can be viewed/edited through the swagger tooling and/or a code editor (like Visual Studio) equiped with the Yaml language support and/or an OpenAPI validator.
# Versions
There are three branches: COI_v1.1, COI_v2.0 and COI_v2.1 (the default one). COI_v1.1 version is associated with the SVTA Configuration interface 1.1 (first published version). COI_v2.0 is associated with SVTA Configuration interface 2.x versions. COI_v2.1 is associated with the Configuration interface v2.1. Also COI v2.1 proposes a completely new OpenAPI files distribution aligned with the SVTA Open Caching documentation . Before COI_v2.1 only 3 files contained the complete data model including the REST API definition whereas the last branch COI_v2.1 contains one yaml file per Interface with the exception of the configuration Interface that gathers 10 files. Each openAPI file exhibits a version number it is compliant with and that corresponds to the document version number it is attached to.
# Contributing
Everyone (including those with read access) can contribute through a pull request. Fork the repository and create a branch from the default one, keep it as much as possible in sync with the main default one (rebase). You should check that the pull request merge properly with the default main branch. You can ask for a review from one particular maintainer and/or from anyone. The pull request should mention the prefered maintainer for handling the pull request
There is a list of the repository maintainers (maintainers.md) that can deal with pull requests.
# licence
This work is licensed under the XXX licence. All contributions should be licences under the same XXX licence.
