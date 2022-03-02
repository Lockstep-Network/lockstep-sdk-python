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
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

@dataclass
class FinancialYearSettingModel:
    """
    A Financial Year Setting is used to to set the type, beginning, end,
    and number of periods of a year used to calculate accounting
    reports. The financial setting can either be for a specific app
    enrollment id via a sync or, when the financial year setting is
    manually created, will cover all account data without an app
    enrollment id.
    """

    financialYearSettingId: str = None
    groupKey: str = None
    appEnrollmentId: str = None
    yearType: str = None
    totalPeriods: int = None
    startDate: str = None
    endDate: str = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None

