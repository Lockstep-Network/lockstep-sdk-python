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
# @version    2022.2
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass

"""
A note is a customizable text string that can be attached to various 
account attributes within Lockstep. You can use notes for internal 
communication, correspondence with clients, or personal reminders. The 
Note Model represents a note and a number of different metadata 
attributes related to the creation, storage, and ownership of the note. 
See [Extensibility](https://developer.lockstep.io/docs/extensibility) 
for more information.
"""
@dataclass
class NoteModel:
    noteId: str = None
    groupKey: str = None
    tableKey: str = None
    objectKey: str = None
    noteText: str = None
    noteType: str = None
    isArchived: bool = None
    created: str = None
    createdUserId: str = None
    createdUserName: str = None
    appEnrollmentId: str = None
    recipientName: str = None

