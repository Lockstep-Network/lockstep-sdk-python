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

    transcriptionValidationRequestItemId: str | None = None
    transcriptionValidationRequestId: str | None = None
    groupKey: str | None = None
    fileHash: str | None = None
    fileName: str | None = None
    fileExt: str | None = None
    fileLocation: str | None = None
    transcriptionResult: str | None = None
    processStart: str | None = None
    processEnd: str | None = None
    retryCount: int | None = None
    feedbackResult: str | None = None
    feedbackSent: str | None = None
    statusCode: str | None = None
    created: str | None = None
    createdUserId: str | None = None
    modified: str | None = None
    modifiedUserId: str | None = None

