local socket = require("socket")

-- Adicionando uma verificação para garantir que socket.tcp não é nil
if not socket.tcp then
    print("Error: socket.tcp is nil. Please ensure lua-socket is properly installed and configured.")
    -- Pode ser necessário adicionar um mecanismo de fallback ou sair aqui
    return
end

function initialize_server ()
    local err
    local port = SOCKET_PORT_FIRST
    local res = nil

    server, err = socket.tcp()
    while res == nil and port <= SOCKET_PORT_LAST do
        res, err = server:bind("localhost", port)
        if res == nil and err ~= "address already in use" then
            print(err)
            return
        end

        if res == nil then
            port = port + 1
        end
    end

    if res == nil then
        print("Error: Could not bind to any port in the range.")
        return
    end

    server:settimeout(0)
    print("Server initialized on port " .. port)
end
