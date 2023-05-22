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
from lockstep.models.statusmodel import StatusModel

class StatusClient:
    """
    API methods related to Status
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def ping(self, ) -> LockstepResponse[StatusModel]:
        """
        Verifies that your application can successfully call the
        Lockstep Platform API and returns a successful code regardless
        of your authentication status or permissions.

        The Ping API can be used to verify that your app is working
        correctly. The Ping API will always return 200 OK. If you call
        this API and you receive a code other than 200 OK, you should
        check your network connectivity. A response code of anything
        other than 200 means that a routing issue or proxy issue may
        prevent your application from reaching the Lockstep API

        Parameters
        ----------
        """
        path = "/api/v1/Status"
        result = self.client.send_request("GET", path, None, None, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, StatusModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
