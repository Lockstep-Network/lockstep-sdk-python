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
class UserAccountModel:
    """
    A User represents a person who has the ability to authenticate
    against the Lockstep Platform and use services such as Lockstep
    Inbox. A User is uniquely identified by an Azure identity, and each
    user must have an email address defined within their account. All
    Users must validate their email to make use of Lockstep platform
    services. Users may have different privileges and access control
    rights within the Lockstep Platform.
    """

    userId: object | None = None
    groupKey: object | None = None
    userName: object | None = None
    email: object | None = None
    status: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    modifiedUserName: object | None = None
    b2CUserId: object | None = None
    userRole: object | None = None
    inviteSent: object | None = None
    phoneNumber: object | None = None
    faxNumber: object | None = None
    title: object | None = None
    accountingRoleCodeDefId: object | None = None
    address1: object | None = None
    address2: object | None = None
    address3: object | None = None
    city: object | None = None
    stateRegion: object | None = None
    postalCode: object | None = None
    country: object | None = None
    timeZone: object | None = None
    imageURL: object | None = None
    description: object | None = None
    b2CLastLoggedIn: object | None = None
    defaultCurrencyCode: object | None = None
    locale: object | None = None
    notes: list[object] | None = None
    attachments: list[object] | None = None
    customFieldValues: list[object] | None = None
    accountingRoleCodeDefinition: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
