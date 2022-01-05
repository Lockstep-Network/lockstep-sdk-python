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
# @version    2021.39
# @link       https://github.com/Lockstep-Network/lockstep-sdk-python
#

from src.clients.ActivitiesClient import ActivitiesClient
from src.clients.ApiKeysClient import ApiKeysClient
from src.clients.AppEnrollmentsClient import AppEnrollmentsClient
from src.clients.ApplicationsClient import ApplicationsClient
from src.clients.AttachmentsClient import AttachmentsClient
from src.clients.CodeDefinitionsClient import CodeDefinitionsClient
from src.clients.CompaniesClient import CompaniesClient
from src.clients.ContactsClient import ContactsClient
from src.clients.CreditMemoAppliedClient import CreditMemoAppliedClient
from src.clients.CurrenciesClient import CurrenciesClient
from src.clients.CustomFieldDefinitionsClient import CustomFieldDefinitionsClient
from src.clients.CustomFieldValuesClient import CustomFieldValuesClient
from src.clients.DefinitionsClient import DefinitionsClient
from src.clients.EmailsClient import EmailsClient
from src.clients.InvoiceHistoryClient import InvoiceHistoryClient
from src.clients.InvoicesClient import InvoicesClient
from src.clients.LeadsClient import LeadsClient
from src.clients.MigrationClient import MigrationClient
from src.clients.NotesClient import NotesClient
from src.clients.PaymentApplicationsClient import PaymentApplicationsClient
from src.clients.PaymentsClient import PaymentsClient
from src.clients.ProvisioningClient import ProvisioningClient
from src.clients.ReportsClient import ReportsClient
from src.clients.StatusClient import StatusClient
from src.clients.SyncClient import SyncClient
from src.clients.UserAccountsClient import UserAccountsClient
from src.clients.UserRolesClient import UserRolesClient
from src.models.LockstepResponse import LockstepResponse
import requests
import urllib.parse

class LockstepApi():

    """
    Construct a new LockstepApi client object
    """
    def __init__(self, env: str):
        self.activities = ActivitiesClient(self)
        self.apiKeys = ApiKeysClient(self)
        self.appEnrollments = AppEnrollmentsClient(self)
        self.applications = ApplicationsClient(self)
        self.attachments = AttachmentsClient(self)
        self.codeDefinitions = CodeDefinitionsClient(self)
        self.companies = CompaniesClient(self)
        self.contacts = ContactsClient(self)
        self.creditMemoApplied = CreditMemoAppliedClient(self)
        self.currencies = CurrenciesClient(self)
        self.customFieldDefinitions = CustomFieldDefinitionsClient(self)
        self.customFieldValues = CustomFieldValuesClient(self)
        self.definitions = DefinitionsClient(self)
        self.emails = EmailsClient(self)
        self.invoiceHistory = InvoiceHistoryClient(self)
        self.invoices = InvoicesClient(self)
        self.leads = LeadsClient(self)
        self.migration = MigrationClient(self)
        self.notes = NotesClient(self)
        self.paymentApplications = PaymentApplicationsClient(self)
        self.payments = PaymentsClient(self)
        self.provisioning = ProvisioningClient(self)
        self.reports = ReportsClient(self)
        self.status = StatusClient(self)
        self.sync = SyncClient(self)
        self.userAccounts = UserAccountsClient(self)
        self.userRoles = UserRolesClient(self)
        if env == "sbx":
            self.serverUrl = "https://api.sbx.lockstep.io/"
        elif env == "prd":
            self.serverUrl = "https://api.lockstep.io/"
        else:
            self.serverUrl = env
        self.version = "2021.39"

    """
    Configure this API client to use API Key authentication
    """
    def with_api_key(self, apiKey: str):
        self.apiKey = apiKey
        self.bearerToken = None
    
    """
    Configure this API client to use Bearer Token authentication
    """
    def with_bearer_token(self, bearerToken: str):
        self.apiKey = None
        self.bearerToken = bearerToken
    
    """
    Send a request and parse the result
    """
    def send_request(self, method: str, path: str, body: object, query_params: object) -> LockstepResponse:
        if query_params != None:
            url = urllib.parse.urljoin(self.serverUrl, path) + "?" + urllib.parse.urlencode(query_params)
        else:
            url = urllib.parse.urljoin(self.serverUrl, path)
        
        if self.apiKey != None:
            headers = {"Accept": "application/json", "Api-Key": self.apiKey}
        elif self.bearerToken != None:
            headers = {"Accept": "application/json", "Authorization": "Bearer " + self.bearerToken}
        else:
            headers = {"Accept": "application/json"}
    
        response = requests.request("GET", url, headers=headers)
        return response
        
