# OC-API
OpenAPI descriptions of the SVA Open Caching interface based on CDNI modeling (RFC8006, RFC8007, RFC8008, RFC8804) and SVA extensions

- README.md: this file
- SVA_OC_openAPI.yaml : the API acording to SVA (and some interpretations/additions)
- SVA_OC_CDNI_openapi.yaml : the OpenAPI/json schemas according to CDNI (RFC8006, RFC8007, RFC8008, RFC8804)
- SVA_OC_CDNI_SVA_openapi.yaml (under construction): gathers new SVA specific and CDNI extended (inherited from SVA_OC_CDNI_openapi.yaml) OpenAPI/json schemas according to SVA OC "Configuration" and "Capacity insight" subgroups specification 
This is an ongoing work.
# Format
The files are JSON objects, yaml formated according to the OpenAPI specification (http://spec.openapis.org/oas/v3.0.3)
# Viewing/editing
The files can be viewed/edited through the swagger tooling and/or a code editor (like Visual Studio) equiped with the Yaml language support and/or the swagger validator.
# Versions
There are two branches: COI_v1.1 and COI_v2.0 (the default one). COI_v1.1 version is associated with the SVTA Configuration interface 1.1 (first published version). COI_v2.0 is associated with SVTA Configuration interface 2.x versions. Any significant enhancement might be potentially the subject of a labeling. 
# Contributing
Everyone (including those with read access) can contribute through a pull request. Fork the repository and create a branch from the default one, keep it as much as possible in sync with the main default one (rebase). You should check that the pull request merge properly with the default main branch. You can ask for a review from one particular maintainer and/or from anyone. The pull request should mention the prefered maintainer for handling the pull request
There is a list of the repository maintainers (maintainers.md) that can deal with pull requests.
# licence
This work is licensed under the XXX licence. All contributions should be licences under the same XXX licence.
