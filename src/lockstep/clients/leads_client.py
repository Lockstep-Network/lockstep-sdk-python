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
from lockstep.models.leadmodel import LeadModel

class LeadsClient:
    """
    API methods related to Leads
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def create_leads(self, body: list[object]) -> LockstepResponse[list[LeadModel]]:
        """
        Creates one or more Leads within the Lockstep platform and
        returns the records as created.

        A Lead is a person who is interested in the Lockstep platform
        but needs certain new features in order to use it. If you are
        interested in the Lockstep platform, you can create a lead with
        your information and our team will prioritize the feature you
        need.

        Parameters
        ----------
        body : list[object]
            The Leads to create
        """
        path = "/api/v1/Leads"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [LeadModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
