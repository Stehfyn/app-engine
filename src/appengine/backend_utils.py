import ctypes
import glfw
from imgui_bundle import imgui
from typing import cast

def get_glfw_handle_from_imgui_viewport(vp: imgui.Viewport) -> glfw._GLFWwindow:
    ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
    ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object]
    address = ctypes.pythonapi.PyCapsule_GetPointer(vp.platform_handle, None)
    handle = ctypes.cast(address, ctypes.POINTER(glfw._GLFWwindow))
    return cast(glfw._GLFWwindow, handle)


def get_hwnd_from_imgui_viewport(vp: imgui.Viewport) -> int:
    ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
    ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]
    handle = ctypes.pythonapi.PyCapsule_GetPointer(vp.platform_handle_raw, None)
    return handle


