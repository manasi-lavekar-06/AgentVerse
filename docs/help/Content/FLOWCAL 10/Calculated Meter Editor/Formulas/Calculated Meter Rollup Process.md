# <span id="aanchor507"></span> Calculated Meter Rollup Process

The Calculated Meter Rollup service performs calculations as follows:

1.  Gathers final form data for meter and location members. If [Component Calculation](../Operations%20Tab.md) is configured for a particular component, the selected component total data from the members are gathered.
2.  For non-quantity flow parameters, calculates averages of final form hourly values of members according to the selected [Averaging Pool](../Formulas%20Tab.md#Average) option and populates into the final form hourly record of the calculated meter.
3.  If the [Formulas](../Formulas%20Tab.md#Formulas) option is enabled, then for each measurement hour of the calculated meter:
    1.  Reads the IF statement for the calculated meter.
    2.  Retrieves the specified data point from each member that appear in the IF statement, from the final form record of the specified resolution.
    3.  Substitutes in the retrieved member values into the IF statement and evaluates it.
    4.  According to the evaluation result, reads either the DO or the ELSE DO statement of the calculated meter.
    5.  For each quantity, such as volume, energy, and mass, calculates as specified by the statement using the final form hourly data of the members that appear in the statement, and adds the data to the final form hourly record of the calculated meter.
4.  If the Formulas option is not enabled, calculates the hourly values of the calculated meter following standard FLOWCAL rollup processes. The rollup arithmetic is determined by directions of the calculated meter and the members. See: [Calculated Meter Direction](../Operations%20Tab.md)
5.  Rolls the final form hourly data of the calculated meter up to the daily and monthly resolutions following the standard FLOWCAL rollup processes.
