# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PlaceDigestPlaceDigestGHGMonthlyResponseDTOGHGScopeDTO(Model):
    """PlaceDigestPlaceDigestGHGMonthlyResponseDTOGHGScopeDTO.

    :param ghg_scope_id: GHG scope identifier
    :type ghg_scope_id: int
    :param ghg_scope_code: GHG scope code
    :type ghg_scope_code: str
    :param ghg_scope_info: GHG scope info
    :type ghg_scope_info: str
    :param target_comparison: The target monthly info
    :type target_comparison:
     ~energycap.sdk.models.PlaceDigestPlaceDigestGHGMonthlyResponseDTOTargetComparisonDTO
    :param results: An array of monthly data
    :type results:
     list[~energycap.sdk.models.PlaceDigestPlaceDigestGHGMonthlyResponseDTOResultsDTO]
    """

    _attribute_map = {
        'ghg_scope_id': {'key': 'ghgScopeId', 'type': 'int'},
        'ghg_scope_code': {'key': 'ghgScopeCode', 'type': 'str'},
        'ghg_scope_info': {'key': 'ghgScopeInfo', 'type': 'str'},
        'target_comparison': {'key': 'targetComparison', 'type': 'PlaceDigestPlaceDigestGHGMonthlyResponseDTOTargetComparisonDTO'},
        'results': {'key': 'results', 'type': '[PlaceDigestPlaceDigestGHGMonthlyResponseDTOResultsDTO]'},
    }

    def __init__(self, ghg_scope_id=None, ghg_scope_code=None, ghg_scope_info=None, target_comparison=None, results=None):
        super(PlaceDigestPlaceDigestGHGMonthlyResponseDTOGHGScopeDTO, self).__init__()
        self.ghg_scope_id = ghg_scope_id
        self.ghg_scope_code = ghg_scope_code
        self.ghg_scope_info = ghg_scope_info
        self.target_comparison = target_comparison
        self.results = results
