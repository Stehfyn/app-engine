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
        self.runner_params.app_window_params.window_geometry.size = (1400, 900)
        self.runner_params.imgui_window_params.show_menu_bar = True
        self.runner_params.imgui_window_params.show_status_bar = True
        self.runner_params.app_window_params.restore_previous_geometry = True
        self.runner_params.app_window_params.borderless = True
       #self.runner_params.app_window_params.borderless = True
        self.runner_params.app_window_params.resizable = True

        # First, tell HelloImGui that we want full screen dock space (this will create "MainDockSpace")
        self.runner_params.imgui_window_params.default_imgui_window_type = (
            hello_imgui.DefaultImGuiWindowType.provide_full_screen_dock_space
        )

        self.runner_params.imgui_window_params.enable_viewports = True
        #self.runner_params.docking_params.dockable_windows = dockable_windows

        @static(nb_frames=0, sel=False)
        def show_gui():
            if show_gui.nb_frames == 1:
                # Focus cannot be given at frame 0, since some additional windows will
                # be created after (and will steal the focus)
                #self.runner_params.app_window_params.borderless = True
                self.runner_params.imgui_window_params.show_status_fps = True
                self.runner_params.imgui_window_params.show_status_bar = False
                self.runner_params.imgui_window_params.background_color = (0,0,0,0)
                self.runner_params.imgui_window_params.show_menu_bar = False
                imgui.get_io().config_viewports_no_decoration = True
                # hello_imgui.image_from_asset("images/UNR-active.png", imgui.ImVec2(32,32))

            tex = hello_imgui.im_texture_id_from_asset("images/UNR-active.png")
            close = hello_imgui.im_texture_id_from_asset("images/close.png")
            imgui.push_style_var(imgui.StyleVar_.frame_padding, imgui.ImVec2(10, 10))
            if (imgui.begin_main_menu_bar()):
                imgui.pop_style_var(1)
                # imgui.image(tex, imgui.ImVec2(32,32))
                start = imgui.get_cursor_screen_pos()
                start.y -= 2
                end = imgui.ImVec2(start.x + 36, start.y + 36)
                imgui.get_window_draw_list().add_image(tex, start, end)
                imgui.dummy(imgui.ImVec2(36, 36))
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


                imgui.indent(600)
                imgui.push_item_width(120)

                imgui.set_cursor_pos_y(imgui.get_cursor_pos_y() +6)
                imgui.input_text_with_hint("Search","Search (Ctrl+Q)","")
                imgui.pop_item_width()
                start = imgui.ImVec2(imgui.get_window_width() - imgui.get_style().window_padding.x - 32, imgui.get_cursor_pos_y())
                start.y -= 2
                end = imgui.ImVec2(start.x + 32, start.y + 32)
                imgui.set_cursor_pos(start)
                #imgui.get_window_draw_list().add_image(close, start, end)
                #imgui.dummy(imgui.ImVec2(36, 36))
                if(imgui.image_button("", close, imgui.ImVec2(32,32))):
                    hello_imgui.get_runner_params().app_shall_exit = True
                if imgui.is_window_hovered() and imgui.is_mouse_dragging(0):
                    viewport = imgui.get_main_viewport().pos
                    viewport.x += imgui.get_mouse_drag_delta().x
                    viewport.y += imgui.get_mouse_drag_delta().y
                    #hello_imgui.get_runner_params().app_window_params.window_geometry.position_mode = hello_imgui.WindowPositionMode(2)
                    hello_imgui.get_runner_params().app_window_params.window_geometry.position[0] = 10
                    hello_imgui.get_runner_params().app_window_params.window_geometry.position[1] = 10
                    #hello_imgui.get_runner_params().app_window_params.window_geometry.resize_app_window_at_next_frame = True
                    imgui.get_io().config_windows_move_from_title_bar_only = False


                imgui.end_main_menu_bar()




            show_gui.nb_frames += 1

        self.runner_params.callbacks.show_gui = show_gui
        #imgui.internal.DockNodeFlags.
        #imgui.internal.find_window_by_name()


        bottom = hello_imgui.DockingSplit()
        bottom.initial_dock = "MainDockSpace"
        bottom.new_dock = "BottomSpace"
        bottom.direction = imgui.Dir_(3)
        bottom.ratio = 0.25

        self.runner_params.docking_params.docking_splits = [ bottom]

        #filemenu.imgui_window_flags = (1 << 21)

        logsWindow = hello_imgui.DockableWindow()
        logsWindow.label = "Logs"
        logsWindow.dock_space_name = "BottomSpace"
        #logsWindow.gui_function = hello_imgui.log_gui
        #mgui.IO.config_viewports_no_decoration = True

        @static(init=0, x=0, y=0)
        def logger():
            if logger.init == 1:
                pass
                #flags = imgui.internal.get_current_window().dock_node.local_flags
                #flags |= (1 << 15)
                #imgui.internal.get_current_window().dock_node.set_local_flags(flags)
                #imgui.get_io().config_viewports_no_decoration = True
            imgui.show_style_editor()
            yah1, logger.x = imgui.slider_float("x", logger.x, 0, 1080)
            yah2, logger.y = imgui.slider_float("y", logger.y, 0, 1920)
            #imgui.set_window_pos("Logs", imgui.ImVec2(logger.x,logger.y))
            ##imgui.internal.get_current_window().set_window_pos_val.x = logger.x
            ##imgui.internal.get_current_window().set_window_pos_val.x = logger.y

            logger.init += 1

        logsWindow.gui_function = logger
        self.runner_params.docking_params.dockable_windows = [logsWindow]

        def load_fonts():
            myriadpro = hello_imgui.load_font_ttf("fonts/MyriadPro-Light.ttf", 14)
            imgui.get_io().font_default = myriadpro

        self.runner_params.callbacks.load_additional_fonts = load_fonts
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def run(self):
        immapp.run(runner_params=self.runner_params)