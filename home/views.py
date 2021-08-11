import pandas as pd
import numpy as np
import openpyxl
from openpyxl import load_workbook
from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to navigate to the index page """

    workbook = load_workbook('excel-files/EnergyConsumptionDetail_updated.xlsx')
    sheet_names = workbook.sheetnames[0:4]

    """ Customer 1 """
    sheet1 = workbook["Customer 1"]
    sheet_name1 = workbook.sheetnames[0]
    for value in sheet1.iter_cols(min_row=1,
                                  max_row=7,
                                  min_col=1,
                                  max_col=1,
                                  values_only=True):
        headings1 = value
    
    for value in sheet1.iter_cols(min_row=1,
                                  max_row=7,
                                  min_col=2,
                                  max_col=2,
                                  values_only=True):
        first_row1 = value
    
    for value in sheet1.iter_cols(min_row=1,
                                  max_row=7,
                                  min_col=3,
                                  max_col=3,
                                  values_only=True):
        second_row1 = value
    

    """ Customer 2 """
    sheet2 = workbook["Customer 2"]
    sheet_name2 = workbook.sheetnames[1]
    for value in sheet2.iter_cols(min_row=1,
                                  max_row=8,
                                  min_col=1,
                                  max_col=1,
                                  values_only=True):
        headings2 = value
    
    for value in sheet2.iter_cols(min_row=1,
                                  max_row=8,
                                  min_col=2,
                                  max_col=2,
                                  values_only=True):
        first_row2 = value
    
    for value in sheet2.iter_cols(min_row=1,
                                  max_row=8,
                                  min_col=3,
                                  max_col=3,
                                  values_only=True):
        second_row2 = value

    """ Customer 3 """
    sheet3 = workbook["Customer 3"]
    sheet_name3 = workbook.sheetnames[2]
    for value in sheet3.iter_cols(min_row=1,
                                  max_row=8,
                                  min_col=1,
                                  max_col=1,
                                  values_only=True):
        headings3 = value
    
    for value in sheet3.iter_cols(min_row=1,
                                  max_row=8,
                                  min_col=2,
                                  max_col=2,
                                  values_only=True):
        first_row3 = value
    
    for value in sheet3.iter_cols(min_row=1,
                                  max_row=8,
                                  min_col=3,
                                  max_col=3,
                                  values_only=True):
        second_row3 = value

    """ Customer 4 """
    sheet4 = workbook["Customer 4"]
    sheet_name4 = workbook.sheetnames[3]
    for value in sheet4.iter_cols(min_row=1,
                                  max_row=8,
                                  min_col=1,
                                  max_col=1,
                                  values_only=True):
        headings4 = value
    
    for value in sheet4.iter_cols(min_row=1,
                                  max_row=8,
                                  min_col=2,
                                  max_col=2,
                                  values_only=True):
        first_row4 = value
    
    for value in sheet4.iter_cols(min_row=1,
                                  max_row=8,
                                  min_col=3,
                                  max_col=3,
                                  values_only=True):
        second_row4 = value

    context = {
        'sheet_names': sheet_names,
        'sheet_name1': sheet_name1,
        'headings1': headings1,
        'first_row1': first_row1,
        'second_row1': second_row1,
        'sheet_name2': sheet_name2,
        'headings2': headings2,
        'first_row2': first_row2,
        'second_row2': second_row2,
        'sheet_name3': sheet_name3,
        'headings3': headings3,
        'first_row3': first_row3,
        'second_row3': second_row3,
        'sheet_name4': sheet_name4,
        'headings4': headings4,
        'first_row4': first_row4,
        'second_row4': second_row4,
    }

    return render(request, 'home/index.html', context)
