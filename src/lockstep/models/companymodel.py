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
# @version    2022.2
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass
from lockstep.models.notemodel import NoteModel
from lockstep.models.attachmentmodel import AttachmentModel
from lockstep.models.contactmodel import ContactModel
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel
from lockstep.models.codedefinitionmodel import CodeDefinitionModel

"""
A Company represents a customer, a vendor, or a company within the 
organization of the account holder. Companies can have parents and 
children, representing an organizational hierarchy of corporate 
entities. You can use Companies to track projects and financial data 
under this Company label. See [Vendors, Customers, and 
Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors) 
for more information.
"""
@dataclass
class CompanyModel:
    companyId: str = None
    companyName: str = None
    erpKey: str = None
    companyType: str = None
    companyStatus: str = None
    parentCompanyId: str = None
    enterpriseId: str = None
    groupKey: str = None
    isActive: bool = None
    defaultCurrencyCode: str = None
    companyLogoUrl: str = None
    primaryContactId: str = None
    address1: str = None
    address2: str = None
    address3: str = None
    corpCity: str = None
    corpState: str = None
    corpPostalCode: str = None
    corpCountry: str = None
    corpPhone: str = None
    corpFax: str = None
    city: str = None
    stateRegion: str = None
    postalCode: str = None
    country: str = None
    phoneNumber: str = None
    faxNumber: str = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None
    modifiedUserName: str = None
    taxId: str = None
    dunsNumber: str = None
    apEmailAddress: str = None
    arEmailAddress: str = None
    domainName: str = None
    companyClassificationCodeDefId: str = None
    description: str = None
    website: str = None
    appEnrollmentId: str = None
    notes: list[NoteModel] = None
    attachments: list[AttachmentModel] = None
    contacts: list[ContactModel] = None
    invoices: list[object] = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] = None
    customFieldValues: list[CustomFieldValueModel] = None
    companyClassificationCodeDefinition: CodeDefinitionModel = None

