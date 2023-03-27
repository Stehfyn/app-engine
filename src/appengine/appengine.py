from imgui_bundle import imgui, hello_imgui, immapp, glfw_utils
from imgui_bundle.immapp import static
from enum import Flag
import glfw
from  . import backend_utils
from .window_effect import *
import ctypes
import win32gui


class AppFlags(Flag):
    MonitorDockspace = (1 << 0)
    CustomTitlebar = (1 << 1)


def go(flags: AppFlags) -> int:
    app = __App(flags)
    try:
        with app:
            app.run()

    except Exception as e:
        raise e

    return 0


class __App:
    def __init__(self, flags: AppFlags) -> None:
        self.runner_params = hello_imgui.RunnerParams()
        self.runner_params.app_window_params.hidden = False
        self.runner_params.imgui_window_params.default_imgui_window_type = (
            hello_imgui.DefaultImGuiWindowType.provide_full_screen_dock_space
        )
        self.runner_params.imgui_window_params.enable_viewports = True
        self.runner_params.imgui_window_params.config_windows_move_from_title_bar_only = False
        self.flags = flags
        self.coords = None

        @static()
        def init():
            imgui.get_io().config_viewports_no_decoration = False
            imgui.get_io().config_viewports_no_auto_merge = True
            imgui.get_io().config_windows_move_from_title_bar_only = False

            self.monitors = glfw.get_monitors()
            for monitor in self.monitors:
                print(glfw.get_monitor_workarea(monitor))
            print(len(self.monitors))

        @static(nb_frames=0, do_overlap=False)
        def show_gui():
            def do_monitor_dockspace():
                for i, monitor in enumerate(self.monitors):
                    if show_gui.nb_frames == 0:
                        workarea = glfw.get_monitor_workarea(monitor)
                        imgui.set_next_window_pos(imgui.ImVec2(workarea[0], workarea[1]))
                        imgui.set_next_window_size(imgui.ImVec2(workarea[2], workarea[3]))

                    mdock_flags = imgui.WindowFlags_.no_title_bar | imgui.WindowFlags_.no_background | imgui.WindowFlags_.no_resize | imgui.WindowFlags_.no_move | imgui.WindowFlags_.no_collapse | imgui.WindowFlags_.no_bring_to_front_on_focus
                    wc = imgui.WindowClass()
                    wc.docking_always_tab_bar = False
                    wc.dock_node_flags_override_set = imgui.DockNodeFlags_.auto_hide_tab_bar | imgui.DockNodeFlags_.no_docking_in_central_node
                    imgui.set_next_window_class(wc)
                    imgui.begin(f"md{i+1}", None, mdock_flags)
                    imgui.end()

            #do_monitor_dockspace()

            wc = imgui.WindowClass()
            wc.docking_always_tab_bar = False
            #wc.dock_node_flags_override_set = imgui.DockNodeFlags_.auto_hide_tab_bar
            imgui.set_next_window_class(wc)
            imgui.begin("hi", None, imgui.WindowFlags_.no_bring_to_front_on_focus)
            vp = imgui.get_window_viewport()
            if show_gui.nb_frames > 10:
                handle = backend_utils.get_glfw_handle_from_imgui_viewport(vp)
                #glfw.set_window_pos_callback(handle, )
                hwnd = backend_utils.get_hwnd_from_imgui_viewport(vp)

                if show_gui.nb_frames == 12:
                    window_effect = WindowsWindowEffect()
                    glfw.set_window_pos(handle, 8, 31)
                    #window_effect.setAeroEffect(hwnd)
                    print(win32gui.GetWindowRect(hwnd))
                    self.coords = win32gui.GetWindowRect(hwnd)
                    show_gui.do_overlap = True


            #handle = ctypes.cast(ctypes.c_void_p(int(vp.platform_handle)), ctypes.POINTER(ctypes.c_int))
            imgui.end()

            if self.coords != None:
                print(show_gui.nb_frames)
                print(self.coords)
                self.coords = win32gui.GetWindowRect(hwnd)
                wc = imgui.WindowClass()
                wc.viewport_flags_override_set = imgui.ViewportFlags_.no_decoration | imgui.ViewportFlags_.top_most
                imgui.set_next_window_class(wc)
                imgui.set_next_window_pos(imgui.ImVec2(self.coords[0], self.coords[1]))
                imgui.set_next_window_size(imgui.ImVec2(400, 31))
                imgui.begin("anotherWindow", True, imgui.WindowFlags_.no_inputs)
                imgui.end()

            show_gui.nb_frames += 1

        self.runner_params.callbacks.post_init = init
        self.runner_params.callbacks.show_gui = show_gui

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def run(self):
        immapp.run(runner_params=self.runner_params)

