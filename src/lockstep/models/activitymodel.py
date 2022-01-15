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
from lockstep.models.companymodel import CompanyModel
from lockstep.models.attachmentmodel import AttachmentModel
from lockstep.models.notemodel import NoteModel
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel
from lockstep.models.activityxrefmodel import ActivityXRefModel

"""
An Activity contains information about work being done on a specific 
accounting task. You can use Activities to track information about who 
has been assigned a specific task, the current status of the task, the 
name and description given for the particular task, the priority of the 
task, and any amounts collected, paid, or credited for the task.
"""
@dataclass
class ActivityModel:
    activityId: str = None
    groupKey: str = None
    companyId: str = None
    activityTypeCode: str = None
    activityName: str = None
    activityDescription: str = None
    activityStatus: str = None
    isOpen: bool = None
    priority: str = None
    userAssignedTo: str = None
    dateAssigned: str = None
    dateClosed: str = None
    snoozeUntilDate: str = None
    created: str = None
    createdUserId: str = None
    modified: str = None
    modifiedUserId: str = None
    amountCollected: float = None
    amountPaid: float = None
    creditGiven: float = None
    isUnread: bool = None
    isArchived: bool = None
    company: CompanyModel = None
    attachments: list[AttachmentModel] = None
    notes: list[NoteModel] = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] = None
    customFieldValues: list[CustomFieldValueModel] = None
    references: list[ActivityXRefModel] = None

