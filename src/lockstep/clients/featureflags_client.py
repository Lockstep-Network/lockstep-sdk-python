#
# Lockstep Platform SDK for Python
#
# (c) 2021-2023 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2023 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from lockstep.lockstep_response import LockstepResponse
from lockstep.models.errorresult import ErrorResult
from lockstep.models.featureflagsrequestmodel import FeatureFlagsRequestModel
from lockstep.models.featureflagsresponsemodel import FeatureFlagsResponseModel

class FeatureFlagsClient:
    """
    API methods related to FeatureFlags
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_feature_flags(self, body: FeatureFlagsRequestModel) -> LockstepResponse[FeatureFlagsResponseModel]:
        """
        Retrieves the specified feature flags. True if they are enabled,
        false otherwise.

        Parameters
        ----------
        body : FeatureFlagsRequestModel

        """
        path = "/api/v1/feature-flags"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FeatureFlagsResponseModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
