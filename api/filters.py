from rest_framework.compat import coreapi
from rest_framework.filters import SearchFilter
import coreapi

class UsernameFilter(SearchFilter):
    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name="username",
                location="query",
                required=False,
                type="string",
                description="filter by Username",
            )
        ]