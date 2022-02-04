# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMagneticLine_members.html
class IMagneticLine:
	def __init__(self, parent=None):
		self._instance = parent

	def angle(self):
		"""Gets and sets the angle of this magnetic line with respect to the horizontal axis."""
		# return self._instance.Angle
		raise NotImplemented

	def end_point(self):
		"""Gets and sets the end point of this magnetic line."""
		# return self._instance.EndPoint
		raise NotImplemented

	def equal_spacing(self):
		"""Gets and sets whether to equally space the notes on this magnetic line."""
		# return self._instance.EqualSpacing
		raise NotImplemented

	def length(self):
		"""Gets and sets the length of this magnetic line."""
		# return self._instance.Length
		raise NotImplemented

	def start_point(self):
		"""Gets and sets the start point of this magnetic line."""
		# return self._instance.StartPoint
		raise NotImplemented

	def add_note(self, note, position):
		"""
		Attaches to this magnetic line the specified note at the specified position.
		:param note: INote to attach to this magnetic line
		:param position: 0.0 <= Attachment position on magnetic line <= 1.0; valid only if IMagneticLine::EqualSpacing is false
		"""
		# return self._instance.AddNote(note, position)
		raise NotImplemented

	def get_notes(self):
		"""Gets the notes attached to this magnetic line."""
		# return self._instance.GetNotes
		raise NotImplemented

	def get_notes_count(self):
		"""Gets the number of notes attached to this magnetic line."""
		# return self._instance.GetNotesCount
		raise NotImplemented

	def i_get_notes(self, count):
		"""
		Gets the notes attached to this magnetic line.
		:param count: Number of notes returned by this method (see Remarks)
		"""
		# return self._instance.IGetNotes(count)
		raise NotImplemented

	def remove_note(self, note, location):
		"""
		Detaches the specified note from this magnetic line and moves it to the specified location.
		:param note: INote to detach from this magnetic line
		:param location: IMathPoint where to move the note specified by Note
		"""
		# return self._instance.RemoveNote(note, location)
		raise NotImplemented

