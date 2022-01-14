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

"""
Represents a line in an invoice
"""
@dataclass
class InvoiceLineModel:
    invoiceLineId: str = None
    groupKey: str = None
    invoiceId: str = None
    erpKey: str = None
    lineNumber: str = None
    productCode: str = None
    description: str = None
    unitMeasureCode: str = None
    unitPrice: float = None
    quantity: float = None
    quantityShipped: float = None
    quantityReceived: float = None
    totalAmount: float = None
    exemptionCode: str = None
    reportingDate: str = None
    overrideOriginAddressId: str = None
    overrideBillToAddressId: str = None
    overrideShipToAddressId: str = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None
    appEnrollmentId: str = None
    notes: list[NoteModel] = None
    attachments: list[AttachmentModel] = None

