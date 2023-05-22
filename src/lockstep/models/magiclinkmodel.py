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
class MagicLinkModel:
    """
    Represents a magic link that can be used to log in to a Lockstep
    application.
    """

    magicLinkId: object | None = None
    groupKey: object | None = None
    userId: object | None = None
    userRole: object | None = None
    applicationId: object | None = None
    expires: object | None = None
    revoked: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    companyId: object | None = None
    accountingProfileId: object | None = None
    magicLinkUrl: object | None = None
    user: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
