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
class FinancialAccountBalanceHistorySyncModel:
    """
    The FinancialAccountBalanceHistorySyncModel represents information
    coming into Lockstep from an external financial system or other
    enterprise resource planning system. To import data from an external
    system, convert your original data into the
    FinancialAccountBalanceHistorySyncModel format and call the [Upload
    Sync File API](https://developer.lockstep.io/reference/post_api-v1-sync-zip).
    This API retrieves all of the data you uploaded in a compressed ZIP
    file and imports it into the Lockstep platform. If the
    FinancialAccountBalanceHistorySyncModels are imported via a
    connector instead, please ensure that all records are passed in on
    every sync. Records that are not passed in will be assumed to be
    deleted. Once imported, this record will be available in the
    Lockstep API as a [FinancialAccountBalanceHistoryModel](https://developer.lockstep.io/docs/financialaccountbalancehistorymodel).
    For more information on writing your own connector, see [Connector
    Data](https://developer.lockstep.io/docs/connector-data).
    """

    financialAccountCode: object | None = None
    financialAccountErpKey: object | None = None
    financialYear: object | None = None
    periodNumber: object | None = None
    periodStartDate: object | None = None
    periodEndDate: object | None = None
    status: object | None = None
    balance: object | None = None
    balanceType: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
