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
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from lockstep.lockstep_response import LockstepResponse
from lockstep.models.webhookmodel import WebhookModel

class WebhooksClient:

    def __init__(self, client):
        self.client = client

    def retrieve_webhook(self, id: str) -> LockstepResponse:
        """
        Retrieves the Webhook specified by this unique identifier.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of this Webhook
        """
        path = f"/api/v1/Webhooks/{id}"
        return self.client.send_request("GET", path, None, {"id": id})

    def update_webhook(self, id: str, body: object) -> LockstepResponse:
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
        return self.client.send_request("PATCH", path, body, {"id": id, "body": body})

    def delete_webhook(self, id: str) -> LockstepResponse:
        """
        Deletes the Webhook referred to by this unique identifier.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Webhook to
            delete.
        """
        path = f"/api/v1/Webhooks/{id}"
        return self.client.send_request("DELETE", path, None, {"id": id})

    def create_webhooks(self, body: list[WebhookModel]) -> LockstepResponse:
        """
        Creates one or more webhooks from a given model.

        Parameters
        ----------
        body : list[WebhookModel]
            The Webhooks to create
        """
        path = f"/api/v1/Webhooks"
        return self.client.send_request("POST", path, body, {"body": body})

    def regenerate_client_secret(self, id: str) -> LockstepResponse:
        """
        Updates a webhook that matches the specified id with a new
        client secret.

        Parameters
        ----------
        id : str
            The unique Lockstep Platform ID number of the Webhook to
            update.
        """
        path = f"/api/v1/Webhooks/{id}/regenerateclientsecret"
        return self.client.send_request("PATCH", path, None, {"id": id})

    def query_webhooks(self, filter: str, order: str, pageSize: int, pageNumber: int) -> LockstepResponse:
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
        order : str
            The sort order for this query. See See [Searchlight Query
            Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageSize : int
            The page size for results (default 200). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        pageNumber : int
            The page number for results (default 0). See [Searchlight
            Query Language](https://developer.lockstep.io/docs/querying-with-searchlight)
        """
        path = f"/api/v1/Webhooks/query"
        return self.client.send_request("GET", path, None, {"filter": filter, "order": order, "pageSize": pageSize, "pageNumber": pageNumber})
