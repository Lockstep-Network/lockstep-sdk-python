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
from lockstep.models.batchsyncmodel import BatchSyncModel
from lockstep.models.syncrequestmodel import SyncRequestModel
from lockstep.models.syncsubmitmodel import SyncSubmitModel

class SyncClient:
    """
    API methods related to Sync
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def create_sync(self, body: SyncSubmitModel) -> LockstepResponse[SyncRequestModel]:
        """
        Requests a new Sync task from the Application specified in the
        request and returns a token that can be used to check the
        progress and status of the task.

        A Sync task represents an action performed by an Application for
        a particular account. An Application can provide many different
        tasks as part of their capabilities. Sync tasks are executed in
        the background and will continue running after they are created.
        Use one of the creation APIs to request execution of a task. To
        check on the progress of the task, call GetSync or QuerySync.

        Parameters
        ----------
        body : SyncSubmitModel
            Information about the Sync to execute
        """
        path = "/api/v1/Sync"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, SyncRequestModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_batch_import(self, body: BatchSyncModel) -> LockstepResponse[SyncRequestModel]:
        """
        Creates a new batch import Sync task that imports all the models
        provided to this API call.

        A Sync task represents ingestion of data from a source. For each
        data model in the source, the Sync process will determine
        whether the data is new, updated, or unchanged from data that
        already exists within the Lockstep Platform. For records that
        are new, the Sync process will add them to the Lockstep Platform
        data. For records that are updated, the Sync process will update
        existing data to match the newly uploaded records. If records
        have not changed, no action will be taken.

        You can use this Batch Import process to load data in bulk
        directly into the Lockstep Platform.

        Parameters
        ----------
        body : BatchSyncModel
            Information about the Sync to execute
        """
        path = "/api/v1/Sync/batch"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, SyncRequestModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def upload_sync_file(self, appEnrollmentId: str, isFullSync: bool, filename: str) -> LockstepResponse[SyncRequestModel]:
        """
        Requests a new Sync task from a ZIP file you provide. This ZIP
        file can contain one or more files with data from the customer's
        platform. Individual files can be in the format CSV or JSONL
        (JSON with Lines).

        A Sync task represents an action performed by an Application for
        a particular account. An Application can provide many different
        tasks as part of their capabilities. Sync tasks are executed in
        the background and will continue running after they are created.
        Use one of the creation APIs to request execution of a task. To
        check on the progress of the task, call GetSync or QuerySync.

        Parameters
        ----------
        appEnrollmentId : str
            The optional existing app enrollment to associate with the
            data in the zip file.
        isFullSync : bool
            True if this is a full sync, false if this is a partial
            sync. Defaults to false.
        filename : str
            The full path of a file to upload to the API
        """
        path = "/api/v1/Sync/zip"
        result = self.client.send_request("POST", path, None, {"appEnrollmentId": appEnrollmentId, "isFullSync": isFullSync}, filename)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, SyncRequestModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_sync(self, id: str, body: object) -> LockstepResponse[SyncRequestModel]:
        """
        Updates an existing Sync with the information supplied to this
        PATCH call.

        This API is restricted to internal service users and may not be
        called by customers or partners.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. For example, you
        can provide the field name "IsActive" and specify the new value
        "False"; this API will then change the value of IsActive to
        false.

        A Sync task represents an action performed by an Application for
        a particular account. An Application can provide many different
        tasks as part of their capabilities. Sync tasks are executed in
        the background and will continue running after they are created.
        Use one of the creation APIs to request execution of a task. To
        check on the progress of the task, call GetSync or QuerySync.

        Parameters
        ----------
        id : str
            The unique ID number of the Sync to update
        body : object
            A list of changes to apply to this Application
        """
        path = f"/api/v1/Sync/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, SyncRequestModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retrieve_sync(self, id: str, include: str) -> LockstepResponse[SyncRequestModel]:
        """
        Retrieves the status and information about a Sync operation by
        the requested ID. Provides status and progress information about
        this task.

        A Sync task represents an action performed by an Application for
        a particular account. An Application can provide many different
        tasks as part of their capabilities. Sync tasks are executed in
        the background and will continue running after they are created.
        Use one of the creation APIs to request execution of a task. To
        check on the progress of the task, call GetSync or QuerySync.

        Parameters
        ----------
        id : str
            The unique ID number of the Sync task to retrieve
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collections: Details
        """
        path = f"/api/v1/Sync/{id}"
        result = self.client.send_request("GET", path, None, {"include": include}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, SyncRequestModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def cancel_sync(self, id: str) -> LockstepResponse[SyncRequestModel]:
        """
        Cancels a Sync process for an Application if the request is
        still being processed within the Application. This does not
        cancel Sync processes which have already proceeded to completion
        within the Application, or Sync processes outside of
        Applications such as from a Zip file or Batch Import.

        A Sync task represents an action performed by an Application for
        a particular account. An Application can provide many different
        tasks as part of their capabilities. Sync tasks are executed in
        the background and will continue running after they are created.
        Use one of the creation APIs to request execution of a task. To
        check on the progress of the task, call GetSync or QuerySync.

        Parameters
        ----------
        id : str
            The unique ID number of the Sync task to cancel
        """
        path = f"/api/v1/Sync/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, SyncRequestModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_syncs(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[SyncRequestModel]]:
        """
        Queries Sync tasks for this account using the specified
        filtering, sorting, nested fetch, and pagination rules
        requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Lockstep Developer website.

        A Sync task represents an action performed by an Application for
        a particular account. An Application can provide many different
        tasks as part of their capabilities. Sync tasks are executed in
        the background and will continue running after they are created.
        Use one of the creation APIs to request execution of a task. To
        check on the progress of the task, call GetSync or QuerySync.

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
            The page size for results (default 250, maximum of 500). See
            [Searchlight Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/Sync/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), SyncRequestModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
