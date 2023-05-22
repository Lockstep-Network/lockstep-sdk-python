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
class AccountingProfileContactModel:
    """
    An Accounting Profile Contact has a link to a Contact that is
    associated with your company's Accounting Profile. These Contacts
    are secondary contacts to the primary that is on the profile.
    """

    accountingProfileContactId: object | None = None
    accountingProfileId: object | None = None
    contactId: object | None = None
    isPrimary: object | None = None
    groupKey: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
