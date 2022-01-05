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



from src.models.attachmentmodel import AttachmentModel
from src.models.notemodel import NoteModel
from src.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from src.models.customfieldvaluemodel import CustomFieldValueModel

"""
Credit Memos reflect credits granted to a customer for various reasons, 
such as discounts or refunds. Credit Memos may be applied to Invoices as 
Payments. When a Credit Memo is applied as payment to an Invoice, 
Lockstep creates a Credit Memo Application record to track the amount 
from the Credit Memo that was applied as payment to the Invoice. You can 
examine Credit Memo Application records to track which Invoices were 
paid using this Credit.
"""
class CreditMemoAppliedModel:
    creditMemoAppliedId: str
    groupKey: str
    invoiceId: str
    creditMemoInvoiceId: str
    erpKey: str
    entryNumber: int
    applyToInvoiceDate: str
    creditMemoAppliedAmount: float
    created: str
    createdUserId: str
    modified: str
    modifiedUserId: str
    appEnrollmentId: str
    attachments: list[AttachmentModel]
    notes: list[NoteModel]
    customFieldDefinitions: list[CustomFieldDefinitionModel]
    customFieldValues: list[CustomFieldValueModel]

