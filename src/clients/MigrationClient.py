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

from src.LockstepApi import LockstepApi
from src.models.LockstepResponse import LockstepResponse

class MigrationClient:

    def __init__(self, client: LockstepApi):
        self.client = client

    # Migrates all customer data from the Lockstep Collect system to the API, including all stored data for contacts, companies, payments, and invoices.
    # 
    def migrate_data(self, ) -> LockstepResponse:
        path = f"/api/v1/Migration"
        return self.client.send_request("POST", path, None, None)

    # Lists all of the customer, contact, payment, and invoice data currently available for Migration.
    # 
    def list_migrations(self, ) -> LockstepResponse:
        path = f"/api/v1/Migration/list"
        return self.client.send_request("GET", path, None, None)
