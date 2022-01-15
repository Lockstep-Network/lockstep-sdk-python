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
# @version    2022.2
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from lockstep.lockstep_response import LockstepResponse
from lockstep.models.provisioningmodel import ProvisioningModel
from lockstep.models.provisioningfinalizerequestmodel import ProvisioningFinalizeRequestModel

class ProvisioningClient:

    def __init__(self, client):
        self.client = client

    """
    Creates a new User or updates an Invited user based on metadata 
    provided by the User during the onboarding process

    Parameters
    ----------
    body : ProvisioningModel
        Represents a User and their related metadata
    """
    def provision_user_account(self, body: ProvisioningModel) -> LockstepResponse:
        path = f"/api/v1/Provisioning"
        return self.client.send_request("POST", path, body, {body: ProvisioningModel})

    """
    Updates user, company and group metadata for a User of status 
    'Onboarding' and finalizes a user's onboarding process by changing 
    the user status to 'Active'

    Parameters
    ----------
    body : ProvisioningFinalizeRequestModel
        Represents a User and their related metadata
    """
    def finalize_user_account_provisioning(self, body: ProvisioningFinalizeRequestModel) -> LockstepResponse:
        path = f"/api/v1/Provisioning/finalize"
        return self.client.send_request("POST", path, body, {body: ProvisioningFinalizeRequestModel})
