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


from dataclasses import dataclass
from src.models.attachmentmodel import AttachmentModel
from src.models.notemodel import NoteModel
from src.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from src.models.customfieldvaluemodel import CustomFieldValueModel

"""
An Activity contains information about work being done on a specific 
accounting task. You can use Activities to track information about who 
has been assigned a specific task, the current status of the task, the 
name and description given for the particular task, the priority of the 
task, and any amounts collected, paid, or credited for the task.
"""
@dataclass
class ActivityModel:
    activityId: str
    groupKey: str
    companyId: str
    activityTypeCode: str
    activityName: str
    activityDescription: str
    activityStatus: str
    isOpen: bool
    priority: str
    userAssignedTo: str
    dateAssigned: str
    dateClosed: str
    snoozeUntilDate: str
    created: str
    createdUserId: str
    modified: str
    modifiedUserId: str
    amountCollected: float
    amountPaid: float
    creditGiven: float
    isUnread: bool
    isArchived: bool
    attachments: list[AttachmentModel]
    notes: list[NoteModel]
    customFieldDefinitions: list[CustomFieldDefinitionModel]
    customFieldValues: list[CustomFieldValueModel]

