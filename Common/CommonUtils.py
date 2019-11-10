from Config import Config
import platform

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