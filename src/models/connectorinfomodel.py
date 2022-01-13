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
Represents all possible data required to set up an app enrollment for a 
connector. Only send required fields for the given connector.
"""
@dataclass
class ConnectorInfoModel:
    authCode: str = None
    realmId: str = None
    redirectUri: str = None
    email: str = None

