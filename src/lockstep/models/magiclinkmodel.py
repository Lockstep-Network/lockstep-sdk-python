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
from lockstep.models.useraccountmodel import UserAccountModel

@dataclass
class MagicLinkModel:
    """
    Represents a magic link that can be used to log in to a Lockstep
    application.
    """

    magicLinkId: str | None = None
    groupKey: str | None = None
    userId: str | None = None
    userRole: str | None = None
    applicationId: str | None = None
    expires: str | None = None
    revoked: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    companyId: str | None = None
    accountingProfileId: str | None = None
    magicLinkUrl: str | None = None
    user: UserAccountModel | None = None

