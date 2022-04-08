#
# Lockstep Platform SDK for Python
#
# (c) 2021-2022 Lockstep, Inc.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#
# @author     Lockstep Network <support@lockstep.io>
# @copyright  2021-2022 Lockstep, Inc.
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#


from dataclasses import dataclass
from lockstep.models.companymodel import CompanyModel
from lockstep.models.attachmentmodel import AttachmentModel
from lockstep.models.notemodel import NoteModel
from lockstep.models.customfielddefinitionmodel import CustomFieldDefinitionModel
from lockstep.models.customfieldvaluemodel import CustomFieldValueModel
from lockstep.models.activityxrefmodel import ActivityXRefModel

@dataclass
class ActivityModel:
    """
    An Activity contains information about work being done on a specific
    accounting task. You can use Activities to track information about
    who has been assigned a specific task, the current status of the
    task, the name and description given for the particular task, the
    priority of the task, and any amounts collected, paid, or credited
    for the task.
    """

    activityId: str | None = None
    groupKey: str | None = None
    companyId: str | None = None
    activityTypeCode: str | None = None
    activityName: str | None = None
    activityDescription: str | None = None
    activityStatus: str | None = None
    isOpen: bool | None = None
    priority: str | None = None
    userAssignedTo: str | None = None
    dateAssigned: str | None = None
    dateClosed: str | None = None
    snoozeUntilDate: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    amountCollected: float | None = None
    amountPaid: float | None = None
    creditGiven: float | None = None
    isUnread: bool | None = None
    isArchived: bool | None = None
    company: CompanyModel | None = None
    userAssignedToName: str | None = None
    attachments: list[AttachmentModel] | None = None
    notes: list[NoteModel] | None = None
    customFieldDefinitions: list[CustomFieldDefinitionModel] | None = None
    customFieldValues: list[CustomFieldValueModel] | None = None
    references: list[ActivityXRefModel] | None = None

