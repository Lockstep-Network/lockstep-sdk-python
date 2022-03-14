#
# Lockstep Software Development Kit for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Ted Spence <tspence@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from src.lockstep.lockstep_api import LockstepApi
from src.lockstep.lockstep_response import LockstepResponse
from src.lockstep.action_result_model import ActionResultModel
from src.lockstep.models.developeraccountsubmitmodel import DeveloperAccountSubmitModel
from src.lockstep.models.provisioningfinalizerequestmodel import ProvisioningFinalizeRequestModel
from src.lockstep.models.provisioningmodel import ProvisioningModel
from src.lockstep.models.provisioningresponsemodel import ProvisioningResponseModel

class ProvisioningClient:
    """
    Lockstep Platform methods related to Provisioning
    """

    def __init__(self, client: LockstepApi):
        self.client = client

    def provision_user_account(self, body: ProvisioningModel) -> LockstepResponse[ProvisioningResponseModel]:
        """
        Creates a new User or updates an Invited user based on metadata
        provided by the User during the onboarding process

        Parameters
        ----------
        body : ProvisioningModel
            Represents a User and their related metadata
        """
        path = "/api/v1/Provisioning"
        result = self.client.send_request("POST", path, body, {})
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, result.json(), None)
        else:
            return LockstepResponse(False, result.status_code, None, result.json())

    def finalize_user_account_provisioning(self, body: ProvisioningFinalizeRequestModel) -> LockstepResponse[ProvisioningResponseModel]:
        """
        Updates user, company and group metadata for a User of status
        'Onboarding' and finalizes a user's onboarding process by
        changing the user status to 'Active'

        Parameters
        ----------
        body : ProvisioningFinalizeRequestModel
            Represents a User and their related metadata
        """
        path = "/api/v1/Provisioning/finalize"
        result = self.client.send_request("POST", path, body, {})
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, result.json(), None)
        else:
            return LockstepResponse(False, result.status_code, None, result.json())

    def provision_free_developer_account(self, body: DeveloperAccountSubmitModel) -> LockstepResponse[ActionResultModel]:
        """
        Creates a new account for a developer, sending an email with
        information on how to access the API.

        Parameters
        ----------
        body : DeveloperAccountSubmitModel

        """
        path = "/api/v1/Provisioning/free-account"
        result = self.client.send_request("POST", path, body, {})
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, result.json(), None)
        else:
            return LockstepResponse(False, result.status_code, None, result.json())
