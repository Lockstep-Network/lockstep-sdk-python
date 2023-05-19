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
class InvoiceLineModel:
    """
    Represents a line in an invoice
    """

    invoiceLineId: object | None = None
    groupKey: object | None = None
    invoiceId: object | None = None
    erpKey: object | None = None
    lineNumber: object | None = None
    productCode: object | None = None
    description: object | None = None
    unitMeasureCode: object | None = None
    unitPrice: object | None = None
    quantity: object | None = None
    quantityShipped: object | None = None
    quantityReceived: object | None = None
    totalAmount: object | None = None
    exemptionCode: object | None = None
    reportingDate: object | None = None
    overrideOriginAddressId: object | None = None
    overrideBillToAddressId: object | None = None
    overrideShipToAddressId: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    appEnrollmentId: object | None = None
    erpWriteStatus: object | None = None
    erpWriteStatusName: object | None = None
    sourceModifiedDate: object | None = None
    notes: list[object] | None = None
    attachments: list[object] | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
