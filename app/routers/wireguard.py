from fastapi import APIRouter

from app.utils.feature_flags import feature_flag


@feature_flag('api_endpoint_wireguard')
def get_wireguard_router() -> APIRouter():
    router = APIRouter()

    @router.get("/wireguard/", tags=["wireguard"])
    async def read_wireguard_config():
        return[{"ifname": "eth0"}, {"ip_addr": "192.168.178.2"}]

    @router.get("/users/", tags=["users"])
    async def read_users():
        return [{"username": "Rick"}, {"username": "Morty"}]

    @router.get("/users/me", tags=["users"])
    async def read_user_me():
        return {"username": "fakecurrentuser"}

    @router.get("/users/{username}", tags=["users"])
    async def read_user(username: str):
        return {"username": username}

    return router
