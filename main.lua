
_G.Settings = {
['Name'] = 'Plane Crazy',
['Intro'] = false,
['Keybind'] = 'P'
}

local Creation = game.Workspace.PlayerAircraft
local PersonCopy = game.Workspace.PlayerAircraft
local Player = game.Players.LocalPlayer
local PersonCopyName = tostring("a")
local WedgeAboutToPutDown = 7
local TheShape = ""
local newblock = ""
local Ori = {}
local BuildZone = {}
local GridCenter = {}
local GridX = {}
local GridY = {}
local GridZ = {}
local colourE = {}
local materials = {
    ["Default"] = "Default",
    ["Glass"] = "g",
    ["Legacy Glass"] = "c",
    ["Wood"] = "w",
    ["Wooden Planks"] = "e",
    ["Metal"] = "m",
    ["Cobblestone"] = "t",
    ["Grass"] = "v",
    ["Diamond Plate"] = "d",
    ["Fabric"] = "f",
    ["Slate"] = "s",
    ["Corroded Metal"] = "n",
    ["Foil"] = "z",
    ["Ice"] = "i",
    ["Sand"] = "x"
}


game.Workspace.PlayerAircraft[game.Players.LocalPlayer.Name].ChildAdded:Connect(function(instance)
    newblock = instance
end)

function paint(instance, R, G, B)
    spawn(function()
        local A_1 = instance
        local A_2 = Color3.new(R, G, B)
        local Event = game:GetService("ReplicatedStorage").Remotes.Paint
        Event:FireServer(A_1, A_2)
    end)
end

function pmaterial(instance, material)
    spawn(function()
        local A_1 = instance
        local A_2 = material
        local Event = game:GetService("ReplicatedStorage").Remotes.Paint
        Event:FireServer(A_1, A_2)
    end)
end

function build(Pos, CFame, Type)
    local A_1 = Pos
    local A_2 = CFame
    local A_3 = Type
    local A_4 = ""
    local Event = game:GetService("ReplicatedStorage").Remotes.PlaceBIockRegion
    Event:InvokeServer(A_1, A_2, A_3, A_4)
end
function transformToColor3(col) --Function to convert, just cuz c;
    local r = col.r --Red value
    local g = col.g --Green value
    local b = col.b --Blue value
    return Color3.new(r,g,b); --Color3 datatype, made of the RGB inputs
end

function round(n)
    return (n + 0.5) - (n + 0.5) % 1
end

function Copy()
    for i,v in pairs(game.Workspace.BuildingZones:GetChildren()) do 
        if v.Owner.Value ~= nil then
            if tostring(v.Owner.Value) == PersonCopyName then
                BuildZone = v
                print(v)
                GridX = v.CFrame.x
                GridY = v.CFrame.y
                GridZ = v.CFrame.z
                GridCenter = v.CFrame.x, v.CFrame.y, v.CFrame.z
            end
        end
    end
                
    for i,v in pairs(game.Workspace.PlayerAircraft:GetChildren()) do
        if tostring(v.Name) == PersonCopyName then
            for a, model in pairs(v:GetChildren()) do
                print(model:getFullName())
                
                if model:IsA("Model") then
                    local TheLength = string.split(tostring(model.PrimaryPart.Size), ",")
                    local LengthX = TheLength[1] / 2.5
                    local LengthY = TheLength[2] / 2.5
                    local LengthZ = TheLength[3] / 2.5
                    colourE = string.split(tostring(transformToColor3(model.PrimaryPart.BrickColor)), ",")
                    local DifferenceX = round((model.PrimaryPart.CFrame.x - GridX) / 2.5)
                    local DifferenceY = round((model.PrimaryPart.CFrame.y - GridY) / 2.5)
                    local DifferenceZ = round((model.PrimaryPart.CFrame.z - GridZ) / 2.5)
                    local ThePos = Vector3.new(DifferenceX, DifferenceY, DifferenceZ)
                    print(LengthX, LengthY, LengthZ)
                    print(model.PrimaryPart.Name)
                    pcall(function()
                        TheShape = model.PrimaryPart.Shape
                        print(model.PrimaryPart.Shape)
                    end)
                    
                    if model:FindFirstChild("MotorBlock") then
                        build(ThePos, model.PrimaryPart.CFrame, 12)
                    elseif model:FindFirstChild("SelectedPart") then
                        build(ThePos, model.PrimaryPart.CFrame, 69)
                    elseif TheShape == Enum.PartType.Cylinder then
                        print("Found Cylinder")
                        if LengthY == 1 then
                            build(ThePos, model.PrimaryPart.CFrame, 78)
                        elseif LengthY == 2 then
                            if model:FindFirstChild("ArrowOffset") then
                                build(ThePos, model.PrimaryPart.CFrame, 112)
                            else 
                                build(ThePos, model.PrimaryPart.CFrame, 125)
                            end
                        elseif LengthY == 3 then
                            build(ThePos, model.PrimaryPart.CFrame, 79)
                        elseif LengthY == 5 then
                            build(ThePos, model.PrimaryPart.CFrame, 120)
                        end
                        TheShape = ""
                        
                    elseif tostring(model.PrimaryPart.ClassName) == "WedgePart" then
                        if LengthX == 1 and LengthY == 0.5 and LengthZ == 0.5 then
                            WedgeAboutToPutDown = 70
                        elseif LengthX == 1 and LengthY == 0.5 and LengthZ == 1 then
                            WedgeAboutToPutDown = 45
                        elseif LengthX == 1 and LengthY == 0.5 and LengthZ == 2 then
                            WedgeAboutToPutDown = 85
                        elseif LengthZ == 1 then
                            WedgeAboutToPutDown = 7
                        elseif LengthZ == 2 then
                            WedgeAboutToPutDown = 17
                        elseif LengthZ == 3 then
                            WedgeAboutToPutDown = 31
                        elseif LengthZ == 4 then
                            WedgeAboutToPutDown = 87
                        end
                        build(Vector3.new(DifferenceX, DifferenceY, DifferenceZ), model.PrimaryPart.CFrame, WedgeAboutToPutDown)
                    elseif LengthX == 1 and LengthY == 0.5 and LengthZ == 1 then
                        build(ThePos, model.PrimaryPart.CFrame, 26)
                    elseif LengthY == 1 then
                        build(ThePos, model.PrimaryPart.CFrame, 1)
                    elseif LengthX == 1 and LengthY == 1 and LengthZ == 4 then
                        build(ThePos, model.PrimaryPart.CFrame, 16)
                    elseif LengthX == 1 and LengthY == 1 and LengthZ == 7 then
                        build(ThePos, model.PrimaryPart.CFrame, 38)
                    end
                    
                    pcall(function()
                        paint(newblock.PrimaryPart, colourE[1], colourE[2], colourE[3])
                        pmaterial(newblock.PrimaryPart, materials[newblock.PrimaryPart.Material])
                    end)
                end
            end
        end
    end
end

local Library = loadstring(game:HttpGet("https://pastebin.com/raw/QPehPJ6m", true))()

local Tab1 = Library:CreateTab('Tab1')

Tab1:Label('Copy Builds')
Tab1:Button('Copy', function()
Copy()
end)

Tab1:TextBox('Name', 'Name Here', function(output)
pcall(function()
PersonCopy = Creation[output]
PersonCopyName = tostring(output)
print(PersonCopy)
print(PersonCopyName)
end)
end)

Tab1:Label('Made by Nexity#3200')

local Tab2 = Library:CreateTab('Tab2')
Tab2:Button('Destroy this GUI', function()
    game:GetService("CoreGui").ShadowLib:Destroy()
end)
