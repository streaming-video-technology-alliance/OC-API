OPENAPI_SPEC := SVA_OC_openAPI_extended.yaml
HTTP_PROXY_HOST = $(shell echo ${http_proxy} | sed 's/http:\/\/\(.*\):\([0-9]*\)\//\1/g' )
HTTP_PROXY_PORT = $(shell echo ${http_proxy} | sed 's/http:\/\/\(.*\):\([0-9]*\)\//\2/g' )


.PHONY: generate-server
generate-server:
	-sudo rm -rf ./out
#	docker run -v ${PWD}/out:/out -v ${PWD}:/specs -e  JAVA_TOOL_OPTIONS="-Dhttp.proxyHost=${HTTP_PROXY_HOST} -Dhttp.proxyPort=${HTTP_PROXY_PORT} -Dhttp.nonProxyHosts=localhost|127.0.0.1" openapitools/openapi-generator-cli:v5.1.0 generate -i /specs/${OPENAPI_SPEC} -g python-flask -o /out 
	docker run -v ${PWD}/out:/out -v ${PWD}:/specs -e  JAVA_TOOL_OPTIONS="-Dhttp.proxyHost=${HTTP_PROXY_HOST} -Dhttp.proxyPort=${HTTP_PROXY_PORT} -Dhttp.nonProxyHosts=localhost|127.0.0.1" openapitools/openapi-generator-cli generate -i /specs/${OPENAPI_SPEC} -g python-flask -o /out 
.PHONY: build-server
build-server:
	docker build -f ./out/Dockerfile --build-arg=http_proxy=${http_proxy} --build-arg=https_proxy=${https_proxy} -t openapi-server ./out

.PHONY: launch-server
launch-server:
	-docker rm -f openapi-server
	docker run --name=openapi-server -p 8080:8080 openapi-server 

.PHONY: edit
edit:
	docker run -d -p 80:8080 -v $(pwd):/tmp -e SWAGGER_FILE=/tmp/${OPENAPI_SPEC} swaggerapi/swagger-editor
