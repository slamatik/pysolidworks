# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionArrow_members.html
class IProjectionArrow:
	def __init__(self, parent=None):
		self._instance = parent

	def visible(self):
		"""Gets whether the projection arrow is visible."""
		# return self._instance.Visible
		raise NotImplemented

	def get_coordinates(self):
		"""Gets the location of this projection arrow's line and its label."""
		# return self._instance.GetCoordinates
		raise NotImplemented

	def get_label(self):
		"""Gets the label for this view's projection arrow."""
		# return self._instance.GetLabel
		raise NotImplemented

	def get_projected_view(self):
		"""Gets the projected view."""
		# return self._instance.GetProjectedView
		raise NotImplemented

	def get_text_format(self):
		"""Gets the format of the text for this projection arrow."""
		# return self._instance.GetTextFormat
		raise NotImplemented

	def get_use_doc_text_format(self):
		"""Gets whether the document default auxiliary text format is being used."""
		# return self._instance.GetUseDocTextFormat
		raise NotImplemented

	def get_view(self):
		"""Gets the base drawing view for this projection arrow."""
		# return self._instance.GetView
		raise NotImplemented

	def i_get_coordinates(self):
		"""Gets the location of this projection arrow's line and its label."""
		# return self._instance.IGetCoordinates
		raise NotImplemented

	def i_get_projected_view(self):
		"""Gets the projected view."""
		# return self._instance.IGetProjectedView
		raise NotImplemented

	def i_get_text_format(self):
		"""Gets the format of the text for this projection arrow."""
		# return self._instance.IGetTextFormat
		raise NotImplemented

	def i_get_view(self):
		"""Gets the base drawing view for this projection arrow."""
		# return self._instance.IGetView
		raise NotImplemented

	def set_label(self, label):
		"""
		Sets the label for this view's projection arrow.
		:param label: Label for this projection arrow
		"""
		# return self._instance.SetLabel(label)
		raise NotImplemented

