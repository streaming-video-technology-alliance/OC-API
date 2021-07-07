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

``` plantuml
@startuml
skinparam ParticipantPadding 30
skinparam BoxPadding 20

box "UCDN" #LightBlue
  participant "OC_FCI client" as OCFCI_client
end box

box "DCDN" #AntiqueWhite
  participant "OC_Auth API" as OCAUTH_api
  participant "OC_FCI API" as OCFCI_api
end box

== Login to OC_FCI API ==

== Get Advertisement ==

OCFCI_client -> OCFCI_api: ""GET /oc/fci/advertisement""
activate  OCFCI_api #FFBBBB


OCFCI_api -> OCFCI_client: ""200 OK""
deactivate OCFCI_api
rnote left of OCFCI_api
{
  "capabilities": [
    {
      "capability-type": "FCI.DeliveryProtocol",
      "footprints": [
        {
          "footprint-type": "ipv4cidr",
          "footprint-value": [
            "192.168.1.1/32"
          ]
        }
      ],
      "capability-value": {
        "delivery-protocols": [
          "http1.1","http1.2","http/2"
        ]
      }
    },
    {
      "capability-type": "FCI.RedirectionMode",
      "footprints": [
        {
          "footprint-type": "ipv4cidr",
          "footprint-value": [
            "192.168.1.1/32"
          ]
        }
      ],
      "capability-value": "HTTP-I"
    },
    {
      "capability-type": "FCI.Metadata",
      "capability-value": {
        "metadata": [
          "MI.SourceMetadata",
          "MI.LocationACL",
          "MI.ProtocolACL",
          "MI.FallbackTarget"
        ]
      },
      "footprints": [
        {
          "footprint-type": "ipv4cidr",
          "footprint-value": [
            "192.168.1.0/24"
          ]
        }
      ]
    }
  ]
}
end rnote
@enduml
```
  
## Workflow OC-APIs Test Bed Service Configuration 2
``` plantuml
@startuml
skinparam ParticipantPadding 60
skinparam BoxPadding 100

box "UCDN" #LightBlue
  participant "OC_COI API" as OCCOI_client
end box

box "DCDN" #AntiqueWhite
  participant "OC_COI_simple" as OCCOI_api
  participant "CDN Orange Manager(AMC)" as AMC
end box

== Put Configuration ==

OCCOI_client -> OCCOI_api: ""PUT /oc/ci/configuration""
activate  OCCOI_api #FFBBBB
rnote right of OCCOI_client
{
  "hosts": [
    {
      "host": "192.168.1.106",
      "host-metadata": {
        "metadata": [
          {
            "generic-metadata-type": "MI.FallbackTarget",
            "generic-metadata-value": {
              "host": "vod-akc-na-east-1.media.dssott.com"
            }
          }
        ],
        "paths": [
          {
            "path-metadata": {
              "metadata": [
                {
                  "generic-metadata-type": "MI.SourceMetadata",
                  "generic-metadata-value": {
                    "sources": [
                      {
                        "endpoints": [
                          "http://vod-akc-na-east-1.media.dssott.com"
                        ]
                      }
                    ]
                  }
                }
              ]
            },
            "path-pattern": {
              "case-sensitive": true,
              "pattern": "/ps01/disney/test/*"
            }
          }
        ]
      }
    }
  ]
}
end rnote

OCCOI_api -> AMC: create Prefix disney.ak2.inter-cdnrd.orange-business.com on AMC, may be origin server if necessary....
AMC -> OCCOI_api: Return result of configuration (200 if OK)

OCCOI_api -> OCCOI_client: ""200 OK""
deactivate OCCOI_api
rnote left of OCCOI_api
TO BE FILLED
MUST CONTAIN CDN prefixe created on dCDN side (disney.ak2.inter-cdnrd.orange-business.com)
This way, UCDN will know where to redirect client for this service
end rnote

@enduml
```
  
## Workflow OC-APIs Test Bed Service Configuration 3
``` plantuml
@startuml
skinparam ParticipantPadding 100
skinparam BoxPadding 100

box "UCDN" #LightBlue
  participant "OC_FCI client" as OCFCI_client
end box

box "DCDN" #AntiqueWhite
  participant "OC_FCI API" as OCFCI_api
end box

== Get Advertisement ==

OCFCI_client -> OCFCI_api: ""GET /oc/fci/advertisement""
activate  OCFCI_api #FFBBBB


OCFCI_api -> OCFCI_client: ""200 OK""
deactivate OCFCI_api
rnote left of OCFCI_api
{
  "capabilities": [
    {
      "capability-type": "FCI.DeliveryProtocol",
      "footprints": [
        {
          "footprint-type": "ipv4cidr",
          "footprint-value": [
            "192.168.1.1/32"
          ]
        }
      ],
      "capability-value": {
        "delivery-protocols": [
          "http1.1","http1.2","http/2"
        ]
      }
    },
    {
      "capability-type": "FCI.RedirectionMode",
      "footprints": [
        {
          "footprint-type": "ipv4cidr",
          "footprint-value": [
            "192.168.1.1/32"
          ]
        }
      ],
      "capability-value": "HTTP-I"
    },
    {
      "capability-type": "FCI.Metadata",
      "capability-value": {
        "metadata": [
          "MI.SourceMetadata",
          "MI.LocationACL",
          "MI.ProtocolACL",
          "MI.FallbackTarget"
        ]
      },
      "footprints": [
        {
          "footprint-type": "ipv4cidr",
          "footprint-value": [
            "192.168.1.0/24"
          ]
        }
      ]
    },
    {
      "capability-type": "FCI.RedirecTarget",
      "capability-value": {
        "redirecting-hosts": [
          "192.168.1.106"
        ],
        "http-target": {
          "host": "disney.ak2.inter-cdnrd.orange-business.com",
          "include-redirecting-host": false
        }
      },
      "footprints": [
        {
          "footprint-type": "ipv4cidr",
          "footprint-value": [
            "192.168.1.0/24"
          ]
        }
      ]
    }
  ]
}

end rnote
@enduml
```
  
## Workflow OC-APIs Test Bed End User service access With DNS Redirect
``` plantuml
@startuml

skinparam ParticipantPadding 60
skinparam BoxPadding 60

box "User" #Yellow
  participant "Final User (HTTP client)" as FU
end box

box "UCDN" #LightBlue
  participant "User Redirect Module" as UR
end box

box "DCDN" #AntiqueWhite
  participant "Request Router" as RR
  participant "Cache" as CC
  participant "Origin Server" as OS
end box

FU -> UR: ""GET http://192.168.1.106(UCDN ip)/ps01/disney/test/hd_avc_master_all.m3u8""
UR -> FU: ""HTTP1.1 Moved Permanently Location: http://disney.ak2.inter-cdnrd.orange-business.com/ps01/disney/test/hd_avc_master_all.m3u8""
FU -> RR: ""DNS Request for fqdn disney.ak2.inter-cdnrd.orange-business.com""
activate RR
RR -> FU: ""DNS response with cache IP""
deactivate RR
FU -> CC: ""GET http://(cache ip)/ps01/disney/test/hd_avc_master_all.m3u8""
CC -> OS:""GET http://vod-akc-na-east-1.media.dssott.com(Origin fqdn)/ps01/disney/test/hd_avc_master_all.m3u8""
OS -> CC: ""Return content""
CC -> FU: ""Return content""
@enduml
```












