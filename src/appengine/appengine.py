from imgui_bundle import imgui, hello_imgui, immapp, glfw_utils
from imgui_bundle.immapp import static
from enum import Flag
import glfw


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
        self.flags = flags

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def run(self):
        pass

