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
from lockstep.models.paymentmodel import PaymentModel
from lockstep.models.invoicemodel import InvoiceModel

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

    groupKey: str | None = None
    paymentAppliedId: str | None = None
    invoiceId: str | None = None
    paymentId: str | None = None
    erpKey: str | None = None
    entryNumber: int | None = None
    applyToInvoiceDate: str | None = None
    paymentAppliedAmount: float | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    appEnrollmentId: str | None = None
    payment: PaymentModel | None = None
    invoice: InvoiceModel | None = None

