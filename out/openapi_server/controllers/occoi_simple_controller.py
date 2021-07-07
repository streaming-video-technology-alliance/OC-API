import connexion
import six

from openapi_server.models.mi_host_index import MIHostIndex  # noqa: E501
from openapi_server import util


def oc_ci_configure(mi_host_index):  # noqa: E501
    """Communicates the metadata/configuration (RFC8006 + RFC8804) to the ISP with a simple API

    To be used when the metadata to communicate is pseudo static and simple. The ISP (dCDN) processes the request and answers immediately. For a more complex metadata then use the CI API. # noqa: E501

    :param mi_host_index: the metadata(configuration) to be considered/processed by the ISP According to SVA OpenCaching specification and CDNI RFCs 8006/8804. It is the entire dataset (HostIndex)
    :type mi_host_index: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        mi_host_index = MIHostIndex.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
