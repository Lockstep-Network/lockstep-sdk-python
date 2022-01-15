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


from dataclasses import dataclass

"""
Represents the response to either a successful or failed account 
provisioning
"""
@dataclass
class ProvisioningResponseModel:
    userName: str = None
    accountName: str = None
    userId: str = None
    groupKey: str = None
    appEnrollmentId: str = None
    syncRequestId: str = None
    errorMessage: str = None

