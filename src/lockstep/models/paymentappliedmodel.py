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
from lockstep.models.invoicemodel import InvoiceModel

"""
A Payment Application is created by a business who receives a Payment 
from a customer. A customer may make a single Payment to match an 
Invoice exactly, a partial Payment for an Invoice, or a single Payment 
may be made for multiple smaller Invoices. The Payment Application 
contains information about which Invoices are connected to which 
Payments and for which amounts.
"""
@dataclass
class PaymentAppliedModel:
    groupKey: str = None
    paymentAppliedId: str = None
    invoiceId: str = None
    paymentId: str = None
    erpKey: str = None
    entryNumber: int = None
    applyToInvoiceDate: str = None
    paymentAppliedAmount: float = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None
    appEnrollmentId: str = None
    invoice: InvoiceModel = None

