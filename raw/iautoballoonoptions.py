# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html
class IAutoBalloonOptions:
	def __init__(self, parent=None):
		self._instance = parent

	def custom_size(self):
		"""Gets and sets the user-defined size of the balloons."""
		# return self._instance.CustomSize
		raise NotImplemented

	def edit_balloon_option(self):
		"""Gets and sets edit balloon options."""
		# return self._instance.EditBalloonOption
		raise NotImplemented

	def edit_balloons(self):
		"""Gets and sets whether to use edit balloon options when creating the auto balloon."""
		# return self._instance.EditBalloons
		raise NotImplemented

	def first_item(self):
		"""Gets and sets the first balloon item."""
		# return self._instance.FirstItem
		raise NotImplemented

	def ignore_multiple(self):
		"""Gets and sets whether to create balloons for multiple instances of an item."""
		# return self._instance.IgnoreMultiple
		raise NotImplemented

	def insert_magnetic_line(self):
		"""Gets and sets whether to insert magnetic lines with balloons."""
		# return self._instance.InsertMagneticLine
		raise NotImplemented

	def item_number_increment(self):
		"""Gets and sets the item number increment."""
		# return self._instance.ItemNumberIncrement
		raise NotImplemented

	def item_number_start(self):
		"""Gets and sets the starting item number."""
		# return self._instance.ItemNumberStart
		raise NotImplemented

	def item_order(self):
		"""Gets and sets item ordering."""
		# return self._instance.ItemOrder
		raise NotImplemented

	def layername(self):
		"""Gets and sets the name of the layer on which to create balloons."""
		# return self._instance.Layername
		raise NotImplemented

	def layout(self):
		"""Gets and sets the style of the layout of balloons."""
		# return self._instance.Layout
		raise NotImplemented

	def leader_attachment_to_faces(self):
		"""Gets and sets whether to attach balloons to faces."""
		# return self._instance.LeaderAttachmentToFaces
		raise NotImplemented

	def lower_text(self):
		"""Gets and sets the lower text of the balloons."""
		# return self._instance.LowerText
		raise NotImplemented

	def lower_text_content(self):
		"""Gets and sets the style of the lower text of the balloons."""
		# return self._instance.LowerTextContent
		raise NotImplemented

	def reverse_direction(self):
		"""Gets and sets whether to reverse the item ordering of the balloons."""
		# return self._instance.ReverseDirection
		raise NotImplemented

	def size(self):
		"""Gets and sets the size of the balloons."""
		# return self._instance.Size
		raise NotImplemented

	def style(self):
		"""Gets and sets the style of the balloons."""
		# return self._instance.Style
		raise NotImplemented

	def upper_text(self):
		"""Gets and sets the upper text of the balloons."""
		# return self._instance.UpperText
		raise NotImplemented

	def upper_text_content(self):
		"""Gets and sets the style of the upper text of the balloons."""
		# return self._instance.UpperTextContent
		raise NotImplemented

