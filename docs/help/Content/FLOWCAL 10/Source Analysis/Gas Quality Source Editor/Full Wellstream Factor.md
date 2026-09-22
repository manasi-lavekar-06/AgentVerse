# <span id="aanchor37"></span> Full Wellstream Factor

In FLOWCAL, as in wide industry practice, full wellstream factor (Fws) is a term used to indicate the fraction of the measured wellhead production that is natural gas. It is a direct multiplier of the metered well volume, and it is never greater than 1.0000.

Technically, full wellstream is the whole volume produced from a well. It is common for wells to produce a mix of natural gas, condensate and water. It is best to separate these products and to meter them individually but often this is not practical or economical. Therefore, a procedure is periodically conducted to determine the fractional content of each part. In this process, a test separator is used to separate the well production into the three products for some period of time. The separated contents are each measured and fractions of the whole for each part are determined from this data. The portion that is natural gas is called the natural gas gross withdrawal (U.S. EIA).

Subsequent to the test procedure, the produced gas portion (i.e., the natural gas gross withdrawal) can be calculated by multiplying the metered well volume by the gas fraction.

In FLOWCAL meters, there are two references to full wellstream:

- In **Meter Analysis**, there is a full wellstream factor. This may be imported from the flow computer (as original data), edited locally or copied from a Source Analysis.
- In **Meter Characteristics**, there is a Yes/No flag that indicates whether the flow computer applied a full wellstream factor to the volume imported by FLOWCAL. If yes, FLOWCAL applies the analysis full wellstream factor to the FLOWCAL-calculated import volume prior to calculating the VCF. On edit recalcs, without regard to the flag, the full wellstream factor is applied to the FLOWCAL-calculated volume along with the VCF.

The meter analysis full wellstream factor and the meter characteristic full wellstream flag are both importable via CFX.

The BLM does not permit the use of full wellstream factor calculations.

</div>
