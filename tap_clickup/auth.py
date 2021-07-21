"""ClickUp Authentication."""


from singer_sdk.authenticators import OAuthAuthenticator


class ClickUpAuthenticator(OAuthAuthenticator):
    """Authenticator class for ClickUp."""

    @property
    def oauth_request_body(self) -> dict:
        """Define the OAuth request body for the ClickUp API."""
        # TODO: Define the request body needed for the API.
        return {
            'resource': 'https://analysis.windows.net/powerbi/api',
            'scope': self.oauth_scopes,
            'client_id': self.config["client_id"],
            'username': self.config["username"],
            'password': self.config["password"],
            'grant_type': 'password',
        }

    @classmethod
    def create_for_stream(cls, stream) -> "ClickUpAuthenticator":
        return cls(
            stream=stream,
            auth_endpoint="TODO: OAuth Endpoint URL",
            oauth_scopes="TODO: OAuth Scopes",
        )
