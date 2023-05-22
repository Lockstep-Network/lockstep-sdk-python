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
from lockstep.models.actionresultmodel import ActionResultModel
from lockstep.models.notemodel import NoteModel

class NotesClient:
    """
    API methods related to Notes
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_note(self, id: str, include: str) -> LockstepResponse[NoteModel]:
        """
        Retrieves the note with the specified note identifier.

        A note is a customizable text string that can be attached to
        various account attributes within Lockstep. You can use notes
        for internal communication, correspondence with clients, or
        personal reminders. The Note Model represents a note and a
        number of different metadata attributes related to the creation,
        storage, and ownership of the note.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        id : str
            The unique ID number of the Note to retrieve
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. No collections are currently available
            but may be offered in the future
        """
        path = f"/api/v1/Notes/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, NoteModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def archive_note(self, id: str) -> LockstepResponse[ActionResultModel]:
        """
        Archives the Note with the unique ID specified.

        A note is a customizable text string that can be attached to
        various account attributes within Lockstep. You can use notes
        for internal communication, correspondence with clients, or
        personal reminders. The Note Model represents a note and a
        number of different metadata attributes related to the creation,
        storage, and ownership of the note.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        id : str
            Note id to be archived
        """
        path = f"/api/v1/Notes/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ActionResultModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_notes(self, body: list[object]) -> LockstepResponse[list[NoteModel]]:
        """
        Creates one or more notes from the specified array of Note
        Models

        A note is a customizable text string that can be attached to
        various account attributes within Lockstep. You can use notes
        for internal communication, correspondence with clients, or
        personal reminders. The Note Model represents a note and a
        number of different metadata attributes related to the creation,
        storage, and ownership of the note.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        body : list[object]
            The array of notes to be created
        """
        path = "/api/v1/Notes"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [NoteModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_notes(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[NoteModel]]:
        """
        Queries Notes on the Lockstep Platform using the specified
        filtering, sorting, nested fetch, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        A note is a customizable text string that can be attached to
        various account attributes within Lockstep. You can use notes
        for internal communication, correspondence with clients, or
        personal reminders. The Note Model represents a note and a
        number of different metadata attributes related to the creation,
        storage, and ownership of the note.

        See [Extensibility](https://developer.lockstep.io/docs/extensibility)
        for more information.

        Parameters
        ----------
        filter : str
            The filter to use to select from the list of available
            applications, in the [Searchlight query
            syntax](https://github.com/tspence/csharp-searchlight).
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. No collections are currently available
            but may be offered in the future
        order : str
            The sort order for the results, in the [Searchlight order
            syntax](https://github.com/tspence/csharp-searchlight).
        pageSize : int
            The page size for results (default 250, maximum of 500)
        pageNumber : int
            The page number for results (default 0)
        """
        path = "/api/v1/Notes/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), NoteModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
