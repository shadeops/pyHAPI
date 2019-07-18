import ctypes as _ctypes
from platform import system as _system_platform

if _system_platform() == 'Windows':
    libHAPI = _ctypes.cdll.LoadLibrary('libHAPIL.lib')
else:
    libHAPI = _ctypes.cdll.LoadLibrary('libHAPIL.so')

