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
from lockstep.models.leadmodel import LeadModel

class LeadsClient:

    def __init__(self, client):
        self.client = client

    """
    Creates one or more Leads within the Lockstep platform and returns 
    the records as created. 

    A Lead is a person who is interested in the Lockstep platform but 
    needs certain new features in order to use it. If you are interested 
    in the Lockstep platform, you can create a lead with your 
    information and our team will prioritize the feature you need.

    Parameters
    ----------
    body : list[LeadModel]
        The Leads to create
    """
    def create_leads(self, body: list[LeadModel]) -> LockstepResponse:
        path = f"/api/v1/Leads"
        return self.client.send_request("POST", path, body, {body: list[LeadModel]})
