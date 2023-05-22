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

    onMatchAction: object | None = None
    erpKey: object | None = None
    companyName: object | None = None
    companyType: object | None = None
    parentCompanyErpKey: object | None = None
    isActive: object | None = None
    defaultCurrencyCode: object | None = None
    companyLogoUrl: object | None = None
    primaryContactErpKey: object | None = None
    address1: object | None = None
    address2: object | None = None
    address3: object | None = None
    city: object | None = None
    stateRegion: object | None = None
    postalCode: object | None = None
    country: object | None = None
    phoneNumber: object | None = None
    faxNumber: object | None = None
    created: object | None = None
    modified: object | None = None
    taxId: object | None = None
    dunsNumber: object | None = None
    apEmailAddress: object | None = None
    arEmailAddress: object | None = None
    preferredDeliveryMethod: object | None = None
    emailAddress: object | None = None
    externalReference: object | None = None
    companyRegistrationNumber: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
