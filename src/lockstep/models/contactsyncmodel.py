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
class ContactSyncModel:
    """
    The ContactSyncModel represents information coming into Lockstep
    from an external financial system or other enterprise resource
    planning system. To import data from an external system, convert
    your original data into the ContactSyncModel format and call the
    [Upload Sync File API](https://developer.lockstep.io/reference/post_api-v1-sync-zip).
    This API retrieves all of the data you uploaded in a compressed ZIP
    file and imports it into the Lockstep platform. Once imported, this
    record will be available in the Lockstep API as a
    [ContactModel](https://developer.lockstep.io/docs/contactmodel). For
    more information on writing your own connector, see [Connector
    Data](https://developer.lockstep.io/docs/connector-data).
    """

    erpKey: str | None = None
    companyErpKey: str | None = None
    contactName: str | None = None
    contactCode: str | None = None
    title: str | None = None
    roleCode: str | None = None
    emailAddress: str | None = None
    phone: str | None = None
    fax: str | None = None
    address1: str | None = None
    address2: str | None = None
    address3: str | None = None
    city: str | None = None
    stateRegion: str | None = None
    postalCode: str | None = None
    countryCode: str | None = None
    isActive: bool | None = None
    webpageUrl: str | None = None
    pictureUrl: str | None = None
    created: str | None = None
    modified: str | None = None

