from lockstep.lockstep_api import LockstepApi
import os

def main():
    apikey = os.environ.get('LOCKSTEP_API_SBX')
    client = LockstepApi('sbx', 'DEFAULT_APP_NAME')
    client.with_api_key(apikey)

    status_results = client.status.ping()
    print(f"StatusResult: {status_results}")

main()