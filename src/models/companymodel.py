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
# @version    2021.39
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#



from src.models.notemodel import NoteModel
from src.models.attachmentmodel import AttachmentModel
from src.models.contactmodel import ContactModel
from src.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from src.models.customfieldvaluemodel import CustomFieldValueModel
from src.models.codedefinitionmodel import CodeDefinitionModel

"""
A Company represents a customer, a vendor, or a company within the 
organization of the account holder. Companies can have parents and 
children, representing an organizational hierarchy of corporate 
entities. You can use Companies to track projects and financial data 
under this Company label. See [Vendors, Customers, and 
Companies](https://developer.lockstep.io/docs/companies-customers-and-vendors) 
for more information.
"""
class CompanyModel:
    companyId: str
    companyName: str
    erpKey: str
    companyType: str
    companyStatus: str
    parentCompanyId: str
    enterpriseId: str
    groupKey: str
    isActive: bool
    defaultCurrencyCode: str
    companyLogoUrl: str
    primaryContactId: str
    address1: str
    address2: str
    address3: str
    corpCity: str
    corpState: str
    corpPostalCode: str
    corpCountry: str
    corpPhone: str
    corpFax: str
    city: str
    stateRegion: str
    postalCode: str
    country: str
    phoneNumber: str
    faxNumber: str
    created: str
    createdUserId: str
    modified: str
    modifiedUserId: str
    modifiedUserName: str
    taxId: str
    dunsNumber: str
    apEmailAddress: str
    arEmailAddress: str
    domainName: str
    companyClassificationCodeDefId: str
    description: str
    website: str
    appEnrollmentId: str
    notes: list[NoteModel]
    attachments: list[AttachmentModel]
    contacts: list[ContactModel]
    invoices: list[object]
    customFieldDefinitions: list[CustomFieldDefinitionModel]
    customFieldValues: list[CustomFieldValueModel]
    companyClassificationCodeDefinition: CodeDefinitionModel

