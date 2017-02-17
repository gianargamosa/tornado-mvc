import tornado
import datatables

class ExampleDatatable(AjaxDatatableGradle):

  def sortable_columns():
    sortable_columns = ['Examples.id']

  def searchable_columns():
    searchable_columns = ['Examples.id']

  def data():
    pass

  def get_raw_records():
    pass
  
    