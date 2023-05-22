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
class TranscriptionValidationRequestItemModel:
    """
    Represents a transcription validation request item to be validated.
    """

    transcriptionValidationRequestItemId: object | None = None
    transcriptionValidationRequestId: object | None = None
    groupKey: object | None = None
    fileHash: object | None = None
    fileName: object | None = None
    fileExt: object | None = None
    fileLocation: object | None = None
    transcriptionResult: object | None = None
    processStart: object | None = None
    processEnd: object | None = None
    retryCount: object | None = None
    feedbackResult: object | None = None
    feedbackSent: object | None = None
    statusCode: object | None = None
    created: object | None = None
    createdUserId: object | None = None
    modified: object | None = None
    modifiedUserId: object | None = None

    def to_dict(self) -> dict:
        return dataclass.asdict(self)
