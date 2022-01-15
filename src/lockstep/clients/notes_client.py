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

from lockstep.lockstep_response import LockstepResponse
from lockstep.models.notemodel import NoteModel

class NotesClient:

    def __init__(self, client):
        self.client = client

    """
    Retrieves the note with the specified note identifier. A note is a 
    customizable text string that can be attached to various account 
    attributes within Lockstep. You can use notes for internal 
    communication, correspondence with clients, or personal reminders. 
    The Note Model represents a note and a number of different metadata 
    attributes related to the creation, storage, and ownership of the 
    note. 

    See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    id : str
        The unique ID number of the Note to retrieve
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. No collections are currently available but 
        may be offered in the future
    """
    def retrieve_note(self, id: str, include: str) -> LockstepResponse:
        path = f"/api/v1/Notes/{id}"
        return self.client.send_request("GET", path, None, {id: str, include: str})

    """
    Archives the Note with the unique ID specified. A note is a 
    customizable text string that can be attached to various account 
    attributes within Lockstep. You can use notes for internal 
    communication, correspondence with clients, or personal reminders. 
    The Note Model represents a note and a number of different metadata 
    attributes related to the creation, storage, and ownership of the 
    note. 

    See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    id : str
        Note id to be archived
    """
    def archive_note(self, id: str) -> LockstepResponse:
        path = f"/api/v1/Notes/{id}"
        return self.client.send_request("DELETE", path, None, {id: str})

    """
    Creates one or more notes from the specified array of Note Models 

    A note is a customizable text string that can be attached to various 
    account attributes within Lockstep. You can use notes for internal 
    communication, correspondence with clients, or personal reminders. 
    The Note Model represents a note and a number of different metadata 
    attributes related to the creation, storage, and ownership of the 
    note. 

    See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    body : list[NoteModel]
        The array of notes to be created
    """
    def create_notes(self, body: list[NoteModel]) -> LockstepResponse:
        path = f"/api/v1/Notes"
        return self.client.send_request("POST", path, body, {body: list[NoteModel]})

    """
    Queries Notes on the Lockstep Platform using the specified 
    filtering, sorting, nested fetch, and pagination rules requested. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. A note is a customizable 
    text string that can be attached to various account attributes 
    within Lockstep. You can use notes for internal communication, 
    correspondence with clients, or personal reminders. The Note Model 
    represents a note and a number of different metadata attributes 
    related to the creation, storage, and ownership of the note. 

    See 
    [Extensibility](https://developer.lockstep.io/docs/extensibility) 
    for more information.

    Parameters
    ----------
    filter : str
        The filter to use to select from the list of available 
        applications, in the [Searchlight query 
        syntax](https://github.com/tspence/csharp-searchlight).
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. No collections are currently available but 
        may be offered in the future
    order : str
        The sort order for the results, in the [Searchlight order 
        syntax](https://github.com/tspence/csharp-searchlight).
    pageSize : int
        The page size for results (default 200, maximum of 10,000)
    pageNumber : int
        The page number for results (default 0)
    """
    def query_notes(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/Notes/query"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})
