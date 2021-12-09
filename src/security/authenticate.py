import os

from fastapi.security import APIKeyHeader
from fastapi import HTTPException, Security, status
 
X_API_KEY = APIKeyHeader(name="X-API-Key", auto_error=True)

async def validate_api_key(api_key_header: str = Security(X_API_KEY)):
    if api_key_header != os.getenv("X_API_KEY"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
