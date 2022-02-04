# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConnectionPointFeatureData_members.html
class IConnectionPointFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	def direction(self):
		"""Gets the x, y, z coordinates of the direction vector of this connection point feature."""
		# return self._instance.Direction
		raise NotImplemented

	def electrical_pin_i_d(self):
		"""Gets and sets the electrical pin ID of this connection point feature."""
		# return self._instance.ElectricalPinID
		raise NotImplemented

	def location(self):
		"""Gets the x,y,z coordinates of this connection point feature."""
		# return self._instance.Location
		raise NotImplemented

	def name(self):
		"""Gets and sets the name of this connection point feature."""
		# return self._instance.Name2
		raise NotImplemented

	def port_i_d(self):
		"""Gets and sets the port ID for this connection point feature."""
		# return self._instance.PortID
		raise NotImplemented

	def route_diameter(self):
		"""Gets and sets the route diameter at this connection point."""
		# return self._instance.RouteDiameter
		raise NotImplemented

	def route_sub_type(self):
		"""Gets and sets the route sub-type of this connection point feature."""
		# return self._instance.RouteSubType
		raise NotImplemented

	def route_type(self):
		"""Gets and sets the route type of this connection point feature."""
		# return self._instance.RouteType
		raise NotImplemented

	def stub_length(self):
		"""Gets and sets the stub length that extends from the connector or fitting when inserted into routes."""
		# return self._instance.StubLength
		raise NotImplemented

	def access_selections(self, top_doc, component):
		"""
		Allows access to the selections that describe this connection point feature.
		:param top_doc: Top-level document
		:param component: Component in which the feature is to be modified
		"""
		# return self._instance.AccessSelections(top_doc, component)
		raise NotImplemented

	def i_access_selections(self, top_doc, component):
		"""
		Allows access to the selections that describe this connection point feature.
		:param top_doc: Top-level document
		:param component: Component in which the feature is to be modified
		"""
		# return self._instance.IAccessSelections(top_doc, component)
		raise NotImplemented

	def release_selection_access(self):
		"""Releases access to selections that describe this connection point feature."""
		# return self._instance.ReleaseSelectionAccess
		raise NotImplemented

