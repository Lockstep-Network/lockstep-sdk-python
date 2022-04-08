#
# Lockstep Platform SDK for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from lockstep.lockstep_response import LockstepResponse
from lockstep.error_result import ErrorResult
from lockstep.action_result_model import ActionResultModel
from lockstep.models.developeraccountsubmitmodel import DeveloperAccountSubmitModel
from lockstep.models.provisioningfinalizerequestmodel import ProvisioningFinalizeRequestModel
from lockstep.models.provisioningmodel import ProvisioningModel
from lockstep.models.provisioningresponsemodel import ProvisioningResponseModel

class ProvisioningClient:
    """
    API methods related to Provisioning
    """
    from lockstep.lockstep_api import LockstepApi

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
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ProvisioningResponseModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

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
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ProvisioningResponseModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

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
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))
