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
from lockstep.models.paymentappliedmodel import PaymentAppliedModel
from lockstep.models.notemodel import NoteModel
from lockstep.models.attachmentmodel import AttachmentModel
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel

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
@dataclass
class PaymentModel:
    groupKey: str = None
    paymentId: str = None
    companyId: str = None
    erpKey: str = None
    paymentType: str = None
    tenderType: str = None
    isOpen: bool = None
    memoText: str = None
    paymentDate: str = None
    postDate: str = None
    paymentAmount: float = None
    unappliedAmount: float = None
    currencyCode: str = None
    referenceCode: str = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None
    appEnrollmentId: str = None
    isVoided: bool = None
    inDispute: bool = None
    applications: list[PaymentAppliedModel] = None
    notes: list[NoteModel] = None
    attachments: list[AttachmentModel] = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] = None
    customFieldValues: list[CustomFieldValueModel] = None

