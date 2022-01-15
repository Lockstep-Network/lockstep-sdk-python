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
Represents the status of a user's credentials
"""
@dataclass
class StatusModel:
    userName: str = None
    accountName: str = None
    accountCompanyId: str = None
    userId: str = None
    groupKey: str = None
    loggedIn: bool = None
    errorMessage: str = None
    roles: list[str] = None
    lastLoggedIn: str = None
    apiKeyId: str = None
    userStatus: str = None
    environment: str = None
    version: str = None
    dependencies: object = None

