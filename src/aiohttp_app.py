from aiohttp import web

async def handle_ping(request):
    return web.json_response({"pong": True})

async def handle_echo(request):
    data = await request.json()
    data["echoed"] = True
    return web.json_response(data)

def create_app():
    app = web.Application()
    app.router.add_get("/ping", handle_ping)
    app.router.add_post("/echo", handle_echo)
    return app
