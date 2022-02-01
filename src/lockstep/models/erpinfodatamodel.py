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
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class ErpInfoDataModel:
    """
    Represents all the possible data sent as a part of the provisioning
    post. Only send required fields for the given connector.
    """

    authCode: str = None
    realmId: str = None
    redirectUri: str = None

