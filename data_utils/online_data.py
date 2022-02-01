import requests
from bs4 import BeautifulSoup

names_descriptions = """ Method	ActivateSheet	Activates the specified drawing sheet.  
 Method	ActivateView	Activates the specified drawing view.  
 Method	AddCenterMark	Obsolete. Superseded by IDrawingDoc::InsertCenterMark2.  
 Method	AddChamferDim	Adds a chamfer dimension.  
 Method	AddHoleCallout	Obsolete. Superseded by IDrawingDoc::AddHoleCallout2.  
 Method	AddHoleCallout2	Adds a hole callout at the specified position to the hole whose edge is selected.  
 Method	AddLineStyle	Adds a line style to the current drawing.  
 Method	AddOrdinateDimension	Obsolete. Superseded by IModelDocExtension::AddOrdinateDimension.  
 Method	AddOrdinateDimension2	Obsolete. Superseded by IModelDocExtension::AddOrdinateDimension.  
 Method	AlignHorz	Uses the selected edge to align the current drawing view.  
 Method	AlignOrdinate	Aligns the ordinate dimension.  
 Method	AlignVert	Uses the selected edge to align the current drawing view.  
 Method	AttachAnnotation	Attaches an existing annotation to a drawing sheet or view.  
 Method	AttachDimensions	Attaches unattached dimensions.  
 Method	AutoBalloon	Obsolete. Superseded by IDrawingDoc::AutoBalloon3.  
 Method	AutoBalloon2	Obsolete. Superseded by IDrawingDoc::AutoBalloon3.  
 Method	AutoBalloon3	Obsolete. Superseded by IDrawingDoc::AutoBalloon4.  
 Method	AutoBalloon4	Obsolete. Superseded by IDrawingDoc::AutoBalloon5.  
 Method	AutoBalloon5	Automatically inserts BOM balloons in selected drawing views.  
 Method	AutoDimension	Automatically dimensions the selected drawing view.  
 Method	BreakLineSplineCut	Obsolete. Superseded by IBreakLine::Style.  
 Method	BreakLineStraightCut	Obsolete. Superseded by IBreakLine::Style.  
 Method	BreakLineZigZagCut	Obsolete. Superseded by IBreakLine::Style.  
 Method	BreakView	Breaks the drawing view along the existing break lines.  
 Method	CenterMark	Obsolete. Not superseded.  
 Method	ChangeComponentLayer	Puts the selected components on the specified layer.  
 Method	ChangeOrdDir	Changes the ordinate direction.  
 Method	ChangeRefConfigurationOfFlatPatternView	Changes the referenced configuration of the flat-pattern view.  
 Method	Create1stAngleViews	Obsolete. Superseded by IDrawingDoc::1stAngleViews2.  
 Method	Create1stAngleViews2	Creates standard three orthographic views (first angle projection) for the specified model.  
 Method	Create3rdAngleViews	Obsolete. Superseded by IDrawingDoc::Create3rdAngleViews2.  
 Method	Create3rdAngleViews2	Creates standard three orthographic views (third angle projection) for the specified model.  
 Method	CreateAngDim	Obsolete. Superseded by IDrawingDoc::CreateAngDim4.  
 Method	CreateAngDim2	Obsolete. Superseded by IDrawingDoc::CreateAngDim4.  
 Method	CreateAngDim3	Obsolete. Superseded by IDrawingDoc::CreateAngDim4.  
 Method	CreateAngDim4	Creates a non-associative angular dimension.  
 Method	CreateAutoBalloonOptions	Creates an object that stores auto balloon options.  
 Method	CreateAuxiliaryViewAt	Obsolete. Superseded by IDrawingDoc::CreateAuxiliaryViewAt2.  
 Method	CreateAuxiliaryViewAt2	Creates an auxiliary view based on a selected edge in a drawing view.  
 Method	CreateBlockDefinition	Obsolete. Superseded by ISketchManager::MakeSketchBlockFromFile, ISketchManager::MakeSketchBlockSelected, and ISketchManager::MakeSketchBlockFromSketch.  
 Method	CreateBreakOutSection	Creates a broken-out section in a drawing document.  
 Method	CreateCompoundNote	Obsolete for documents created in SOLIDWORKS 2016 and later. Superseded by ISketchBlockDefinition and ISketchBlockInstance. Creates and returns a compound note.  
 Method	CreateConstructionGeometry	Sets the selected sketch segments to be construction geometry instead of sketch geometry.  
 Method	CreateCustomSymbol	Obsolete. Superseded by ISkethcManager::MakeSketchBlockFromFile, ISketchManager::MakeSketchBlockSelected, and ISketchManager::MakeSketchBlockFromSketch.  
 Method	CreateDetailView	Obsolete. Superseded by IDrawingDoc::CreateDetailViewAt3.  
 Method	CreateDetailViewAt	Obsolete. Superseded by IDrawingDoc::CreateDetailViewAt3.  
 Method	CreateDetailViewAt2	Obsolete. Superseded by IDrawingDoc::CreateDetailViewAt3.  
 Method	CreateDetailViewAt3	Obsolete. Superseded by IDrawingDoc::CreateDetailViewAt4.  
 Method	CreateDetailViewAt4	Creates a detail view in a drawing document.  
 Method	CreateDiamDim	Obsolete. Superseded by IDrawingDoc::CreateDiamDim4.  
 Method	CreateDiamDim2	Obsolete. Superseded by IDrawingDoc::CreateDiamDim4.  
 Method	CreateDiamDim3	Obsolete. Superseded by IDrawingDoc::CreateDiamDim4.  
 Method	CreateDiamDim4	Creates a non-associative diameter dimension.  
 Method	CreateDrawViewFromModelView	Obsolete. Superseded by IDrawingDoc::CreateDrawViewFromModelView3.  
 Method	CreateDrawViewFromModelView2	Obsolete. Superseded by IDrawingDoc::CreateDrawViewFromModelView3.  
 Method	CreateDrawViewFromModelView3	Creates a drawing view on the current drawing sheet using the specified model view.  
 Method	CreateFlatPatternViewFromModelView	Obsolete. Superseded by IDrawingDoc::CreateFlatPatternViewFromModelView2.  
 Method	CreateFlatPatternViewFromModelView2	Obsolete. Superseded by IDrawingDoc::CreateFlatPatternViewFromModelView3.  
 Method	CreateFlatPatternViewFromModelView3	Creates a flat-pattern view from a model view.  
 Method	CreateLayer	Obsolete. Superseded by IDrawingDoc::CreateLayer2.  
 Method	CreateLayer2	Creates a layer for this document.  
 Method	CreateLinearDim	Obsolete. Superseded by IDrawingDoc::CreateLinearDim4.  
 Method	CreateLinearDim2	Obsolete. Superseded by IDrawingDoc::CreateLinearDim4.  
 Method	CreateLinearDim3	Obsolete. Superseded by IDrawingDoc::CreateLinearDim4.  
 Method	CreateLinearDim4	Creates a non-associative linear dimension.  
 Method	CreateOrdinateDim	Obsolete. Superseded by IDrawingDoc::CreateOrdinateDim4.  
 Method	CreateOrdinateDim2	Obsolete. Superseded by IDrawingDoc::CreateOrdinateDim4.  
 Method	CreateOrdinateDim3	Obsolete. Superseded by IDrawingDoc::CreateOrdinateDim4.  
 Method	CreateOrdinateDim4	Creates a non-associative ordinate dimension.  
 Method	CreateRelativeView	Creates a relative drawing view.  
 Method	CreateSectionView	Creates a section view in the drawing using the selected section line.  
 Method	CreateSectionViewAt	Obsolete. Superseded by IDrawingDoc::CreateSectionViewAt4.  
 Method	CreateSectionViewAt2	Obsolete. Superseded by IDrawingDoc::CreateSectionViewAt4.  
 Method	CreateSectionViewAt3	Obsolete. Superseded by IDrawingDoc::CreateSectionViewAt4.  
 Method	CreateSectionViewAt4	Obsolete. Superseded by IDrawingDoc::CreateSectionViewAt5.  
 Method	CreateSectionViewAt5	Creates the specified section view.  
 Method	CreateText	Obsolete. Superseded by IDrawingDoc::CreateText2.  
 Method	CreateText2	Creates a note containing the specified text at a given location.  
 Method	CreateUnfoldedViewAt	Obsolete. Superseded by IDrawingDoc::CreateUnfoldedViewAt3.  
 Method	CreateUnfoldedViewAt2	Obsolete. Superseded by IDrawingDoc::CreateUnfoldedViewAt3.  
 Method	CreateUnfoldedViewAt3	Creates an unfolded drawing view from the selected drawing view and places it in the drawing at the specified location.  
 Method	CreateViewport	Obsolete. Superseded by IDrawingDoc::CreateViewport3.  
 Method	CreateViewport2	Obsolete. Superseded by IDrawingDoc::CreateViewport3.  
 Method	CreateViewport3	Creates a an empty view in a drawing.  
 Method	DeleteAllCosmeticThreads	Deletes all cosmetic threads, which do not have callouts, in a drawing of an assembly only.  
 Method	DeleteLineStyle	Deletes the specified line style from the current drawing.  
 Method	Dimensions	Adds dimensions to the drawing from model.  
 Method	DragModelDimension	Copies or moves dimensions to a different drawing view.  
 Method	DrawingViewRotate	Rotates the selected drawing view.  
 Method	DropDrawingViewFromPalette	Obsolete. Superseded by IDrawingDoc::DropDrawingViewFromPalette2.  
 Method	DropDrawingViewFromPalette2	Moves the specified drawing view from the View Palette to the current drawing sheet.  
 Method	EditCenterMarkProperties	Edits center mark properties.  
 Method	EditOrdinate	Edits an ordinate dimension.  
 Method	EditRebuild	Obsolete. Superseded by IModelDoc2::EditRebuild3.  
 Method	EditSelectedGtol	Gets the selected GTol to edit.  
 Method	EditSheet	Puts the current drawing sheet in edit mode.  
 Method	EditSketch	Allows editing of a sketch in the selected drawing view or sheet.  
 Method	EditTemplate	Puts the template of the current drawing sheet in edit mode.  
 Method	EndDrawing	Provides faster creation of entities in a drawing when used with IDrawingDoc::StartDrawing.  
 Method	ExplodeBlockInstance	Obsolete. Superseded by ISketchManager::ExplodeSketchBlockInstance.  
 Method	ExplodeCustomSymbol	Obsolete. Superseded by ISketchManager::ExplodeSketchBlockInstance.  
 Method	FeatureByName	Gets the specified feature in the drawing.  
 Method	FlipSectionLine	Flips the cut direction of the selected section line.  
 Method	ForceRebuild	Obsolete. Superseded by IModel2::ForceRebuild3.  
 Method	GenerateViewPaletteViews	Adds the specified document's predefined drawing views to the View Palette.  
 Method	GetBlockDefinition	Obsolete. Superseded by SketchManager::GetSketchBlockDefinitions.  
 Method	GetBlockDefinitionCount	Obsolete. Superseded by ISketchManager::GetSketchBlockDefinitionCount.  
 Method	GetBlockDefinitions	Obsolete. Superseded by ISketchManager::GetSketchBlockDefinitions.  
 Method	GetCurrentSheet	Gets the currently active drawing sheet.  
 Method	GetDrawingPaletteViewNames	Gets the names of drawing views in the View Palette for the active drawing sheet.  
 Method	GetEditBlock	Obsolete. Superseded by ISketchManager::EditSketchBlock and ISketchManager::EndEditSketchBlock.  
 Method	GetEditSheet	Gets whether the current drawing is in edit sheet mode or edit template mode.  
 Method	GetFirstView	Gets the first drawing view on the current sheet.  
 Method	GetInsertionPoint	Gets the current insertion (pick) point in a drawing.  
 Method	GetLineFontCount	Obsolete. Superseded by IDrawingDoc::GetLineFontCount2.  
 Method	GetLineFontCount2	Gets the a number line fonts supported by this drawing.  
 Method	GetLineFontId	Gets the associated line font ID.  
 Method	GetLineFontInfo	Obsolete. Superseded by IDrawingDoc::GetLineFontInfo2.  
 Method	GetLineFontInfo2	Gets the detailed information about the specified line font.  
 Method	GetLineFontName	Obsolete. Superseded by IDrawingDoc::GetLineFontName2.  
 Method	GetLineFontName2	Gets the name of the specified line font.  
 Method	GetLineStyles	Gets all of the line styles used in the current document.  
 Method	GetPenCount	Gets the number of pens currently defined in SOLIDWORKS.  
 Method	GetPenInfo	Gets information about the pens used in SOLIDWORKS.  
 Method	GetSheetCount	Gets the number of drawing sheets in this drawing.  
 Method	GetSheetNames	Gets a list of the names of the drawing sheets in this drawing.  
 Method	GetViewCount	Gets all of the number of all of views, including the number of sheets, in this drawing document.  
 Method	GetViews	Gets the all of the views, including the sheets, in this drawing document.  
 Method	HideEdge	Hides selected visible edges in a drawing document.  
 Method	HideShowDimensions	Sets whether to display suppressed dimensions as dimmed and hide them.  
 Method	HideShowDrawingViews	Sets whether to hide or show hidden drawing views.  
 Method	IAddChamferDim	Adds a chamfer dimension.  
 Method	IAddHoleCallout2	Adds a hole callout at the specified position to the hole whose edge is selected.  
 Method	ICreateAngDim	Obsolete. Superseded by IDrawingDoc::ICreateAngDim4.  
 Method	ICreateAngDim2	Obsolete. Superseded by IDrawingDoc::ICreateAngDim4.  
 Method	ICreateAngDim3	Obsolete. Superseded by IDrawingDoc::ICreateAngDim4.  
 Method	ICreateAngDim4	Creates a non-associative angular dimension.  
 Method	ICreateAuxiliaryViewAt2	Creates an auxiliary view based on a selected edge in a drawing view.  
 Method	ICreateBlockDefinition	Obsolete. Superseded by ISketchManager::MakeSketchBlockFromFile, ISketchManager::MakeSketchBlockSelected, and ISketchManager::MakeSketchBlockFromSketch.  
 Method	ICreateCompoundNote	Obsolete for documents created in SOLIDWORKS 2016 and later. Creates and returns a compound note.  
 Method	ICreateCustomSymbol	Obsolete. Superseded by ISkethcManager::MakeSketchBlockFromFile, ISketchManager::MakeSketchBlockSelected, and ISketchManager::MakeSketchBlockFromSketch.  
 Method	ICreateDetailViewAt3	Obsolete. Superseded by IDrawingDoc::CreateDetailViewAt4.  
 Method	ICreateDiamDim	Obsolete. Superseded by IDrawingDoc::ICreateDiamDim4.  
 Method	ICreateDiamDim2	Obsolete. Superseded by IDrawingDoc::ICreateDiamDim4.  
 Method	ICreateDiamDim3	Obsolete. Superseded by IDrawingDoc::ICreateDiamDim4.  
 Method	ICreateDiamDim4	Creates a non-associative diameter dimension.  
 Method	ICreateLinearDim	Obsolete. Superseded by IDrawingDoc::ICreateLinearDim4.  
 Method	ICreateLinearDim2	Obsolete. Superseded by IDrawingDoc::ICreateLinearDim4.  
 Method	ICreateLinearDim3	Obsolete. Superseded by IDrawingDoc::ICreateLinearDim4.  
 Method	ICreateLinearDim4	Creates a non-associative linear dimension.  
 Method	ICreateOrdinateDim	Obsolete. Superseded by IDrawingDoc::ICreateOrdinateDim4.  
 Method	ICreateOrdinateDim2	Obsolete. Superseded by IDrawingDoc::ICreateOrdinateDim4.  
 Method	ICreateOrdinateDim3	Obsolete. Superseded by IDrawingDoc::ICreateOrdinateDim4.  
 Method	ICreateOrdinateDim4	Creates a non-associative ordinate dimension.  
 Method	ICreateSectionViewAt2	Obsolete. Superseded by IDrawingDoc::ICreateSectionViewAt4.  
 Method	ICreateSectionViewAt3	Obsolete. Superseded by IDrawingDoc::ICreateSectionViewAt4.  
 Method	ICreateSectionViewAt4	Obsolete. Superseded by IDrawingDoc::ICreateSectionViewAt5.  
 Method	ICreateSectionViewAt5	Creates a section view from the section line up to the specified distance at the specified distance.  
 Method	ICreateText2	Creates a note containing the specified text at a given location.  
 Method	IEditSelectedGtol	Gets the selected GTol to edit.  
 Method	IFeatureByName	Gets the specified feature in the drawing.  
 Method	IGetBlockDefinitions	Obsolete. Superseded by SketchManager::GetSketchBlockDefinitions.  
 Method	IGetCurrentSheet	Gets the currently active drawing sheet.  
 Method	IGetFirstView	Gets the first drawing view on the current sheet.  
 Method	IGetInsertionPoint	Gets the current insertion (pick) point in a drawing.  
 Method	IGetPenInfo	Gets information about the pens used in SOLIDWORKS.  
 Method	IGetSheetNames	Gets a list of the names of the drawing sheets in this drawing.  
 Method	IInsertCustomSymbol2	Obsolete. Superseded by ISketchManager::InsertSketchBlockInstance.  
 Method	IInsertDowelSymbol	Inserts a dowel pin symbol on the currently selected edge or edges.  
 Method	IInsertMultiJogLeader2	Obsolete. Superseded by IDrawingDoc::InsertMultiJogLeader3.  
 Method	IInsertMultiJogLeader3	Inserts a multi-jog leader.  
 Method	IInsertRevisionCloud	Inserts a revision cloud annotation with the specified shape into a view or sheet.  
 Method	IMakeCustomSymbol2	Obsolete. Superseded by ISkethcManager::MakeSketchBlockFromFile, ISketchManager::MakeSketchBlockSelected, and ISketchManager::MakeSketchBlockFromSketch.  
 Method	INewGtol	Creates a new GTol.  
 Method	InsertAngularRunningDim	Inserts an angular running dimension into this drawing.  
 Method	InsertBaseDim	Inserts the base model dimensions into this drawing.  
 Method	InsertBlock	Obsolete. Superseded by ISketchManager::InsertSketchBlockInstance.  
 Method	InsertBreakHorizontal	Inserts a horizontal break in the drawing view.  
 Method	InsertBreakVertical	Inserts a vertical break in this drawing.  
 Method	InsertCenterLine	Obsolete. Superseded by IDrawingDoc::InsertCenterLine2.  
 Method	InsertCenterLine2	Inserts a centerline on the selected entities.  
 Method	InsertCenterMark	Obsolete. Superseded by IDrawingDoc::InsertCenterMark2.  
 Method	InsertCenterMark2	Obsolete. Superseded by IDrawingDoc::InsertCenterMark3.  
 Method	InsertCenterMark3	Inserts a center mark in a drawing document.  
 Method	InsertChainDim	Obsolete. Superseded by IModelDocExtension::InsertChainDimensions.  
 Method	InsertCircularNotePattern	Inserts a circular note pattern using the selected note.  
 Method	InsertCustomSymbol	Obsolete. Superseded by ISketchManager::InsertSketchBlockInstance.  
 Method	InsertCustomSymbol2	Obsolete. Superseded by ISketchManager::InsertSketchBlockInstance.  
 Method	InsertDatumTag	Obsolete. Superseded by IModelDoc2::InsertDatumTag2.  
 Method	InsertDowelSymbol	Inserts a dowel pin symbol on the currently selected edge or edges in this drawing.  
 Method	InsertGroup	Inserts the currently selected items into a group (or view).  
 Method	InsertHorizontalOrdinate	Inserts a horizontal ordinate dimension into this drawing.  
 Method	InsertLinearNotePattern	Inserts a linear note pattern using the selected note.  
 Method	InsertModelAnnotations	Obsolete. Superseded by IDrawingDoc::InsertModelAnnotations3.  
 Method	InsertModelAnnotations2	Obsolete. Superseded by IDrawingDoc::InsertModelAnnotations3.  
 Method	InsertModelAnnotations3	Inserts model annotations into this drawing document in the currently selected drawing view.  
 Method	InsertModelDimensions	Inserts model dimensions into the selected drawing view according to the option specified.  
 Method	InsertModelInPredefinedView	Inserts the model into the predefined drawing views in the active drawing sheet.  
 Method	InsertMultiJogLeader	Obsolete. Superseded by IDrawingDoc::InsertMultiJogLeader3.  
 Method	InsertMultiJogLeader2	Obsolete. Superseded by IDrawingDoc::InsertMultiJogLeader3.  
 Method	InsertMultiJogLeader3	Inserts a multi-jog leader.  
 Method	InsertNewNote	Obsolete. Superseded by IDrawingDoc::InsertNewNote2.  
 Method	InsertNewNote2	Creates a new note in this drawing.  
 Method	InsertOrdinate	Inserts an ordinate dimension into this drawing.  
 Method	InsertRefDim	Inserts reference dimensions in this drawing.  
 Method	InsertRevisionCloud	Inserts a revision cloud annotation with the specified shape into a view or sheet.  
 Method	InsertRevisionSymbol	Inserts a revision symbol note in this drawing.  
 Method	InsertSurfaceFinishSymbol	Obsolete. Superseded by IModelDocExtension::InsertSurfaceFinishSymbol3.  
 Method	InsertTableAnnotation	Obsolete. Superseded by IDrawingDoc::InsertTableAnnotation2.  
 Method	InsertTableAnnotation2	Inserts a table annotation in this drawing.  
 Method	InsertThreadCallout	Inserts a thread callout into this drawing.  
 Method	InsertVerticalOrdinate	Inserts a vertical ordinate dimension in this drawing.  
 Method	InsertWeldSymbol	Creates a weld symbol located at the last edge selection.  
 Method	IReorderSheets	Reorders the drawing sheets per their positions in the input array.  
 Method	IsDetailingMode	Gets whether this drawing is in detailing mode.  
 Method	IsolateChangedDimensions	Isolates changed dimensions.  
 Method	LoadLineStyles	Loads the specified line styles into the current drawing.  
 Method	MakeBlockDefinition	Obsolete. Superseded by ISkethcManager::MakeSketchBlockFromFile, ISketchManager::MakeSketchBlockSelected, and ISketchManager::MakeSketchBlockFromSketch.  
 Method	MakeCustomSymbol	Obsolete. Superseded by ISkethcManager::MakeSketchBlockFromFile, ISketchManager::MakeSketchBlockSelected, and ISketchManager::MakeSketchBlockFromSketch.  
 Method	MakeCustomSymbol2	Obsolete. Superseded by ISkethcManager::MakeSketchBlockFromFile, ISketchManager::MakeSketchBlockSelected, and ISketchManager::MakeSketchBlockFromSketch.  
 Method	MakeSectionLine	Makes a section line from a set of connected sketch lines.  
 Method	ModifySurfaceFinishSymbol	Modifies the selected surface finish symbol.  
 Method	NewGtol	Creates a new GTol object and returns the pointer to that object.  
 Method	NewNote	Creates a new note at the selected location.  
 Method	NewSheet	Obsolete. Superseded by IDrawingDoc::NewSheet3.  
 Method	NewSheet2	Obsolete. Superseded by IDrawingDoc::NewSheet3.  
 Method	NewSheet3	Obsolete. Superseded by IDrawingDoc::NewSheet4.  
 Method	NewSheet4	Creates a new drawing sheet in this drawing document.  
 Method	OnComponentProperties	Displays the Component Properties dialog for the selected view.  
 Method	PasteSheet	Copies and pastes a drawing sheet to the specified location of the drawing document, optionally renaming whenever duplicate names occur.  
 Method	ReorderSheets	Reorders the drawing sheets per their positions in the input array.  
 Method	ReplaceViewModel	Replaces the specified instances of a model in the specified drawing views.  
 Method	ResolveOutOfDateLightWeightComponents	Resolves out-of-date lightweight components in the selected drawing view or drawing sheet.  
 Method	RestoreRotation	Restores rotation for the selected drawing view.  
 Method	SaveBlock	Obsolete. Superseded by ISketchBlockDefinition::Save.  
 Method	SaveLineStyles	Exports to a file the specified line styles in the current drawing.  
 Method	SetCurrentLayer	Sets the current layer used by this document.  
 Method	SetLineColor	Sets the line color for a selected edge or sketch entity.  
 Method	SetLineStyle	Sets the style or font for the line for a selected edge or sketch entity.  
 Method	SetLineWidth	Sets the line thickness for a selected edge or sketch entity to a SOLIDWORKS-supplied weight (width).  
 Method	SetLineWidthCustom	Sets the line thickness to the specified custom width for a selected edge or sketch entity.  
 Method	SetSheetsSelected	Sets the specified drawing sheets whose setups to modify.  
 Method	SetupSheet	Obsolete. Superseded by IDrawingDoc::SetupSheet4.  
 Method	SetupSheet2	Obsolete. Superseded by IDrawingDoc::SetupSheet4.  
 Method	SetupSheet3	Obsolete. Superseded by IDrawingDoc::SetupSheet4.  
 Method	SetupSheet4	Obsolete. Superseded by IDrawingDoc::SetupSheet5.  
 Method	SetupSheet5	Obsolete. Superseded by IDrawingDoc::SetupSheet6.  
 Method	SetupSheet6	Sets up the specified drawing sheet.  
 Method	SheetNext	Moves to the next sheet in the drawing.  
 Method	SheetPrevious	Returns to the previous sheet in a drawing.  
 Method	ShowEdge	Shows the selected hidden edges in a drawing document.  
 Method	SketchDim	Inserts a sketch dimension in this drawing.  
 Method	StartDrawing	Provides faster creation of entities within a drawing.  
 Method	SuppressView	Hides the selected drawing view.  
 Method	ToggleGrid	Obsolete. Superseded by IModelDocExtension::GetUserPreferenceToggle and IModelDocExtension::SetUserPreferenceToggle and swUserPreferenceToggle_e.swGridDisplay.  
 Method	TranslateDrawing	Translates the entire drawing.  
 Method	UnBreakView	Removes a break in the selected drawing view.  
 Method	UnsuppressView	Hides the selected drawing view.  
 Method	ViewDisplayHidden	Sets the current display mode to Hidden Lines Removed.  
 Method	ViewDisplayHiddengreyed	Sets the current display mode to Hidden Lines Visible.  
 Method	ViewDisplayShaded	Sets the current display mode to Shaded.  
 Method	ViewDisplayWireframe	Sets the current display mode to Wireframe.  
 Method	ViewFullPage	Fits the drawing to the full page.  
 Method	ViewHlrQuality	Toggles the Hidden Lines Removed mode for the drawing view.  
 Method	ViewModelEdges	Toggles the mode for viewing model edges when in shaded mode.  
 Method	ViewTangentEdges	Toggles display of tangent edges in the selected drawing view.  """.strip()

