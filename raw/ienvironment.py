# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.html
class IEnvironment:
	def __init__(self, parent=None):
		self._instance = parent

	def get_is_bound(self, sym_id, retval):
		"""
		Gets whether the specified geometric tolerance symbol is bound.
		:param sym_id: Name of the geometric tolerance symbol formatted as:
<LibraryName-SymbolName>
where LibraryName and SymbolName are in the SOLIDWORKS text file C:\ProgramData\SolidWorks\SolidWorks 20nn\lang\english\gtol.sym.
NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.
		:param retval: True if the geometric tolerance symbol is bound, false if not
		"""
		# return self._instance.GetIsBound(sym_id, retval)
		raise NotImplemented

	def get_sym_arcs(self, sym_id):
		"""
		Gets an array of information about all arcs in the specified geometric tolerance symbol.
		:param sym_id: Name of the geometric tolerance symbol formatted as:
<LibraryName-SymbolName>
where LibraryName and SymbolName are in the SOLIDWORKS text file C:\ProgramData\SolidWorks\SolidWorks 20nn\lang\english\gtol.sym.
NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.
		"""
		# return self._instance.GetSymArcs2(sym_id)
		raise NotImplemented

	def get_sym_circles(self, sym_id):
		"""
		Gets an array that defines all circles in the geometric tolerance symbol.
		:param sym_id: Name of the geometric tolerance symbol formatted as:
<LibraryName-SymbolName>
where LibraryName and SymbolName are in the SOLIDWORKS text file C:\ProgramData\SolidWorks\SolidWorks 20nn\lang\english\gtol.sym.
NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.
		"""
		# return self._instance.GetSymCircles(sym_id)
		raise NotImplemented

	def get_sym_edge_counts(self, sym_id):
		"""
		Gets an array that contains the number of lines, arcs, circles, text strings, and triangles in the specified geometric tolerance symbol.
		:param sym_id: Name of the geometric tolerance symbol formatted as:
<LibraryName-SymbolName>
where LibraryName and SymbolName are in the SOLIDWORKS text file C:\ProgramData\SolidWorks\SolidWorks 20nn\lang\english\gtol.sym.
NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.
		"""
		# return self._instance.GetSymEdgeCounts(sym_id)
		raise NotImplemented

	def get_sym_lines(self, sym_id):
		"""
		Gets an array that defines all lines in the specified geometric tolerance symbol.
		:param sym_id: Name of the geometric tolerance symbol formatted as:
<LibraryName-SymbolName>
where LibraryName and SymbolName are in the SOLIDWORKS text file C:\ProgramData\SolidWorks\SolidWorks 20nn\lang\english\gtol.sym.
NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.
		"""
		# return self._instance.GetSymLines(sym_id)
		raise NotImplemented

	def get_sym_text(self, sym_id):
		"""
		Gets an array containing the text associated with the specified geometric tolerance symbol.
		:param sym_id: Name of the geometric tolerance symbol formatted as:
<LibraryName-SymbolName>
where LibraryName and SymbolName are in the SOLIDWORKS text file C:\ProgramData\SolidWorks\SolidWorks 20nn\lang\english\gtol.sym.
NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.
		"""
		# return self._instance.GetSymText(sym_id)
		raise NotImplemented

	def get_sym_text_points(self, sym_id):
		"""
		Gets an array that defines all text points in the specified geometric tolerance symbol.
		:param sym_id: Name of the geometric tolerance symbol formatted as:
<LibraryName-SymbolName>
where LibraryName and SymbolName are in the SOLIDWORKS text file C:\ProgramData\SolidWorks\SolidWorks 20nn\lang\english\gtol.sym.
NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.
		"""
		# return self._instance.GetSymTextPoints(sym_id)
		raise NotImplemented

	def get_sym_triangles(self, sym_id):
		"""
		Gets an array that defines all triangles in the specified geometric tolerance symbol.
		:param sym_id: Name of the geometric tolerance symbol formatted as:
<LibraryName-SymbolName>
where LibraryName and SymbolName are in the SOLIDWORKS text file C:\ProgramData\SolidWorks\SolidWorks 20nn\lang\english\gtol.sym.
NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.
		"""
		# return self._instance.GetSymTriangles(sym_id)
		raise NotImplemented

	def i_get_sym_circles(self, sym_id):
		"""
		Gets an array that defines all circles in the specified geometric tolerance symbol.
		:param sym_id: Name of the geometric tolerance symbol formatted as:
<LibraryName-SymbolName>
where LibraryName and SymbolName are in the SOLIDWORKS text file C:\ProgramData\SolidWorks\SolidWorks 20nn\lang\english\gtol.sym.
NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.
		"""
		# return self._instance.IGetSymCircles(sym_id)
		raise NotImplemented

	def i_get_sym_edge_counts(self, sym_id):
		"""
		Gets an array that contains the number of lines, arcs, circles, text strings, and triangles in the specified geometric tolerance symbol.
		:param sym_id: Name of the geometric tolerance symbol formatted as:
<LibraryName-SymbolName>
where LibraryName and SymbolName are in the SOLIDWORKS text file C:\ProgramData\SolidWorks\SolidWorks 20nn\lang\english\gtol.sym.
NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.
		"""
		# return self._instance.IGetSymEdgeCounts(sym_id)
		raise NotImplemented

	def i_get_sym_lines(self, sym_id):
		"""
		Gets an array that defines all lines in the specified geometric tolerance symbol.
		:param sym_id: Name of the geometric tolerance symbol formatted as:
<LibraryName-SymbolName>
where LibraryName and SymbolName are in C:\ProgramData\SolidWorks\SolidWorks 20nn\lang\english\gtol.sym.
NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.
		"""
		# return self._instance.IGetSymLines(sym_id)
		raise NotImplemented

	def i_get_sym_text_points(self, sym_id):
		"""
		Gets an array that defines all text points in the specified geometric tolerance symbol.
		:param sym_id: Name of the geometric tolerance symbol formatted as:
<LibraryName-SymbolName>
where LibraryName and SymbolName are in the SOLIDWORKS text file C:\ProgramData\SolidWorks\SolidWorks 20nn\lang\english\gtol.sym.
NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.
		"""
		# return self._instance.IGetSymTextPoints(sym_id)
		raise NotImplemented

	def i_get_sym_triangles(self, sym_id):
		"""
		Gets an array that defines all triangles in the specified geometric tolerance symbol.
		:param sym_id: Name of the geometric tolerance symbol formatted as:
<LibraryName-SymbolName>
where LibraryName and SymbolName are in the SOLIDWORKS text file C:\ProgramData\SolidWorks\SolidWorks 20nn\lang\english\gtol.sym.
NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.
		"""
		# return self._instance.IGetSymTriangles(sym_id)
		raise NotImplemented

