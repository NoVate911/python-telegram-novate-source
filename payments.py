from yoomoney import Authorize, Client


def main() -> None:
    print("1 - TOKEN\n"
          "2 - RECEIVER ID")
    type: int = int(input("Type: "))
    match(type):
        case 1:
            client_id: str = input("Client ID: ")
            redirect_uri: str = input("Redirect URI: ")
            get_token(client_id=client_id, redirect_uri=redirect_uri)
        case 2:
            token: str = input("Token: ")
            print(f"Receiver ID: {get_receiver_id(token=token)}")
        case _:
            print("Invalid type")

def get_token(client_id: str, redirect_uri: str) -> None:
    Authorize(client_id=client_id, redirect_uri=redirect_uri, scope=['account-info', 'operation-history', 'operation-details', 'incoming-transfers', 'payment-p2p', 'payment-shop'])

def get_receiver_id(token: str) -> str:
    client: Client = Client(token=token)
    user = client.account_info()
    return str(user.account)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")