# initial_link = 'http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html'
initial_link = 'http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html'
link = 'http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~'


# # link = 'http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.html'

# https://saralgyaan.com/posts/f-string-in-python-usage-guide/
# https://www.google.com/search?q=python+string+comprehension&oq=python+string+com&aqs=chrome.2.0i512l3j69i57j0i512j69i60l3.4677j0j7&sourceid=chrome&ie=UTF-8


def convert_name(name, method=True):
    new_name = f'{name[0].lower()}'
    for letter in name[1:]:
        if letter.isupper():
            new_name += '_'
        if letter.isnumeric():
            if method:
                continue
            # else:
                # new_name += letter
        new_name += letter.lower()
    return new_name


with open('idrawingdoc.txt', 'w') as file:
    for idx, line in enumerate(names_descriptions.split('\n')):
        line = line.split('\t')
        method_name = line[1]
        method_description = line[2].strip()
        new_method_name = convert_name(method_name, True)
        if method_description.startswith('Obsolete'): continue
        r = requests.get(link + method_name + '.html')
        soup = BeautifulSoup(r.text, "html.parser")
        data = soup.find('dl')
        attributes = True
        try:
            dt = data.find_all('dt')
            dd = data.find_all('dd')
            dt_str = [i.text for i in dt]
            dt_str = [convert_name(i, False) for i in dt_str]
            dd_str = [i.text for i in dd]
            combined_str = zip(dt_str, dd_str)
            doc_string = ''
            for i in combined_str:
                doc_string += '\t:param ' + ': '.join(i) + '\n'
        except AttributeError:
            attributes = False
            dt_str = ''

        result = ''
        if attributes:
            result += f'def {new_method_name}(self, {", ".join(dt_str)}):\n' \
                      f'\t"""\n' \
                      f'\t{method_description}\n' \
                      f'{doc_string}' \
                      f'\t"""\n' \
                      f'\t# return self._instance.{method_name}({", ".join(dt_str)})\n'
        else:
            result += f'def {new_method_name}(self):\n' \
                      f'\t"""{method_description}"""\n' \
                      f'\t# return self._instance.{method_name}\n'
        result += f'\traise NotImplemented\n'
        file.write(result)
        print(f'Completed {idx + 1}')
file.close()



# Case 1: No input.
# Case 2: multiple input lines.
# Case 3: 1 input line.
