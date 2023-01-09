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
from lockstep.models.attachmentmodel import AttachmentModel
from lockstep.models.notemodel import NoteModel
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel
from lockstep.models.invoicemodel import InvoiceModel
from lockstep.models.invoicemodel import InvoiceModel

@dataclass
class CreditMemoAppliedModel:
    """
    Credit Memos reflect credits granted to a customer for various
    reasons, such as discounts or refunds. Credit Memos may be applied
    to Invoices as Payments. When a Credit Memo is applied as payment to
    an Invoice, Lockstep creates a Credit Memo Application record to
    track the amount from the Credit Memo that was applied as payment to
    the Invoice. You can examine Credit Memo Application records to
    track which Invoices were paid using this Credit.
    """

    creditMemoAppliedId: str | None = None
    groupKey: str | None = None
    invoiceId: str | None = None
    creditMemoInvoiceId: str | None = None
    erpKey: str | None = None
    entryNumber: int | None = None
    applyToInvoiceDate: str | None = None
    creditMemoAppliedAmount: float | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    appEnrollmentId: str | None = None
    attachments: list[AttachmentModel] | None = None
    notes: list[NoteModel] | None = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] | None = None
    customFieldValues: list[CustomFieldValueModel] | None = None
    creditMemoInvoice: InvoiceModel | None = None
    invoice: InvoiceModel | None = None

