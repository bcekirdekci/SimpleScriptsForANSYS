def main():

    AllBodies = ExtAPI.DataModel.Project.Model.GetChildren(DataModelObjectCategory.Body,True)

    usedMaterials = set()

    for body in AllBodies:
        mat = body.Material
        usedMaterials.add(mat)



    model = ExtAPI.DataModel.Project.Model

    allAnalyses = model.Analyses


    for mat in usedMaterials:
        temp = model.AddNamedSelection()
        temp.Name = mat
        tempws = ExtAPI.SelectionManager.CreateSelectionInfo(SelectionTypeEnum.WorksheetSpecific)
        temp.Location = tempws

        tempws = temp.Location
        tempws.AddRow()
        tempws.SetEntityType(0, NamedSelectionWorksheetEntityType.Body)
        tempws.SetCriterion(0, NamedSelectionWorksheetCriterion.MaterialName)
        tempws.SetOperator(0, NamedSelectionWorksheetOperator.Equal)
        tempws.SetStringValue(0, mat)
        tempws.Generate()

        for analyses in allAnalyses:
            AddEqvStress(temp, analyses)


def AddEqvStress(ns,analyses):
    matName = ns.Name
    eqvRes = analyses.Solution.AddEquivalentStress()
    eqvRes.ScopingMethod = GeometryDefineByType.Component
    eqvRes.Location = ns
    eqvRes.Name = "Equivalent Stress_" + matName

main()


