# <span id="aanchor133"></span> Vessel Tank Calculation Symbols

## Quantities

**FW (Free Water Volume)** - The water present in a tank that is not suspended in the liquid. Free water may include bottom sediments. Generally, FW is taken from the tank capacity table prior to any corrections, such as those for floating roof and the temperature of the tank shell.

**GOV (Gross Observed Volume)** - The total volume of all petroleum liquids plus entrained sediments and water at observed temperature and pressure. Tank shell corrections due to the temperature of the liquid and the tank pressure are applied. An adjustment for a floating roof may also be included.

GOV = \[(TOV - FW) \* CTSh(liq) \*CPSh\] ± \<FRA or FRC\>

**GSV (Gross Standard Volume)** - The total volume of the petroleum liquids and entrained sediments and water, plus the volume of product vapor, stated at base temperature and pressure conditions.

GSV = VOL + VOV

**MASS (Total Mass)** - The total mass of the petroleum liquids and entrained sediments and water, plus the mass of product vapor.

MASS = MOL + MOV

**MOL (Mass of Liquid)** - The mass of the petroleum liquids plus entrained sediments and water.

Volumetric:  
MOL = VOL / Rho(base)(liq)

 

Inferred Mass:  
MOL = GOV \* Rho(alt)(liq)

**MOV (Mass of Vapor)** - The mass of the product vapors in the vapor space.

MOV = VS \* Rho(alt)(vap)

**NVOL (Net Volume of Liquid)** - The volume of petroleum liquids at to base temperature and pressure conditions.

NVOL = VOL \* CSW

**NSV (Net Standard Volume)** - The total volume of the petroleum liquids plus the volume of product vapor, stated at base temperute and pressure conditions.

NSV = NVOL + VOV

**SWV (Sediment & Water Volume)** - The volume of entrained sediments and water (S&W) at base temperature and pressure conditions

SWV = VOL - NVOL

**TOV (Total Observed Volume)** - The total measured volume of all petroleum liquids, sediments and water (S&W), and free water (FW) at observed temperature and pressure. Generally, TOV is taken from the tank capacity table prior to any corrections, such as those for floating roof and the temperature of the tank shell.

**UVS (Uncorrected Vapor Space)** - The actual volume of space occupied by product vapors at observed temperature and pressure prior to any corrections.

UVS = Tank Capacity - TOV + Tank Dead Space

**VOL (Volume of Liquid)** - The volume of petroleum liquids plus entrained sediments and water corrected to base temperature and pressure conditions.

Volumetric:  
VOL = GOV \* CTL \* CPL

Inferred Mass:  
VOL = MOL / Rho(base)(liq)

**VOV (Volume of Vapor)** - The volume of product vapors in the vapor space corrected to base temperature and pressure conditions.

VOV = MOV / Rho(base)(vap)

**VS (Vapor Space)** - The volume of space occupied by product vapors at observed temperature and pressure and including corrections due to the temperature of the vapor and the tank pressure.

VS = UVS \* CTSh(vap) \* CPSh

## Densities

**Rho(alt)(liq) (Alternate liquid density)** - Density of product liquids at tank conditions.

**Rho(alt)(vap) (Alternate vapor density)** - Density of product vapors at tank conditions.

**Rho(base)(liq) (Base liquid density)** - Density of product liquid at base conditions.

**Rho(base)(vap) (Base vapor density)** - Density of product vapors at base conditions.

## Correction Factors

**CTSh(liq)** - Shell volume correction due to liquid temperature

**CTSh(vap)** - Shell volume correction due to vapor temperature

**CPSh** - Shell volume correction due to tank pressure

**CSW** - Liquid volume correction due to entrained sediments & water

**CTL** - Liquid volume correction due to temperature of the liquid

**CPL** - Liquid volume correction due to pressure of the liquid
