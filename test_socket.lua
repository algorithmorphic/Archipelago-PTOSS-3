local socket = require("socket")

local function test_socket_availability()
    local success, err = pcall(function()
        socket.socket.tcp4()
    end)
    if not success and string.find(err, "attempt to index a nil value") then
        print("TEST FAILED: socket.socket is nil or not callable")
        return false
    elseif not success then
        print("TEST FAILED: " .. err)
        return false
    else
        print("TEST PASSED: socket.socket.tcp4() is callable")
        return true
    end
end

local result = test_socket_availability()

if not result then
    os.exit(1)
end