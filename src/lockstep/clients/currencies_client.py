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
from lockstep.models.bulkcurrencyconversionmodel import BulkCurrencyConversionModel

class CurrenciesClient:

    def __init__(self, client):
        self.client = client

    """
    Retrieve a currency conversation rate from one currency to another 
    as of the specified date. Optionally, you can specify which currency 
    data provider to use. 

    The currency rate model contains all of the information used to make 
    the API call, plus the rate to use for the conversion.

    Parameters
    ----------
    sourceCurrency : str
        The ISO 4217 currency code of the origin currency. For a list of 
        currency codes, call List Currencies.
    destinationCurrency : str
        The ISO 4217 currency code of the target currency. For a list of 
        currency codes, call List Currencies.
    date : str
        The date for which we should cto use for this currency 
        conversion.
    dataProvider : str
        Optionally, you can specify a data provider.
    """
    def retrieve_currency_rate(self, sourceCurrency: str, destinationCurrency: str, date: str, dataProvider: str) -> LockstepResponse:
        path = f"/api/v1/Currencies/{sourceCurrency}/{destinationCurrency}"
        return self.client.send_request("GET", path, None, {sourceCurrency: str, destinationCurrency: str, date: str, dataProvider: str})

    """
    Receives an array of dates and currencies and a destination currency 
    and returns an array of the corresponding currency rates to the 
    given destination currency (Limit X).

    Parameters
    ----------
    destinationCurrency : str
        The currency to convert to.
    body : list[BulkCurrencyConversionModel]
        A list of dates and source currencies.
    """
    def bulk_currency_data(self, destinationCurrency: str, body: list[BulkCurrencyConversionModel]) -> LockstepResponse:
        path = f"/api/v1/Currencies/bulk"
        return self.client.send_request("POST", path, body, {destinationCurrency: str, body: list[BulkCurrencyConversionModel]})
