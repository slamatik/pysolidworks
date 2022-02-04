# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.html
class IFaceHatch:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the angle of the face hatch."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the angle of the face hatch."""
		self._instance.Angle = value

	@property
	def color(self):
		"""Gets the color of the face hatch. 
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Color

	@color.setter
	def color(self, value):
		"""Gets the color of the face hatch. 
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Color = value

	@property
	def definition(self):
		"""Gets the definition for the face hatch. 
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Definition

	@definition.setter
	def definition(self, value):
		"""Gets the definition for the face hatch. 
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Definition = value

	@property
	def face(self):
		"""Gets the face that is associated with the hatch. 
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Face

	@face.setter
	def face(self, value):
		"""Gets the face that is associated with the hatch. 
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Face = value

	@property
	def hatch_scope(self):
		"""Gets or sets the scope for this face hatch."""
		return self._instance.HatchScope

	@hatch_scope.setter
	def hatch_scope(self, value):
		"""Gets or sets the scope for this face hatch."""
		self._instance.HatchScope = value

	@property
	def hatch_type(self):
		"""Gets or sets the type of this face hatch."""
		return self._instance.HatchType

	@hatch_type.setter
	def hatch_type(self, value):
		"""Gets or sets the type of this face hatch."""
		self._instance.HatchType = value

	@property
	def layer(self):
		"""Gets the drawing layer of the component to which the hatch is attached. 
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Layer

	@layer.setter
	def layer(self, value):
		"""Gets the drawing layer of the component to which the hatch is attached. 
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Layer = value

	@property
	def pattern(self):
		"""Gets the pattern for the face hatch. 
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Pattern

	@pattern.setter
	def pattern(self, value):
		"""Gets the pattern for the face hatch. 
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Pattern = value

	@property
	def pattern_id(self):
		"""Gets the pattern ID of this face hatch. Read-only."""
		return self._instance.PatternId

	@pattern_id.setter
	def pattern_id(self, value):
		"""Gets the pattern ID of this face hatch. Read-only."""
		self._instance.PatternId = value

	@property
	def scale(self):
		"""Gets or sets the scale for this face hatch."""
		return self._instance.Scale2

	@scale.setter
	def scale(self, value):
		"""Gets or sets the scale for this face hatch."""
		self._instance.Scale2 = value

	@property
	def solid_fill(self):
		"""Gets whether the face hatch is a solid color. 
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.SolidFill

	@solid_fill.setter
	def solid_fill(self, value):
		"""Gets whether the face hatch is a solid color. 
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.SolidFill = value

	@property
	def use_material_hatch(self):
		"""Gets or sets whether this face hatch uses material crosshatch."""
		return self._instance.UseMaterialHatch

	@use_material_hatch.setter
	def use_material_hatch(self, value):
		"""Gets or sets whether this face hatch uses material crosshatch."""
		self._instance.UseMaterialHatch = value

