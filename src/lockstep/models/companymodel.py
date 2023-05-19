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
class CompanyModel:
    """
    A Company represents a customer, a vendor, or a company within the
    organization of the account holder. Companies can have parents and
    children, representing an organizational hierarchy of corporate
    entities. You can use Companies to track projects and financial data
    under this Company label. See [Vendors, Customers, and
    Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors)
    for more information.
    """

    companyId: object | None = None
    companyName: object | None = None
    erpKey: object | None = None
    companyType: object | None = None
    parentCompanyId: object | None = None
    enterpriseId: object | None = None
    groupKey: object | None = None
    isActive: object | None = None
    defaultCurrencyCode: object | None = None
    companyLogoUrl: object | None = None
    primaryContactId: object | None = None
    address1: object | None = None
    address2: object | None = None
    address3: object | None = None
    city: object | None = None
    stateRegion: object | None = None
    postalCode: object | None = None
    country: object | None = None
    timeZone: object | None = None
    phoneNumber: object | None = None
    faxNumber: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    modifiedUserName: object | None = None
    taxId: object | None = None
    dunsNumber: object | None = None
    apEmailAddress: object | None = None
    arEmailAddress: object | None = None
    preferredDeliveryMethod: object | None = None
    domainName: object | None = None
    companyClassificationCodeDefId: object | None = None
    description: object | None = None
    website: object | None = None
    appEnrollmentId: object | None = None
    emailAddress: object | None = None
    publicUrlSlug: object | None = None
    stateTaxId: object | None = None
    stateOfIncorporation: object | None = None
    linkedInUrlSlug: object | None = None
    isVerified: object | None = None
    lastVerifiedDate: object | None = None
    viewBoxSettings: object | None = None
    serviceFabricOrgId: object | None = None
    serviceFabricCompanyId: object | None = None
    companyRegistrationNumber: object | None = None
    notes: list[object] | None = None
    attachments: list[object] | None = None
    contacts: list[object] | None = None
    invoices: list[object] | None = None
    customFieldDefinitions: list[object] | None = None
    customFieldValues: list[object] | None = None
    companyClassificationCodeDefinition: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
