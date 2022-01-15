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
from lockstep.models.syncsubmitmodel import SyncSubmitModel

class SyncClient:

    def __init__(self, client):
        self.client = client

    """
    Requests a new Sync task from the Application specified in the 
    request and returns a token that can be used to check the progress 
    and status of the task. 

    A Sync task represents an action performed by an Application for a 
    particular account. An Application can provide many different tasks 
    as part of their capabilities. Sync tasks are executed in the 
    background and will continue running after they are created. Use one 
    of the creation APIs to request execution of a task. To check on the 
    progress of the task, call GetSync or QuerySync.

    Parameters
    ----------
    body : SyncSubmitModel
        Information about the Sync to execute
    """
    def create_sync(self, body: SyncSubmitModel) -> LockstepResponse:
        path = f"/api/v1/Sync"
        return self.client.send_request("POST", path, body, {body: SyncSubmitModel})

    """
    Requests a new Sync task from a ZIP file you provide. This ZIP file 
    can contain one or more files with data from the customer's 
    platform. Individual files can be in the format CSV or JSONL (JSON 
    with Lines). 

    A Sync task represents an action performed by an Application for a 
    particular account. An Application can provide many different tasks 
    as part of their capabilities. Sync tasks are executed in the 
    background and will continue running after they are created. Use one 
    of the creation APIs to request execution of a task. To check on the 
    progress of the task, call GetSync or QuerySync.

    Parameters
    ----------
    """
    def upload_sync_file(self, ) -> LockstepResponse:
        path = f"/api/v1/Sync/zip"
        return self.client.send_request("POST", path, None, None)

    """
    Updates an existing Sync with the information supplied to this PATCH 
    call. 

    This API is restricted to internal service users and may not be 
    called by customers or partners. 

    The PATCH method allows you to change specific values on the object 
    while leaving other values alone. As input you should supply a list 
    of field names and new values. For example, you can provide the 
    field name "IsActive" and specify the new value "False"; this API 
    will then change the value of IsActive to false. 

    A Sync task represents an action performed by an Application for a 
    particular account. An Application can provide many different tasks 
    as part of their capabilities. Sync tasks are executed in the 
    background and will continue running after they are created. Use one 
    of the creation APIs to request execution of a task. To check on the 
    progress of the task, call GetSync or QuerySync.

    Parameters
    ----------
    id : str
        The unique ID number of the Sync to update
    body : object
        A list of changes to apply to this Application
    """
    def update_sync(self, id: str, body: object) -> LockstepResponse:
        path = f"/api/v1/Sync/{id}"
        return self.client.send_request("PATCH", path, body, {id: str, body: object})

    """
    Retrieves the status and information about a Sync operation by the 
    requested ID. Provides status and progress information about this 
    task. 

    A Sync task represents an action performed by an Application for a 
    particular account. An Application can provide many different tasks 
    as part of their capabilities. Sync tasks are executed in the 
    background and will continue running after they are created. Use one 
    of the creation APIs to request execution of a task. To check on the 
    progress of the task, call GetSync or QuerySync.

    Parameters
    ----------
    id : str
        The unique ID number of the Sync task to retrieve
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: Details
    """
    def retrieve_sync(self, id: str, include: str) -> LockstepResponse:
        path = f"/api/v1/Sync/{id}"
        return self.client.send_request("GET", path, None, {id: str, include: str})

    """
    Queries Sync tasks for this account using the specified filtering, 
    sorting, nested fetch, and pagination rules requested. 

    More information on querying can be found on the [Searchlight Query 
    Language](https://developer.lockstep.io/docs/querying-with-searchlight) 
    page on the Lockstep Developer website. 

    A Sync task represents an action performed by an Application for a 
    particular account. An Application can provide many different tasks 
    as part of their capabilities. Sync tasks are executed in the 
    background and will continue running after they are created. Use one 
    of the creation APIs to request execution of a task. To check on the 
    progress of the task, call GetSync or QuerySync.

    Parameters
    ----------
    filter : str
        The filter for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    include : str
        To fetch additional data on this object, specify the list of 
        elements to retrieve. Available collections: Details
    order : str
        The sort order for this query. See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageSize : int
        The page size for results (default 200). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    pageNumber : int
        The page number for results (default 0). See [Searchlight Query 
        Language](https://developer.lockstep.io/docs/querying-with-searchlight)
    """
    def query_syncs(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
        path = f"/api/v1/Sync/query"
        return self.client.send_request("GET", path, None, {filter: str, include: str, order: str, pageSize: int, pageNumber: int})
