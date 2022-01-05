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



from src.models.invoicemodel import InvoiceModel

"""
A Payment Application is created by a business who receives a Payment
from a customer. A customer may make a single Payment to match an
Invoice exactly, a partial Payment for an Invoice, or a single Payment
may be made for multiple smaller Invoices. The Payment Application
contains information about which Invoices are connected to which
Payments and for which amounts.
"""
class PaymentAppliedModel:
    groupKey: str
    paymentAppliedId: str
    invoiceId: str
    paymentId: str
    erpKey: str
    entryNumber: int
    applyToInvoiceDate: str
    paymentAppliedAmount: float
    created: str
    createdUserId: str
    modified: str
    modifiedUserId: str
    appEnrollmentId: str
    invoice: InvoiceModel

