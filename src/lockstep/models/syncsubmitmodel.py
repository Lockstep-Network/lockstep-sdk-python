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
class SyncSubmitModel:
    """
    A SyncSubmitModel represents a task that loads data from a connector
    to load into the Lockstep Platform. Data contained in a sync will be
    merged with your existing data. Each record will be matched with
    existing data inside the Lockstep Platform using the [Identity
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

    appEnrollmentId: object | None = None
    runFullSync: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
