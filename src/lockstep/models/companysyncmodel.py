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

    erpKey: str = None
    companyName: str = None
    companyType: str = None
    companyStatus: str = None
    parentCompanyErpKey: str = None
    isActive: bool = None
    defaultCurrencyCode: str = None
    companyLogoUrl: str = None
    primaryContactErpKey: str = None
    address1: str = None
    address2: str = None
    address3: str = None
    city: str = None
    stateRegion: str = None
    postalCode: str = None
    country: str = None
    phoneNumber: str = None
    faxNumber: str = None
    created: str = None
    modified: str = None
    taxId: str = None
    dunsNumber: str = None
    apEmailAddress: str = None
    arEmailAddress: str = None

