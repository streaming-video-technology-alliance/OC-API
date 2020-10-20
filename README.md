# OC-API
OpenAPI descriptions of the SVA Open Caching interface based on CDNI modeling (RFC8006, RFC8007, RFC8008, RFC8804) and SVA extensions

- README.md: this file
- SVA_OC_openAPI.yaml : the API acording to SVA (and some interpretations/additions)
- SVA_OC_CDNI_openapi.yaml : the OpenAPI/json schemas according to CDNI (RFC8006, RFC8007, RFC8008, RFC8804)
- SVA_OC_CDNI_openapi_extended.yaml : gathers new SVA specific and CDNI extended (inherited from SVA_OC_CDNI_openapi.yaml) OpenAPI/json schemas 

This is an ongoing work. The idea is that new schemas can be added refrering to the CDNI or CDNI_extended once validated

# Format
The files are JSON objects, yaml formated according to the OpenAPI specification (http://spec.openapis.org/oas/v3.0.3)
# Viewing/editing
The files can be viewed/edited through the swagger tooling and/or a code editor (like Visual Studio) equiped with the Yaml language support and/or the swagger validator.


