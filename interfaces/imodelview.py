# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html


class IModelView:
    def __init__(self, parent=None):
        self._instance = parent

    @property
    def camera(self):
        """Gets or sets the camera."""
        return self._instance.Camera

    @camera.setter
    def camera(self, value):
        """Gets or sets the camera."""
        self._instance.Camera = value

    @property
    def display_mode(self):
        """Gets or sets the display mode for this model view."""
        return self._instance.DisplayMode

    @display_mode.setter
    def display_mode(self, value):
        """Gets or sets the display mode for this model view."""
        self._instance.DisplayMode = value

    @property
    def display_zebra_stripes(self):
        """Gets or sets the zebra-line display state."""
        return self._instance.DisplayZebraStripes

    @display_zebra_stripes.setter
    def display_zebra_stripes(self, value):
        """Gets or sets the zebra-line display state."""
        self._instance.DisplayZebraStripes = value

    @property
    def dynamic_mode(self):
        """Gets the dynamic mode."""
        return self._instance.DynamicMode

    @dynamic_mode.setter
    def dynamic_mode(self, value):
        """Gets the dynamic mode."""
        self._instance.DynamicMode = value

    @property
    def enable_graphics_update(self):
        """Gets or sets whether or not to refresh the model view."""
        return self._instance.EnableGraphicsUpdate

    @enable_graphics_update.setter
    def enable_graphics_update(self, value):
        """Gets or sets whether or not to refresh the model view."""
        self._instance.EnableGraphicsUpdate = value

    @property
    def frame_height(self):
        """Get or sets the height of the frame of the document window that contains the model view in the SOLIDWORKS
        client area."""
        return self._instance.FrameHeight

    @frame_height.setter
    def frame_height(self, value):
        """Get or sets the height of the frame of the document window that contains the model view in the SOLIDWORKS
        client area."""
        self._instance.FrameHeight = value

    @property
    def frame_left(self):
        """Gets or sets the left position of the frame of the document window that contains the model view in the
        SOLIDWORKS client area."""
        return self._instance.FrameLeft

    @frame_left.setter
    def frame_left(self, value):
        """Gets or sets the left position of the frame of the document window that contains the model view in the
        SOLIDWORKS client area."""
        self._instance.FrameLeft = value

    @property
    def frame_state(self):
        """Gets or sets the window state (minimum, maximum, or normal) for the frame of the document window that
        contains the model view in the SOLIDWORKS client area."""
        return self._instance.FrameState

    @frame_state.setter
    def frame_state(self, value):
        """Gets or sets the window state (minimum, maximum, or normal) for the frame of the document window that
        contains the model view in the SOLIDWORKS client area."""
        self._instance.FrameState = value

    @property
    def frame_top(self):
        """Gets or sets the top position of the frame of the document window that contains the model view in the
        SOLIDWORKS client area."""
        return self._instance.FrameTop

    @frame_top.setter
    def frame_top(self, value):
        """Gets or sets the top position of the frame of the document window that contains the model view in the
        SOLIDWORKS client area."""
        self._instance.FrameTop = value

    @property
    def frame_width(self):
        """Gets or sets the width of the frame of the document window that contains the model view in the SOLIDWORKS
        client area."""
        return self._instance.FrameWidth

    @frame_width.setter
    def frame_width(self, value):
        """Gets or sets the width of the frame of the document window that contains the model view in the SOLIDWORKS
        client area."""
        self._instance.FrameWidth = value

    @property
    def hlr_quality(self):
        """Gets or sets the hidden-line removal quality property of this model view."""
        return self._instance.HlrQuality

    @hlr_quality.setter
    def hlr_quality(self, value):
        """Gets or sets the hidden-line removal quality property of this model view."""
        self._instance.HlrQuality = value

    @property
    def linked(self):
        """Gets whether or not this viewport is linked or not."""
        return self._instance.Linked

    @linked.setter
    def linked(self, value):
        """Gets whether or not this viewport is linked or not."""
        self._instance.Linked = value

    @property
    def object_sizes_away(self):
        """Helps define the perspective of the current model view by relating the size of a displayed object with the
        distance of the object from the observer."""
        return self._instance.ObjectSizesAway

    @object_sizes_away.setter
    def object_sizes_away(self, value):
        """Helps define the perspective of the current model view by relating the size of a displayed object with the
        distance of the object from the observer."""
        self._instance.ObjectSizesAway = value

    @property
    def orientation(self):
        """Gets or sets the model view orientation matrix."""
        return self._instance.Orientation3

    @orientation.setter
    def orientation(self, value):
        """Gets or sets the model view orientation matrix."""
        self._instance.Orientation3 = value

    @property
    def scale(self):
        """Gets and sets the model view scale factor."""
        return self._instance.Scale2

    @scale.setter
    def scale(self, value):
        """Gets and sets the model view scale factor."""
        self._instance.Scale2 = value

    @property
    def suppress_wait_cursor_during_redraw(self):
        """Gets or sets the state of the wait cursor (also called the hourglass) while this model view is being
        redrawn."""
        return self._instance.SuppressWaitCursorDuringRedraw

    @suppress_wait_cursor_during_redraw.setter
    def suppress_wait_cursor_during_redraw(self, value):
        """Gets or sets the state of the wait cursor (also called the hourglass) while this model view is being
        redrawn."""
        self._instance.SuppressWaitCursorDuringRedraw = value

    @property
    def transform(self):
        """Gets the model space to the model view plane transform.
NOTE: This property is a get-only property. Set is not implemented."""
        return self._instance.Transform

    @transform.setter
    def transform(self, value):
        """Gets the model space to the model view plane transform.
NOTE: This property is a get-only property. Set is not implemented."""
        self._instance.Transform = value

    @property
    def translation(self):
        """Gets or sets the model view translation vector."""
        return self._instance.Translation3

    @translation.setter
    def translation(self, value):
        """Gets or sets the model view translation vector."""
        self._instance.Translation3 = value

    @property
    def update_all_graphics_layers(self):
        """Gets or sets whether to update all graphic layers in any mode."""
        return self._instance.UpdateAllGraphicsLayers

    @update_all_graphics_layers.setter
    def update_all_graphics_layers(self, value):
        """Gets or sets whether to update all graphic layers in any mode."""
        self._instance.UpdateAllGraphicsLayers = value

    @property
    def visibility_view_tools(self):
        """Gets or sets the visibility of the Heads-up View Toolbar for this model view."""
        return self._instance.VisibilityViewTools

    @visibility_view_tools.setter
    def visibility_view_tools(self, value):
        """Gets or sets the visibility of the Heads-up View Toolbar for this model view."""
        self._instance.VisibilityViewTools = value

    @property
    def xor_highlight(self):
        """Gets or sets the Xor highlight state."""
        return self._instance.XorHighlight

    @xor_highlight.setter
    def xor_highlight(self, value):
        """Gets or sets the Xor highlight state."""
        self._instance.XorHighlight = value

    @property
    def activate(self):
        """Activates the model view."""
        return self._instance.Activate

    @activate.setter
    def activate(self, value):
        """Activates the model view."""
        self._instance.Activate = value

    @property
    def add_perspective(self):
        """Adds perspective to the model view."""
        return self._instance.AddPerspective

    @add_perspective.setter
    def add_perspective(self, value):
        """Adds perspective to the model view."""
        self._instance.AddPerspective = value

    @property
    def create_callout(self):
        """Creates a callout on this model view."""
        return self._instance.CreateCallout

    @create_callout.setter
    def create_callout(self, value):
        """Creates a callout on this model view."""
        self._instance.CreateCallout = value

    @property
    def draw_highlighted_items(self):
        """Draws or redraws the highlighted items."""
        return self._instance.DrawHighlightedItems

    @draw_highlighted_items.setter
    def draw_highlighted_items(self, value):
        """Draws or redraws the highlighted items."""
        self._instance.DrawHighlightedItems = value

    @property
    def draw_transparent_feature_tree(self):
        """Draws a transparent FeatureManager design tree."""
        return self._instance.DrawTransparentFeatureTree

    @draw_transparent_feature_tree.setter
    def draw_transparent_feature_tree(self, value):
        """Draws a transparent FeatureManager design tree."""
        self._instance.DrawTransparentFeatureTree = value

    @property
    def get_bkgd_image_display_area_aspect_ratio(self):
        """Gets the aspect ratio (width/height) of the area of the window where the background image is displayed."""
        return self._instance.GetBkgdImageDisplayAreaAspectRatio

    @get_bkgd_image_display_area_aspect_ratio.setter
    def get_bkgd_image_display_area_aspect_ratio(self, value):
        """Gets the aspect ratio (width/height) of the area of the window where the background image is displayed."""
        self._instance.GetBkgdImageDisplayAreaAspectRatio = value

    @property
    def get_display_state(self):
        """Gets the display state of this model view."""
        return self._instance.GetDisplayState

    @get_display_state.setter
    def get_display_state(self, value):
        """Gets the display state of this model view."""
        self._instance.GetDisplayState = value

    @property
    def get_eye_point(self):
        """Gets the eye position for perspective viewing."""
        return self._instance.GetEyePoint

    @get_eye_point.setter
    def get_eye_point(self, value):
        """Gets the eye position for perspective viewing."""
        self._instance.GetEyePoint = value

    @property
    def get_iso_plane_distance(self):
        """Gets the distance, in terms of screen space, from the eye position to the plane at which there is no scaling due to perspective."""
        return self._instance.GetIsoPlaneDistance

    @get_iso_plane_distance.setter
    def get_iso_plane_distance(self, value):
        """Gets the distance, in terms of screen space, from the eye position to the plane at which there is no scaling due to perspective."""
        self._instance.GetIsoPlaneDistance = value

    @property
    def get_mouse(self):
        """Gets the mouse for this model view."""
        return self._instance.GetMouse

    @get_mouse.setter
    def get_mouse(self, value):
        """Gets the mouse for this model view."""
        self._instance.GetMouse = value

    @property
    def get_next(self):
        """Gets the next model view after this model view."""
        return self._instance.GetNext

    @get_next.setter
    def get_next(self, value):
        """Gets the next model view after this model view."""
        self._instance.GetNext = value

    @property
    def get_view_d_i_b(self):
        """Gets an image of the document as it looks in Normal view or in the print preview."""
        return self._instance.GetViewDIB

    @get_view_d_i_b.setter
    def get_view_d_i_b(self, value):
        """Gets an image of the document as it looks in Normal view or in the print preview."""
        self._instance.GetViewDIB = value

    @property
    def get_view_d_i_bx(self):
        """Gets an image of the document as it looks in Normal view or in the print preview in 64-bit applications."""
        return self._instance.GetViewDIBx64

    @get_view_d_i_bx.setter
    def get_view_d_i_bx(self, value):
        """Gets an image of the document as it looks in Normal view or in the print preview in 64-bit applications."""
        self._instance.GetViewDIBx64 = value

    @property
    def get_view_h_wnd(self):
        """Gets the Microsoft window handle for this model view."""
        return self._instance.GetViewHWnd

    @get_view_h_wnd.setter
    def get_view_h_wnd(self, value):
        """Gets the Microsoft window handle for this model view."""
        self._instance.GetViewHWnd = value

    @property
    def get_view_h_wndx(self):
        """Gets the Microsoft window handle for this model view in 64-bit applications."""
        return self._instance.GetViewHWndx64

    @get_view_h_wndx.setter
    def get_view_h_wndx(self, value):
        """Gets the Microsoft window handle for this model view in 64-bit applications."""
        self._instance.GetViewHWndx64 = value

    @property
    def get_view_plane_distance(self):
        """Gets the model view plane distance for perspective viewing."""
        return self._instance.GetViewPlaneDistance

    @get_view_plane_distance.setter
    def get_view_plane_distance(self, value):
        """Gets the model view plane distance for perspective viewing."""
        self._instance.GetViewPlaneDistance = value

    @property
    def get_visible_box(self):
        """Gets the boundaries of the visible model view window."""
        return self._instance.GetVisibleBox

    @get_visible_box.setter
    def get_visible_box(self, value):
        """Gets the boundaries of the visible model view window."""
        self._instance.GetVisibleBox = value

    @property
    def graphics_redraw(self):
        """Redraws the specified region of or the entire SOLIDWORKS graphics window."""
        return self._instance.GraphicsRedraw

    @graphics_redraw.setter
    def graphics_redraw(self, value):
        """Redraws the specified region of or the entire SOLIDWORKS graphics window."""
        self._instance.GraphicsRedraw = value

    @property
    def has_perspective(self):
        """Determines if the model view currently has perspective."""
        return self._instance.HasPerspective

    @has_perspective.setter
    def has_perspective(self, value):
        """Determines if the model view currently has perspective."""
        self._instance.HasPerspective = value

    @property
    def hide_magnifying_glass(self):
        """Hides the Magnifying Glass tool."""
        return self._instance.HideMagnifyingGlass

    @hide_magnifying_glass.setter
    def hide_magnifying_glass(self, value):
        """Hides the Magnifying Glass tool."""
        self._instance.HideMagnifyingGlass = value

    @property
    def i_get_eye_point(self):
        """Gets the eye position for perspective viewing."""
        return self._instance.IGetEyePoint

    @i_get_eye_point.setter
    def i_get_eye_point(self, value):
        """Gets the eye position for perspective viewing."""
        self._instance.IGetEyePoint = value

    @property
    def i_get_next(self):
        """Gets the next model view after this model view."""
        return self._instance.IGetNext

    @i_get_next.setter
    def i_get_next(self, value):
        """Gets the next model view after this model view."""
        self._instance.IGetNext = value

    @property
    def i_get_visible_box(self):
        """Gets the boundaries of the visible model view window."""
        return self._instance.IGetVisibleBox

    @i_get_visible_box.setter
    def i_get_visible_box(self, value):
        """Gets the boundaries of the visible model view window."""
        self._instance.IGetVisibleBox = value

    @property
    def i_graphics_redraw(self):
        """Redraws the specified region of or the entire SOLIDWORKS graphics window."""
        return self._instance.IGraphicsRedraw

    @i_graphics_redraw.setter
    def i_graphics_redraw(self, value):
        """Redraws the specified region of or the entire SOLIDWORKS graphics window."""
        self._instance.IGraphicsRedraw = value

    @property
    def initialize_shading(self):
        """Sets up the model view for OpenGL shading."""
        return self._instance.InitializeShading

    @initialize_shading.setter
    def initialize_shading(self, value):
        """Sets up the model view for OpenGL shading."""
        self._instance.InitializeShading = value

    @property
    def i_set_eye_point(self):
        """Sets the eye position for perspective viewing."""
        return self._instance.ISetEyePoint

    @i_set_eye_point.setter
    def i_set_eye_point(self, value):
        """Sets the eye position for perspective viewing."""
        self._instance.ISetEyePoint = value

    @property
    def move_magnifying_glass(self):
        """Moves Magnifying Glass tool to the specified coordinates."""
        return self._instance.MoveMagnifyingGlass

    @move_magnifying_glass.setter
    def move_magnifying_glass(self, value):
        """Moves Magnifying Glass tool to the specified coordinates."""
        self._instance.MoveMagnifyingGlass = value

    @property
    def remove_perspective(self):
        """Removes perspective from the model view."""
        return self._instance.RemovePerspective

    @remove_perspective.setter
    def remove_perspective(self, value):
        """Removes perspective from the model view."""
        self._instance.RemovePerspective = value

    @property
    def roll_by(self):
        """Rolls the model view about the line of sight by the specified angle."""
        return self._instance.RollBy

    @roll_by.setter
    def roll_by(self, value):
        """Rolls the model view about the line of sight by the specified angle."""
        self._instance.RollBy = value

    @property
    def rotate_about_axis(self):
        """Rotates the model view about a point, by an angle in the specified direction."""
        return self._instance.RotateAboutAxis

    @rotate_about_axis.setter
    def rotate_about_axis(self, value):
        """Rotates the model view about a point, by an angle in the specified direction."""
        self._instance.RotateAboutAxis = value

    @property
    def rotate_about_center(self):
        """Rotates the model view about the screen X and Y axes."""
        return self._instance.RotateAboutCenter

    @rotate_about_center.setter
    def rotate_about_center(self, value):
        """Rotates the model view about the screen X and Y axes."""
        self._instance.RotateAboutCenter = value

    @property
    def rotate_about_point(self):
        """Rotates the model view about the specified point by the specified angles in the directions of the screen X and Y axes."""
        return self._instance.RotateAboutPoint

    @rotate_about_point.setter
    def rotate_about_point(self, value):
        """Rotates the model view about the specified point by the specified angles in the directions of the screen X and Y axes."""
        self._instance.RotateAboutPoint = value

    @property
    def set_camera_by_name(self):
        """Sets the model view to that of the specified camera, if in camera view mode."""
        return self._instance.SetCameraByName

    @set_camera_by_name.setter
    def set_camera_by_name(self, value):
        """Sets the model view to that of the specified camera, if in camera view mode."""
        self._instance.SetCameraByName = value

    @property
    def set_eye_point(self):
        """Sets the eye position for perspective viewing."""
        return self._instance.SetEyePoint

    @set_eye_point.setter
    def set_eye_point(self, value):
        """Sets the eye position for perspective viewing."""
        self._instance.SetEyePoint = value

    @property
    def show_magnifying_glass(self):
        """Shows the Magnifying Glass tool at the specified coordinates."""
        return self._instance.ShowMagnifyingGlass

    @show_magnifying_glass.setter
    def show_magnifying_glass(self, value):
        """Shows the Magnifying Glass tool at the specified coordinates."""
        self._instance.ShowMagnifyingGlass = value

    @property
    def start_dynamics(self):
        """Provides faster rotation of model views."""
        return self._instance.StartDynamics

    @start_dynamics.setter
    def start_dynamics(self, value):
        """Provides faster rotation of model views."""
        self._instance.StartDynamics = value

    @property
    def stop_dynamics(self):
        """Ends dynamic model view motion."""
        return self._instance.StopDynamics

    @stop_dynamics.setter
    def stop_dynamics(self, value):
        """Ends dynamic model view motion."""
        self._instance.StopDynamics = value

    @property
    def translate_by(self):
        """Translates the model view in the screen."""
        return self._instance.TranslateBy

    @translate_by.setter
    def translate_by(self, value):
        """Translates the model view in the screen."""
        self._instance.TranslateBy = value

    @property
    def turn_by(self):
        """Rotates the camera by the specified angles about the camera's x and y axes."""
        return self._instance.TurnBy

    @turn_by.setter
    def turn_by(self, value):
        """Rotates the camera by the specified angles about the camera's x and y axes."""
        self._instance.TurnBy = value

    @property
    def zoom_by_factor(self):
        """Modifies the zoom factor for the model view."""
        return self._instance.ZoomByFactor

    @zoom_by_factor.setter
    def zoom_by_factor(self, value):
        """Modifies the zoom factor for the model view."""
        self._instance.ZoomByFactor = value
