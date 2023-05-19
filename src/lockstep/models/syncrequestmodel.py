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
class SyncRequestModel:
    """
    Represents a Sync action that loads data from a connector into the
    Lockstep Platform. Users can request Sync actions manually using
    Lockstep Inbox, or via the [Create Sync
    API](https://developer.lockstep.io/reference/post_api-v1-sync). Each
    Sync action is tied to an [AppEnrollment](https://developer.lockstep.io/docs/applications-and-enrollments).
    When the Sync action is complete, the field `StatusCode` will be set
    to either `Success` or `Failed`. You can fetch a list of detailed
    results for the Sync API by calling Retrieve or Query with an
    `include` parameter of `details`. These detailed results contain
    line-by-line errors that were detected during processing of this
    sync.
    """

    syncRequestId: object | None = None
    groupKey: object | None = None
    statusCode: object | None = None
    operationTypeName: object | None = None
    operationType: object | None = None
    processResultMessage: object | None = None
    failureCount: object | None = None
    runFullSync: object | None = None
    appEnrollmentId: object | None = None
    created: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None
    details: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
