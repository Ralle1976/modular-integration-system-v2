class GoogleDriveModule:
    def __init__(self, credentials_path: str):
        self.credentials = Credentials.from_authorized_user_file(credentials_path, ['https://www.googleapis.com/auth/drive'])
...