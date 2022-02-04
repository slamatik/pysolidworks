# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.html
class ITreeControlItem:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def expanded(self):
		"""Gets or sets whether to expand this item in the FeatureManager design tree."""
		return self._instance.Expanded

	@expanded.setter
	def expanded(self, value):
		"""Gets or sets whether to expand this item in the FeatureManager design tree."""
		self._instance.Expanded = value

	@property
	def is_root(self):
		"""Gets whether this item is the root item of the FeatureManager design tree."""
		return self._instance.IsRoot

	@is_root.setter
	def is_root(self, value):
		"""Gets whether this item is the root item of the FeatureManager design tree."""
		self._instance.IsRoot = value

	@property
	def object(self):
		"""Gets the SOLIDWORKS object associated with this item in the FeatureManager design tree."""
		return self._instance.Object

	@object.setter
	def object(self, value):
		"""Gets the SOLIDWORKS object associated with this item in the FeatureManager design tree."""
		self._instance.Object = value

	@property
	def object_type(self):
		"""Gets the type of SOLIDWORKS object for this item in the FeatureManager design tree."""
		return self._instance.ObjectType

	@object_type.setter
	def object_type(self, value):
		"""Gets the type of SOLIDWORKS object for this item in the FeatureManager design tree."""
		self._instance.ObjectType = value

	@property
	def text(self):
		"""Gets the text for this item in the FeatureManager design tree."""
		return self._instance.Text

	@text.setter
	def text(self, value):
		"""Gets the text for this item in the FeatureManager design tree."""
		self._instance.Text = value

	@property
	def get_first_child(self):
		"""Gets the first child of this item in the FeatureManager design tree."""
		return self._instance.GetFirstChild

	@get_first_child.setter
	def get_first_child(self, value):
		"""Gets the first child of this item in the FeatureManager design tree."""
		self._instance.GetFirstChild = value

	@property
	def get_next(self):
		"""Gets the next sibling of this item in the FeatureManager design tree."""
		return self._instance.GetNext

	@get_next.setter
	def get_next(self, value):
		"""Gets the next sibling of this item in the FeatureManager design tree."""
		self._instance.GetNext = value

	@property
	def get_parent(self):
		"""Gets the parent of this item in the FeatureManager design tree."""
		return self._instance.GetParent

	@get_parent.setter
	def get_parent(self, value):
		"""Gets the parent of this item in the FeatureManager design tree."""
		self._instance.GetParent = value

	@property
	def get_previous(self):
		"""Gets the previous sibling of this item in the FeatureManager design tree."""
		return self._instance.GetPrevious

	@get_previous.setter
	def get_previous(self, value):
		"""Gets the previous sibling of this item in the FeatureManager design tree."""
		self._instance.GetPrevious = value

	@property
	def get_root(self):
		"""Gets the root item of the FeatureManager design tree."""
		return self._instance.GetRoot

	@get_root.setter
	def get_root(self, value):
		"""Gets the root item of the FeatureManager design tree."""
		self._instance.GetRoot = value

