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


from dataclasses import dataclass

@dataclass
class ConnectorInfoModel:
    """
    Represents all possible data required to set up an app enrollment
    for a connector. Only send required fields for the given connector.
    """

    authCode: object | None = None
    tokenId: object | None = None
    tokenSecret: object | None = None
    realmId: object | None = None
    subsidiaryId: object | None = None
    redirectUri: object | None = None
    email: object | None = None
    username: object | None = None
    password: object | None = None
    serverName: object | None = None
    serverPort: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
