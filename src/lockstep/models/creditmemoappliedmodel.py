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

    creditMemoAppliedId: object | None = None
    groupKey: object | None = None
    invoiceId: object | None = None
    creditMemoInvoiceId: object | None = None
    erpKey: object | None = None
    erpWriteStatus: object | None = None
    erpWriteStatusName: object | None = None
    entryNumber: object | None = None
    applyToInvoiceDate: object | None = None
    creditMemoAppliedAmount: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    appEnrollmentId: object | None = None
    sourceModifiedDate: object | None = None
    attachments: list[object] | None = None
    notes: list[object] | None = None
    customFieldDefinitions: list[object] | None = None
    customFieldValues: list[object] | None = None
    creditMemoInvoice: object | None = None
    invoice: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
