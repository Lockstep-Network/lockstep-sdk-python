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

    syncRequestId: str = None
    groupKey: str = None
    statusCode: str = None
    processResultMessage: str = None
    appEnrollmentId: str = None
    created: str = None
    modified: str = None
    modifiedUserId: str = None
    details: object = None

