import connexion
import six

from openapi_server.models.advertisement import Advertisement  # noqa: E501
from openapi_server import util
from openapi_server.models.mi_protocol import MIProtocol
from openapi_server.models.fci_capabilitytype import FCICapabilitytype
from openapi_server.models.fci_delivery_protocol import FCIDeliveryProtocol
from openapi_server.models.fci_redirection_mode import FCIRedirectionMode
from openapi_server.models.fci_redirectionmodevalue import FCIRedirectionmodevalue
from openapi_server.models.mi_footprint import MIFootprint
from openapi_server.models.mi_footprinttype import MIFootprinttype
from openapi_server.models.fci_genericbase import FCIGenericbase
from openapi_server.models.mi_footprinttype import MIFootprinttype
from openapi_server.models.fci_metadata import FCIMetadata
from openapi_server.models.mi_payloadtype import MIPayloadtype




def oc_fci_get_advertisement():  # noqa: E501
    """get the FCI advertisements according to SVA and CDNI (RFC8008/RFC8804)

    This operation is used to pull the FCI advertisement related to the requester (identified thanks to the security token obtained) # noqa: E501


    :rtype: Advertisement
    """
    fcidp=FCIGenericbase(capability_type=FCICapabilitytype.DELIVERYPROTOCOL,capability_value=FCIDeliveryProtocol(delivery_protocols=[MIProtocol.HTTP_1_1,MIProtocol.HTTPS_1_1,MIProtocol.HTTP_2]),footprints=[MIFootprint(footprint_type=MIFootprinttype.IPV4CIDR,footprint_value=["192.168.1.1/32"])])


    fcirm=FCIGenericbase(capability_type=FCICapabilitytype.REDIRECTIONMODE,capability_value=FCIRedirectionMode(redirection_modes=[FCIRedirectionmodevalue.HTTP_I]),footprints=[MIFootprint(footprint_type=MIFootprinttype.IPV4CIDR,footprint_value=["192.168.1.1/32"])])

    fcim=FCIGenericbase(capability_type=FCICapabilitytype.METADATA,capability_value=FCIMetadata(metadata=[MIPayloadtype.SOURCEMETADATA,MIPayloadtype.LOCATIONACL,MIPayloadtype.PROTOCOLACL,MIPayloadtype.FALLBACKTARGET]),footprints=[MIFootprint(MIFootprinttype.IPV4CIDR,footprint_value=["192.168.1.0/24"])])



    ad = Advertisement(capabilities=[fcidp,fcirm,fcim])




    return ad
