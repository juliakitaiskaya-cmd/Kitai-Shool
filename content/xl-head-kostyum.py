# -*- coding: utf-8 -*-
# ТЗ «Традиционный костюм в Китае» в XLSX — 9 листов
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

OUT = "tz-kostyum.xlsx"
BRICK = "A41E3A"
CREAM = "FAF7F2"
HAIR = "EAE3D8"

wb = openpyxl.Workbook()
wb.remove(wb.active)

thin = Side(style="thin", color=HAIR)
BORD = Border(left=thin, right=thin, top=thin, bottom=thin)


def sheet(name, title, widths, rows):
    ws = wb.create_sheet(name[:31])
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = w
    ws["A1"] = title
    ws["A1"].font = Font(bold=True, size=14, color=BRICK)
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=max(1, len(widths)))
    ws.row_dimensions[1].height = 24
    r = 3
    for row in rows:
        if row and row[0] == "__H__":
            for c, val in enumerate(row[1:], start=1):
                cell = ws.cell(row=r, column=c, value=val)
                cell.font = Font(bold=True, color="FFFFFF", size=11)
                cell.fill = PatternFill("solid", fgColor=BRICK)
                cell.alignment = Alignment(vertical="center", wrap_text=True)
                cell.border = BORD
            ws.row_dimensions[r].height = 22
        elif not row:
            pass
        else:
            for c, val in enumerate(row, start=1):
                cell = ws.cell(row=r, column=c, value=val)
                cell.alignment = Alignment(vertical="top", wrap_text=True)
                cell.border = BORD
                if c == 1 and len(row) > 1:
                    cell.font = Font(bold=True)
                cell.fill = PatternFill("solid", fgColor=CREAM)
        r += 1
    ws.freeze_panes = "A4"
    return ws


# -*- coding: utf-8 -*-
# Листы ТЗ «Самые известные китайские писатели». Шапка берётся из xl-head.py
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

