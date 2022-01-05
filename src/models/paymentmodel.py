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



from src.models.paymentappliedmodel import PaymentAppliedModel
from src.models.notemodel import NoteModel
from src.models.attachmentmodel import AttachmentModel
from src.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from src.models.customfieldvaluemodel import CustomFieldValueModel

"""
A Payment represents money sent from one company to another. A single 
payment may contain payments for one or more invoices; it is also 
possible for payments to be made in advance of an invoice, for example, 
as a deposit. The creator of the Payment is identified by the 
`CustomerId` field, and the recipient of the Payment is identified by 
the `CompanyId` field. Most Payments are uniquely identified both by a 
Lockstep Platform ID number and a customer ERP "key" that was generated 
by the system that originated the Payment. Payments that have not been 
fully applied have a nonzero `UnappliedAmount` value, which represents a 
deposit that has been paid and not yet applied to an Invoice.
"""
class PaymentModel:
    groupKey: str
    paymentId: str
    companyId: str
    erpKey: str
    paymentType: str
    tenderType: str
    isOpen: bool
    memoText: str
    paymentDate: str
    postDate: str
    paymentAmount: float
    unappliedAmount: float
    currencyCode: str
    referenceCode: str
    created: str
    createdUserId: str
    modified: str
    modifiedUserId: str
    appEnrollmentId: str
    isVoided: bool
    inDispute: bool
    applications: list[PaymentAppliedModel]
    notes: list[NoteModel]
    attachments: list[AttachmentModel]
    customFieldDefinitions: list[CustomFieldDefinitionModel]
    customFieldValues: list[CustomFieldValueModel]

