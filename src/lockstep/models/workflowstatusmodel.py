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
class WorkflowStatusModel:
    """
    A Workflow Status represents the state for a specific workflow for
    an entity.
    """

    id: object | None = None
    name: object | None = None
    description: object | None = None
    parentWorkflowStatusId: object | None = None
    category: object | None = None
    code: object | None = None
    isNotesRequired: object | None = None
    promoteToErp: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
