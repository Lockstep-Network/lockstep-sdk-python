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
View to return Payment Detail information for a given Invoice record.
"""
@dataclass
class InvoicePaymentDetailModel:
    groupKey: str = None
    paymentAppliedId: str = None
    invoiceId: str = None
    paymentId: str = None
    applyToInvoiceDate: str = None
    paymentAppliedAmount: float = None
    referenceCode: str = None
    companyId: str = None
    paymentAmount: float = None
    unappliedAmount: float = None

