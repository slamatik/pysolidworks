# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html
class IDrawingComponent:
	def __init__(self, parent=None):
		self._instance = parent

	def component(self):
		"""Gets the assembly component referenced in this drawing component."""
		# return self._instance.Component
		raise NotImplemented

	@property
	def layer(self):
		"""Gets or sets the name of the layer on which the component resides in the view."""
		return self._instance.Layer

	@layer.setter
	def layer(self, value):
		"""Gets or sets the name of the layer on which the component resides in the view."""
		self._instance.Layer = value

	@property
	def layer_override(self):
		"""Gets or sets whether the drawing component has properties that override the default properties of the layer."""
		return self._instance.LayerOverride

	@layer_override.setter
	def layer_override(self, value):
		"""Gets or sets whether the drawing component has properties that override the default properties of the layer."""
		self._instance.LayerOverride = value

	@property
	def name(self):
		"""Gets the name of the drawing component."""
		return self._instance.Name

	@name.setter
	def name(self, value):
		"""Gets the name of the drawing component."""
		self._instance.Name = value

	@property
	def style(self):
		"""Gets or sets the style for the line for this component in this drawing view."""
		return self._instance.Style

	@style.setter
	def style(self, value):
		"""Gets or sets the style for the line for this component in this drawing view."""
		self._instance.Style = value

	@property
	def use_document_defaults(self):
		"""Gets or sets whether to use the document default settings for the component's line fonts."""
		return self._instance.UseDocumentDefaults

	@use_document_defaults.setter
	def use_document_defaults(self, value):
		"""Gets or sets whether to use the document default settings for the component's line fonts."""
		self._instance.UseDocumentDefaults = value

	@property
	def view(self):
		"""Gets the drawing view on which this component resides."""
		return self._instance.View

	@view.setter
	def view(self, value):
		"""Gets the drawing view on which this component resides."""
		self._instance.View = value

	@property
	def visible(self):
		"""Gets or sets the visibility state for this component for this drawing view."""
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Gets or sets the visibility state for this component for this drawing view."""
		self._instance.Visible = value

	@property
	def width(self):
		"""Gets or sets the width of the line for this component for this drawing view."""
		return self._instance.Width

	@width.setter
	def width(self, value):
		"""Gets or sets the width of the line for this component for this drawing view."""
		self._instance.Width = value

	@property
	def de_select(self):
		"""Deselects this drawing component."""
		return self._instance.DeSelect

	@de_select.setter
	def de_select(self, value):
		"""Deselects this drawing component."""
		self._instance.DeSelect = value

	@property
	def get_children(self):
		"""Gets the child components for this drawing component."""
		return self._instance.GetChildren

	@get_children.setter
	def get_children(self, value):
		"""Gets the child components for this drawing component."""
		self._instance.GetChildren = value

	@property
	def get_children_count(self):
		"""Gets the number of child components for this drawing component."""
		return self._instance.GetChildrenCount

	@get_children_count.setter
	def get_children_count(self, value):
		"""Gets the number of child components for this drawing component."""
		self._instance.GetChildrenCount = value

	@property
	def get_line_style(self):
		"""Gets the line style for the drawing component."""
		return self._instance.GetLineStyle

	@get_line_style.setter
	def get_line_style(self, value):
		"""Gets the line style for the drawing component."""
		self._instance.GetLineStyle = value

	@property
	def get_line_thickness(self):
		"""Gets the line thickness for the drawing component."""
		return self._instance.GetLineThickness

	@get_line_thickness.setter
	def get_line_thickness(self, value):
		"""Gets the line thickness for the drawing component."""
		self._instance.GetLineThickness = value

	@property
	def i_get_children(self):
		"""Gets the child components for this drawing component."""
		return self._instance.IGetChildren

	@i_get_children.setter
	def i_get_children(self, value):
		"""Gets the child components for this drawing component."""
		self._instance.IGetChildren = value

	@property
	def is_root(self):
		"""Gets whether this is the root drawing component."""
		return self._instance.IsRoot

	@is_root.setter
	def is_root(self, value):
		"""Gets whether this is the root drawing component."""
		self._instance.IsRoot = value

	@property
	def select(self):
		"""Selects the specified drawing component."""
		return self._instance.Select

	@select.setter
	def select(self, value):
		"""Selects the specified drawing component."""
		self._instance.Select = value

	@property
	def set_line_style(self):
		"""Sets the line style for the drawing component."""
		return self._instance.SetLineStyle

	@set_line_style.setter
	def set_line_style(self, value):
		"""Sets the line style for the drawing component."""
		self._instance.SetLineStyle = value

	@property
	def set_line_thickness(self):
		"""Sets the line thickness for the drawing component."""
		return self._instance.SetLineThickness

	@set_line_thickness.setter
	def set_line_thickness(self, value):
		"""Sets the line thickness for the drawing component."""
		self._instance.SetLineThickness = value

