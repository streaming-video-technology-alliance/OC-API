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

# Testbed

- testbed.yaml : derive from SVA_OC_openAPI.yaml and SVA_OC_CDNI_openapi.yaml to ease code generation for testbed  
	- Some naming has changed(remove upper cases from path and operationId, remove. and _ from type's names),  
	- Restrict endpoints to testbed functional scope  
	- Endpoint definitions have been concatenated in one single file  
	- Remove use of oneOf and allOf: this allows code generation with most of generators,  
	  since we lost this way some payload type, you'll have to add a few lines of code to decode payload and check type:  

Use :

```bash
make generate-server
make build-server
make launch-server
```
To test generation. 

Once server is launch, you are able to test the first request of below ewample workflow:

```bash
curl -X 'GET' \
  'http://localhost:8080/oc/fci/advertisement' \
  -H 'accept: application/cdni'
``

To see testbed.yaml in swagger editor:
```bash
make edit
``` 

Then access to http://localhost in browser.

#Testbed use case workflow example
## Workflow OC-APIs Test Bed Service Configuration 1
![alternative text](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/streaming-video-alliance/OC-API/try-to-generate-server/workflows/serviceconf1.txt?token=AMOK4S6ZL22DIAFTH2WDER3A53FZM)
  
## Workflow OC-APIs Test Bed Service Configuration 2
``` plantuml
```
  
## Workflow OC-APIs Test Bed Service Configuration 3
``` plantuml
```
  
## Workflow OC-APIs Test Bed End User service access With DNS Redirect
``` plantuml
```












