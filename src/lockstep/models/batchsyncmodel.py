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
from lockstep.models.companysyncmodel import CompanySyncModel
from lockstep.models.contactsyncmodel import ContactSyncModel
from lockstep.models.creditmemoappliedsyncmodel import CreditMemoAppliedSyncModel
from lockstep.models.invoicesyncmodel import InvoiceSyncModel
from lockstep.models.invoicelinesyncmodel import InvoiceLineSyncModel
from lockstep.models.customfieldsyncmodel import CustomFieldSyncModel
from lockstep.models.paymentsyncmodel import PaymentSyncModel
from lockstep.models.paymentappliedsyncmodel import PaymentAppliedSyncModel
from lockstep.models.financialyearsettingsyncmodel import FinancialYearSettingSyncModel
from lockstep.models.financialaccountsyncmodel import FinancialAccountSyncModel
from lockstep.models.financialaccountbalancehistorysyncmodel import FinancialAccountBalanceHistorySyncModel
from lockstep.models.basecurrencysyncmodel import BaseCurrencySyncModel

@dataclass
class BatchSyncModel:
    """
    A BatchSyncModel contains a collection of records to load into the
    Lockstep Platform. Data contained in this batch will be merged with
    your existing data. Each record will be matched with existing data
    inside the Lockstep Platform using the [Identity
    Column](https://developer.lockstep.io/docs/identity-columns) rules.
    Any record that represents a new AppEnrollmentId+ErpKey will be
    inserted. A record that matches an existing AppEnrollmentId+ErpKey
    will be updated, but only if the data has changed. A Sync process
    permits either a complete data file or a partial / delta data file.
    Lockstep recommends using a sliding time window to avoid the risk of
    clock skew errors that might accidentally omit records. Best
    practice is to run a Sync process daily, and to export all data that
    has changed in the past 48 hours.
    """

    appEnrollmentId: str | None = None
    isFullSync: bool | None = None
    companies: list[CompanySyncModel] | None = None
    contacts: list[ContactSyncModel] | None = None
    creditMemoApplications: list[CreditMemoAppliedSyncModel] | None = None
    invoices: list[InvoiceSyncModel] | None = None
    invoiceLines: list[InvoiceLineSyncModel] | None = None
    customFields: list[CustomFieldSyncModel] | None = None
    payments: list[PaymentSyncModel] | None = None
    paymentApplications: list[PaymentAppliedSyncModel] | None = None
    financialYearSettings: list[FinancialYearSettingSyncModel] | None = None
    financialAccounts: list[FinancialAccountSyncModel] | None = None
    financialAccountBalanceHistories: list[FinancialAccountBalanceHistorySyncModel] | None = None
    baseCurrencies: list[BaseCurrencySyncModel] | None = None

