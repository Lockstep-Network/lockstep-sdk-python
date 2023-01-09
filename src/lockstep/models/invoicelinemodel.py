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
from lockstep.models.notemodel import NoteModel
from lockstep.models.attachmentmodel import AttachmentModel

@dataclass
class InvoiceLineModel:
    """
    Represents a line in an invoice
    """

    invoiceLineId: str | None = None
    groupKey: str | None = None
    invoiceId: str | None = None
    erpKey: str | None = None
    lineNumber: str | None = None
    productCode: str | None = None
    description: str | None = None
    unitMeasureCode: str | None = None
    unitPrice: float | None = None
    quantity: float | None = None
    quantityShipped: float | None = None
    quantityReceived: float | None = None
    totalAmount: float | None = None
    exemptionCode: str | None = None
    reportingDate: str | None = None
    overrideOriginAddressId: str | None = None
    overrideBillToAddressId: str | None = None
    overrideShipToAddressId: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    appEnrollmentId: str | None = None
    notes: list[NoteModel] | None = None
    attachments: list[AttachmentModel] | None = None

