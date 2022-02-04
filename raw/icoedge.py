# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html
class ICoEdge:
	def __init__(self, parent=None):
		self._instance = parent

	def evaluate(self, param, number_of_derivatives):
		"""
		Gets the (X,Y,Z) location and the tangency vector on the coedge at the specified position.
		:param param: Curve parameter desired (U value desired for evaluation)
		:param number_of_derivatives: Number of derivatives
		"""
		# return self._instance.Evaluate2(param, number_of_derivatives)
		raise NotImplemented

	def get_curve(self):
		"""Gets the underlying curve of this coedge if the coedge is a result of imprecisely sewing two surfaces together."""
		# return self._instance.GetCurve
		raise NotImplemented

	def get_curve_params(self):
		"""Gets the curve parameters."""
		# return self._instance.GetCurveParams
		raise NotImplemented

	def get_edge(self):
		"""Gets the edge that corresponds to this coedge."""
		# return self._instance.GetEdge
		raise NotImplemented

	def get_loop(self):
		"""Gets the loop containing this coedge."""
		# return self._instance.GetLoop
		raise NotImplemented

	def get_next(self):
		"""Gets the next coedge from the current coedge."""
		# return self._instance.GetNext
		raise NotImplemented

	def get_partner(self):
		"""Gets the partner for this coedge."""
		# return self._instance.GetPartner
		raise NotImplemented

	def get_sense(self):
		"""Gets the sense of the coedge."""
		# return self._instance.GetSense
		raise NotImplemented

	def i_evaluate(self, param, number_of_derivatives):
		"""
		Gets the (x,y, z) location and the tangency vector on the coedge at the specified position.
		:param param: Curve parameter desired (U value desired for evaluation)
		:param number_of_derivatives: Number of derivatives
		"""
		# return self._instance.IEvaluate2(param, number_of_derivatives)
		raise NotImplemented

	def i_get_curve(self):
		"""Gets the underlying curve of this coedge if the coedge is a result of imprecisely sewing two surfaces together."""
		# return self._instance.IGetCurve
		raise NotImplemented

	def i_get_curve_params(self):
		"""Gets the curve parameters."""
		# return self._instance.IGetCurveParams
		raise NotImplemented

	def i_get_edge(self):
		"""Gets the edge that corresponds to this coedge."""
		# return self._instance.IGetEdge
		raise NotImplemented

	def i_get_loop(self):
		"""Gets the loop containing this coedge."""
		# return self._instance.IGetLoop2
		raise NotImplemented

	def i_get_next(self):
		"""Gets the next coedge from the current coedge."""
		# return self._instance.IGetNext
		raise NotImplemented

	def i_get_partner(self):
		"""Gets the partner for this coedge."""
		# return self._instance.IGetPartner
		raise NotImplemented

