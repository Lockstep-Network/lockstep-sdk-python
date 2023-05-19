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
from lockstep.models.actionresultmodel import ActionResultModel
from lockstep.models.developeraccountsubmitmodel import DeveloperAccountSubmitModel

class ProvisioningClient:
    """
    API methods related to Provisioning
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def provision_free_developer_account(self, body: DeveloperAccountSubmitModel) -> LockstepResponse[ActionResultModel]:
        """
        Creates a new account for a developer, sending an email with
        information on how to access the API.

        Parameters
        ----------
        body : DeveloperAccountSubmitModel

        """
        path = "/api/v1/Provisioning/free-account"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ActionResultModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
