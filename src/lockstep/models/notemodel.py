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
class NoteModel:
    """
    A note is a customizable text string that can be attached to various
    account attributes within Lockstep. You can use notes for internal
    communication, correspondence with clients, or personal reminders.
    The Note Model represents a note and a number of different metadata
    attributes related to the creation, storage, and ownership of the
    note. See [Extensibility](https://developer.lockstep.io/docs/extensibility)
    for more information.
    """

    noteId: str | None = None
    groupKey: str | None = None
    tableKey: str | None = None
    objectKey: str | None = None
    noteText: str | None = None
    noteType: str | None = None
    isArchived: bool | None = None
    created: str | None = None
    createdUserId: str | None = None
    createdUserName: str | None = None
    appEnrollmentId: str | None = None
    recipientName: str | None = None

