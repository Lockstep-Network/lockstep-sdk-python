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
class CompanySyncModel:
    """
    The CompanySyncModel represents information coming into Lockstep
    from an external financial system or other enterprise resource
    planning system. To import data from an external system, convert
    your original data into the CompanySyncModel format and call the
    [Upload Sync File API](https://developer.lockstep.io/reference/post_api-v1-sync-zip).
    This API retrieves all of the data you uploaded in a compressed ZIP
    file and imports it into the Lockstep platform. Once imported, this
    record will be available in the Lockstep API as a
    [CompanyModel](https://developer.lockstep.io/docs/companymodel). For
    more information on writing your own connector, see [Connector
    Data](https://developer.lockstep.io/docs/connector-data).
    """

    onMatchAction: int | None = None
    erpKey: str | None = None
    companyName: str | None = None
    companyType: str | None = None
    parentCompanyErpKey: str | None = None
    isActive: bool | None = None
    defaultCurrencyCode: str | None = None
    companyLogoUrl: str | None = None
    primaryContactErpKey: str | None = None
    address1: str | None = None
    address2: str | None = None
    address3: str | None = None
    city: str | None = None
    stateRegion: str | None = None
    postalCode: str | None = None
    country: str | None = None
    phoneNumber: str | None = None
    faxNumber: str | None = None
    created: str | None = None
    modified: str | None = None
    taxId: str | None = None
    dunsNumber: str | None = None
    apEmailAddress: str | None = None
    arEmailAddress: str | None = None
    preferredDeliveryMethod: str | None = None
    emailAddress: str | None = None
    externalReference: str | None = None

