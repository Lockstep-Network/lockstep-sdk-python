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
from lockstep.models.transcriptionvalidationrequestitemmodel import TranscriptionValidationRequestItemModel

@dataclass
class TranscriptionValidationRequestModel:
    """
    Represents a transcription validation request that is used to
    validate if file is of a specific type.
    """

    transcriptionValidationRequestId: str | None = None
    groupKey: str | None = None
    statusCode: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None
    items: list[TranscriptionValidationRequestItemModel] | None = None

