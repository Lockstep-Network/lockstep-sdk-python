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

from lockstep.lockstep_response import LockstepResponse
from lockstep.models.errorresult import ErrorResult
from lockstep.fetch_result import FetchResult
from lockstep.models.deleteresult import DeleteResult
from lockstep.models.emailreplygeneratorrequest import EmailReplyGeneratorRequest
from lockstep.models.emailreplygeneratorresponse import EmailReplyGeneratorResponse
from lockstep.models.transcriptionrequestsubmit import TranscriptionRequestSubmit
from lockstep.models.transcriptionvalidationrequestitemmodel import TranscriptionValidationRequestItemModel
from lockstep.models.transcriptionvalidationrequestmodel import TranscriptionValidationRequestModel

class TranscriptionsClient:
    """
    API methods related to Transcriptions
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_transcription_validation_request(self, id: str, include: str) -> LockstepResponse[TranscriptionValidationRequestModel]:
        """
        Retrieves the Transcription Validation Request specified by this
        unique identifier, optionally including nested data sets.

        A Transcription Validation Request represents a collection of
        files sent from the client to verify the file type using the
        machine learning platform Sage AI.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the transcription
            validation request
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Items
        """
        path = f"/api/v1/Transcriptions/validate/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, TranscriptionValidationRequestModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_transcription_validation_request(self, id: str, body: object) -> LockstepResponse[TranscriptionValidationRequestModel]:
        """
        Updates an existing Transcription Validation Request with the
        information supplied to this PATCH call.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        A Transcription Validation Request represents a collection of
        files sent from the client to verify the file type using the
        machine learning platform Sage AI.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Transcription
            Validation Request to update
        body : object
            A list of changes to apply to this Transcription Validation
            Request
        """
        path = f"/api/v1/Transcriptions/validate/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, TranscriptionValidationRequestModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_transcription_validation_request(self, id: str) -> LockstepResponse[DeleteResult]:
        """
        Deletes the Transcription Validation Request and all associated
        items referred to by this unique identifier.

        A Transcription Validation Request represents a collection of
        files sent from the client to verify the file type using the
        machine learning platform Sage AI.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the transcription
            validation request to delete
        """
        path = f"/api/v1/Transcriptions/validate/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, DeleteResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_transcription_validation_request(self, body: list[object]) -> LockstepResponse[TranscriptionValidationRequestModel]:
        """
        Creates one Transcription Validation Request with all the
        associated request items within this account and returns the
        record as created.

        A Transcription Validation Request represents a collection of
        files sent from the client to verify the file type using the
        machine learning platform Sage AI.

        Parameters
        ----------
        body : list[object]
            The files which will be verified
        """
        path = "/api/v1/Transcriptions/validate"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, TranscriptionValidationRequestModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_transcription_validation_requests(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[TranscriptionValidationRequestModel]]:
        """
        Queries transcription validation requests transactions for this
        account using the specified filtering, sorting, nested fetch,
        and pagination rules requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Items
        order : str
            The sort order for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageSize : int
            The page size for results (default 250, maximum of 500). See
            [Searchlight Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/Transcriptions/validate/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), TranscriptionValidationRequestModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def creates_a_transcriptionvalidationrequestitemmodel(self, body: list[object]) -> LockstepResponse[list[TranscriptionValidationRequestItemModel]]:
        """
        Retrieves the TranscriptionValidationRequestItemModel specified
        by this unique identifier.

        A TranscriptionValidationRequestItemModel represents a file sent
        from the client to verify the file type using the machine
        learning platform Sage AI.

        Parameters
        ----------
        body : list[object]
            The TranscriptionValidationRequestItemModels to add to an
            existing TranscriptionValidationRequestItemModel
        """
        path = "/api/v1/Transcriptions/validation-items"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [TranscriptionValidationRequestItemModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retrieve_a_transcriptionvalidationrequestitemmodel(self, id: str) -> LockstepResponse[TranscriptionValidationRequestItemModel]:
        """
        Retrieves the TranscriptionValidationRequestItemModel specified
        by this unique identifier.

        A TranscriptionValidationRequestItemModel represents a file sent
        from the client to verify the file type using the machine
        learning platform Sage AI.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the
            TranscriptionValidationRequestItemModel
        """
        path = f"/api/v1/Transcriptions/validation-items/{id}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, TranscriptionValidationRequestItemModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_a_transcriptionvalidationrequestitemmodel(self, id: str, body: object) -> LockstepResponse[TranscriptionValidationRequestItemModel]:
        """
        Updates the TranscriptionValidationRequestItemModel specified by
        this unique identifier.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        A TranscriptionValidationRequestItemModel represents a file sent
        from the client to verify the file type using the machine
        learning platform Sage AI.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the
            TranscriptionValidationRequestItemModel
        body : object
            A list of changes to apply to this
            TranscriptionValidationRequestItemModel
        """
        path = f"/api/v1/Transcriptions/validation-items/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, TranscriptionValidationRequestItemModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_a_transcriptionvalidationrequestitemmodel(self, id: str) -> LockstepResponse[DeleteResult]:
        """
        Deletes the TranscriptionValidationRequestItemModel specified by
        this unique identifier.

        A TranscriptionValidationRequestItemModel represents a file sent
        from the client to verify the file type using the machine
        learning platform Sage AI.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the
            TranscriptionValidationRequestItemModel
        """
        path = f"/api/v1/Transcriptions/validation-items/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, DeleteResult(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_transcription_validation_request_items(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[TranscriptionValidationRequestItemModel]]:
        """
        Queries TranscriptionValidationRequestItemModels for this
        account using the specified filtering, sorting, nested fetch,
        and pagination rules requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. No collections are currently available
            but may be offered in the future ///
        order : str
            The sort order for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageSize : int
            The page size for results (default 250, maximum of 500). See
            [Searchlight Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/Transcriptions/validation-items/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), TranscriptionValidationRequestItemModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retrieve_an_emailreplygeneratorresponse(self, body: EmailReplyGeneratorRequest) -> LockstepResponse[EmailReplyGeneratorResponse]:
        """
        Retrieves the Email Reply Generator Response containing a list
        of email reply suggestions

        An Email Reply Generator Request represents an email to be sent
        for a list of email reply suggestions.

        Parameters
        ----------
        body : EmailReplyGeneratorRequest
            The Email Reply Generator Request to be sent
        """
        path = "/api/v1/Transcriptions/email-reply-suggestions"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, EmailReplyGeneratorResponse(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
