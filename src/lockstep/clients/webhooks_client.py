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
from lockstep.models.webhookhistorytablestoragemodel import WebhookHistoryTableStorageModel
from lockstep.models.webhookmodel import WebhookModel

class WebhooksClient:
    """
    API methods related to Webhooks
    """
    from lockstep.lockstep_api import LockstepApi

    def __init__(self, client: LockstepApi):
        self.client = client

    def retrieve_webhook(self, id: str) -> LockstepResponse[WebhookModel]:
        """
        Retrieves the Webhook specified by this unique identifier.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this Webhook
        """
        path = f"/api/v1/Webhooks/{id}"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, WebhookModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def update_webhook(self, id: str, body: object) -> LockstepResponse[WebhookModel]:
        """
        Updates a webhook that matches the specified id with the
        requested information.

        The PATCH method allows you to change specific values on the
        object while leaving other values alone. As input you should
        supply a list of field names and new values. If you do not
        provide the name of a field, that field will remain unchanged.
        This allows you to ensure that you are only updating the
        specific fields desired.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Webhook to
            update.
        body : object
            A list of changes to apply to this Webhook
        """
        path = f"/api/v1/Webhooks/{id}"
        result = self.client.send_request("PATCH", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, WebhookModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def delete_webhook(self, id: str) -> LockstepResponse[ActionResultModel]:
        """
        Deletes the Webhook referred to by this unique identifier.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Webhook to
            delete.
        """
        path = f"/api/v1/Webhooks/{id}"
        result = self.client.send_request("DELETE", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, ActionResultModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def create_webhooks(self, body: list[object]) -> LockstepResponse[list[WebhookModel]]:
        """
        Creates one or more webhooks from a given model.

        Parameters
        ----------
        body : list[object]
            The Webhooks to create
        """
        path = "/api/v1/Webhooks"
        result = self.client.send_request("POST", path, body, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, [WebhookModel(**item) for item in result.json()], None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def regenerate_client_secret(self, id: str) -> LockstepResponse[WebhookModel]:
        """
        Updates a webhook that matches the specified id with a new
        client secret.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Webhook to
            update.
        """
        path = f"/api/v1/Webhooks/{id}/regenerate-client-secret"
        result = self.client.send_request("PATCH", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, WebhookModel(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_webhooks(self, filter: str, include: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[WebhookModel]]:
        """
        Queries Webhooks for this account using the specified filtering,
        sorting, and pagination rules requested.

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
            elements to retrieve. Available collection: WebhookRules
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
        path = "/api/v1/Webhooks/query"
        result = self.client.send_request("GET", path, None, {"filter": filter, "include": include, "order": order, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), WebhookModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def query_webhook_history(self, webhookId: str, include: str, filter: str, select: str, pageSize: int, pageNumber: int) -> LockstepResponse[FetchResult[WebhookHistoryTableStorageModel]]:
        """


        Parameters
        ----------
        webhookId : str
            The unique Lockstep Platform ID number of this Webhook
        include : str
            To fetch additional data on this object, specify the list of
            elements to retrieve. Available collection: Records,
            RequestMessage, ResponseMessage
        filter : str
            The filter for this query. See [Azure Query
            Language](https://docs.microsoft.com/en-us/rest/api/storageservices/querying-tables-and-entities)
        select : str
            The selection for this query. Selection is the desired
            properties of an entity to pull from the set. If a property
            is not selected, it will either return as null or empty. See
            [Azure Query Language](https://docs.microsoft.com/en-us/rest/api/storageservices/querying-tables-and-entities)
        pageSize : int
            The page size for results (default 250, maximum of 500).
        pageNumber : int
            The page number for results (default 0).
        """
        path = f"/api/v1/Webhooks/{webhookId}/history/query"
        result = self.client.send_request("GET", path, None, {"include": include, "filter": filter, "select": select, "pageSize": pageSize, "pageNumber": pageNumber}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, FetchResult.from_json(result.json(), WebhookHistoryTableStorageModel), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))

    def retry_failed_webhook_history(self, webhookId: str, webhookHistoryId: str) -> LockstepResponse[str]:
        """


        Parameters
        ----------
        webhookId : str
            The unique Lockstep Platform ID number of this Webhook
        webhookHistoryId : str
            The unique Lockstep Platform ID number of the Webhook
            History to be retried. Note: the webhook history supplied
            must have a isSuccessful status of false to be retried.
        """
        path = f"/api/v1/Webhooks/{webhookId}/history/{webhookHistoryId}/retry"
        result = self.client.send_request("GET", path, None, {}, None)
        if result.status_code >= 200 and result.status_code < 300:
            return LockstepResponse(True, result.status_code, str(**result.json()), None)
        else:
            return LockstepResponse(False, result.status_code, None, ErrorResult.from_json(result.json()))
