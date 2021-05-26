from connection_pool import ConnectionPool

import asyncio

#######  TCP SERVER #######
async def handle_connection(reader, writer):
    # Get a nickname for the new client
    writer.write('> Choose your nickname: '.encode())

    response = await reader.readuntil(b'\n')
    writer.nickname = response.decode().strip()

    connection_pool.add_new_user_to_pool(writer)
    connection_pool.send_welcome_message(writer)

    # Announce the arrivel of this new user
    connection_pool.broadcast_user_join(writer)

    while True:
        try:
            data = await reader.readuntil(b'\n')
        except asyncio.exceptions.IncompleteReadError:
            connection_pool.broadcast_user_quit(writer)
            break
        
        message = data.decode().strip()
        if message == '/quit':
            connection_pool.broadcast_user_quit(writer)
            break
        elif message == '/list':
            connection_pool.list_users(writer)
        else:
            connection_pool.broadcast_new_message(writer, message)
        await writer.drain()

        if writer.is_closing():
            break

    # We are now outside the message loop, and the user has quit. Let's clean up...
    writer.close()
    await writer.wait_closed()
    connection_pool.remove_user_from_pool(writer)

async def main():
    
    server = await asyncio.start_server(handle_connection, "0.0.0.0", 8889)

    async with server:
        await server.serve_forever()

connection_pool = ConnectionPool()
asyncio.run(main())