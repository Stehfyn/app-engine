from imgui_bundle import imgui, hello_imgui, immapp
from imgui_bundle.immapp import static

def go():
    app = __App()
    try:
        with app:
            app.run()

    except Exception as e:
        raise e

    return 0

class __App:
    def __init__(self):

        self.runner_params = hello_imgui.RunnerParams()
        self.runner_params.app_window_params.window_title = "Dear ImGui Bundle interactive manual"

        self.runner_params.app_window_params.hidden = True

        self.runner_params.imgui_window_params.show_menu_bar = True
        self.runner_params.imgui_window_params.show_status_bar = True
        self.runner_params.imgui_window_params.config_windows_move_from_title_bar_only = False

        self.runner_params.imgui_window_params.default_imgui_window_type = (
            hello_imgui.DefaultImGuiWindowType.no_default_window
        )

        self.runner_params.imgui_window_params.enable_viewports = True

        def init():
            imgui.get_io().config_viewports_no_auto_merge = True
            self.logo_tex = hello_imgui.im_texture_id_from_asset("images/UNR-active.png")
            self.close_tex = hello_imgui.im_texture_id_from_asset("images/close.png")

        @static(init=True, sel=False)
        def show_gui():
            imgui.show_style_editor()

            imgui.begin("hi", None, imgui.WindowFlags_.menu_bar | imgui.WindowFlags_.no_title_bar | imgui.WindowFlags_.no_docking | imgui.WindowFlags_.no_bring_to_front_on_focus)
            if show_gui.init:
                imgui.set_window_size(imgui.ImVec2(400, 60))
                show_gui.init = False
            #imgui.push_style_var(imgui.StyleVar_.frame_padding, imgui.ImVec2(0, 10))

            if (imgui.internal.begin_viewport_side_bar("MainMenuBar", imgui.get_window_viewport(), imgui.Dir_.up,
                                                       imgui.get_frame_height(),
                                                       imgui.WindowFlags_.menu_bar | imgui.WindowFlags_.no_title_bar | imgui.WindowFlags_.no_docking | imgui.WindowFlags_.no_saved_settings)):
                imgui.push_clip_rect(imgui.ImVec2(imgui.get_window_width(), imgui.get_frame_height()), imgui.ImVec2(imgui.get_window_width(), imgui.get_frame_height() * 2), True)
                #imgui.pop_style_var(1)
                if (imgui.begin_menu_bar()):
                    start = imgui.get_cursor_screen_pos()
                    end = imgui.ImVec2(start.x + imgui.get_frame_height(), start.y + imgui.get_frame_height())
                    imgui.get_window_draw_list().add_image(self.logo_tex, start, end)
                    imgui.dummy(imgui.ImVec2(imgui.get_frame_height(), imgui.get_frame_height()))

                    if (imgui.begin_popup_context_item("App Context Menu")):
                        if (imgui.selectable("Restore", show_gui.sel)):
                            pass
                        if (imgui.selectable("Move", show_gui.sel)):
                            pass
                        if (imgui.selectable("Size", show_gui.sel)):
                            pass
                        if (imgui.selectable("Minimize", show_gui.sel)):
                            pass
                        clicked, val = imgui.selectable("Close", show_gui.sel)
                        if clicked:
                            hello_imgui.get_runner_params().app_shall_exit = True
                        imgui.end_popup()
                    imgui.open_popup_on_item_click("App Context Menu", 0)

                    if (imgui.is_item_hovered() and imgui.is_mouse_double_clicked(0)):
                        self.runner_params.app_shall_exit = True
                    if (imgui.begin_menu(("File"))):
                        imgui.end_menu()
                    if (imgui.begin_menu(("Edit"))):
                        imgui.end_menu()
                    if (imgui.begin_menu(("Select"))):
                        imgui.end_menu()

                    imgui.push_item_width(120)
                    imgui.input_text_with_hint("##search", "Search (Ctrl+Q)", "",)
                    imgui.pop_item_width()

                    start = imgui.get_cursor_pos()
                    start.x = imgui.get_window_width() - imgui.get_frame_height() - imgui.get_style().frame_padding.x
                    imgui.set_cursor_pos(start)
                    #imgui.push_style_var(imgui.StyleVar_.frame_padding, imgui.ImVec2(0,0))
                    padding = imgui.get_style().frame_padding
                    if (imgui.image_button("", self.close_tex, imgui.ImVec2(imgui.get_frame_height() - padding.x, imgui.get_frame_height() - padding.x))):
                        hello_imgui.get_runner_params().app_shall_exit = True
                    #imgui.pop_style_var(1)
                    imgui.end_menu_bar()

                    imgui.pop_clip_rect()

                    imgui.end()

            imgui.end()

        self.runner_params.callbacks.post_init = init
        self.runner_params.callbacks.show_gui = show_gui

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def run(self):
        immapp.run(runner_params=self.runner_params)