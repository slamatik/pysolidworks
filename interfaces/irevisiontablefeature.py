from interfaces.ifeature import IFeature
import interfaces.irevisiontableannotation as rta


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableFeature_members.html
class IRevisionTableFeature:
    def __init__(self, parent=None):
        self._instance = parent

    def get_feature(self):
        """Gets the revision table feature."""
        return IFeature(self._instance)

    def get_table_annotation_count(self):
        """Gets the number of revision table annotations for this revision table."""
        return self._instance.GetTableAnnotationCount

    def get_table_annotations(self):
        """Gets the revision table annotations for this revision table."""
        array = self._instance.GetTableAnnotations
        array = [rta.IRevisionTableAnnotation(i) for i in array]
        return array

    def i_get_table_annotations(self, count):
        """
        Gets the revision table annotations for this revision table.
        :param count: Number of revision table annotations
        """
        # return self._instance.IGetTableAnnotations(count)
        raise NotImplemented
