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
from lockstep.models.workflowstatusmodel import WorkflowStatusModel

class WorkflowStatusesClient:
    """
    API methods related to WorkflowStatuses
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_workflow_status(self, id: str) -> LockstepResponse[WorkflowStatusModel]:
        """
        Retrieves the Workflow Status specified by this unique
        identifier.

        A Workflow Status represents the state for a specific workflow
        for an entity. A Workflow Status may be generic for common use
        cases or specific to a set of predefined statuses.

        Parameters
        ----------
        id : str
            The unique ID number of the Workflow Status to retrieve
        """
        path = f"/api/v1/workflow-statuses/{id}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, WorkflowStatusModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_workflow_statuses(self, body: list[object]) -> LockstepResponse[list[WorkflowStatusModel]]:
        """
        Creates one or more Workflow Statuses from a given model.

        A Workflow Status represents the state for a specific workflow
        for an entity. A Workflow Status may be generic for common use
        cases or specific to a set of predefined statuses.

        Parameters
        ----------
        body : list[object]
            The Workflow Statuses to create
        """
        path = "/api/v1/workflow-statuses"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [WorkflowStatusModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_workflow_statuses(self, filter: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[WorkflowStatusModel]]:
        """
        Queries Workflow Statuses using the specified filtering,
        sorting, nested fetch, and pagination rules requested.

        More information on querying can be found on the [Searchlight
        Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        page on the Accounting Data Services Developer website.

        A Workflow Status represents the state for a specific workflow
        for an entity. A Workflow Status may be generic for common use
        cases or specific to a set of predefined statuses.

        Parameters
        ----------
        filter : str
            The filter for this query. See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        order : str
            The sort order for this query. See See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageSize : int
            The page size for results (default 250, maximum of 500). See
            [Searchlight Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = "/api/v1/workflow-statuses/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), WorkflowStatusModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
