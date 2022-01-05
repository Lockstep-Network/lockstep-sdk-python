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
# @version    2021.39
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#




"""
Represents the status of a user's credentials
"""
class StatusModel:
    userName: str
    accountName: str
    accountCompanyId: str
    userId: str
    groupKey: str
    loggedIn: bool
    errorMessage: str
    roles: list[str]
    lastLoggedIn: str
    apiKeyId: str
    userStatus: str
    dependencies: object

