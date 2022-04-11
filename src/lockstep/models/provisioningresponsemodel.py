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


from dataclasses import dataclass

@dataclass
class ProvisioningResponseModel:
    """
    Represents the response to either a successful or failed account
    provisioning
    """

    userName: str | None = None
    accountName: str | None = None
    userId: str | None = None
    groupKey: str | None = None
    appEnrollmentId: str | None = None
    syncRequestId: str | None = None
    errorMessage: str | None = None

