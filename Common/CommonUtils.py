from Config import Config
import platform
import enum

def get_os_system() -> Config.OsSystem:
    sys = platform.system()
    # print(f"system is {sys}")
    if sys == "Linux":
        return Config.OsSystem.LINUX
    elif sys == "Darwin":
        return Config.OsSystem.MAC
    elif sys == "Windows":
        return Config.OsSystem.WINDOWS
    return Config.OsSystem.UNKNOWN

def sort_enum(enum_list: [], reverse: bool = False):
    return sorted(enum_list, key=__sort, reverse= reverse)

def __sort(en: enum.Enum):
    return en.value