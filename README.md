# Depreciation-Table-Generator

# This application allows user to calculate depreciation for a long-term asset.
    # Depreciation is the process of allocating the appropriate expense related to the cost of a long-term asset over its useful life
    # Depreciation must be calculated in order for businesses to match their expenses with revenues within a single fiscal period
    # This program supports calculation of depreciation with three methods (all GAAP approved)
        1) Straight-Line method
            - Features a constant depreciation expense that is recorded every year throughout the useful life of the asset
            - Depreciation expense per fiscal period is calculated once and recorded each year of the useful life
            
        2) Units of Activity method
            - Based upon the principle that an assets' depreciation is tied to its production of units
            - Features a yearly depreciation expense that is based upon the units the asset produced during that fiscal period
            - Predictions about total and yearly expected output are required
        3) Double Declining method
            - Based upon the principle that an asset will experience a higher amount of wear in the first years of its useful life because newer equipment is generally more efficient
            - Features a yearly depreciation expense that is calculated based on a declining book value of the asset 
    # The date an asset is purchased is important when using the 1) straight-line or 3) double-declining methods
            } When using the Units of Activity method, the purchase date isn't important for calculating the amount of depreciation an asset experiences within a fiscal period 
        - For assets purchased on the first of the fiscal period, a full year of depreciation expense will be recorded every year of the asset's useful life
        - If an asset is purchased any other time throughout the fiscal period, only a portion of the full-year depreciation expense will be recorded in the first and last year of the asset's useful life
            } The depreciation expense for a partial year is calculated based on how many months the asset was held during that fiscal period
                > If an asset is held for 15 or more days in a month, the entire month counts towards the total months of depreciation for that year
                > If an asset is held for less than 15 days in a month, the month is not counted towards the total months of depreciation for that year
            } The ratio of months the asset is held to the total months in the fiscal period is multiplied by the standard depreciation expense calculated for a full year to result in the
            appropriate depreciation expense for the partial year
            
    # With the 2) units of activity and 3) double-declining methods, there is potential for the asset to be completely depreciated to its salvage value before reaching the end of its useful life
        - The straight-line method will result in a depreciaton expense being calculated in every single year of an asset's useful life until reaching its salvage value in the last year
