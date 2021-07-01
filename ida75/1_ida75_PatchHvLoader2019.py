__author__ = "Gerhart"
__license__ = "GPL3"
__version__ = "1.0.0"

import idaapi

def GetFuncByName(name):

    var_address = idc.get_name_ea_simple(name)

    if var_address == 0:
        print("variable "+name+" was not found")
        return 0

    f_address = idc.get_qword(var_address)

    if f_address == 0:
        print("function address is 0")
        return 0

    print(name+":"+hex(f_address))

    return f_address

def PatchHvLoader(hv_base_address, nop_count):

    print("patched hvloader address: " + hex(hv_base_address))

    ida_bytes.patch_byte(hv_base_address, 0xEB)
    ida_bytes.patch_byte(hv_base_address + 1, 0xFE)

    for i in range(0, nop_count):
        ida_bytes.patch_byte(hv_base_address + 2 + i, 0x90)


hv_load_address = GetFuncByName("p_HvlLoadHypervisor")
hv_launch_address = GetFuncByName("p_HvlLaunchHypervisor")
hvloader_base = GetFuncByName("hvloader_image_base")

# PatchHvLoader(hv_load_address, 3)
PatchHvLoader(hv_launch_address, 1)

print("patch is finished")
