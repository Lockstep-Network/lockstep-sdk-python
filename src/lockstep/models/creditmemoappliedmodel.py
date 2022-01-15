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
from lockstep.models.attachmentmodel import AttachmentModel
from lockstep.models.notemodel import NoteModel
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel

"""
Credit Memos reflect credits granted to a customer for various reasons, 
such as discounts or refunds. Credit Memos may be applied to Invoices as 
Payments. When a Credit Memo is applied as payment to an Invoice, 
Lockstep creates a Credit Memo Application record to track the amount 
from the Credit Memo that was applied as payment to the Invoice. You can 
examine Credit Memo Application records to track which Invoices were 
paid using this Credit.
"""
@dataclass
class CreditMemoAppliedModel:
    creditMemoAppliedId: str = None
    groupKey: str = None
    invoiceId: str = None
    creditMemoInvoiceId: str = None
    erpKey: str = None
    entryNumber: int = None
    applyToInvoiceDate: str = None
    creditMemoAppliedAmount: float = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None
    appEnrollmentId: str = None
    attachments: list[AttachmentModel] = None
    notes: list[NoteModel] = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] = None
    customFieldValues: list[CustomFieldValueModel] = None

