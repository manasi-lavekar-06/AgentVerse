# Lab Analysis Import Format

Two lab analysis import file formats are available in FLOWCAL.

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="V1">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Lab Analysis Import Format V1</a>

<div class="drop-down" style="display: none;" mc-target-name="V1">

Items are listed in a line in the following order:

Meter Number

Effective Date/Time

Sample Date/Time

Heating Value

Relative Density

CO2 mole%

N2 mole%

C1 mole%

C2 mole%

C3 mole%

Isobutane mole%

n-Butane mole%

Isopentane mole%

N-Pentane mole%

Neopentane mole%

C6 mole%

C7 mole%

O2 mole%

H2O mole%

H2S mole%

He mole%

Viscosity

Specific Heat Ratio

C8 mole%

C9 mole%

C10 mole%

Ar mole%

CO mole%

H2 mole%

</div>

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler MCTogglerHotSpot_ MCHotSpotImage" data-mc-targets="V2">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Lab Analysis Import Format V2</a>

<div class="drop-down" style="display: none;" mc-target-name="V2">

This file includes a header and the file body. The header ("VERSION=2") must be present for FLOWCAL to recognize and understand the file contents. The body is the same as Lab Analysis Import Format V1, but it also includes Btu condition and Pressure Base fields.

Any analysis containing a Btu condition of "A" (as delivered) will be discarded if the station setup is anything other than "as delivered" (e.g., Dry, Wet, Calc). FLOWCAL will convert the analysis record Btu condition and pressure base to those reflected by the station description in the FLOWCAL database.

Items are listed in the following order:

Meter Number

Effective Date/Time

Sample Date/Time

Heating Value

Heating Value condition ('W'- Wet Saturated 'D'- dry 'A'- As delivered)

Pressure Base

Relative Density

CO2 mole%

N2 mole%

C1 mole%

C2 mole%

C3 mole%

Isobutane mole%

n-Butane mole%

Isopentane mole%

n-pentane mole%

Neopentane mole%

C6 mole%

C7 mole%

O2 mole%

H2O mole%

H2S mole%

He mole%

Viscosity

Specific Heat Ratio

C8 mole%

C9 mole%

C10 mole%

Ar mole%

CO mole%

H2 mole%

</div>

## Format Parameters

All lab analysis import files will use the following format:

- The lab analysis import file should not exceed 255 characters.
- There is one meter gas sample analysis record per line.
- Blank lines and lines that start with **\#**, **;** or **/** are discarded as comments.
- Each data point in a line is separated by spaces or commas. If commas are used as separators, extra spaces are ignored. When using the space-separated format, use a minus sign (-) to indicate a blank or skipped field.
- Any field may be left blank. Additionally, all fields do not have to be present. Missing trailing fields are assumed to be blank or NULL.
- Values for gas analysis mole percent fields should be a percentage in the range of 0 to 100.
- Other special characters are the carat (^) or tilde (~), which are used to indicate numeric blank value, and the double quote (""), which is used to indicate that a field has the same value as the corresponding field on the previous line.

<div class="example">

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler togglerBRDToggler MCTogglerHotSpot_ MCTogglerHotSpot_BRDToggler MCHotSpotImage" data-mc-targets="Example 1">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Example</a>

<div style="display: none;" mc-target-name="Example 1">

; this is how a file containing gas analysis import information

; would look

/ The next record will update the CO2 and N2

/ components to 5% and 3.25% respectively

STA_NUM 10/1/2001 7:00 - - - 5 3.25

; the next record does the same using a comma-delimited format

STA_NUM,10/1/2001 7:00, , , ,5,3.25

; the above 2 records also demonstrate skipped fields

; for sample date, btu, and gravity.

 

</div>

</div>

## <span id="Alternate"></span>Alternate File Format

This file contains a cross reference of meter numbers which must be updated with the lab analysis information of a meter found in the primary file (File Name). For every lab analysis record for a meter in the primary file, a corresponding record will be created and applied for every meter which references the meter found in the primary file.

- This is a text file composed of lines of up to 255 characters in length.
- Each line contains meter numbers separated by commas or spaces.
- The first meter number in a line is a meter number which may be in the primary file.
- The remaining meter numbers will use any gas analysis information found in the primary file which belongs to the first meter number mentioned above.

<div class="example">

<a href="javascript:void(0);" class="MCToggler MCTogglerHead MCTogglerHotSpot MCToggler_Open toggler togglerBRDToggler MCTogglerHotSpot_ MCTogglerHotSpot_BRDToggler MCHotSpotImage" data-mc-targets="Example 2">

<img src="data:image/gif;base64,R0lGODlhEAAQAPcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAP8ALAAAAAAQABAAAAgdAP8JHEiwoMGDCBMqXMiwocOHECNKnEixosWBAQEAOw==" class="MCToggler_Image_Icon" data-mc-alt2="Open" width="16" height="11" alt="Closed" />Example</a>

<div style="display: none;" mc-target-name="Example 2">

Primary file record:

MET_NUM,2/1/2005,1/30/2005,,,,,,

Alternate file line:

MET_NUM, MET1, MET2, MET3

The record for MET_NUM will be used to update meters MET1, MET2, and MET3.

</div>

</div>
