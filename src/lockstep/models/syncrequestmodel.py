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
# @version    2022.4
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class SyncRequestModel:
    """
    Represents a user request to sync data
    """

    syncRequestId: str = None
    groupKey: str = None
    statusCode: str = None
    processResultMessage: str = None
    appEnrollmentId: str = None
    created: str = None
    modified: str = None
    modifiedUserId: str = None
    details: object = None

