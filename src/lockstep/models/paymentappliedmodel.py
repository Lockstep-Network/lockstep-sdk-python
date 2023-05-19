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
class PaymentAppliedModel:
    """
    A Payment Application is created by a business who receives a
    Payment from a customer. A customer may make a single Payment to
    match an Invoice exactly, a partial Payment for an Invoice, or a
    single Payment may be made for multiple smaller Invoices. The
    Payment Application contains information about which Invoices are
    connected to which Payments and for which amounts.
    """

    groupKey: object | None = None
    paymentAppliedId: object | None = None
    invoiceId: object | None = None
    paymentId: object | None = None
    erpKey: object | None = None
    erpWriteStatus: object | None = None
    erpWriteStatusName: object | None = None
    entryNumber: object | None = None
    applyToInvoiceDate: object | None = None
    paymentAppliedAmount: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    appEnrollmentId: object | None = None
    sourceModifiedDate: object | None = None
    payment: object | None = None
    invoice: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
