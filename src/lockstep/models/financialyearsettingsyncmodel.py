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
class FinancialYearSettingSyncModel:
    """
    The FinancialYearSettingSyncModel represents information coming into
    Lockstep from an external financial system or other enterprise
    resource planning system. To import data from an external system,
    convert your original data into the FinancialYearSettingSyncModel
    format and call the [Upload Sync File
    API](https://developer.lockstep.io/reference/post_api-v1-sync-zip).
    This API retrieves all of the data you uploaded in a compressed ZIP
    file and imports it into the Lockstep platform. Once imported, this
    record will be available in the Lockstep API as a
    [FinancialYearSettingModel](https://developer.lockstep.io/docs/financialyearsettingmodel).
    Sync is supported for only one FinancialYearSetting per app
    enrollment and one FinancialYearSetting imported outside of an app
    enrollment - please submit only one model here. If multiple models
    are submitted, only the latest one is considered for Sync. For more
    information on writing your own connector, see [Connector
    Data](https://developer.lockstep.io/docs/connector-data).
    """

    yearType: object | None = None
    totalPeriods: object | None = None
    startDate: object | None = None
    endDate: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
