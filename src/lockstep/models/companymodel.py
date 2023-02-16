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
from lockstep.models.viewboxsettingsmodel import ViewBoxSettingsModel
from lockstep.models.notemodel import NoteModel
from lockstep.models.attachmentmodel import AttachmentModel
from lockstep.models.contactmodel import ContactModel
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel
from lockstep.models.codedefinitionmodel import CodeDefinitionModel

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

    companyId: str | None = None
    companyName: str | None = None
    erpKey: str | None = None
    companyType: str | None = None
    parentCompanyId: str | None = None
    enterpriseId: str | None = None
    groupKey: str | None = None
    isActive: bool | None = None
    defaultCurrencyCode: str | None = None
    companyLogoUrl: str | None = None
    primaryContactId: str | None = None
    address1: str | None = None
    address2: str | None = None
    address3: str | None = None
    city: str | None = None
    stateRegion: str | None = None
    postalCode: str | None = None
    country: str | None = None
    timeZone: str | None = None
    phoneNumber: str | None = None
    faxNumber: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    modifiedUserName: str | None = None
    taxId: str | None = None
    dunsNumber: str | None = None
    apEmailAddress: str | None = None
    arEmailAddress: str | None = None
    preferredDeliveryMethod: str | None = None
    domainName: str | None = None
    companyClassificationCodeDefId: str | None = None
    description: str | None = None
    website: str | None = None
    appEnrollmentId: str | None = None
    emailAddress: str | None = None
    publicUrlSlug: str | None = None
    stateTaxId: str | None = None
    stateOfIncorporation: str | None = None
    linkedInUrlSlug: str | None = None
    isVerified: bool | None = None
    lastVerifiedDate: str | None = None
    viewBoxSettings: ViewBoxSettingsModel | None = None
    serviceFabricOrgId: str | None = None
    serviceFabricCompanyId: str | None = None
    notes: list[NoteModel] | None = None
    attachments: list[AttachmentModel] | None = None
    contacts: list[ContactModel] | None = None
    invoices: list[object] | None = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] | None = None
    customFieldValues: list[CustomFieldValueModel] | None = None
    companyClassificationCodeDefinition: CodeDefinitionModel | None = None

