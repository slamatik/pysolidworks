# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html
class ITessellation:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def curve_chord_angle_tolerance(self):
		"""Gets or sets the maximum angle, in radians, that is allowed between a chord and its originating curve."""
		return self._instance.CurveChordAngleTolerance

	@curve_chord_angle_tolerance.setter
	def curve_chord_angle_tolerance(self, value):
		"""Gets or sets the maximum angle, in radians, that is allowed between a chord and its originating curve."""
		self._instance.CurveChordAngleTolerance = value

	@property
	def curve_chord_tolerance(self):
		"""Gets or sets the maximum permitted distance from a chord (facet fin) to the curve (edge entity)."""
		return self._instance.CurveChordTolerance

	@curve_chord_tolerance.setter
	def curve_chord_tolerance(self, value):
		"""Gets or sets the maximum permitted distance from a chord (facet fin) to the curve (edge entity)."""
		self._instance.CurveChordTolerance = value

	@property
	def improved_quality(self):
		"""Gets or sets whether to return higher-quality data."""
		return self._instance.ImprovedQuality

	@improved_quality.setter
	def improved_quality(self, value):
		"""Gets or sets whether to return higher-quality data."""
		self._instance.ImprovedQuality = value

	@property
	def match_type(self):
		"""Gets or sets the type of Parasolid facet match for the tessellation."""
		return self._instance.MatchType

	@match_type.setter
	def match_type(self, value):
		"""Gets or sets the type of Parasolid facet match for the tessellation."""
		self._instance.MatchType = value

	@property
	def max_facet_width(self):
		"""Gets or sets the maximum width of any side of a facet."""
		return self._instance.MaxFacetWidth

	@max_facet_width.setter
	def max_facet_width(self, value):
		"""Gets or sets the maximum width of any side of a facet."""
		self._instance.MaxFacetWidth = value

	@property
	def min_facet_width(self):
		"""Gets or sets the minimum facet width for this tessellation."""
		return self._instance.MinFacetWidth

	@min_facet_width.setter
	def min_facet_width(self, value):
		"""Gets or sets the minimum facet width for this tessellation."""
		self._instance.MinFacetWidth = value

	@property
	def need_edge_fin_map(self):
		"""Gets or sets the need edge fin map option."""
		return self._instance.NeedEdgeFinMap

	@need_edge_fin_map.setter
	def need_edge_fin_map(self, value):
		"""Gets or sets the need edge fin map option."""
		self._instance.NeedEdgeFinMap = value

	@property
	def need_error_list(self):
		"""Gets or sets the need error list option."""
		return self._instance.NeedErrorList

	@need_error_list.setter
	def need_error_list(self, value):
		"""Gets or sets the need error list option."""
		self._instance.NeedErrorList = value

	@property
	def need_face_facet_map(self):
		"""Gets or sets the need face facet map option."""
		return self._instance.NeedFaceFacetMap

	@need_face_facet_map.setter
	def need_face_facet_map(self, value):
		"""Gets or sets the need face facet map option."""
		self._instance.NeedFaceFacetMap = value

	@property
	def need_vertex_normal(self):
		"""Gets or sets the need vertex normal option."""
		return self._instance.NeedVertexNormal

	@need_vertex_normal.setter
	def need_vertex_normal(self, value):
		"""Gets or sets the need vertex normal option."""
		self._instance.NeedVertexNormal = value

	@property
	def need_vertex_params(self):
		"""Gets or sets the need vertex params option."""
		return self._instance.NeedVertexParams

	@need_vertex_params.setter
	def need_vertex_params(self, value):
		"""Gets or sets the need vertex params option."""
		self._instance.NeedVertexParams = value

	@property
	def surface_plane_angle_tolerance(self):
		"""Gets or sets the surface plane angle tolerance."""
		return self._instance.SurfacePlaneAngleTolerance

	@surface_plane_angle_tolerance.setter
	def surface_plane_angle_tolerance(self, value):
		"""Gets or sets the surface plane angle tolerance."""
		self._instance.SurfacePlaneAngleTolerance = value

	@property
	def surface_plane_tolerance(self):
		"""Gets or sets the surface plane tolerance."""
		return self._instance.SurfacePlaneTolerance

	@surface_plane_tolerance.setter
	def surface_plane_tolerance(self, value):
		"""Gets or sets the surface plane tolerance."""
		self._instance.SurfacePlaneTolerance = value

	@property
	def get_edge_fins(self):
		"""Gets all of the fin IDs corresponding to a edge."""
		return self._instance.GetEdgeFins

	@get_edge_fins.setter
	def get_edge_fins(self, value):
		"""Gets all of the fin IDs corresponding to a edge."""
		self._instance.GetEdgeFins = value

	@property
	def get_error_list(self):
		"""Gets the tessellation error list."""
		return self._instance.GetErrorList

	@get_error_list.setter
	def get_error_list(self, value):
		"""Gets the tessellation error list."""
		self._instance.GetErrorList = value

	@property
	def get_face_facets(self):
		"""Gets the facets IDs that correspond to a SOLIDWORKS face."""
		return self._instance.GetFaceFacets

	@get_face_facets.setter
	def get_face_facets(self, value):
		"""Gets the facets IDs that correspond to a SOLIDWORKS face."""
		self._instance.GetFaceFacets = value

	@property
	def get_facet_count(self):
		"""Gets the number of facets used to create this tessellation."""
		return self._instance.GetFacetCount

	@get_facet_count.setter
	def get_facet_count(self, value):
		"""Gets the number of facets used to create this tessellation."""
		self._instance.GetFacetCount = value

	@property
	def get_facet_face(self):
		"""Gets a face that corresponds to a facet."""
		return self._instance.GetFacetFace

	@get_facet_face.setter
	def get_facet_face(self, value):
		"""Gets a face that corresponds to a facet."""
		self._instance.GetFacetFace = value

	@property
	def get_facet_fins(self):
		"""Gets all of the fin IDs of the fins that border this facet."""
		return self._instance.GetFacetFins

	@get_facet_fins.setter
	def get_facet_fins(self, value):
		"""Gets all of the fin IDs of the fins that border this facet."""
		self._instance.GetFacetFins = value

	@property
	def get_fin_co_fin(self):
		"""Gets the ID of the CoFin that is shared by a fin."""
		return self._instance.GetFinCoFin

	@get_fin_co_fin.setter
	def get_fin_co_fin(self, value):
		"""Gets the ID of the CoFin that is shared by a fin."""
		self._instance.GetFinCoFin = value

	@property
	def get_fin_count(self):
		"""Gets the number of fins for this tessellation."""
		return self._instance.GetFinCount

	@get_fin_count.setter
	def get_fin_count(self, value):
		"""Gets the number of fins for this tessellation."""
		self._instance.GetFinCount = value

	@property
	def get_fin_edge(self):
		"""Gets the edge corresponding to a fin."""
		return self._instance.GetFinEdge

	@get_fin_edge.setter
	def get_fin_edge(self, value):
		"""Gets the edge corresponding to a fin."""
		self._instance.GetFinEdge = value

	@property
	def get_fin_vertices(self):
		"""Gets the IDs of the two vertices that correspond to a fin."""
		return self._instance.GetFinVertices

	@get_fin_vertices.setter
	def get_fin_vertices(self, value):
		"""Gets the IDs of the two vertices that correspond to a fin."""
		self._instance.GetFinVertices = value

	@property
	def get_vertex_count(self):
		"""Gets the number of vertices for this tessellation."""
		return self._instance.GetVertexCount

	@get_vertex_count.setter
	def get_vertex_count(self, value):
		"""Gets the number of vertices for this tessellation."""
		self._instance.GetVertexCount = value

	@property
	def get_vertex_normal(self):
		"""Gets the information that describes the normal direction corresponding to vertex."""
		return self._instance.GetVertexNormal

	@get_vertex_normal.setter
	def get_vertex_normal(self, value):
		"""Gets the information that describes the normal direction corresponding to vertex."""
		self._instance.GetVertexNormal = value

	@property
	def get_vertex_params(self):
		"""Gets the parameters corresponding to a tessellation vertex."""
		return self._instance.GetVertexParams

	@get_vertex_params.setter
	def get_vertex_params(self, value):
		"""Gets the parameters corresponding to a tessellation vertex."""
		self._instance.GetVertexParams = value

	@property
	def get_vertex_point(self):
		"""Gets the X, Y and Z values that describe a tessellation vertex."""
		return self._instance.GetVertexPoint

	@get_vertex_point.setter
	def get_vertex_point(self, value):
		"""Gets the X, Y and Z values that describe a tessellation vertex."""
		self._instance.GetVertexPoint = value

	@property
	def i_get_edge_fins(self):
		"""Gets all of the fin IDs corresponding to a edge."""
		return self._instance.IGetEdgeFins

	@i_get_edge_fins.setter
	def i_get_edge_fins(self, value):
		"""Gets all of the fin IDs corresponding to a edge."""
		self._instance.IGetEdgeFins = value

	@property
	def i_get_edge_fins_count(self):
		"""Gets the number of fins corresponding to an edge."""
		return self._instance.IGetEdgeFinsCount

	@i_get_edge_fins_count.setter
	def i_get_edge_fins_count(self, value):
		"""Gets the number of fins corresponding to an edge."""
		self._instance.IGetEdgeFinsCount = value

	@property
	def i_get_error_list(self):
		"""Gets the tessellation error list."""
		return self._instance.IGetErrorList2

	@i_get_error_list.setter
	def i_get_error_list(self, value):
		"""Gets the tessellation error list."""
		self._instance.IGetErrorList2 = value

	@property
	def i_get_error_list_count(self):
		"""Gets number of tessellation errors by error type."""
		return self._instance.IGetErrorListCount

	@i_get_error_list_count.setter
	def i_get_error_list_count(self, value):
		"""Gets number of tessellation errors by error type."""
		self._instance.IGetErrorListCount = value

	@property
	def i_get_face_facets(self):
		"""Gets the facets IDs that correspond to a face."""
		return self._instance.IGetFaceFacets2

	@i_get_face_facets.setter
	def i_get_face_facets(self, value):
		"""Gets the facets IDs that correspond to a face."""
		self._instance.IGetFaceFacets2 = value

	@property
	def i_get_face_facets_count(self):
		"""Gets the number of facets corresponding to a face."""
		return self._instance.IGetFaceFacetsCount2

	@i_get_face_facets_count.setter
	def i_get_face_facets_count(self, value):
		"""Gets the number of facets corresponding to a face."""
		self._instance.IGetFaceFacetsCount2 = value

	@property
	def i_get_facet_face(self):
		"""Gets a face that corresponds to a facet."""
		return self._instance.IGetFacetFace2

	@i_get_facet_face.setter
	def i_get_facet_face(self, value):
		"""Gets a face that corresponds to a facet."""
		self._instance.IGetFacetFace2 = value

	@property
	def i_get_facet_fins(self):
		"""Gets all of the fin IDs of the fins that border this facet."""
		return self._instance.IGetFacetFins

	@i_get_facet_fins.setter
	def i_get_facet_fins(self, value):
		"""Gets all of the fin IDs of the fins that border this facet."""
		self._instance.IGetFacetFins = value

	@property
	def i_get_facet_fins_count(self):
		"""Gets the number of fins corresponding to a facet."""
		return self._instance.IGetFacetFinsCount

	@i_get_facet_fins_count.setter
	def i_get_facet_fins_count(self, value):
		"""Gets the number of fins corresponding to a facet."""
		self._instance.IGetFacetFinsCount = value

	@property
	def i_get_fin_edge(self):
		"""Gets the edge corresponding to a fin."""
		return self._instance.IGetFinEdge

	@i_get_fin_edge.setter
	def i_get_fin_edge(self, value):
		"""Gets the edge corresponding to a fin."""
		self._instance.IGetFinEdge = value

	@property
	def i_get_fin_vertices(self):
		"""Gets the IDs of the two vertices that correspond to a fin."""
		return self._instance.IGetFinVertices

	@i_get_fin_vertices.setter
	def i_get_fin_vertices(self, value):
		"""Gets the IDs of the two vertices that correspond to a fin."""
		self._instance.IGetFinVertices = value

	@property
	def i_get_vertex_normal(self):
		"""Gets the information that describes the normal direction corresponding to vertex."""
		return self._instance.IGetVertexNormal

	@i_get_vertex_normal.setter
	def i_get_vertex_normal(self, value):
		"""Gets the information that describes the normal direction corresponding to vertex."""
		self._instance.IGetVertexNormal = value

	@property
	def i_get_vertex_params(self):
		"""Gets the parameters corresponding to a tessellation vertex."""
		return self._instance.IGetVertexParams

	@i_get_vertex_params.setter
	def i_get_vertex_params(self, value):
		"""Gets the parameters corresponding to a tessellation vertex."""
		self._instance.IGetVertexParams = value

	@property
	def i_get_vertex_point(self):
		"""Gets the X, Y and Z values that describe a tessellation vertex."""
		return self._instance.IGetVertexPoint

	@i_get_vertex_point.setter
	def i_get_vertex_point(self, value):
		"""Gets the X, Y and Z values that describe a tessellation vertex."""
		self._instance.IGetVertexPoint = value

	@property
	def tessellate(self):
		"""Performs the tessellation."""
		return self._instance.Tessellate

	@tessellate.setter
	def tessellate(self, value):
		"""Performs the tessellation."""
		self._instance.Tessellate = value

