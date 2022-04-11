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
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))

    def error_test(self, err: str) -> LockstepResponse[str]:
        """
        Generates an error code that your program may use to test
        handling of common types of error conditions.

        * If you specify `?err=500`, you will receive a 500 internal
        server error. * If you specify `?err=timeout`, the API will
        stall for 90 seconds and then return 200 OK. Many network
        connections will drop after 60 seconds of no activity. * If you
        do not specify any of these errors, the API will return 200 OK.

        The Error Test API allows you to test whether your client
        program is capable of handling certain types of error codes.
        Developers writing libraries may find it useful to create
        integration tests that verify that their code can correctly
        detect the difference between a validation error resulting in a
        400 error code, a network timeout resulting in a broken network
        connection, and a server error resulting in a 500 error code.
        You may use the Error Test API to verify that your code is able
        to identify and handle these cases correctly.

        Parameters
        ----------
        err : str
            The type of error test to execute. Supported error types:
            500, timeout
        """
        path = "/api/v1/Status/testing"
        result = self.client.send_request("GET", path, None, {"err": err}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, str(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult(**result.json()))
