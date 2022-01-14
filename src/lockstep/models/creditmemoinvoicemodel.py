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

"""
Contains information about a credit memo invoice
"""
@dataclass
class CreditMemoInvoiceModel:
    groupKey: str = None
    creditMemoAppliedId: str = None
    invoiceId: str = None
    creditMemoInvoiceId: str = None
    applyToInvoiceDate: str = None
    creditMemoAppliedAmount: float = None
    referenceCode: str = None
    companyId: str = None
    customerId: str = None
    invoiceStatusCode: str = None
    totalAmount: float = None
    outstandingBalanceAmount: float = None

