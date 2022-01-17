from enum import Enum


class CEnum(Enum):
    def __str__(self):
        return self.name.split("_")[1]


class CEnum2(Enum):
    def __str__(self):
        return self.name


class ApplicationType(Enum):
    EXPERIENCE3D = 1
    DESKTOP = 0


class ComponentSuppressionState(Enum):
    FULLY_LIGHTWEIGHT = 4  # Recursive
    FULLY_RESOLVED = 2  # Recursive
    INTERNAL_ID_MISMATCH = 5
    LIGHTWEIGHT = 1
    RESOLVED = 3
    SUPPRESSED = 0


class CustomPropertyAddOption(Enum):
    DELETE_AND_ADD = 1
    ONLY_IF_NEW = 0
    REPLACE_VALUE = 2


class CustomInfoAddResult(CEnum):
    swCustomInfoAddResult_AddedOrChanged = 0
    swCustomInfoAddResult_GenericFail = 1
    swCustomInfoAddResult_MismatchAgainstExistingType = 2
    swCustomInfoAddResult_MismatchAgainstSpecifiedType = 3


class CustomInfoDeleteResult(Enum):
    LINKED_PROP = 2
    NOT_PRESENT = 1
    OK = 0


class CustomInfoGetResult(CEnum2):
    CACHED_VALUE = 0
    NOT_PRESENT = 1
    RESOLVED_VALUE = 2


class CustomInfoSetResult(Enum):
    LINKED_PROP = 3
    NOT_PRESENT = 1
    OK = 0
    TYPE_MISMATCH = 2


class CustomLinkSetResult(Enum):
    LEGACY = 2
    NOT_PRESENT = 1
    OK = 0
    USER_PROP = 3


class CustomInfoType(CEnum2):
    DATE = 64
    DOUBLE = 5
    NUMBER = 3
    TEXT = 30
    UNKNOWN = 0
    YES_OR_NO = 11

    # def __str__(self):
    #     return self.name
    #
    # def __repr__(self):
    #     return str(self.name)


class DocumentTypes(Enum):
    ASSEMBLY = 2
    DRAWING = 3
    IMPORTED_ASSEMBLY = 7
    IMPORTED_PART = 6
    LAYOUT = 5
    NONE = 0
    PART = 1
    SDM = 4


class FileSaveError(Enum):
    FILE_LOCK_ERROR = 16
    FILE_NAME_CONTAINS_AT_SIGN = 8
    FILE_NAME_EMPTY = 4
    FILE_SAVE_AS_BAD_EDRAWINGS_VERSION = 1024
    FILE_SAVE_AS_DO_NOT_OVERWRITE = 128
    FILE_SAVE_AS_INVALID_FILE_EXTENSION = 256
    FILE_SAVE_AS_NO_SELECTION = 512
    FILE_SAVE_AS_NOT_SUPPORTED = 4096
    FILE_SAVE_FORMAT_NOT_AVAILABLE = 32
    FILE_SAVE_REQUIRES_SAVING_REFERENCES = 8192
    GENERIC_SAVE_ERROR = 1
    READ_ONLY_SAVE_ERROR = 2


class FileLoadError(Enum):
    ADDIN_INTERUPT_ERROR = 1048576
    FILE_NOT_FOUND_ERROR = 2
    FILE_WITH_SAME_TITLE_ALREADY_OPEN = 65536
    FUTURE_VERSION = 8192
    GENERIC_ERROR = 1
    INVALID_FILE_TYPE_ERROR = 1024
    LIQUID_MACHINE_DOC = 131072
    LOW_RESOURCES_ERROR = 262144
    NO_DISPLAY_DATA = 524288


class FileSaveWarning(Enum):
    ANIMATOR_CAMERA_VIEWS = 128
    ANIMATOR_FEATURE_EDITS = 16
    ANIMATOR_LIGHT_EDITS = 64
    ANIMATOR_NEED_TO_SOLVE = 8
    ANIMATOR_SECTION_VIEWS = 256
    EDRWINGS_BAD_SELECTION = 32
    MISSING_OLE_OBJECTS = 512
    NEEDS_REBUILD = 2
    OPENED_VIEW_ONLY = 1024
    REBUILD_ERROR = 1
    VIEWS_NEED_UPDATE = 4


class FileLoadWarning(Enum):
    ALREADY_OPEN = 128
    BASE_PART_NOT_LOADED = 64
    COMPONENT_MISSING_REFERENCED_CONFIG = 32768
    DIMENSIONS_REFERENCED_INCORRECTLY_TO_MODELS = 16384
    DRAWING_ANSI_UPDATE = 8
    DRAWING_SF_SYMBOL_CONVERT = 2048
    DRAWINGS_ONLY_RAPID_DRAFT = 256
    ID_MISMATCH = 1
    INVISIBLE_DOC_LINKED_DESIGN_TABLE_UPDATE_FAIL = 65536
    MISSING_DESIGN_TABLE = 131072
    MODEL_OUT_OF_DATE = 8192
    NEEDS_REGEN = 32
    READ_ONLY = 2
    RESOLVE_DIM_TOLERANCE = 4096
    SHARING_VIOLATION = 4
    SHEET_SCALE_UPDATE = 16
    VIEW_MISSING_REFERENCED_CONFIG = 1024
    VIEW_ONLY_RESTRICTIONS = 512


class OpenDocOptions(Enum):
    LIGHTWEIGHT = 32
    RAPID_DRAFT = 8
    READ_ONLY = 2
    SILENT = 1
    LARGE_DESIGN_REVIEW = 4


class SummInfoField(Enum):
    AUTHOR = 2
    COMMENT = 4
    CREATE_DATE = 6
    CREATE_DATE2 = 8
    KEYWORDS = 3
    SAVE_DATE = 7
    SAVE_DATE2 = 9
    SAVED_BY = 5
    SUBJECT = 1
    TITLE = 0


class StandardViews(Enum):
    BACK = 2
    BOTTOM = 6
    DIMETRIC = 9
    FRONT = 1
    ISOMETRIC = 7
    LEFT = 3
    RIGHT = 4
    TOP = 5
    TRIMETRIC = 8


class SaveAsOptions(Enum):
    AVOID_REBUILD_ON_SAVE = 8
    COPY = 2
    DETACHED_DRAWING = 128
    IGNORE_BIOGRAPHY = 256
    OVERRIDE_SAVE_EMODEL = 32
    SAVE_REFERENCED = 4
    SILENT = 1
    UPDATE_INACTIVE_VIEWS = 16


class TableAnnotation(CEnum):
    TABLEANNOTATION_BendTable = 7
    TABLEANNOTATION_BillOfMaterials = 2
    TABLEANNOTATION_General = 0
    TABLEANNOTATION_GeneralTolerance = 9
    TABLEANNOTATION_HoleChart = 1
    TABLEANNOTATION_PunchTable = 8
    TABLEANNOTATION_RevisionBlock = 3
    TABLEANNOTATION_TitleBlock = 5
    TABLEANNOTATION_WeldmentCutList = 4
    TABLEANNOTATION_WeldTable = 6


class VisibilityState(Enum):
    swVisibilityStateHide = 1
    swVisibilityStateShown = 2
    swVisibilityStateUnknown = 3
