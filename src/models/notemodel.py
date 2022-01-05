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
# @version    2021.39
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#




"""
A note is a customizable text string that can be attached to various
account attributes within Lockstep. You can use notes for internal
communication, correspondence with clients, or personal reminders. The
Note Model represents a note and a number of different metadata
attributes related to the creation, storage, and ownership of the note.
See [Extensibility](https://developer.lockstep.io/docs/extensibility)
for more information.
"""
class NoteModel:
    noteId: str
    groupKey: str
    tableKey: str
    objectKey: str
    noteText: str
    noteType: str
    isArchived: bool
    created: str
    createdUserId: str
    createdUserName: str
    appEnrollmentId: str

