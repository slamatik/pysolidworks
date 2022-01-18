from interfaces.ifeature import IFeature
import interfaces.irevisiontableannotation as rta


# http://help.solidworks.com/2019/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableFeature.html

class IRevisionTableFeature:
    def __init__(self, instance=None):
        self._instance = instance

    def get_feature(self):
        return IFeature(self._instance.GetFeature)

    def get_table_annotation_count(self):
        return self._instance.GetTableAnnotationCount

    def get_table_annotations(self):
        array = self._instance.GetTableAnnotations
        array = [rta.IRevisionTableAnnotation(i) for i in array]
        return array
