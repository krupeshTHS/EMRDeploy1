from django.contrib import admin

# Register your models here.

from . models import Record
from .models import ChildForm
from .models import BriefNote
from .models import PsychiatricEvaluationAdult

from import_export.admin import ImportExportModelAdmin

admin.site.register(Record, ImportExportModelAdmin)
admin.site.register(ChildForm, ImportExportModelAdmin)
admin.site.register(BriefNote, ImportExportModelAdmin)
admin.site.register(PsychiatricEvaluationAdult, ImportExportModelAdmin)



