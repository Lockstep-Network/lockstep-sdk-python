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
from lockstep.models.invoicesummarymodel import InvoiceSummaryModel
from lockstep.models.invoicesummarytotalsmodel import InvoiceSummaryTotalsModel
from lockstep.models.summaryagingtotalsmodel import SummaryAgingTotalsModel

@dataclass
class InvoiceSummaryModelInvoiceSummaryTotalsModelSummaryFetchResult:

    records: list[InvoiceSummaryModel] | None = None
    totalCount: int | None = None
    pageSize: int | None = None
    pageNumber: int | None = None
    summary: InvoiceSummaryTotalsModel | None = None
    agingSummary: list[SummaryAgingTotalsModel] | None = None

