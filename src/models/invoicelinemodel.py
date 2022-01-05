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

"""
Represents a line in an invoice
"""
class InvoiceLineModel:
    invoiceLineId: str
    groupKey: str
    invoiceId: str
    erpKey: str
    lineNumber: str
    productCode: str
    description: str
    unitMeasureCode: str
    unitPrice: float
    quantity: float
    quantityShipped: float
    quantityReceived: float
    totalAmount: float
    exemptionCode: str
    reportingDate: str
    overrideOriginAddressId: str
    overrideBillToAddressId: str
    overrideShipToAddressId: str
    created: str
    createdUserId: str
    modified: str
    modifiedUserId: str
    notes: list[NoteModel]
    attachments: list[AttachmentModel]

